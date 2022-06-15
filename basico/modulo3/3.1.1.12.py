year = int(input("Introduce un año: "))

if not(year % 4 ==0):
    print("año comun")
elif not(year % 100==0):
    print("año bisiesto")
elif not(year%400==0):
    print("año comun")
else:
    print("año bisiesto")

    '''pendiente'''