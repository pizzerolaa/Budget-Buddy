import flet as ft
from views.home import HomeView

def main(page: ft.Page):
    page.title= "Mi app"
    page.go("/home")

    #Rutas para las vistas
    def route_change(route):
        page.views.clear()
        if page.route  == "/home":
            page.views.append(HomeView(page))
        page.update()
    
    page.on_route_change = route_change

ft.app(target=main)