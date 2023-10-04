"""
Konversi Jarak dari km->m->cm
- rumus km -> m: km*1000
- rumus m -> cm: m*100
"""
km = float(input('Masukkan jarak km: '))

m = km*1000
cm = m*100

print(f'km: {km}\nm: {m}\ncm: {cm}')