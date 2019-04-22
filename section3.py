import dash_core_components as dcc
import dash_html_components as html
from multipage import Route, Section, Page

class Page3Index(Page):

    def __init__(self):

        self.layout = html.Div([
            html.H1("PAGE 3 INDEX"),
            dcc.Link('Navigate to App 1', href='./demo'),
        ])

        self.callbacks = []

class Demo(Page):

    def __init__(self):

        self.layout = html.Div([
            html.H1("Demo"),
        ])

        self.callbacks = []

class Section3(Section):

    def __init__(self):

        self.routes = [
            Route('/', Page3Index),
            Route('/demo', Demo),
        ]
