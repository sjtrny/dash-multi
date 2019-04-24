import dash_core_components as dcc
import dash_html_components as html
from multipage import Route, Page
from page1 import Page1

page3index = Page()
page3index.layout = html.Div([
            html.H1("PAGE 3 INDEX"),
            dcc.Link('Navigate to App 1', href='./demo'),
        ])

demo = Page()
demo.layout = html.Div([
            html.H1("Demo"),
        ])

section2_routes = [
            Route('/', page3index),
            Route('/demo', demo),
            Route('/page1', Page1())
        ]
