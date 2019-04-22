import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

class Section():

    @classmethod
    def as_app(cls, *args, **kwargs):

        app = MultiPageApp(*args, **kwargs)
        app.root(cls)

        return app

class Page():

    @classmethod
    def namespaced(cls, namespace):

        page = cls()

        # Namespace layout
        if hasattr(page, 'layout'):
            page_layout = page.layout

            # This only skims the surface, we need to parse the full layout tree
            # Could be a problem if the layout is a func rather than component
            # as the layout can change and we would need to reparse every god
            # damn time
            for child in page_layout.children:
                if hasattr(child, 'id'):
                    child.id = f"{namespace}-{child.id}"

            page.layout = page_layout

        # Namespace callbacks
        if hasattr(page, 'callbacks'):
            page_callbacks = page.callbacks

            for cback_func in page_callbacks:

                for arg in cback_func.get_args():
                    if type(arg) is list:
                        for component in arg:
                            component.component_id = f"{namespace}-{component.component_id}"
                    else:
                        arg.component_id = f"{namespace}-{arg.component_id}"

            page.callbacks = page_callbacks

        return page

    @classmethod
    def as_app(cls, *args, **kwargs):

        class TempSection(Section):

            def __init__(self):
                self.routes = routes = [
                    Route('/', cls),
                ]

        app = MultiPageApp(*args, **kwargs)
        app.root(TempSection)

        return app

class Route:

    def __init__(self, path, section_cls):
        self.path = path
        self.handler_cls = section_cls

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

        self.layout_lists = []
        self.callback_lists = []
        self.routing_dict = {}

    def _route(self, pathname):

        if pathname in self.routing_dict:
            page = self.routing_dict[pathname]
        elif pathname is None:
            page = self.routing_dict['/']
        else:
            raise Exception(f"PATHNAME {pathname} does not exist in routes.")

        return page.layout

    # RECURSIVE
    def parse_routes(self, handler):

        routing_dict = {}
        layout_list = []
        callback_list = []

        for sub_route in handler.routes:

            if issubclass(sub_route.handler_cls, Section):
                handler = sub_route.handler_cls()

                sub_routing_dict, sub_layout_list, sub_callback_list = self.parse_routes(handler)

                spaced_sub_routing_dict = {}
                # Prefix the routing dict
                for k, v in sub_routing_dict.items():
                    spaced_sub_routing_dict[f"{sub_route.path}{k}"] = v

                routing_dict.update(spaced_sub_routing_dict)
                layout_list.append(sub_layout_list)
                callback_list.extend(sub_callback_list)

            elif issubclass(sub_route.handler_cls, Page):
                handler = sub_route.handler_cls.namespaced(sub_route.path)

                routing_dict[sub_route.path] = handler

                if hasattr(handler, 'layout'):
                    layout_list.append(handler.layout)
                else:
                    raise Exception("Page must have a layout")

                if hasattr(handler, 'callbacks') and handler.callbacks:
                    callback_list.extend(handler.callbacks)
            else:
                raise Exception("Handler invalid")

        return routing_dict, layout_list, callback_list

    def root(self, routes):

        section = routes()

        routing_dict, layout_list, callback_list = self.parse_routes(section)

        self.routing_dict.update(routing_dict)
        self.layout_lists.extend(layout_list)

        if callback_list:
            self.callback_lists.append(callback_list)

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
            return html.Div([url_bar_and_content_div] + self.layout_lists)

        # Register all layout elements
        self.layout = serve_layout

        # Register root node callback
        self.callback(Output('page-content', 'children'), [Input('url', 'pathname')])(self._route)

        # Register all callbacks
        for callback_list in self.callback_lists:
            for cback_func in callback_list:
                self.callback(*cback_func.get_args())(cback_func)



