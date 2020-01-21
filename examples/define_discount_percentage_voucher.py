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
            "count": 2,
            "description": "Discount 20% with maximum 1,000 Rials",
            "discountPercentage": 20
        },
        {
            "name": "اعتبار دو هزار ریالی",
            "amount": 2000,
            "count": 1,
            "description": "Discount 5% with maximum 2,000 Rials",
            "discountPercentage": 5
        }
    ]

    expire_date = "1400/12/01"

    print(pod_voucher.define_discount_percentage_voucher(vouchers=vouchers, guild_code=GUILD_CODE, discount_type=4,
                                                         expire_date=expire_date))

    # OUTPUT
    # [
    #   {
    #     "id": 89876,
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
    #     "hash": "M4********1M",
    #     "name": "اعتبار هزار ریالی",
    #     "description": "Discount 20% with maximum 1,000 Rials",
    #     "creditAmount": 1000,
    #     "discountPercentage": 20,
    #     "creationDate": 1579443322742,
    #     "expireDate": 1645302600000,
    #     "productList": [],
    #     "dealerBusinessList": [],
    #     "usedAmount": 0,
    #     "type": 4,
    #     "usageList": [],
    #     "used": false
    #   },
    #   {
    #     "id": 89877,
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
    #     "hash": "X8SRU3L5RDZ4",
    #     "name": "اعتبار هزار ریالی",
    #     "description": "Discount 20% with maximum 1,000 Rials",
    #     "creditAmount": 1000,
    #     "discountPercentage": 20,
    #     "creationDate": 1579443322744,
    #     "expireDate": 1645302600000,
    #     "productList": [],
    #     "dealerBusinessList": [],
    #     "usedAmount": 0,
    #     "type": 4,
    #     "usageList": [],
    #     "used": false
    #   },
    #   {
    #     "id": 89878,
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
    #     "hash": "OA********SB",
    #     "name": "اعتبار دو هزار ریالی",
    #     "description": "Discount 5% with maximum 2,000 Rials",
    #     "creditAmount": 2000,
    #     "discountPercentage": 5,
    #     "creationDate": 1579443322744,
    #     "expireDate": 1645302600000,
    #     "productList": [],
    #     "dealerBusinessList": [],
    #     "usedAmount": 0,
    #     "type": 4,
    #     "usageList": [],
    #     "used": false
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
