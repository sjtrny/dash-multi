from multipage import MultiPageApp, Route, Page
from page1 import Page1
from section2 import section2_routes
import dash_core_components as dcc
import dash_html_components as html
from header import header
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = MultiPageApp(__name__, external_stylesheets=external_stylesheets)

# Create a new page
index_page = Page()

index_page.layout = html.Div(header.children + [
            html.H3('Home'),
            dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0),
            html.Div(id='display-value'),
        ])

@index_page.callback(Output('display-value', 'children'), [Input('interval-component', 'n_intervals')])
def my_callback(n_intervals):
    return f"Seconds since load: {n_intervals}."

# Configure routing
routes = [
    Route('', index_page),              # Locally defined page
    Route('/page1', Page1()),           # Seperately defined page
    Route('/page2', section2_routes),   # Section containing pages and further sections
]

app.set_routes(routes)

if __name__ == '__main__':
    app.run_server(debug=True)
