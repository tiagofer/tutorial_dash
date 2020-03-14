import pandas as pd 
import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input,Output
import plotly.express as px


#colunas que serão utilizadas
cols = ['mesano_de_referencia','tribunal','cargo','total_de_rendimentos']
#carregar dataset salários
df_salarios = pd.read_csv("datasets/salarios.csv",usecols=cols,low_memory=False)

#instanciando dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(name=__name__,external_stylesheets=external_stylesheets)

#criando uma lista com os nomes de tribunais existentes no dataset
tribunal = df_salarios.tribunal.unique()

#criação do layout
app.layout = html.Div([
    #menu dropdown com a id para ser acessado via callback e a lista de opções geradas a partir do dataframe
    dcc.Dropdown(
        id='tribunal-dropdown',
        options=[{'label':i,'value':i} for i in tribunal]
    ),
    #div para a exibição do gráfico. Repare que o elemento graph só tem o ID, o gráfico será gerado no callback
    html.Div([
        dcc.Graph(
            id='meu-grafico-aqui'
        )
    ])

])

#neste callback utilizaremos como Output o Graph "meu-grafico-aqui"
#como Input recebemos o valor ativo no menu Dropdown (value)
@app.callback(
    Output('meu-grafico-aqui','figure'),
    [Input('tribunal-dropdown','value')]
)
#Após o callback, teremos a função que fará o update no output de acordo com o valor (value) recebido (sacou?!?!)
def update_output(value):
    #aqui criaremos um novo dataframe que será filtrado conforme o tribunal selecionado
    #o resultado será agrupado pela data de pagamento utilizando a soma dos valores
    #ao final, resetamos o índice para a geração do gráfico
    df_filtered = df_salarios[df_salarios.tribunal == value].groupby("mesano_de_referencia").sum().reset_index()
    #como retorno, entregamos um gráfico de barras que utiliza como eixo x mesano_de_referencia e y o total_de_redimentos
    return px.bar(df_filtered,x=cols[0],y=cols[3])

#não esqueça desta linha para conseguir rodar sua aplicação
if __name__ == '__main__':
    app.run_server(debug=True)

