import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Create a simple dataset
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
}
df = pd.DataFrame(data)

# Create a simple plot
fig = px.line(df, x='x', y='y', title='Simple Line Plot')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Quantium Starter App"),
    html.P("This is a simple Dash app to test the setup!"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    # Use the current Dash API to start the server
    app.run(debug=True)
