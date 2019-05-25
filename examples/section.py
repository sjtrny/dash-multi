import dash
import dash_html_components as html
from multipage import Route, MultiPageApp
from page import Page1

section_header = html.Div(
    [
        html.Br(),
        html.A("Section Home", href="./"),
        html.Br(),
        html.A("Navigate to Demo", href="./demo"),
    ]
)


class Index(dash.Dash):
    def __init__(self, name, server, url_base_pathname):

        # Must initialise the parent class
        super().__init__(
            name=name, server=server, url_base_pathname=url_base_pathname
        )

        self.layout = html.Div(
            section_header.children + [html.H1("Section 2 Index")]
        )


class Demo(dash.Dash):
    def __init__(self, name, server, url_base_pathname):

        # Must initialise the parent class
        super().__init__(
            name=name, server=server, url_base_pathname=url_base_pathname
        )

        self.layout = html.Div(section_header.children + [html.H1("Demo")])


class Section(MultiPageApp):
    def get_routes(self):

        return [
            Route(Index, "index", "/"),
            Route(Demo, "demo", "/demo/"),
            Route(Page1, "page1", "/page1/"),
        ]
