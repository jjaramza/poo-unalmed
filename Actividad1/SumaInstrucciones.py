# Ejercicio resuelto No 5 del libro de Lógica de Programación de Efrain Oviedo

class SumaInstrucciones:
    """
    Realiza una suma a partir de ciertas instrucciones.
    """
    def __init__(self):
        """
        Constructor para inicializar las variables a emplear
        """
        self.SUMA = 0
        self.X = 20
        self.Y = 40
        
    def realizar_calculos(self):
        """
        Método para realizar los cáculos
        """
        self.SUMA += self.X
        self.X += self.Y ** 2
        self.SUMA += self.X / self.Y
    
    def mostrar_mensaje(self):
        """
        Método para mostrar el resultado de la suma
        """
        self.realizar_calculos() # Se llama al método para que realice los cáculos
        return f"El valor de la suma es: {self.SUMA}"


if __name__ == "__main__":
    # Crear instancia de clase
    sumar_ins = SumaInstrucciones()
    
    # Mostrar resultado
    print(sumar_ins.mostrar_mensaje())
