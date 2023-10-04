"""
Konversi Suhu dari °C -> °F -> °K
- rumus °C -> °F: (°C*9/5)+32
- rumus °F -> °K: (°F-32)*5/9+273.15
"""
c = float(input('Masukkan suhu °C: '))

f = (c*9/5)+32
k = (f-32)*5/9+273.15

print(f'°C: {c}\n°F: {f}\n°K: {k}')
print("C: ", c, "F: ", f, "K: ", k)