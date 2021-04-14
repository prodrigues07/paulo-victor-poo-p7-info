import random

lista = ['Português', 'Matemática', 'História', 'Geografia', 'Biologia', 'Química']

print(f'\nNecessito estudar e realizar as atividades de {len(lista)} disciplinas.')
print(f'São as disciplinas: {lista}\n')

atividade = list(range(1, 3))
random.shuffle(atividade)

for x in atividade:
    print(f'Atividade de {lista[x]} concluída.')
    lista.pop(x)

print(f'\nFalta realizar {len(lista)} atividades.')
print(f'Sendo elas das discciplinas de: {lista}\n')