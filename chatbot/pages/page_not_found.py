from dash import html


def page_not_found():
    """
    :return: html div element
    """

    return html.Div([
        html.H1('404'),
        html.H2('Page not found'),
        html.H2('Oh, something went wrong!')
    ])