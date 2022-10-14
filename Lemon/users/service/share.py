from django.core.mail import send_mail


def send(user_email, user_name):
    send_mail(
        'Добро пожаловать на Lemon',
        f'Ваша учетная запись {user_name} была успешно зарегистрирована',
        'LemonSendMes@gmail.com',
        [user_email],
        fail_silently=False,
    )