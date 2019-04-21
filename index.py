import dash_core_components as dcc
import dash_html_components as html
from multipage import MultiPageApp
from app1 import App1
from app2 import App2

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = MultiPageApp(__name__, external_stylesheets=external_stylesheets)

server = app.server

nav_bar = html.Div([
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

# TODO, routing and reverse like functionality

routing_dict = {
    '/apps/app1': pages['app1'],
    '/apps/app2': pages['app2'],
}

def main_layout(pathname):

    extras = []

    if pathname in routing_dict:
        extras.extend(routing_dict[pathname].layout().children)

    return html.Div(nav_bar.children + extras)

app.set_layout(main_layout)

if __name__ == '__main__':
    app.run_server(debug=True)
