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
        "sheba": "IR640170000000000000000007",
        "currencyCode": "IRR",
        "uniqueId": str(randint(10000, 99999999)),
        "description": "درخواست برداشت وجه با پایتون",
    }
    print(pod_settlement.request_wallet_settlement(amount=10000, **params))

    # OUTPUT
    # {
    #   "id": 8057,
    #   "amount": 10000,
    #   "requestDate": 1581851133317,
    #   "customerProfileSrv": {
    #     "version": 25,
    #     "firstName": "شرکت رضا",
    #     "lastName": "زارع",
    #     "name": "re******2",
    #     "email": "rz***e@gmail.com",
    #     "nationalCode": "0800000002",
    #     "nickName": "re******2",
    #     "birthDate": 635459400000,
    #     "followingCount": 6,
    #     "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=...",
    #     "joinDate": 1564292432135,
    #     "cellphoneNumber": "09220000006",
    #     "userId": 16128,
    #     "sheba": "640170000000000000000007",
    #     "guest": False,
    #     "chatSendEnable": True,
    #     "chatReceiveEnable": True,
    #     "username": "re******2",
    #     "ssoId": "11963175",
    #     "ssoIssuerCode": 1,
    #     "legalInfo": {},
    #     "financialLevelSrv": {
    #       "id": 0,
    #       "level": "USER_FINANCIAL_LEVEL_CELLPHONE_VERIFIED",
    #       "levelName": "کاربر با شماره موبایل تایید شده",
    #       "value": 1
    #     },
    #     "readOnlyFields": "score,followingCount,joinDate"
    #   },
    #   "settleDate": 1581851133528,
    #   "status": "SETTLEMENT_DONE",
    #   "currency": {
    #     "name": "ریال",
    #     "code": "IRR"
    #   },
    #   "toolCode": "SETTLEMENT_TOOL_PAYA",
    #   "toolId": "640170000000000000000007",
    #   "firstName": "شرکت رضا",
    #   "lastName": "زارع",
    #   "settlementLogSrvs": [
    #     {
    #       "success": True,
    #       "date": 1581851133528
    #     }
    #   ],
    #   "wallet": "PODLAND_WALLET",
    #   "description": "درخواست برداشت وجه با پایتون",
    #   "uniqueId": "1234560",
    #   "instant": False,
    #   "sendToBankDate": 1581851133505
    # }

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
