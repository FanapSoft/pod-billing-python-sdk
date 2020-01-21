# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodVoucher

try:
    pod_voucher = PodVoucher(api_token=API_TOKEN, server_type=SERVER_MODE)
    vouchers = [
        {
            "name": "اعتبار هزار ریالی",
            "amount": 1000,
            "count": 5,
            "description": "Credit 1,000 Rials"
        },
        {
            "name": "اعتبار دو هزار ریالی",
            "amount": 2000,
            "count": 3,
            "description": "Credit 2,000 Rials"
        }
    ]

    expire_date = "1400/12/01"

    print(pod_voucher.define_credit_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                            expire_date=expire_date))

    # OUTPUT
    # [
    #   {
    #     "id": 89841,
    #     "active": True,
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
    #       "id": 52,
    #       "name": "پوشاک",
    #       "code": "CLOTHING_GUILD"
    #     },
    #     "hash": "G6********HJ",
    #     "name": "اعتبار هزار ریالی",
    #     "description": "Credit 1,000 Rials",
    #     "creditAmount": 1000,
    #     "discountPercentage": 0,
    #     "creationDate": 1579438461902,
    #     "expireDate": 1645302600000,
    #     "productList": [],
    #     "dealerBusinessList": [],
    #     "usedAmount": 0,
    #     "type": 1,
    #     "usageList": [],
    #     "used": False
    #   },
    #   ...
    #   {
    #     "id": 89846,
    #     "active": True,
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
    #       "id": 52,
    #       "name": "پوشاک",
    #       "code": "CLOTHING_GUILD"
    #     },
    #     "hash": "OI********LG",
    #     "name": "اعتبار دو هزار ریالی",
    #     "description": "Credit 2,000 Rials",
    #     "creditAmount": 2000,
    #     "discountPercentage": 0,
    #     "creationDate": 1579438461910,
    #     "expireDate": 1645302600000,
    #     "productList": [],
    #     "dealerBusinessList": [],
    #     "usedAmount": 0,
    #     "type": 1,
    #     "usageList": [],
    #     "used": False
    #   },
    #   ...
    # ]

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
