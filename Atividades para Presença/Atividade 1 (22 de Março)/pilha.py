# Pilha de Leituras Acumuladas

pilha = []

for x in range (1, 15):
    pilha.insert(0, x)

print(f'\nTenho {len(pilha)} livros para finalizar a leitura.')

for x in range(14, 10, -1):
    print(f'Já finalizei a leitura do livro {x}!')
    pilha.pop(0)

print(f'\nRestam {len(pilha)} livros para ler.')