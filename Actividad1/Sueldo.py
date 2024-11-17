# Ejercicio propuesto No 12 del libro de Lógica de Programación de Efrain Oviedo

class Sueldo:
    """
    Clase para calcular el salario bruto, retención en la fuente y 
    salario neto de un trabajador.
    """
    VALOR_HORA = 5000  # Constante de clase: valor por hora
    RETE_FUENTE = 0.125  # Constante de clase: porcentaje de retención
    
    def __init__(self, horas_laboradas: float):
        """
        Constructor para inicilizar las horas laboradas.
        """
        self.horas_laboradas = horas_laboradas
        
    def calcular_salario_bruto(self) -> float:
        """
        Calcula el salario bruto basado en las horas trabajadas.
        """
        return Sueldo.VALOR_HORA * self.horas_laboradas
        
    def calcular_rete_fuente(self, salario_bruto: float) -> float:
        """
        Calcula el valor de la retención en la fuente sobre el salario bruto.
        """
        return salario_bruto * Sueldo.RETE_FUENTE
    
    def calcular_salario_neto(self, salario_bruto: float, rete_fuente: float) -> float:
        """
        Calcula el salario neto después de retención en la fuente.
        """
        return salario_bruto - rete_fuente
    
    def mostrar_info_salario(self):
        """
        Muestra el detalle del salario del trabajador.
        """
        salario_bruto = self.calcular_salario_bruto()
        rete_fuente = self.calcular_rete_fuente(salario_bruto)
        salario_neto = self.calcular_salario_neto(salario_bruto, rete_fuente)
        
        print(f"Salario bruto: {salario_bruto:.2f}")
        print(f"Retención en la fuente: {rete_fuente:.2f}")
        print(f"Salario netro: {salario_neto:.2f}")


if __name__ == "__main__":
    horas = float(input("Ingrese las horas laboradas: "))
    trabajador = Sueldo(horas)
    trabajador.mostrar_info_salario()
