# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodBilling
from random import randint

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)
    invoice_items = [
        {
            "invoiceItemId": 64267,
            "price": 4500,
            "quantity": 1,
            "itemDescription": "محصول اول در پایتون"
        },
        {
            "invoiceItemId": 64268,
            "price": 8000,
            "quantity": 3,
            "itemDescription": "محصول دوم در پایتون - کاهش تعداد محصولات از 5 به 3"
        }
    ]
    invoice_id = 123456

    invoice = pod_billing.reduce_invoice(invoice_id=invoice_id, items=invoice_items, preferred_tax_rate=0.09)
    print("Invoice :\n", invoice)
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

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
