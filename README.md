[![Build Status](https://travis-ci.org/sjtrny/dash-multi.svg?branch=master)](https://travis-ci.org/sjtrny/dash-multi)
[![Documentation Status](https://readthedocs.org/projects/dash-multi/badge/?version=latest)](https://dash-multi.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/dash-multi)](https://pepy.tech/project/dash-multi)

# Dash Multi(Page)

Wrapper on top of Dash to support multi page apps.

### Running Examples

Run one of:

- index.py
- standalone_page.py
- standalone_section.py

### Illustrative Example

#### Create a single page app
    
    server = Flask(__name__)
    
    app = Page1(name="home", server=server, url_base_pathname="/")
    
    if __name__ == "__main__":
        server.run(host="0.0.0.0")

#### Create a multipage app (Method 1)

    server = Flask(__name__)
    
    index_app = IndexApp(name="home", server=server, url_base_pathname="/")
    section_app = Section(name="section", server=server, url_base_pathname="/app1")
    
    if __name__ == "__main__":
        server.run(host="0.0.0.0")

#### Create a multipage app (Method 2)

    class MyApp(MultiPageApp):
        def get_routes(self):
    
            return [
                Route(IndexApp, "index", "/"),
                Route(Section, "home", "/app1")
            ]
    
    server = Flask(__name__)
    
    app = MyApp(name="", server=server, url_base_pathname="")
