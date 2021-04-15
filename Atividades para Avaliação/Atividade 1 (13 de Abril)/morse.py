print("========================")
print("TRADUTOR DE CÓDIGO MORSE")
print("========================")
print("\n")

dictionaryOfMorseCode = {'A': '.-',   'B': '-...',    'C': '-.-.',    'D': '-..',
       'E': '.',    'F': '..-.',    'G': '--.',     'H': '....',
       'I': '..',   'J': '.---',    'K': '-.-',     'L': '.-..',
       'M': '--',   'N': '-.',      'O': '---',     'P': '.--.',
       'Q': '--.-', 'R': '.-.',     'S': '...',     'T': '-',
       'U': '..-',  'V': '...-',    'W': '.--',     'X': '-..-',
       'Y': '-.--', 'Z': '--..',

       '0': '-----',    '1': '.----',   '2': '..---',   '3': '...--',
       '4': '....-',    '5': '.....',   '6': '-....',   '7': '--...',
       '8': '---..',    '9': '----.',   ' ': '\n'
        }

i = 1
inMorse = ''
while i == 1:
    texto = input('Digite seu texto para tradução: ').upper()
    for char in texto:
        if char != ' ':
            inMorse = inMorse + dictionaryOfMorseCode.get(char) + ' '
        else:
            inMorse = inMorse + ' '     
    i = i+1
 
print(f'A Tradução em Código Morse é: {inMorse}')
print('\n')
decision = int(input('Deseja ver a tradução letra por letra?\n\t1 - Sim\n\t2 - Não\n\tDigite uma Opção: '))
if decision == 1:
    print('\n')
    i = 1
    morse = ''
    while i == 1:
        for char in texto:
            morse = dictionaryOfMorseCode[char]
            if char != ' ':
                print("{} = {}".format(char, morse))
            else:
                print(morse)     
        i = i+1
else:
    print('\nObrigado por usar nosso tradutor!')