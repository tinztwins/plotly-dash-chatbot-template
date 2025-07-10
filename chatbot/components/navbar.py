import dash_bootstrap_components as dbc

from environment.settings import VERSION

def render_navbar(brand_name:str = "Chatbot", brand_color:str = "#165AA7"):
    navbar = dbc.NavbarSimple(
            brand=brand_name + " " + VERSION,
            brand_href="/",
            color=brand_color,
            sticky='top',
            links_left=True,
            dark=True,
            expand=True
        )
    return navbar