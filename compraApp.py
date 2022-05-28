class Shoplist():
    "Contenedor de articulos"
    def __init__(self,name):
        self.name = name
        self.articulos = []
    
    def cambiarNombre(self,name):
        if name != None or name != "" or name != " ":
            self.name = name
    
    def agregar(self,article):
        self.articulos.append(article)
    
    def tachar(self,article):
        if len(self.articulos) > 0:
            try:
                self.articulos.remove(article)
            except:
                pass
    
class Article():
    def __init__(self,name,quantity,price) -> None:
        self.articleName = name
        self.quantity = quantity
        self.articlePrice = price
    
    def editar(self,name=None,cantidad=None,price=None):
        
        if name != None and name != "" and name != " " :
            self.articleName = name
        if cantidad != None and cantidad != "" and cantidad != " ":
            self.quantity = cantidad
        if price != None and price != "" and price != " ":
            self.articlePrice = price
