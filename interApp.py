from os import system
import time

class Interfaz():
    def limpiaPantalla(self):
        system("cls")

    def crealista(self):
        print("\n Nombre de la lista")
        return input(" >>> ")
           
    def mostrarLista(self,listas):
       
        print("\n   Nombre de Lista \n")
        for index,list in enumerate(listas):
            print("   " + str(list.name) + " (%s)"%(index)) # Muestra las listas enumeradas
        print("\n")

        try:
            return listas[int(input(" >>> Seleccione:  "))] # Devuelve la lista que se seleccione 
        except:
            self.mensajes("Lista Inexistente") # Mensaje de error
           
    def menuEditar(self,nameLista):
        # Muestra las opciones para editar listas 
        print("\n Agregar Articulo(1)  Eliminar Articulo(2) Editar Articulo(3) Editar Nombre(4) \n   Lista (%s) \n"%(nameLista))
        return input("  -> Seleccione:  ")

    def crearArticulomenu(self,info:dict):
        "Sirve para cualquier entrada multiple utilizando las claves de un diccionario"

        print("\n")
        for i in info:
            print("%s de Articulo "%(i))
            info[i] = input(" >>> ")
        return info # Devuelve el dict con las entradas del usuario

    def menu(self):
        # Menu Principal de la aplicacion
        print( "\n Crear Lista(1)   Editar Lista(2)   Eliminar Lista(3)  Detallar Lista(4) Salir(5)  ")
        return input("  -> Seleccione una opcion:  ")
    
    def menuArticulos(self,listaDecompras):
        """Recibe un objeto shoplist muestra un menu con los detalles de los articulos del objeto y devuelve  
        un objeto articulo"""

        print("\n Articulos de la lista de compra %s (%s)"%(listaDecompras.name,len(listaDecompras.articulos)))
        if len(listaDecompras.articulos) == 0:
            self.mensajes("Sin articulos")
        else:
            print("\n  Nombre   Cantidad   Precio")
            for index,article in enumerate(listaDecompras.articulos):
                print("\n   {0} {1} {2} ({3})".format(article.articleName,article.quantity,article.articlePrice,index))
            try:
                article = listaDecompras.articulos[int(input(" -> Seleccione: "))]
                return article 
            except:
                self.mensajes("Articulo Inexistente")

    def mensajes(self,message:str):
        # Imprime un mensaje para el usuario
        time.sleep(2)
        self.limpiaPantalla()
        print(" \n %s"%(message) )
    