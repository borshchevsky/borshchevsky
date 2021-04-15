from random import randint

import vonage

from market.settings import VONAGE_API_KEY, VONAGE_SECRET


def send_sms(phone_number):
    client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_SECRET)
    sms = vonage.Sms(client)
    code = generate_code()
    message = f'Your verification code: {code}'
    response_data = sms.send_message({
        'from': 'Django market',
        'to': phone_number,
        'text': message
    })
    return code, response_data


def generate_code():
    return str(randint(1000, 9999)).zfill(4)
