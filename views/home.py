import flet as ft

def HomeView(page: ft.Page):
    return ft.View(
        "/home",
        controls=[
            ft.Text("Bienvenido a la pagina principal"),
            ft.ElevatedButton(text="Click me", on_click=lambda e: print("Clicked"))
        ]
    )