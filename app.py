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


def build_figure(selected_regions):
    use_all = not selected_regions or "all" in selected_regions
    filtered = df if use_all else df[df["Region"].isin(selected_regions)]
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
        html.H1("Pink Morsel Sales Visualiser"),
        html.P(
            "Daily sales before and after the 15 Jan 2021 price increase. "
            "Filter by region to dig deeper."
        ),
        dcc.Dropdown(
            id="region-dropdown",
            options=[{"label": "All regions", "value": "all"}]
            + [{"label": r.title(), "value": r} for r in regions],
            value=["all"],
            multi=True,
            clearable=False,
        ),
        dcc.Graph(id="sales-chart", config={"displaylogo": False}),
    ],
    style={"maxWidth": "960px", "margin": "0 auto", "padding": "24px"},
)


@app.callback(Output("sales-chart", "figure"), Input("region-dropdown", "value"))
def update_chart(selected_regions):
    selected = selected_regions or ["all"]
    return build_figure(selected)


if __name__ == "__main__":
    app.run(debug=True)
