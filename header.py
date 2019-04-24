import dash_core_components as dcc
import dash_html_components as html

header = html.Div([
            dcc.Link('Home', href='/'),
            html.Br(),
            dcc.Link('Navigate to Page 1', href='/page1'),
            html.Br(),
            dcc.Link('Navigate to Section 2', href='/page2/'),
        ])