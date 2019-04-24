import dash_core_components as dcc
import dash_html_components as html
from multipage import Route, Page
from page1 import Page1
from header import header as site_header

section_header = html.Div([
            html.Br(),
            dcc.Link('Section Home', href='./'),
            html.Br(),
            dcc.Link('Navigate to Demo', href='./demo'),
        ])

section_index = Page()
section_index.layout = html.Div(site_header.children + section_header.children + [
            html.H1("Section 2 Index"),

        ])

demo = Page()
demo.layout = html.Div(site_header.children + section_header.children + [
            html.H1("Demo"),
        ])

section2_routes = [
            # This seems like a potential bug in dash, we should be able to
            # use '' here, however it breaks the ./demo relative linking!
            Route('/', section_index),
            Route('/demo', demo),
            Route('/page1', Page1())
        ]
