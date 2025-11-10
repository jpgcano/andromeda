""" 
    Nivel 5 — Retos (Integración de todo)
    Objetivo: Aplicar todos los conceptos vistos en problemas más completos.
    Cajero automático.
"""

""" 
    Cajeros programado con clases
"""
class Cajero():
    def __init__(self,cuenta,):
        self.cuenta = cuenta
    def ConsultarSaldo(self):
        return f"El saldo actual es: {self.cuenta['saldo']}"
    def AgregarSaldo(self,monto):
        self.cuenta['saldo'] += monto
        return f"Movimiento Finalizado, su saldo actual es: {self.cuenta['saldo']}"
    def RetirarSaldo(self,monto):
        if self.cuenta['saldo'] >= monto:
            self.cuenta['saldo'] -= monto
            return f"Se retiraron {monto} de su cuenta, Su saldo actual es: {self.cuenta['saldo']}"
        else:
            return f"Fondos insuficientes"


cuentas = [
    {"saldo": 100000},
    {"saldo": 50000},
    {"saldo": 20000},
]

# crear objetos Cajero
usuarios = [Cajero(c) for c in cuentas]

# pruebas
print("=== TEST 1: Consultar saldo inicial ===")
for u in usuarios:
    u.ConsultarSaldo()

print("\n=== TEST 2: Agregar saldo ===")
print(usuarios[0].AgregarSaldo(50000))
print(usuarios[1].AgregarSaldo(10000))
print(usuarios[2].AgregarSaldo(30000))

print("\n=== TEST 3: Retirar saldo válido ===")
print(usuarios[0].RetirarSaldo(40000))
print(usuarios[1].RetirarSaldo(20000))
print(usuarios[2].RetirarSaldo(10000))

print("\n=== TEST 4: Retirar más de lo disponible ===")
print(usuarios[0].RetirarSaldo(200000))
print(usuarios[1].RetirarSaldo(100000))
print(usuarios[2].RetirarSaldo(60000))