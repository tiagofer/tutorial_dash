import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
from datetime import datetime as dt

from app import app

DD_LOGO = "assets/images/ds_logo3.png"

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
    dark=True,
)

page = html.Div([
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    html.P("Teste")
                ])
            ]),width={"size":3}
        )
    ])
])

body = html.Div(
    [navbar,page]
)