from dash.dependencies import Input, Output
from dash import dcc, html 

# import pages
from pages.chatbot.chatbot_view import render_chatbot
from pages.chatbot.chatbot_controller import *
from pages.page_not_found import page_not_found

from app import app

from environment.settings import APP_HOST, APP_PORT, APP_DEBUG

server = app.server

def serve_content():
    """
    :return: html div component
    """
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])


app.layout = serve_content()


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    """
    :param pathname: path of the actual page
    :return: page
    """
    print('show page')

    if pathname in '/' or pathname in '/chatbot':
        return render_chatbot()
    return page_not_found()


if __name__ == '__main__':
    app.run_server(debug=APP_DEBUG, host=APP_HOST, port=APP_PORT)