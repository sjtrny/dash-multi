from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from multipage import wrap_callback, Page
from header import header

@wrap_callback(Output('display-value', 'children'), [Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)


class Page2(Page):

    def __init__(self):

        self.layout = html.Div(header.children + [
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

        self.callbacks = [
            display_value
        ]
