from mainApp import App
""" En App se controlan todos los Shoplist sus operaciones y vistas. Ademas de los Article que contienen """

class Main():
    def __init__(self,app) -> None:
        self.app = app
    
    def start(self):
        self.app.iniciar()

if __name__ == "__main__":
    print("\n Bienvenido a la aplicacion de Listas de Compras")
    Main(App()).start()