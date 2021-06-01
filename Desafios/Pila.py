from typing import List, Any
import string

class Pila:
    
    """Clase que instancia una estructura tipo LI-FO o Pila"""
    
    def __init__(self) -> None:
        self._lista : List[Any] = []
            
    def es_vacia(self) -> bool:
        if len(self._lista) == 0:
            return True
        else:
            return False
    
    def desapilar(self) -> Any:
        if not(self.es_vacia()):
            elem: Any = self._lista.pop()
            return elem
        else:
            return "La Pila esta vacía"
        
    def apilar(self, elem: Any) -> None:
        self._lista.append(elem)

    def tope(self) -> Any:
        if not(self.es_vacia()):
            return self._lista[len(self._lista)]
        else:
            return "La Pila esta vacía"
        
    def __str__(self) -> None:
                    
        def detalle (elem : Any) -> str:
            if self._lista.index(elem) == len(self._lista) - 1:
                return str(elem)
            else:
                x : str = str(elem) + " -> " 
                return x
            
        cadena : str = " ".join(list(map(detalle,self._lista)))
        
        if self.es_vacia():
            return "La Pila no contiene elementos"
        else:
            return cadena
    
if __name__ == "__main__":
    objeto = Pila()
    objeto.apilar(2)
    objeto.apilar(-1)
    objeto.apilar(5)
    objeto.apilar("letra")
    print(objeto)
    print(objeto.desapilar())
    print(objeto.desapilar())
    print(objeto.desapilar())
    print(objeto.desapilar())
    print(objeto.desapilar())
    print(objeto)    





