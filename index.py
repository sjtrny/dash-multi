import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from multipage import MultiPageApp
from app1 import App1
from app2 import App2

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = MultiPageApp(__name__, external_stylesheets=external_stylesheets)

server = app.server

layout_index = html.Div([
    dcc.Link('Home', href='/'),
    html.Br(),
    dcc.Link('Navigate to App 1', href='/apps/app1'),
    html.Br(),
    dcc.Link('Navigate to App 2', href='/apps/app2'),
])

pages = {
    'app1': App1(),
    'app2': App2(),
}

app.load_apps(pages)

routing_dict = {
    '/apps/app1': pages['app1'],
    '/apps/app2': pages['app2'],
}

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    extras = []

    if pathname in routing_dict:
        extras.extend(routing_dict[pathname].layout.children)

    return html.Div( layout_index.children + extras)

if __name__ == '__main__':
    app.run_server(debug=True)
