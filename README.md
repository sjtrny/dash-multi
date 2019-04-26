[![Build Status](https://travis-ci.org/sjtrny/dash-multi.svg?branch=master)](https://travis-ci.org/sjtrny/dash-multi)
[![Documentation Status](https://readthedocs.org/projects/dash-multi/badge/?version=latest)](https://dash-multi.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/jitcache)](https://pepy.tech/project/dash-multi)

# Dash Multi(Page)

Wrapper on top of Dash to support multi page apps.

### Running Examples

Run one of:

- index.py
- standalone_page.py
- standalone_section.py

### Illustrative Example

#### Create a multipage app

    app = MultiPageApp(__name__)

    # Configure routing
    routes = [
        Route('', IndexPage()),             
        Route('/page1', Page1()),           
        Route('/page2', section2_routes),   # Section containing pages and further sections
    ]

    app.set_routes(routes)

    if __name__ == '__main__':
        app.run_server(debug=True)


#### Create a single page app (@alexcjohnson style):

    app = MultiPageApp(__name__)

    page = Page()
    page.layout = html.Div(header.children + [
            html.H3('Home'),
            dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0),
            html.Div(id='display-value'),
        ])

    @page.callback(Output('display-value', 'children'), [Input('interval-component', 'n_intervals')])
    def my_callback(n_intervals):
        return f"Seconds since load: {n_intervals}."

    # This will serve the page at "/"
    app.set_routes(page)

    if __name__ == '__main__':
        app.run_server(debug=True)
