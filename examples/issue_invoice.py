# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodBilling
from random import randint

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)
    products = [
        {
            "productId": 0,
            "price": 4500,
            "quantity": 0.1,
            "productDescription": "محصول اول در پایتون"
        },
        {
            "productId": 0,
            "price": 8000,
            "quantity": 5,
            "productDescription": "محصول دوم در پایتون"
        }
    ]
    # invoice = pod_billing.issue_invoice(products=products, guild_code=GUILD_CODE, userId=16849)
    # print("Invoice :\n", invoice)
    # OUTPUT
    # Invoice :
    # {
    #   'id': 59529,
    #   'totalAmountWithoutDiscount': 44500,
    #   'delegationAmount': 0,
    #   'totalAmount': 44500,
    #   'payableAmount': 48505,
    #   'vat': 4005,
    #   'issuanceDate': 1578407318877,
    #   'deliveryDate': 0,
    #   'paymentBillNumber': '1047931',
    #   'uniqueNumber': 'fc5e208662484502',
    #   'paymentDate': 0,
    #   'payed': False,
    #   'serial': 0,
    #   'canceled': False,
    #   'cancelDate': 0,
    #   'business': {
    #       'id': 7867,
    #       'name': 'شرکت رضا',
    #       'numOfProducts': 370,
    #       'rate': {
    #           'rate': 8.0,
    #           'rateCount': 1
    #       },
    #       'sheba': '640170000000108200000007'
    #   },
    #   'invoiceItemSrvs': [
    #       {
    #           'id': 64267,
    #           'amount': 4500,
    #           'description': 'محصول اول در پایتون',
    #           'quantity': 1,
    #           'discount': 0,
    #           'voucherUsageSrvs': []
    #       },
    #       {
    #           'id': 64268,
    #           'amount': 8000,
    #           'description': 'محصول دوم در پایتون',
    #           'quantity': 5,
    #           'discount': 0,
    #           'voucherUsageSrvs': []
    #       }
    #   ],
    #   'guildSrv': {
    #       'id': 561,
    #       'name': 'سرویس دهندگان',
    #       'code': 'API_GUILD'
    #   },
    #   'userSrv': {
    #       'id': 16849,
    #       'name': 'رضا زارع',
    #       'ssoId': '11923337',
    #       'ssoIssuerCode': 1,
    #       'profileImage': 'https://core.pod.ir:443/nzh/image/?imageId=....'
    #   },
    #   'cellphoneNumber': '09370000941',
    #   'closed': False,
    #   'verificationNeeded': False,
    #   'safe': False,
    #   'postVoucherEnabled': False,
    #   'referenceNumber': '70063130',
    #   'issuerSrv': {
    #       'id': 16128,
    #       'name': 'شرکت رضا زارع',
    #       'ssoId': '11963175',
    #       'ssoIssuerCode': 1,
    #       'profileImage': 'https://core.pod.ir:443/nzh/image/?imageId=....'
    #   },
    #   'willBeBlocked': False,
    #   'willBePaid': False,
    #   'unsafeCloseTimeOut': 0,
    #   'subInvoice': False,
    #   'edited': False,
    #   'waiting': False
    # }
    bill_number = "Py_{}".format(randint(1, 100000000))
    params = {
        "redirectURL": "https://karthing.ir/test.php?invoice=true&billNumber=" + bill_number,
        "userId": 16849,    # شناسه کاربری که قصد دارید برایش فاکتور صادر کنید. اگر شناسه کاربر را ندارید 0 ارسال کنید
        "billNumber": bill_number,    # شناسه قبض که باید یکتا باشد
        "description": "ثبت سفارش با اطلاعات کامل",
        "deadline": "1398/12/01",   # تاریخ سر رسید
        "currencyCode": "IRR",  # default : IRR
        "addressId": 0,  # شناسه آدرسی که از لیست آدرس های کاربر دریافت کرده اید
        "voucherHash": [],  # لیست بن های تخفیف برای اعمال بر روی فاکتور
        "preferredTaxRate": 0.09,
        "verificationNeeded": False,
        "verifyAfterTimeout": True,
        "preview": False,
        "safe": False,
        "postVoucherEnabled": True,
        "hasEvent": False,
        "eventTitle": "صدور فاکتور با پایتون",
        "eventTimeZone": "Asia/Tehran",
        "eventDescription": "این رویداد برای یک فاکتور که از طریق پایتون ثبت شده، ثبت شده است",
        "metadata": {"name": "reza", "family": "zare", "price": 12000000},
        "eventMetadata": {"event_type": ["email", "notification"], "id": "1,2"},
        "eventReminders": [{"id": 1, "alarmTime": 1578472427000, "alarmType": "Email"},
                           {"id": 2, "alarmTime": 1578472427000, "alarmType": "Notification"}],
        "sc_voucher_hash": SC_VOUCHER_HASH,
        "sc_api_key": SC_API_KEY,
    }

    invoice = pod_billing.issue_invoice(products=products, guild_code=GUILD_CODE, **params)
    print("Invoice :\n", invoice)
    # OUTPUT
    # Invoice :
    # {
    #     'id': 59678,
    #     'totalAmountWithoutDiscount': 44500,
    #     'delegationAmount': 0,
    #     'totalAmount': 44500,
    #     'payableAmount': 48505,
    #     'vat': 4005,
    #     'issuanceDate': 1578481916475,
    #     'deliveryDate': 1582144200000,
    #     'billNumber': 'Py_56555977',
    #     'paymentBillNumber': '1048043',
    #     'uniqueNumber': 'f924fcbf0949e9b',
    #     'description': 'ثبت سفارش با اطلاعات کامل',
    #     'paymentDate': 0,
    #     'payed': False,
    #     'serial': 0,
    #     'canceled': False,
    #     'cancelDate': 0,
    #     'business': {
    #         'id': 7867,
    #           'name': 'شرکت رضا',
    #           'numOfProducts': 370,
    #           'rate': {
    #               'rate': 8.0,
    #                'rateCount': 1
    #           },
    #           'sheba': '640170000000000000000007'
    #     },
    #     'invoiceItemSrvs': [
    #         {
    #             'id': 64444,
    #              'amount': 4500,
    #              'description': 'محصول اول در پایتون',
    #              'quantity': 1,
    #              'discount': 0,
    #              'voucherUsageSrvs': []
    #         },
    #         {
    #             'id': 64445,
    #              'amount': 8000,
    #              'description': 'محصول دوم در پایتون',
    #              'quantity': 5,
    #              'discount': 0,
    #              'voucherUsageSrvs': []
    #         }
    #     ],
    #     'guildSrv': {
    #         'id': 561,
    #         'name': 'سرویس دهندگان',
    #         'code': 'API_GUILD'
    #     },
    #     'userSrv': {
    #         'id': 16849,
    #         'name': 'رضا زارع',
    #         'ssoId': '11923337',
    #         'ssoIssuerCode': 1,
    #         'profileImage': 'https://core.pod.ir:443/nzh/image/?imageId=...'
    #     },
    #     'cellphoneNumber': '09375334941',
    #     'closed': False,
    #     'verificationNeeded': False,
    #     'metadata': '{"name": "reza", "family": "zare", "price": 12000000}',
    #     'safe': False,
    #     'postVoucherEnabled': True,
    #     'referenceNumber': '70186028',
    #     'issuerSrv': {
    #         'id': 16128,
    #         'name': 'شرکت رضا زارع',
    #         'ssoId': '11963175',
    #         'ssoIssuerCode': 1,
    #         'profileImage': 'https://core.pod.ir:443/nzh/image/?imageId=...'
    #     },
    #     'willBeBlocked': False,
    #     'willBePaid': False,
    #     'unsafeCloseTimeOut': 0,
    #     'subInvoice': False,
    #     'edited': False,
    #     'waiting': False
    # }

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
