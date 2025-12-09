from pathlib import Path

import dash
from dash import Input, Output, dcc, html
import pandas as pd
import plotly.express as px

DATA_PATH = Path(__file__).parent / "data" / "pink_morsel_sales.csv"
PRICE_CHANGE_DATE = pd.Timestamp("2021-01-15")

# Load and prepare the sales data
df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"])
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)
regions = sorted(df["Region"].unique())


def build_figure(selected_region):
    use_all = not selected_region or selected_region == "all"
    filtered = df if use_all else df[df["Region"] == selected_region]
    daily = (
        filtered.groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Date")
    )
    fig = px.line(
        daily,
        x="Date",
        y="Sales",
        labels={"Date": "Date", "Sales": "Sales ($)"},
    )
    fig.add_shape(
        type="line",
        x0=PRICE_CHANGE_DATE,
        x1=PRICE_CHANGE_DATE,
        y0=0,
        y1=1,
        xref="x",
        yref="paper",
        line=dict(color="firebrick", dash="dash"),
    )
    fig.add_annotation(
        x=PRICE_CHANGE_DATE,
        y=1,
        xref="x",
        yref="paper",
        xanchor="left",
        yanchor="bottom",
        showarrow=False,
        text="Price increase (15 Jan 2021)",
        font=dict(color="firebrick", size=12),
    )
    fig.update_layout(margin=dict(l=40, r=20, t=20, b=40))
    return fig


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("Pink Morsel Sales Visualiser", style={"margin": 0}),
                html.P(
                    "Daily sales before and after the 15 Jan 2021 price increase. "
                    "Use the region selector to dig deeper.",
                    style={"margin": "8px 0 0 0"},
                ),
            ],
            style={
                "padding": "16px 20px",
                "background": "linear-gradient(120deg, #ffdee9 0%, #b5fffc 100%)",
                "borderRadius": "14px",
                "boxShadow": "0 10px 30px rgba(0,0,0,0.12)",
                "marginBottom": "18px",
            },
        ),
        html.Div(
            [
                html.Label("Choose region", style={"fontWeight": 600}),
                dcc.RadioItems(
                    id="region-radio",
                    options=[{"label": "All", "value": "all"}]
                    + [{"label": r.title(), "value": r} for r in regions],
                    value="all",
                    labelStyle={
                        "display": "inline-block",
                        "marginRight": "14px",
                        "padding": "8px 10px",
                        "borderRadius": "10px",
                        "background": "#f4f6fb",
                        "cursor": "pointer",
                        "border": "1px solid #dce4ff",
                    },
                    inputStyle={"marginRight": "6px"},
                    style={"marginTop": "6px"},
                ),
            ],
            style={
                "padding": "14px 16px",
                "border": "1px solid #e3e8ef",
                "borderRadius": "12px",
                "backgroundColor": "#fff",
                "boxShadow": "0 6px 18px rgba(0,0,0,0.06)",
                "marginBottom": "18px",
            },
        ),
        dcc.Graph(
            id="sales-chart",
            config={"displaylogo": False},
            style={"background": "#fff", "borderRadius": "14px", "padding": "4px"},
        ),
    ],
    style={
        "maxWidth": "960px",
        "margin": "0 auto",
        "padding": "28px 22px 40px",
        "fontFamily": "'Segoe UI', 'Helvetica Neue', Arial, sans-serif",
        "backgroundColor": "#f6f8fb",
    },
)


@app.callback(Output("sales-chart", "figure"), Input("region-radio", "value"))
def update_chart(selected_region):
    return build_figure(selected_region)


if __name__ == "__main__":
    app.run(debug=True)
