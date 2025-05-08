class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo=0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def deposito_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${self.saldo}")
        else:
            print("La cantidad debe ser mayor que cero.")

    def retiro_dinero(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def mostrar_saldo(self):
        print(f"\n--- Información de la Cuenta ---")
        print(f"Titular: {self.titular}")
        print(f"Número de Cuenta: {self.numero_cuenta}")
        print(f"Saldo actual: ${self.saldo}")


# Menú interactivo
def menu():
    print("Bienvenido al sistema bancario")
    titular = input("Ingrese el nombre del titular: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")

    cuenta = CuentaBancaria(titular, numero_cuenta)

    while True:
        print("\n--- MENÚ ---")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.deposito_dinero(cantidad)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retiro_dinero(cantidad)
        elif opcion == "3":
            cuenta.mostrar_saldo()
        elif opcion == "4":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()