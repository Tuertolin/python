'''
Date: 24/09/2023
Project: Dashboard to show a stock portfolio performance of about 5 to 10 different stocks. 
Non prediction, non-analysis, just a brief summary of how stocks are doing.
Version: 0.1
Notes: 
'''
# importing required libraries
import datetime
import yfinance as yf
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

# The dash_html_components package is deprecated. Please replace `import dash_html_components as html
# URL: https://stackoverflow.com/questions/69314018/the-dash-html-components-package-is-deprecated-please-replace-import-dash-html


app = Dash()
app.title = "Stock Visualisation"
 
app.layout = html.Div(children=[
    html.H1("Stock Visualisation Dashboard"),
    html.H4("Please enter the stock name"),
    dcc.Input(id='input', value='AAPL', type='text'),
    html.Div(id='output-graph')
])

# callback Decorator
@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_graph(input_data):
    start = datetime.datetime(2018, 1, 1)
    end = datetime.datetime.now()
 
    try:
        df = web.DataReader(input_data, 'yahoo', start, end)
 
        graph = dcc.Graph(id ="example", figure ={
            'data':[{'x':df.index, 'y':df.Close, 'type':'line', 'name':input_data}],
            'layout':{
                'title':input_data
            }
        })
 
    except:
        graph = html.Div("Error retrieving stock data.")
 
    return graph

if __name__ == '__main__':
    app.run_server()
    
###The dash_core_components package is deprecated. Please replace
##`import dash_core_components as dcc` with `from dash import dcc`
#  import dash_core_components as dcc
#/home/administrator/Documents/01_Python/06_Graphs/01_StockDashboard.py:7: UserWarning: 
#The dash_html_components package is deprecated. Please replace
#`import dash_html_components as html` with `from dash import html`
#  import dash_html_components as html

