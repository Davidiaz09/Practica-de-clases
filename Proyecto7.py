#PRACTICA CLASES-CREACION CUENTA BANCARIA

#Definir clase "Persona" con atributos: nombre, apellido.
#Definir clase hija "Cliente". Atributos propios: número de cuenta, balance (saldo disponible).
# Metodos de "Cliente": imprimir: cuando el código pida imprimir "cliente" se muestren todos sus datos, incluyendo el balance
#                        depositar: permitirá depositar dinero en la cuenta.
#                        retirar: permitirá retirar dinero de la cuenta.

#Opciones del programa: depositar(seguir), retirar(seguir), salir(finalizar programa).
#Definir funciones: 1. crear al cliente, definir sus atributos.   2. inicio del programa y mostrar opciones(bucle while).

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, saldo):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        
    def __str__(self):
            
        return f"""Nombre: {self.nombre}
Apellido: {self.apellido}
Numero de cuenta: {self.numero_cuenta}
Saldo: {self.saldo}"""

    def depositar(self, deposito):
        self.saldo += deposito
        
    def retirar(self, retiro):
        if retiro <= self.saldo:
            self.saldo -= retiro
        else:
            print("Lo siento. No tienes suficiente dinero para retirar")
       
            
cliente= Cliente("David", "Orozco", 8686, 1000000)

def inicio():
    print("-"*40)
    print("Cuenta Bancaria\n".upper())
    print(cliente)
    
    opcion= ""
    while opcion != 3:
        print("""\n1. Depositar dinero.
2. Retirar dinero.
3. Salir""")
        opcion = int(input("Elige una opcion: "))
        
        if opcion == 1:
            cantidad_d= int(input("\ncuanto dinero quieres depositar?: "))
            cliente.depositar(cantidad_d)
            print(f"Saldo: {cliente.saldo}")
            
        elif opcion == 2: 
            cantidad_r= int(input("\ncuanto dinero quieres retirar?: "))
            cliente.retirar(cantidad_r)
            print(f"Saldo: {cliente.saldo}")
        
        print("Gracias por operar.")
         
    
inicio()



