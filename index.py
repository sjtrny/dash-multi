from multipage import MultiPageApp, Route, Page, Section
from page1 import Page1
from page2 import Page2
from page3 import Page3
from header import header

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = MultiPageApp(__name__, external_stylesheets=external_stylesheets)

server = app.server

class IndexPage(Page):
    def __init__(self):
        self.layout = header
        self.callbacks = []

class IndexSection(Section):
    def __init__(self):
        self.routes = [
            Route('/', IndexPage),
            Route('/page1', Page1),
            Route('/page2', Page2),
            Route('/page3', Page3),
        ]

app.root(IndexSection)

if __name__ == '__main__':
    app.run_server(debug=True)
