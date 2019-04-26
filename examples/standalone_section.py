from multipage import MultiPageApp
from section import section_routes

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = MultiPageApp(__name__, external_stylesheets=external_stylesheets)

app.set_routes(section_routes)

if __name__ == "__main__":
    app.run_server(debug=True)
