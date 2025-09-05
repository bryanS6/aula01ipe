#pedir ao usuario a quantidade de km's percorridos e o consumo de gasolina

gas = float(input("Forneça o consumo de gasolina em litros"))
km = float(input("Forneça os km's percorridos"))

gasolina = km / gas

etanol = gasolina * 0.7

print(f"gasolina {gasolina}""km/L")

print(f"etanol {etanol}""km/L")