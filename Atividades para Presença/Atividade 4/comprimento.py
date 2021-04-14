def comprimento(var1, var2, var3):
    if (var1 == var2 and var1 == var3):
        return(True)
    else:
        return(False)

a = float(input('Digite o valor do Lado A: '))
b = float(input('Digite o valor do Lado B: '))
c = float(input('Digite o valor do Lado C: '))

print(comprimento(a, b, c))