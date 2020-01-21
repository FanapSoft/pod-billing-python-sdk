# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodVoucher

try:
    pod_voucher = PodVoucher(api_token=API_TOKEN, server_type=SERVER_MODE)
    params = {
        # "type": PodVoucher.DISCOUNT_TYPE_ONE_TIME_INVOICE | PodVoucher.DISCOUNT_TYPE_ONE_TIME_ITEM | PodVoucher.DISCOUNT_TYPE_UNLIMITED,
        # "consumerId": 123456,
        # "hash": "",
        # "name": "",
        # "guildCode": ["API_GUILD", "CLOTHING_GUILD"],
        # "currencyCode": "IRR",
        # "amountFrom": 0,
        # "amountTo": 2000,
        # "discountPercentageFrom": 5,
        # "discountPercentageTo": 10,
        # "expireDateFrom": "1398/12/01",
        # "expireDateTo": "1399/01/01",
        # "productId": [1234, 4567],
        # "consumDateFrom": "1398/12/15",
        # "consumDateTo": "1398/12/17",
        # "usedAmountFrom": 10000,
        # "usedAmountTo": 200000,
        # "active": True,
        # "used": False,
    }

    print(pod_voucher.get_voucher_list(page=1, size=10, **params))

    # OUTPUT
    # [
    #   {
    #     "id": 86282,
    #     "active": False,
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
    #       "id": 62,
    #       "name": "فنی و مهندسی",
    #       "code": "ENGINEERING_GUILD"
    #     },
    #     "limitedConsumer": {
    #       "id": 16849,
    #       "name": "رضا زارع",
    #       "ssoId": "11923337",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "hash": "SL********VS",
    #     "name": "کد تخفیف برای کاربر 16849",
    #     "description": "عجب",
    #     "creditAmount": 100,
    #     "discountPercentage": 0,
    #     "creationDate": 1566212578993,
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
