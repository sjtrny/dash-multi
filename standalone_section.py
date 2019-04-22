from section3 import Section3

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Section3.as_app(__name__, external_stylesheets=external_stylesheets)

if __name__ == '__main__':
    app.run_server(debug=True)