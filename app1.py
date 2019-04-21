from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from pages import DashPage
from multipage import wrap_callback

@wrap_callback(Output('display-value', 'children'), [Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

class App1(DashPage):

    def __init__(self):
        super().__init__()

    def _layout(self):
        return html.Div([
            html.H3('App 1'),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                        'NYC', 'MTL', 'LA'
                    ]
                ]
            ),
            html.Div(id='display-value'),
        ])

    def _callbacks(self):

        return [
            display_value
        ]