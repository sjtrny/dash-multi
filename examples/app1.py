from flask import Flask
import dash
import dash_html_components as html
from section import Section


class IndexApp(dash.Dash):
    def __init__(self, name, server, url_base_pathname):

        # Must initialise the parent class
        super().__init__(
            name=name, server=server, url_base_pathname=url_base_pathname
        )

        self.layout = html.Div([html.H1("HOME INDEX")])


server = Flask(__name__)

index_app = IndexApp(name="home", server=server, url_base_pathname="/")
section_app = Section(name="section", server=server, url_base_pathname="/app1")

if __name__ == "__main__":
    server.run(host="0.0.0.0")
