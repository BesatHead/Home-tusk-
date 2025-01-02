def send_email(message, recipient, *, sender = 'university.help@gmail.com'):

    def valid_email(email):
        return '@' in email and (email.endswith('.com') or email.endswith('.ru') or email.endswith('.net'))

    if not valid_email(recipient) or not valid_email(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

print()
send_email('Коля, привет!', 'Nikolai@gmail.com')
print('__________________________________________________________')
send_email('Коля привет!', 'Nikolai@gmail.com', sender = 'Leonid@gmail.com')
print('__________________________________________________________')
send_email('Леонид, проверка связи!', 'Leonid@gmail.com', sender = 'Leonid@gmail.com')
print('__________________________________________________________')
send_email('Проверка связи', 'Leonid-email', sender = 'university.help@gmail.com')
print('__________________________________________________________')