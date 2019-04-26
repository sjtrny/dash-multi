import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import types
import functools


def copy_func(func):
    """
    Makes a new copy of a function.

    :param func: function to be copied
    :return: a copy of the function
    """

    # https://stackoverflow.com/a/13503277
    copied_func = types.FunctionType(
        func.__code__,
        func.__globals__,
        name=func.__name__,
        argdefs=func.__defaults__,
        closure=func.__closure__,
    )
    copied_func = functools.update_wrapper(copied_func, func)
    copied_func.__kwdefaults__ = func.__kwdefaults__
    return copied_func


class Page:
    """
    Represents a single web page with it's own Dash layout and callbacks
    """

    def __init__(self):
        # Set the layout and callback list
        self.layout = None
        self.callbacks = []

    def callback(self, output, inputs=[], state=[]):
        """
        Register a callback to components on the page

        :param output: the target output
        :param inputs: a list of inputs that are listened to
        :param state: a list of states that are listened to
        """

        def wrapper(func):
            func = copy_func(func)

            func.output = output
            func.inputs = inputs
            func.states = state

            def get_args():
                return [func.output, func.inputs, func.states]

            func.get_args = get_args

            self.callbacks.append(func)

            return func

        return wrapper

    def namespace(self, namespace):
        """
        Namespaces layout elements and callbacks

        :param namespace: a string of the namespace
        """

        # Namespace layout
        if hasattr(self, "layout"):

            def parse_layout(child):
                if hasattr(child, "children") and isinstance(
                    child.children, list
                ):
                    for sub_child in child.children:
                        parse_layout(sub_child)
                elif hasattr(child, "id"):
                    child.id = f"{namespace}:{child.id}"

                return child

            self.layout = parse_layout(self.layout)

        # Namespace callbacks
        if hasattr(self, "callbacks"):
            page_callbacks = self.callbacks

            for cback_func in page_callbacks:

                for arg in cback_func.get_args():
                    if type(arg) is list:
                        for component in arg:
                            component.component_id = (
                                f"{namespace}:{component.component_id}"
                            )
                    else:
                        arg.component_id = f"{namespace}:{arg.component_id}"

            self.callbacks = page_callbacks

        return self


class Route:
    """
    Struct to represent a route
    """

    def __init__(self, path, handler):
        self.path = path
        self.handler = handler


class MultiPageApp(dash.Dash):
    """
    Adds multi-page functionality to a normal dash app
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout_lists = []
        self.callback_lists = []
        self.routing_dict = {}

    def _multilayout(self, pathname):
        """
        Returns the layout for the current requested path

        :param pathname:
        :return:
        """
        if pathname in self.routing_dict:
            page = self.routing_dict[pathname]
        elif pathname == "/" or pathname is None:
            page = self.routing_dict[""]
        else:
            raise Exception(f"PATHNAME {pathname} does not exist in routes.")

        return page.layout

    @staticmethod
    def parse_routes(handler, cur_path=None):
        """
        Recursively parse the route tree

        :param handler: either a Page or list of routes
        :param cur_path: parent path of the handler
        :return: routing_dict, layout_list, callback_list
        """

        cur_path = cur_path if cur_path else ""

        routing_dict = {}
        layout_list = []
        callback_list = []

        if isinstance(handler, list):

            route_list = handler

            for sub_route in route_list:

                sub_routing_dict, sub_layout_list, sub_callback_list = MultiPageApp.parse_routes(
                    sub_route.handler, f"{cur_path}{sub_route.path}"
                )

                routing_dict.update(sub_routing_dict)
                layout_list.extend(sub_layout_list)
                callback_list.extend(sub_callback_list)

        elif isinstance(handler, Page):

            page = handler.namespace(cur_path)

            routing_dict[cur_path] = page
            layout_list.append(page.layout)
            if hasattr(page, "callbacks") and page.callbacks:
                callback_list.extend(page.callbacks)
        else:
            raise Exception("Handler Class invalid")

        return routing_dict, layout_list, callback_list

    def set_routes(self, handler):
        """
        Set the routes for the Multi Page App

        :param handler: either a Page or list of Routes
        """

        routing_dict, layout_list, callback_list = self.parse_routes(handler)

        self.routing_dict.update(routing_dict)
        self.layout_lists.extend(layout_list)

        if callback_list:
            self.callback_lists.extend(callback_list)

        url_bar_and_content_div = html.Div(
            [
                dcc.Location(id="url", refresh=False),
                html.Div(id="page-content"),
            ]
        )

        def serve_layout():
            # Check if this is being called due to a HTTP request
            # or layout validation
            if flask.has_request_context():
                # ACTUAL REQUEST, RETURN ROOT OF PAGE CONTENT

                return html.Div([url_bar_and_content_div])

            # TRICK LAYOUT VALIDATION
            return html.Div([url_bar_and_content_div] + self.layout_lists)

        # Register all layout elements
        self.layout = serve_layout

        # Register root node callback
        self.callback(
            Output("page-content", "children"), [Input("url", "pathname")]
        )(self._multilayout)

        # Register all callbacks
        for cback_func in self.callback_lists:
            self.callback(*cback_func.get_args())(cback_func)
