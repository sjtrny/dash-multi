from multipage import MultiPageApp, Route, Page, Section
from page1 import Page1
from page2 import Page2
from section3 import Section3
from header import header

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = MultiPageApp(__name__, external_stylesheets=external_stylesheets)

server = app.server

class IndexPage(Page):
    def __init__(self):
        self.layout = header

class IndexSection(Section):
    def __init__(self):
        self.routes = [
            Route('/', IndexPage),
            Route('/page1', Page1),
            Route('/page2', Page2),
            Route('/page3', Section3),
        ]

app.root(IndexSection)

if __name__ == '__main__':
    app.run_server(debug=True)
