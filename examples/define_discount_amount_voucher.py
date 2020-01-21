# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodVoucher

try:
    pod_voucher = PodVoucher(api_token=API_TOKEN, server_type=SERVER_MODE)
    vouchers = [
        {
            "name": "تخفیف ده ریالی",
            "amount": 10,
            "count": 2,
            "description": "Discount 10 Rials"
        },
        {
            "name": "تخفیف بیست ریالی",
            "amount": 20,
            "count": 1,
            "description": "Discount 20 Rials"
        }
    ]

    expire_date = "1400/12/01"

    print(pod_voucher.define_discount_amount_voucher(vouchers=vouchers, guild_code=GUILD_CODE, expire_date=expire_date))

    # OUTPUT
    # [
    #   {
    #     "id": 89873,
    #     "active": true,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 395,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000007"
    #     },
    #     "guild": {
    #       "id": 561,
    #       "name": "سرویس دهندگان",
    #       "code": "API_GUILD"
    #     },
    #     "hash": "ON********JC",
    #     "name": "تخفیف ده ریالی",
    #     "description": "Discount 10 Rials",
    #     "creditAmount": 10,
    #     "discountPercentage": 0,
    #     "creationDate": 1579440676317,
    #     "expireDate": 1645302600000,
    #     "productList": [],
    #     "dealerBusinessList": [],
    #     "usedAmount": 0,
    #     "type": 2,
    #     "usageList": [],
    #     "used": false
    #   },
    #   ...
    #   {
    #     "id": 89875,
    #     "active": true,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 395,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000007"
    #     },
    #     "guild": {
    #       "id": 561,
    #       "name": "سرویس دهندگان",
    #       "code": "API_GUILD"
    #     },
    #     "hash": "SH********HH",
    #     "name": "تخفیف بیست ریالی",
    #     "description": "Discount 20 Rials",
    #     "creditAmount": 20,
    #     "discountPercentage": 0,
    #     "creationDate": 1579440676318,
    #     "expireDate": 1645302600000,
    #     "productList": [],
    #     "dealerBusinessList": [],
    #     "usedAmount": 0,
    #     "type": 2,
    #     "usageList": [],
    #     "used": false
    #   },
    #   ...
    # ]

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
