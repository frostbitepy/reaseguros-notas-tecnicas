"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from listado_reaseguros.state import State
from listado_reaseguros.navbar_component import navbar

import reflex as rx
import pandas as pd

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"
color = "rgb(107,99,246)"

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


@rx.page(route="/test", title="Test route")
def cuenta():
    return rx.fragment(
        rx.vstack(
            rx.heading("Cuentas Técnicas", font_size="1.5em", padding="1em"),
            rx.box("Upload file"),
            rx.upload(
                rx.text(
                    "Drag and drop files here or click to select files"
                ),
                border="2px dashed",
                bg='gray.50',
                padding="2em",
                boxShadow='md',
                ),
            rx.hstack(rx.foreach(rx.selected_files, rx.text)),
            rx.button(
                "Upload",
                on_click=lambda: State.handle_upload(rx.upload_files()),
            ),
            rx.button(
                "Convert to DataFrame",
                on_click=lambda: State.convert_to_df(rx.upload_files()),
            ),
            rx.html(State.df_html),
        ),
    )
    

# Create app instance and add index page.
app = rx.App()


