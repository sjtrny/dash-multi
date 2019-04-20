import flask
import dash
import dash_html_components as html
import dash_core_components as dcc

class MultiPageApp(dash.Dash):

    def load_apps(self, app_dict):

        for page_name, page_app in app_dict.items():

            page_layout = page_app.layout
            page_callbacks = page_app.callbacks

            # SHOULD PROBABLY STORE A COPY OF LAYOUT RATHER THAN MODIFYING
            # THE LAYOUT OF THE OBJECT ¯\_(ツ)_/¯

            for child in page_layout.children:
                if hasattr(child, 'id'):
                    child.id = f"{page_name}-{child.id}"

            for cback_dict in page_callbacks:
                for arg in cback_dict['args']:
                    if type(arg) is list:
                        for component in arg:
                            component.component_id = f"{page_name}-{component.component_id}"
                    else:
                        arg.component_id = f"{page_name}-{arg.component_id}"

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
            return html.Div([url_bar_and_content_div] + [page_app.layout for page_name, page_app in app_dict.items()])

        self.layout = serve_layout

        for page_name, page_app in app_dict.items():
            for cback_dict in page_app.callbacks:
                self.callback(*cback_dict['args'])(cback_dict['func'])