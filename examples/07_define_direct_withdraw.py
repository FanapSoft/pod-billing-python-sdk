# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodDirectWithdraw

try:
    pod_settlement = PodDirectWithdraw(api_token=API_TOKEN, server_type=SERVER_MODE)

    with open(PRIVATE_KEY_PATH, "r") as private_key_file:
        private_key = private_key_file.read()

    print(pod_settlement.define_direct_withdraw(username=USERNAME_BANK, private_key=private_key,
                                                deposit_number=DEPOSIT_NUMBER, wallet="PODLAND_WALLET",
                                                on_demand=True, min_amount=0, max_amount=1000))

    # OUTPUT
    # {
    #   "id": 323,
    #   "username": USERNAME_BANK,
    #   "depositNumber": DEPOSIT_NUMBER,
    #   "wallet": "PODLAND_WALLET",
    #   "onDemand": True,
    #   "minAmount": 0,
    #   "maxAmount": 1000,
    #   "creationDate": 1583756110102
    # }

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
