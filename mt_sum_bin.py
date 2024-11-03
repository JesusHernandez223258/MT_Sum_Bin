import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, binary_numbers):
        """Inicializa la máquina de Turing con números binarios separados por '#'."""
        self.tape = self.initialize_tape(binary_numbers)
        self.head = len(self.tape) - 1  # Inicia al final de la cinta
        self.carry = 0
        self.result = []

    def initialize_tape(self, binary_numbers):
        """Inicializa la cinta de la máquina de Turing con números binarios."""
        return list("#".join(binary_numbers))

    def turing_machine_sum(self):
        """Ejecuta la suma de números binarios en la cinta."""
        # Divide la cinta en dos partes basadas en el separador '#'
        split_index = self.tape.index('#')
        num1 = self.tape[:split_index]
        num2 = self.tape[split_index + 1:]  # El número 2 está después del '#'
        
        # Reversa los números para empezar la suma desde la derecha
        num1.reverse()
        num2.reverse()

        max_length = max(len(num1), len(num2))

        for i in range(max_length):
            bit1 = int(num1[i]) if i < len(num1) else 0
            bit2 = int(num2[i]) if i < len(num2) else 0

            # Calcular suma y acarreo
            total = bit1 + bit2 + self.carry
            result_bit = total % 2  # Bit resultante
            self.carry = total // 2  # Actualizar acarreo

            self.result.append(str(result_bit))

        # Manejar acarreo final
        if self.carry:
            self.result.append('1')

        # Invertir el resultado para obtener el orden binario correcto
        self.result.reverse()
        return ''.join(self.result)


class TuringGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulación de Máquina de Turing - Suma Binaria")
        
        # Crear widgets
        self.label1 = tk.Label(master, text="Número Binario 1:")
        self.label1.pack()
        self.entry1 = tk.Entry(master)
        self.entry1.pack()
        
        self.label2 = tk.Label(master, text="Número Binario 2:")
        self.label2.pack()
        self.entry2 = tk.Entry(master)
        self.entry2.pack()
        
        self.button = tk.Button(master, text="Sumar", command=self.calculate_sum)
        self.button.pack()
        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_sum(self):
        """Calcula la suma de los números binarios ingresados y muestra el resultado."""
        binary1 = self.entry1.get()
        binary2 = self.entry2.get()
        
        # Validar la entrada
        if not all(char in '01' for char in binary1) or not all(char in '01' for char in binary2):
            messagebox.showerror("Error", "Por favor, ingresa números binarios válidos.")
            return
        
        # Crear instancia de la máquina de Turing
        turing_machine = TuringMachine([binary1, binary2])
        
        # Ejecutar la suma
        result = turing_machine.turing_machine_sum()
        
        # Mostrar el resultado
        self.result_label.config(text=f"Suma: {result}")


# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    gui = TuringGUI(root)
    root.mainloop()
