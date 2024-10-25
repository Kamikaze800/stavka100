import json
from yookassa import Configuration, Payment
import config
import asyncio

Configuration.account_id = config.SHOP_ID
Configuration.secret_key = config.SHOP_API_TOKEN


def payment(value, description):
    payment = Payment.create({
        "amount": {
            "value": value,
            "currency": "RUB"
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/Stavka228_bot"
        },
        "capture": True,
        "description": description
    })
    # file_path = 'data.json'
    # with open(file_path, 'w') as json_file:
    #     json.dump(payment.json(), json_file, indent=4, separators=(',', ': '))
    return json.loads(payment.json())


# async def check_payment(payment_id):
#     payment_dict = json.loads((Payment.find_one(payment_id)).json())
#     while payment_dict['status'] == 'pending':
#         payment_dict = json.loads((Payment.find_one(payment_id)).json())
#         await asyncio.sleep(3)
#
#     if payment_dict['status'] == 'succeeded':
#         print("SUCCSESS RETURN")
#         print(payment)
#         return True
#     else:
#         print("BAD RETURN")
#         print(payment)
#         return False
