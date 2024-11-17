# Ejercicio resuelto No 4 del libro de Lógica de Programación de Efrain Oviendo

class Edades:
    """
    A partir de la edad de Juan se calcula la edad de Alberto y Ana.
    Y la edad de la mamá se calcula a partir de los tres hermanos.
    """
    def __init__(self, edad_juan: int):
        """
        Constructor para inicializar las edades basadas en la edad de Juan.
        """
        self.edad_juan: int = edad_juan
        self.edad_alberto: int = (2 * edad_juan) // 3
        self.edad_ana: int = (4 * edad_juan) // 3
        self.edad_mama: int = self.edad_juan + self.edad_alberto + self.edad_ana
        
    def mostrar_edades(self):
        """
        Método para imprimir las edades.
        """
        print("Las edades son:")
        print(f"Alberto = {self.edad_alberto}")
        print(f"Ana = {self.edad_ana}")
        print(f"Juan = {self.edad_juan}")
        print(f"Mamá = {self.edad_mama}")
    

if __name__ == "__main__":
    # Solicita la edad de Juan al usuario
    edad_juan = int(input("Ingrese la edad de Juan: "))
    
    # Crea una instancia de la clase Edades
    salida_edades = Edades(edad_juan)
    
    # Muestra las edades
    salida_edades.mostrar_edades()
