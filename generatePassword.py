import random, string

tamanho = 16

chars = string.ascii_letters + string.digits + '!@#$%&*()_-+=´`?/:;,.\|/'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))