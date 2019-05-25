from flask import Flask
import dash
import dash_html_components as html
from section import Section
from multipage import Route, MultiPageApp


class IndexApp(dash.Dash):
    def __init__(self, name, server, url_base_pathname):

        # Must initialise the parent class
        super().__init__(
            name=name, server=server, url_base_pathname=url_base_pathname
        )

        self.layout = html.Div([html.H1("HOME INDEX")])


class MyApp(MultiPageApp):
    def get_routes(self):

        return [Route(IndexApp, "index", "/"), Route(Section, "home", "/app1")]


server = Flask(__name__)

app = MyApp(name="", server=server, url_base_pathname="")


if __name__ == "__main__":
    server.run(host="0.0.0.0")
