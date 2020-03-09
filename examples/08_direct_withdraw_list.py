# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodDirectWithdraw

try:
    pod_settlement = PodDirectWithdraw(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        # "wallet": "PODLAND_WALLET",  # کد کیف پول
        "page": 1,
        "size": 50
    }

    print(pod_settlement.direct_withdraw_list(**params))

    # OUTPUT
    # [
    #   {
    #     "id": 323,
    #     "username": USERNAME_BANK,
    #     "depositNumber": DEPOSIT_NUMBER,
    #     "wallet": "PODLAND_WALLET",
    #     "onDemand": True,
    #     "minAmount": 0,
    #     "maxAmount": 1000,
    #     "creationDate": 1583756110102
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
