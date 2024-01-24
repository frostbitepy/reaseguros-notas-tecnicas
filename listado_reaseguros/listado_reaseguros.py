"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from listado_reaseguros.state import State, FileState

import reflex as rx

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
    return rx.fragment(
        rx.vstack(
        rx.heading("Cuentas Técnicas", font_size="1.5em"),
        rx.center(
        rx.hstack(
            rx.upload(
                rx.button(
                "Select File(s)",
                height="30px",
                width="150px",
                color=color,
                bg="white",
                border=f"1px solid {color}",
            ),
            rx.text(
                "Cargar aquí planilla de Emisiones",
                height="40px",
                width="180px",
            ),
            border="1px dotted black",
            padding="2em",
            ), # Upload 
            rx.upload(
                rx.button(
                "Select File(s)",
                height="30px",
                width="150px",
                color=color,
                bg="white",
                border=f"1px solid {color}",
            ),
            rx.text(
                "Cargar aquí planilla de Anulaciones",
                height="40px",
                width="180px",
            ),
            border="1px dotted black",
            padding="2em",
            ), # Upload 
            rx.upload(
                rx.button(
                "Select File(s)",
                height="30px",
                width="150px",
                color=color,
                bg="white",
                border=f"1px solid {color}",
            ),
            rx.text(
                "Cargar aquí planilla de Recuperos",
                height="40px",
                width="180px",
            ),
            border="1px dotted black",
            padding="2em",
            ), # Upload           
        ), # hstack
        ), # center
        rx.vstack(
            rx.button(
                "Upload Files",
                on_click=FileState.handle_upload(rx.upload_files()),
            ), # button
            rx.button(
                    "Clear .xlsx Files",
                    on_click=FileState.clear_xlsx_files,
                ),  # button to clear .xlsx files    
        ),# vstack
        spacing="1.5em",
        font_size="1em",
        padding_top="5%",
        ), # vsatck
        rx.text_area(
                is_disabled=True,
                value=FileState.file_str,
                width="100%",
                height="100%",
                bg="white",
                color="black",
                placeholder="No File",
                min_height="20em",
        ), # text_area
    ) # fragment
    

@rx.page(route="/upload_file", title="Upload xlsx files")
def upload_files():
    return rx.vstack(
        rx.upload(
            rx.button(
                "Select File(s)",
                height="30px",
                width="150px",
                color=color,
                bg="white",
                border=f"1px solid {color}",
            ),
            rx.text(
                "Arrastra los archivos aquí o haz click para seleccionarlos",
                height="60px",
                width="200px",
            ),
            border="1px dotted black",
            padding="2em",
        ),
        rx.hstack(
            rx.button(
                "Upload",
                on_click=FileState.handle_upload(rx.upload_files()),
            ),
        ),
        rx.heading("Files:"),
        rx.cond(
            FileState.is_uploading,
            rx.progress(is_indeterminate=True, color="blue", width="100%"),
            rx.progress(value=0, width="100%"),
        ),
        rx.text_area(
            is_disabled=True,
            value=FileState.file_str,
            width="100%",
            height="100%",
            bg="white",
            color="black",
            placeholder="No File",
            min_height="20em",
        ),
    )

@rx.page(route="/display", title="Display cuenta tecnica")
def upload_files():
    return rx.vstack(
        rx.text_area(
            is_disabled=False,
            value=FileState.file_str,
            width="50%",
            height="50%",
            bg="white",
            color="black",
            placeholder="No File",
            min_height="10em",
        ),
        rx.button(
            "Convert to DataFrame",
            on_click=FileState.convert_to_dataframe(rx.upload_files()[0].filename, rx.get_asset_path(rx.upload_files()[0].filename)),
        ),    
    )

# Create app instance and add index page.
app = rx.App()
#app.add_page(index)     
#app.add_page(about, route="/about")

