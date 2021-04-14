a = float(input('Digite o valor do Lado A: '))
b = float(input('Digite o valor do Lado B: '))
c = float(input('Digite o valor do Lado C: '))

if (a == b and b == c and a==c):
    print('Triângulo do Tipo Equilátero')
elif(a == b and a != c and b != c) or (b == c and a != c and b != a) or (c == a and c != b):
    print('Triângulo do Tipo Isóceles')
else:
    print('Triângulo do Tipo Escaleno')