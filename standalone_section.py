from multipage import MultiPageApp
from section2 import section2_routes

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = MultiPageApp(__name__, external_stylesheets=external_stylesheets)

app.set_routes(section2_routes)

if __name__ == '__main__':
    app.run_server(debug=True)