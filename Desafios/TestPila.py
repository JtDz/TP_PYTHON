import unittest
import Pila

class TestPila(unittest.TestCase):
    
    def test_case1(self):
        """ Testea que la pila este vacia"""
        self.assertEqual(Pila.es_vacia(),True)
    
    def test_case2(self):
        """ Testea que no devuelva tope si la pila es vacía"""
        self.assertEqual("La Pila esta vacía", obj.tope())
    
    def test_case3(self):
        """ Testea que se agregue un elemento a la pila"""
        self.assertEqual(obj.apilar(10), obj.tope())

    def test_case4(self):
        """ Testea que desapile el ultimo elemento"""
        self.assertEqual(obj.desapilar(10), 10)   
        
    def test_case5(self):
        """ Testea que no desapile si la pila esta vacia """
        self.assertEqual("La Pila esta vacía", obj.desapilar())

    def test_case6(self):
        """ Testea que se levante TypeError si se manda más de un argumento """
        self.assertRaises(TypeError, obj.apilar(3,3))
    
    def test_case7(self):
        """ Testea que se levante TypeError si no se le manda un argumento """
        self.assertRaises(TypeError, obj.apilar())
        
    def test_case8(self):
        """ Testea que se levante el error TypeError si se le manda un argumento """
        self.assertRaises(TypeError, obj.desapilar(2))
    
if __name__ == '__main__':
    unittest.main()
