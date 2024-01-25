import reflex as rx

def navbar():
    return rx.hstack(
        rx.hstack(
            rx.image(src="favicon.ico"),
            rx.heading("Cuentas Técnicas"),
        ),
        rx.spacer(),
        rx.menu(
            rx.menu_button("Menu"),
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
    )
