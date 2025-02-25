import random
import string

dovzhina = int(input("Введіть довжину пароля (від 6 до 32)"))
if dovzhina < 6 or dovzhina > 32:
    print("Пароль має бути від 6 до 32 не більше і не менше")
else:
    znak = string.ascii_letters + string.digits + "!@#$%^&*()_-=+?/.,<>;:"
    while True:
        password = ''.join(random.choice(znak) for _ in range(dovzhina))

        if (any(x.islower() for x in password) and
                any(x.isupper() for x in password) and
                any(x.isdigit() for x in password) and
                any(x in "!@#$%^&*()_-=+?/.,<>;:" for x in password)):
            print(f"Ваш пароль: {password}")
            break