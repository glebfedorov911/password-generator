import random
import time
start = time.perf_counter()

let = 'qwertyuiopasdfghjklzxcvbnm'
num = '1234567890'
spec_sim = '%*)?@#$_'
let_big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
symbol = [let, num, spec_sim, let_big]
wish_symbol = input(F'a-z (1), 0-9 (2), spec (3), A-Z(4): ')

itog = ''

for s in wish_symbol:
    itog += symbol[int(s)-1]

def genetare_password(symbol, length):
    for s in range(length):
        r = random.randint(0, len(symbol)-1)
        yield symbol[r]

def password_itog(func):
    password = ''
    for i in func:
        password += i

    return password

password = password_itog(genetare_password(itog, length=int(input('Введите количество символов: '))))

print(password)
finished = time.perf_counter() - start
print(finished)


z = input()