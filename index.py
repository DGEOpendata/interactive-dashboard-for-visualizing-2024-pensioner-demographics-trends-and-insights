python
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load datasets
gender_data = pd.read_excel('Distribution of Pensioners per Gender.xlsx')
overall_data = pd.read_excel('Distribution of Pensioners.xlsx')

# Initialize Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Interactive Dashboard for Pensioners Distribution 2024"),
    html.Label("Select Quarter:"),
    dcc.Dropdown(
        id='quarter-dropdown',
        options=[{'label': quarter, 'value': quarter} for quarter in overall_data['Quarter'].unique()],
        value=overall_data['Quarter'].unique()[0]
    ),
    dcc.Graph(id='gender-distribution'),
    dcc.Graph(id='overall-distribution')
])

# Callback to update gender distribution chart
@app.callback(
    Output('gender-distribution', 'figure'),
    [Input('quarter-dropdown', 'value')]
)
def update_gender_chart(selected_quarter):
    filtered_data = gender_data[gender_data['Quarter'] == selected_quarter]
    fig = px.pie(
        filtered_data,
        names='Gender',
        values='Count',
        title=f'Gender Distribution in {selected_quarter}'
    )
    return fig

# Callback to update overall distribution chart
@app.callback(
    Output('overall-distribution', 'figure'),
    [Input('quarter-dropdown', 'value')]
)
def update_overall_chart(selected_quarter):
    filtered_data = overall_data[overall_data['Quarter'] == selected_quarter]
    fig = px.bar(
        filtered_data,
        x='Type',
        y='Count',
        title=f'Overall Distribution by Type in {selected_quarter}',
        color='Type'
    )
    return fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
