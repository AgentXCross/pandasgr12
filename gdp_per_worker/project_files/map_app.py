import pandas as pd
import json
import plotly.express as px
import dash
from dash import dcc, html, Input, Output

# Load cleaned merged data (U.S. states only)
df = pd.read_csv("../project_data/merged_gdp_data.csv")

# Load US States GeoJSON
with open("../project_data/us-states.geojson") as f:
    geojson = json.load(f)

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("U.S. State Economic Data Viewer"),
    dcc.Graph(id="choropleth-map"),
    html.Div(id="state-data", style={"padding": "20px", "fontSize": "18px"})
])

@app.callback(
    Output("choropleth-map", "figure"),
    Output("state-data", "children"),
    Input("choropleth-map", "clickData")
)
def update_map(click_data):
    fig = px.choropleth(
        df,
        geojson=geojson,
        locations="STATE/PROVINCE",
        featureidkey="properties.name",
        color="Y -  Nominal GDP Per Worker",
        color_continuous_scale="Viridis",
        scope="usa",
        hover_name="STATE/PROVINCE"
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    if click_data:
        state_name = click_data["points"][0]["location"]
        state_row = df[df["STATE/PROVINCE"] == state_name]
        if not state_row.empty:
            row = state_row.iloc[0]
            return fig, html.Div([
                html.H3(f"Details for {state_name}"),
                html.P(f"GDP per Worker: {row['Y -  Nominal GDP Per Worker']}"),
                html.P(f"STEM Workforce %: {row['X1 - % Workforce in STEM']}"),
                html.P(f"Urbanization Rate: {row['X2 - Urbanization Rate (%)']}"),
                html.P(f"Disposable Income: {row['X3 - True Value Disposable Income']}")
            ])

    return fig, "Click on a state to view economic details."


#Run the app
if __name__ == "__main__":
    app.run(debug = True, port = 8051)