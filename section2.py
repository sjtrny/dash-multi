import dash_core_components as dcc
import dash_html_components as html
from multipage import Route, Page
from page1 import Page1
from header import header

section_index = Page()
section_index.layout = html.Div(header.children + [
            html.H1("Section 2 Index"),
            dcc.Link('Navigate to App 1', href='./demo'),
        ])

demo = Page()
demo.layout = html.Div(header.children + [
            html.H1("Demo"),
        ])

section2_routes = [
            # This seems like a potential bug in dash, we should be able to
            # use '' here, however it breaks the ./demo relative linking!
            Route('/', section_index),
            Route('/demo', demo),
            Route('/page1', Page1())
        ]
