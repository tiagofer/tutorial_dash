import dash
import dash_bootstrap_components as dbc

#Importa estilo padrão 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#instancia o objeto da aplicação Dash
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.MATERIA])

#inicia o servidor
server = app.server

#remove o alerta para callbacks
app.config.suppress_callback_exceptions = True