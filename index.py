import dash_core_components as dcc
import dash_html_components as html
from multipage import MultiPageApp
from page1 import Page1
from page2 import Page2

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = MultiPageApp(__name__, external_stylesheets=external_stylesheets)

server = app.server

nav_bar = html.Div([
    dcc.Link('Home', href='/'),
    html.Br(),
    dcc.Link('Navigate to App 1', href='/pages/page1'),
    html.Br(),
    dcc.Link('Navigate to App 2', href='/pages/page2'),
])

pages = {
    'page1': Page1(),
    'page2': Page2(),
}

app.load_apps(pages)

routing_dict = {
    '/pages/page1': pages['page1'],
    '/pages/page2': pages['page2'],
}

def main_layout(pathname):

    extras = []

    if pathname in routing_dict:
        extras.extend(routing_dict[pathname].layout().children)

    return html.Div(nav_bar.children + extras)

app.set_layout(main_layout)

if __name__ == '__main__':
    app.run_server(debug=True)
