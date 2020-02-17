# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodSettlement, ToolCodeSettlement
from random import randint

try:
    pod_settlement = PodSettlement(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        "wallet": "PODLAND_WALLET",
        "firstName": "رضا",
        "lastName": "زارع",
        "currencyCode": "IRR",
        "uniqueId": str(randint(10000, 99999999)),
        "description": "درخواست برداشت وجه با پایتون",
    }

    tool_code = ToolCodeSettlement.CARD  # or ToolCodeSettlement.PAYA or ToolCodeSettlement.SATNA
    tool_id = "6037990000000000"  # card number or sheba number

    print(pod_settlement.request_settlement_by_tool(amount=10000, tool_code=tool_code, tool_id=tool_id,
                                                    guild_code=GUILD_CODE, **params))

    # OUTPUT
    # {
    #   "id": 8071,
    #   "amount": 10000,
    #   "requestDate": 1581857580113,
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
    #   "settleDate": 1581857580259,
    #   "status": "SETTLEMENT_DONE",
    #   "currency": {
    #     "name": "ریال",
    #     "code": "IRR"
    #   },
    #   "toolCode": "SETTLEMENT_TOOL_CARD",
    #   "toolId": "6037990000000000",
    #   "firstName": "رضا",
    #   "lastName": "زارع",
    #   "settlementLogSrvs": [
    #     {
    #       "success": true,
    #       "date": 1581857580259
    #     }
    #   ],
    #   "description": "درخواست برداشت وجه با پایتون",
    #   "uniqueId": "64973000",
    #   "instant": false,
    #   "sendToBankDate": 1581857580241
    # }

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
