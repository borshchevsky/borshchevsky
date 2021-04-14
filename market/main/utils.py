from random import randint

from main.mainsms import SMS
from market.settings import MAINSMS_PROJECT_NAME, MAINSMS_API_KEY


def send_sms(phone_number):
    sms = SMS(MAINSMS_PROJECT_NAME, MAINSMS_API_KEY)
    code = generate_code()
    message = f'Your verification code: {code}'
    sms.sendSMS(phone_number, message)
    return code


def generate_code():
    return randint(100000, 999999)
