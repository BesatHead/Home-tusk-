print('Сгенерированы следующие пароли:')
import time

def pairs_password (n):
    password = []

    for i in range (1, n):
        for j in range (i + 1, n + 1):
            sum_pair = i + j
            if n % sum_pair == 0:
                password.append(f'{i}{j}')

    return ''.join(password)

for number in range (3, 21):
    generat_password = pairs_password (number)

    print(f'{number} - {generat_password}')
    time.sleep(0.4)