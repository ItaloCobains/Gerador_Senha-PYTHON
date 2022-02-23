## Importações

import random;
##import string;


## Inpunt
length = int(input("\nDigite o tamanho da senha:"))

## Dados.

toLower = "abcdefghijklmnopqrstuvwxyzç" ## Ou string.ascii_lowercase
toUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ" ## Ou string.ascii_uppercase
numbers = "0123456789" ## Ou string.digits
symbols = '!"' + "#$%&'()*+,-./:;<=>?@[\]^_`{|}~|" ## Ou string.punctuation

## Juntando/Combinando os dados.
all = toLower + toUpper + numbers + symbols
## print(all)

## Criando a senha.
password = "".join(random.sample(all, length))

## Terminal.
print(password)