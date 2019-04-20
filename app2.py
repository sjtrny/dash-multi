from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from pages import DashPage

def display_value(value):
    return 'You have selected "{}"'.format(value)

class App2(DashPage):

    def __init__(self):
        super().__init__()

    def _layout(self):
        return html.Div([
            html.H3('App 2'),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                        'SYD', 'MEL', 'ADL'
                    ]
                ]
            ),
            html.Div(id='display-value'),
        ])

    def _callbacks(self):

        return [
            {'func' : display_value, 'args': [Output('display-value', 'children'), [Input('dropdown', 'value')]] }
        ]