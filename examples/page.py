from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from multipage import Page
from header import header


def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


class Page1(Page):
    def __init__(self, *args, **kwargs):

        # Must initialise the parent class
        super().__init__(*args, **kwargs)

        self.layout = html.Div(
            header.children
            + [
                html.H3("Page 1"),
                html.Div(
                    [
                        dcc.Dropdown(
                            id="dropdown",
                            options=[
                                {"label": "App 1 - {}".format(i), "value": i}
                                for i in ["NYC", "MTL", "LA"]
                            ],
                        ),
                        html.Div(id="display-value"),
                    ]
                ),
                html.Div(
                    [
                        dcc.Input(
                            id="my-id", value="initial value", type="text"
                        ),
                        html.Div(id="my-div"),
                    ]
                ),
            ]
        )

        # CALLBACK STYLE 1
        @self.callback(
            Output("display-value", "children"), [Input("dropdown", "value")]
        )
        def display_value(value):
            return 'You have selected "{}"'.format(value)

        # CALLBACK STYLE 2
        # The callback could alternatively be defined using
        self.callback(
            Output(component_id="my-div", component_property="children"),
            [Input(component_id="my-id", component_property="value")],
        )(update_output_div)
