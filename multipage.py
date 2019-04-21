import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

def wrap_callback(output, inputs=[], state=[]):

    def wrapper(func):

        func.output = output
        func.inputs = inputs
        func.states = state

        def get_args():
            return [func.output, func.inputs, func.states]

        func.get_args = get_args

        return func

    return wrapper

class MultiPageApp(dash.Dash):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout_list = []
        self.callback_lists = []

    def set_layout(self, layout_func):
        self.callback(Output('page-content', 'children'), [Input('url', 'pathname')])(layout_func)

    def load_apps(self, app_dict):

        for page_name, page_app in app_dict.items():

            page_layout = page_app.layout()
            page_callbacks = page_app.callbacks()

            for child in page_layout.children:
                if hasattr(child, 'id'):
                    child.id = f"{page_name}-{child.id}"

            self.layout_list.append(page_layout)

            for cback_func in page_callbacks:

                for arg in cback_func.get_args():
                    if type(arg) is list:
                        for component in arg:
                            component.component_id = f"{page_name}-{component.component_id}"
                    else:
                        arg.component_id = f"{page_name}-{arg.component_id}"

            self.callback_lists.append(page_callbacks)

        url_bar_and_content_div = html.Div([
            dcc.Location(id='url', refresh=False),
            html.Div(id='page-content')
        ])

        def serve_layout():
            # Check if this is being called due to a HTTP request or layout validation
            if flask.has_request_context():
                # ACTUAL REQUEST, RETURN ROOT OF PAGE CONTENT
                return html.Div([url_bar_and_content_div])

            # TRICK LAYOUT VALIDATION
            return html.Div([url_bar_and_content_div] + self.layout_list)

        self.layout = serve_layout

        for callback_list in self.callback_lists:
            for cback_func in callback_list:
                self.callback(*cback_func.get_args())(cback_func)