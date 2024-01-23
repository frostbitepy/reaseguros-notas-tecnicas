"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from listado_reaseguros.state import State

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


@rx.page()
def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Cuentas Técnicas", font_size="1.5em"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="1.5em",
            padding_top="10%",
        ),
    )

@rx.page(route="/about", title="About my app")
def about():
    return rx.fragment(
        rx.vstack(
            rx.heading("About", 
                        # Event handlers can be bound to event triggers.
                        on_click=State.next_color,
                        # State vars can be bound to component props.
                        color=State.color,
                        _hover={"cursor": "pointer"},
                        font_size="1.5em"),
            rx.box(
            "Reflex is a Python library for building reactive user interfaces with "
            "minimal boilerplate. It's designed to be simple, intuitive, and "
            "powerful. "
        ),
            rx.image(src="/Reflex.svg", width="5em"),
        spacing="1.5em",
        font_size="1em",
        padding_top="5%",
        )
    )

@rx.page(route="/cuenta_tecnica", title="Cuentas Técnicas")
def cuenta_tecnica():
    return rx.upload(
        rx.text(
            "Drag and drop files here or click to select files"
        ),
        spacing="1.5em",
        font_size="1em",
        padding_top="5%",
        border="1px dotted rgb(107,99,246)",
        padding="5em",
    )

# Create app instance and add index page.
app = rx.App()
#app.add_page(index)     
#app.add_page(about, route="/about")
