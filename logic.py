from datetime import datetime
import pytz
from aiogram_forms.errors import ValidationError

from db import select_payments, select_need_payments


def timestamp_to_datetime(timestamp):
    timestamp = timestamp / 1000
    return datetime.fromtimestamp(timestamp, tz=pytz.timezone('Asia/Tashkent'))

def to_timestamp(str_date):
    dt = datetime.strptime(str_date, '%d.%m.%Y')
    return int(dt.timestamp() * 1000)

def sum_payments():
    sum_payments = 0
    payments = select_payments()
    for payment in payments:
        # print(payment[2])
        sum_payments += payment[2]
    return sum_payments


def get_sum_payments():
    payments = sum_payments()
    payments = f"{payments:,.2f}"
    return payments


def get_duty():
    payments = sum_payments()
    duty = 454167000 - payments
    duty = f"{duty:,.2f}"
    return duty


def get_all_need_payments():
    payments = select_need_payments()
    payments_list = []
    for enum, payment in enumerate(payments):
        payment_list = list(payment)
        payment_list[0] = f"{enum + 1}."
        payment_list[2] = f"{payment_list[2]:,.2f}"
        payment_list.append(to_timestamp(payment_list[1]))
        payments_list.append(payment_list)
    payments_list = sorted(payments_list, key=lambda x: x[4])
    return payments_list


def get_all_payments():
    payments = select_payments()
    payments_list = []
    for enum, payment in enumerate(payments):
        payment_list = list(payment)
        payment_list[0] = f"{enum + 1}."
        payment_list[2] = f"{payment_list[2]:,.2f}"
        payment_list.append(to_timestamp(payment_list[1]))
        payments_list.append(payment_list)
    payments_list = sorted(payments_list, key=lambda x: x[3])
    return payments_list



def validate_date_format(date):
    try:
        datetime.strptime(date, '%d.%m.%Y')
        year = datetime.strptime(date, '%d.%m.%Y').year
        if not (year == 2023 or year == 2024 or year == 2025):
            raise ValidationError('Сəне надурыс киритилди.', code='date_prefix')
    except Exception as e:
        raise ValidationError('Сəне надурыс киритилди.', code='date_prefix')


def validate_amount_format(amount):
    try:
        amount = int(amount)
        if amount < 1:
            raise ValidationError('Толеў муғдары надурыс киритилди.', code='amount_prefix')
    except Exception as e:
        raise ValidationError('Толеў муғдары надурыс киритилди.', code='amount_prefix')