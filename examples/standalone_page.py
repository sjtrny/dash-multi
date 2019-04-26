from page import Page1
from multipage import MultiPageApp

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = MultiPageApp(__name__, external_stylesheets=external_stylesheets)

app.set_routes(Page1())

if __name__ == '__main__':
    app.run_server(debug=True)