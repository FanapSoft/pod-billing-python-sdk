# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodSettlement
from random import randint

try:
    pod_settlement = PodSettlement(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        "wallet": "PODLAND_WALLET",
        "firstName": "رضا",
        "lastName": "زارع",
        # "sheba": "IR640170000000000000000007",
        "currencyCode": "IRR",
        "uniqueId": str(randint(10000, 99999999)),
        "description": "درخواست برداشت وجه با پایتون",
    }
    print(pod_settlement.request_guild_settlement(amount=10000, guild_code=GUILD_CODE, **params))

    # OUTPUT
    # {
    #   "id": 8069,
    #   "amount": 10000,
    #   "requestDate": 1581853278696,
    #   "businessSoftSrv": {
    #     "id": 7867,
    #     "name": "شرکت رضا",
    #     "numOfProducts": 471,
    #     "rate": {
    #       "rate": 8,
    #       "rateCount": 1
    #     },
    #     "sheba": "640170000000000000000007"
    #   },
    #   "guildSrv": {
    #     "id": 561,
    #     "name": "سرویس دهندگان",
    #     "code": "API_GUILD"
    #   },
    #   "settleDate": 1581853278823,
    #   "status": "SETTLEMENT_DONE",
    #   "currency": {
    #     "name": "ریال",
    #     "code": "IRR"
    #   },
    #   "toolCode": "SETTLEMENT_TOOL_PAYA",
    #   "toolId": "640170000000000000000007",
    #   "firstName": "رضا",
    #   "lastName": "زارع",
    #   "settlementLogSrvs": [
    #     {
    #       "success": true,
    #       "date": 1581853278823
    #     }
    #   ],
    #   "description": "درخواست برداشت وجه با پایتون",
    #   "uniqueId": "56326808",
    #   "instant": false,
    #   "sendToBankDate": 1581853278804
    # }

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
