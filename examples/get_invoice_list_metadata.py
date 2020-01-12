# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodBilling

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)

    meta_query = {
        "field": "name",
        "has": "reza"
    }

    meta_query = {
        "field": "price",
        "gt": "1200000"
    }

    invoices = pod_billing.get_invoice_list_by_metadata(meta_query, sc_api_key=SC_API_KEY, sc_voucher_hash=[])
    print("Invoices :\n", invoices)
    print("Total :", pod_billing.total_items())
    # OUTPUT
    # Invoices :
    # [
    #   {
    #     "id": 59678,
    #     "totalAmountWithoutDiscount": 44500,
    #     "delegationAmount": 0,
    #     "totalAmount": 44500,
    #     "payableAmount": 48505,
    #     "vat": 4005,
    #     "issuanceDate": 1578481916475,
    #     "deliveryDate": 1582144200000,
    #     "billNumber": "Py_56555977",
    #     "paymentBillNumber": "1048043",
    #     "uniqueNumber": "f924fcbf0949e9b",
    #     "description": "ثبت سفارش با اطلاعات کامل",
    #     "paymentDate": 0,
    #     "payed": false,
    #     "serial": 0,
    #     "canceled": false,
    #     "cancelDate": 0,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 370,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000108211752007"
    #     },
    #     "invoiceItemSrvs": [
    #       {
    #         "id": 64444,
    #         "amount": 4500,
    #         "description": "محصول اول در پایتون",
    #         "quantity": 1,
    #         "discount": 0,
    #         "voucherUsageSrvs": []
    #       },
    #       {
    #         "id": 64445,
    #         "amount": 8000,
    #         "description": "محصول دوم در پایتون",
    #         "quantity": 5,
    #         "discount": 0,
    #         "voucherUsageSrvs": []
    #       }
    #     ],
    #     "guildSrv": {
    #       "id": 561,
    #       "name": "سرویس دهندگان",
    #       "code": "API_GUILD"
    #     },
    #     "userSrv": {
    #       "id": 16849,
    #       "name": "رضا زارع",
    #       "ssoId": "11923337",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "cellphoneNumber": "09375334941",
    #     "closed": false,
    #     "verificationNeeded": false,
    #     "metadata": "{\"name\": \"reza\", \"family\": \"zare\", \"price\": 12000000}",
    #     "safe": false,
    #     "postVoucherEnabled": true,
    #     "referenceNumber": "70186028",
    #     "issuerSrv": {
    #       "id": 16128,
    #       "name": "شرکت رضا زارع",
    #       "ssoId": "11963175",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "willBeBlocked": false,
    #     "willBePaid": false,
    #     "unsafeCloseTimeOut": 0,
    #     "subInvoice": false,
    #     "edited": false,
    #     "waiting": false
    #   },
    #   {
    #     "id": 59674,
    #     "totalAmountWithoutDiscount": 44500,
    #     "delegationAmount": 0,
    #     "totalAmount": 44500,
    #     "payableAmount": 48505,
    #     "vat": 4005,
    #     "issuanceDate": 1578476050255,
    #     "deliveryDate": 1582144200000,
    #     "billNumber": "Py_65329976",
    #     "paymentBillNumber": "1048039",
    #     "uniqueNumber": "9b0369ef05f5ff03",
    #     "description": "ثبت سفارش با اطلاعات کامل",
    #     "paymentDate": 0,
    #     "payed": false,
    #     "serial": 0,
    #     "canceled": false,
    #     "cancelDate": 0,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 370,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000108211752007"
    #     },
    #     "invoiceItemSrvs": [
    #       {
    #         "id": 64439,
    #         "amount": 4500,
    #         "description": "محصول اول در پایتون",
    #         "quantity": 1,
    #         "discount": 0,
    #         "voucherUsageSrvs": []
    #       },
    #       {
    #         "id": 64440,
    #         "amount": 8000,
    #         "description": "محصول دوم در پایتون",
    #         "quantity": 5,
    #         "discount": 0,
    #         "voucherUsageSrvs": []
    #       }
    #     ],
    #     "guildSrv": {
    #       "id": 561,
    #       "name": "سرویس دهندگان",
    #       "code": "API_GUILD"
    #     },
    #     "userSrv": {
    #       "id": 16849,
    #       "name": "رضا زارع",
    #       "ssoId": "11923337",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "cellphoneNumber": "09375334941",
    #     "closed": false,
    #     "verificationNeeded": false,
    #     "metadata": "{\"name\": \"reza\", \"family\": \"zare\", \"price\": 12000000}",
    #     "safe": false,
    #     "postVoucherEnabled": true,
    #     "referenceNumber": "70175508",
    #     "issuerSrv": {
    #       "id": 16128,
    #       "name": "شرکت رضا زارع",
    #       "ssoId": "11963175",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "willBeBlocked": false,
    #     "willBePaid": false,
    #     "unsafeCloseTimeOut": 0,
    #     "subInvoice": false,
    #     "edited": false,
    #     "waiting": false
    #   }
    # ]
    # Total : 2

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
