# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodSettlement, StatusSettlement, ToolCodeSettlement

try:
    pod_settlement = PodSettlement(api_token=API_TOKEN, server_type=SERVER_MODE)

    params = {
        # "id": 8071,  # شناسه درخواست
        # "statusCode": StatusSettlement.DONE,  # کد وضعیت درخواست
        # "currencyCode": "IRR",  # کد ارز
        # "fromAmount": 100.0,  # حد پایین مبلغ درخواست شده
        # "toAmount": 999,  # حد بالای مبلغ درخواست شده
        # "fromDate": "1398/11/22",  # حد پایین تاریخ درخواست شمسی yyyy/mm/dd
        # "toDate": "1398/12/01",  # حد بالای تاریخ درخواست شمسی yyyy/mm/dd
        # "uniqueId": "64973000",  # شناسه یکتا
        # "firstName": "رضا",  # نام صاحب حساب
        # "lastName": "زارع",  # نام خانوادگی صاحب حساب
        # "toolCode": ToolCodeSettlement.CARD,  # نوع ابزار برای تسویه کارت به کارت،پایا،ساتنا
        # "toolId": "6037997256803041",  # شماره ابزاری که تسویه به آن واریز گردیده
        # "invoiceId": 1  # شماره فاکتور
    }

    print(pod_settlement.list_settlements(**params))

    # OUTPUT
    # [
    #   {
    #     "id": 8071,
    #     "amount": 10000,
    #     "requestDate": 1581857580113,
    #     "businessSoftSrv": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 471,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000007"
    #     },
    #     "guildSrv": {
    #       "id": 561,
    #       "name": "سرویس دهندگان",
    #       "code": "API_GUILD"
    #     },
    #     "settleDate": 1581857580259,
    #     "status": "SETTLEMENT_DONE",
    #     "currency": {
    #       "name": "ریال",
    #       "code": "IRR"
    #     },
    #     "toolCode": "SETTLEMENT_TOOL_CARD",
    #     "toolId": "6037990000000000",
    #     "firstName": "رضا",
    #     "lastName": "زارع",
    #     "settlementLogSrvs": [
    #       {
    #         "success": true,
    #         "date": 1581857580259
    #       }
    #     ],
    #     "description": "درخواست برداشت وجه با پایتون",
    #     "uniqueId": "64973000",
    #     "instant": false,
    #     "sendToBankDate": 1581857580241,
    #     "invoiceIds": []
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
