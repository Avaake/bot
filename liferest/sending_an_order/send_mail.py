import smtplib
from aiogram import types


async def send_email(state):
    # дані SMTP-сервера та облікові дані відправника
    smtp_server = 'smtp.ukr.net'
    smtp_port = 465
    sender_email = 'denisergo11@ukr.net'
    password = 'p1c4T1qGv93nleDm'

    # дані отримувача
    recipient_email = 'denisergo11@ukr.net'
    async with state.proxy() as data:
        # Створюємо з'єднання з SMTP-сервером
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            # Виконуємо вхід в обліковий запис відправника
            server.login(sender_email, password)

            # Створюємо заголовок листа
            order, phone_number, table_number = tuple(data.values())
            subject = 'Заказ'
            email_text = f'From: {sender_email}\nSubject: {subject}\n\nЗаказ:{order}\nномер телефону:{phone_number}\nномер столу:{table_number}'.encode(
                'utf-8')

            # Відправляємо лист
            server.sendmail(sender_email, recipient_email, email_text)
