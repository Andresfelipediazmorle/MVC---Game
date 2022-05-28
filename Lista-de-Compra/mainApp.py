from compraApp import Shoplist, Article
from interApp import Interfaz

class App():
    "Contenedor de listas de compras"
    def __init__(self) -> None:
        self.shopLists = []
        self.show = Interfaz()
    
    def crearList(self):
        self.shopLists.append(Shoplist(self.show.crealista())) # Crea una lista con un nombre 
    
    def editarLista(self):
        
        if self.__check():
            # Se obtiene la lista a editar
            lista = None
            if len(self.shopLists) == 1:
                lista = self.shopLists[0]
            else:
                while type(lista) != Shoplist:
                    try:
                        lista = self.show.mostrarLista(self.shopLists)
                    except:
                        continue

            # Muestra la interfaz de opciones de edicion de la lista de compras
            edit = self.show.menuEditar(lista.name)
            if edit == "1": 
                lista.agregar(self.crearArticulo())
            
            elif edit == "2":
                edit = self.show.menuArticulos(lista) # Selecciona el articulo
                if type(edit) == Article:
                    # si no hay errores elimina el articulo de la lista
                    lista.tachar(edit)

            elif edit == "3":
                # Para editar un articulo de la lista
                edit = self.show.menuArticulos(lista) # Intenta seleccionar un articulo
                if type(edit) == Article: # Si no ocurren errores
                    local = self.crearArticulo() # Se crea un nuevo articulo
                    edit.editar(local.articleName,local.quantity,local.articlePrice) # Se pasan los valores del nuevo articulo al que se quiere editar
                    del local
                
            elif edit == "4":
                # Cambia el nombre de la lista
                lista.cambiarNombre(self.show.crealista()) # Reutiliza la vista de crear una lista
            
            del edit,lista

    def eliminaList(self):
        if self.__check():
            try:
                self.shopLists.remove(self.show.mostrarLista(self.shopLists))
            except :
                return
            
    def crearArticulo(self):
        articleInfo = {"nombre":"","cantidad":"","precio":""} # Para obtener los datos del Article
        articleInfo = self.show.crearArticulomenu(articleInfo) # Actualiza el dict con los datos ingresados por el usuario
        return Article(articleInfo["nombre"],articleInfo["cantidad"],articleInfo["precio"])

    def detalles(self):
        "Sirve para detallar los articulos de una lista seleccionada"
        if self.__check():   
            if len(self.shopLists) == 1:
                # Si tiene una sola lista la muestra directamente
                self.show.menuArticulos(self.shopLists[0]) 
            else:
                self.show.menuArticulos(self.show.mostrarLista(self.shopLists)) # Muestra los detalles de los articulos de una lista seleccionada

    def iniciar(self):
        interact = self.show.menu()
        if interact == "1":
            self.crearList()
        elif interact == "2":
            self.editarLista()
        elif interact == "3":
            self.eliminaList()
        elif interact == "4":
            self.detalles()
        elif interact == "5":
            exit()

        self.iniciar()

    def __check(self):
        "Uso esto porque es repetitivo"
        if len(self.shopLists) > 0: # Si tienes listas
            return True
        else:
            self.show.mensajes("No tienes listas")
        return False
