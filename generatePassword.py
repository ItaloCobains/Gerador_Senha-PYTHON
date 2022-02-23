## Importações

import random;
import string;


## Inpunt
length = int(input("\nDigite o tamanho da senha:"))

## Dados.

toLower = string.ascii_lowercase
toUpper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

## Juntando os dados.
all = toLower + toUpper + numbers + symbols

## Random
temp = random.sample(all, length)

## Criando a senha.
password = "".join(temp)

## Terminal.
print(password)