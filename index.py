import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc

from dash.dependencies import Input,Output

from app import app
from apps import dashboard

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div (id='page-content')
])

@app.callback(
    Output('page-content','children'),
    [Input('url','pathname')]
)
def display_page(pathname):
    if pathname=='/dashboard':
        return dashboard.layout
    elif pathname == '/':
        return dashboard.layout
    else:
        return '404'

if __name__ == "__main__":
    app.run_server(debug=True)