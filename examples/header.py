import dash_html_components as html

header = html.Div(
    [
        html.A("Home", href="/"),
        html.Br(),
        html.A("Navigate to Page 1", href="/page1"),
        html.Br(),
        html.A("Navigate to Section 2", href="/page2/"),
    ]
)
