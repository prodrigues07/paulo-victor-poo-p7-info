# Fila de uma Lotérica - Realizar Pagamentos

fila = []

for x in range(1, 9):
    fila.append(x)

print(f'\nAtualmente temos {len(fila)} pessoas na fila da lotérica.')

for x in range(1, 6):
    print(f'A pessoa {x} pagou sua conta!')
    fila.pop(0)

print(f'\nAinda temos {len(fila)} pessoas para realizar o pagamento...')