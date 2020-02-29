import dash
import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
from datetime import datetime as dt

from app import app

DD_LOGO = "assets/images/ds_logo3.png"

def plot_test():
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )

def twolines_dashboard(left_graph,right_graph,size,pd):
    return dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div(left_graph)
                        ])
                    ])
                ],width={"size":size,"padding":pd}),
                dbc.Col([
                    dbc.Card([
                            dbc.CardBody([
                                html.Div(right_graph)
                            ])
                        ])
                ],width={"size":size,"padding":pd},style={"width":"380px"})
            ])
    

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=DD_LOGO, height="50px")),
                    dbc.Col(dbc.NavbarBrand("", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="#",
        ),
        dbc.NavbarToggler(id="navbar-toggler")
    ],
    color="",
    dark=False,
    className="side-nav",
    style={"width":"100%"}
)

body = html.Div([
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    html.P("Filters"),
                    dcc.DatePickerSingle(
                        id="date-picker-range",
                        initial_visible_month=dt(2017,1,1)
                    ),
                    dcc.DatePickerSingle(
                        id="date-picker-end",
                        initial_visible_month=dt(2017,1,1),
                        style={"margin-top":"1rem"}
                    )

                ])
            ]),width={"size":3},style={"padding-top":"5rem"}),
            dbc.Col([
                twolines_dashboard(plot_test(),plot_test(),5,1),
                twolines_dashboard(plot_test(),plot_test(),5,1)
            ],width={"size":9})

    ],style={"margin-top":"1rem"})
])

layout = html.Div(
    [navbar,body]
)

@app.callback(
    Output('output-date','children'),
    [Input('date-picker-range','date')]
)
def update_output(date):
    return date

