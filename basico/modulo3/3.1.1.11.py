income = float(input("Introduce el ingreso anual:"))

if income<=85528:
    tax=income*0.18 - 556.02

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
'''pendiente'''