# Dash Multi Page/Apps Example

Wrapper on top of Dash to support multi page apps.

### Running Examples

Run one of:

- index.py
- standalone_page.py
- standalone_section.py

### Illustrative Example

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

