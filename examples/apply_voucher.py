# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodVoucher, PodBilling

try:
    pod_voucher = PodVoucher(api_token=API_TOKEN, server_type=SERVER_MODE)
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)
    products = [
        {
            "productId": 0,
            "price": 50000,
            "quantity": 1,
            "productDescription": "محصول اول در پایتون"
        }
    ]
    invoice = pod_billing.issue_invoice(products=products, guild_code=GUILD_CODE,
                                        description="تست اعمال کد تخفیف بر روی فاکتور بعد از صدور فاکتور",
                                        postVoucherEnabled=True)
    print(invoice)
    # OUTPUT
    # {
    #   "id": 61489,
    #   "totalAmountWithoutDiscount": 50000,
    #   "delegationAmount": 0,
    #   "totalAmount": 50000,
    #   "payableAmount": 54500,
    #   "vat": 4500,
    #   "issuanceDate": 1579517705964,
    #   "deliveryDate": 0,
    #   "paymentBillNumber": "1049210",
    #   "uniqueNumber": "56b0d97a3aec1034",
    #   "description": "تست اعمال کد تخفیف بر روی فاکتور بعد از صدور فاکتور",
    #   "paymentDate": 0,
    #   "payed": False,
    #   "serial": 0,
    #   "canceled": False,
    #   "cancelDate": 0,
    #   "business": {
    #     "id": 7867,
    #     "name": "شرکت رضا",
    #     "numOfProducts": 395,
    #     "rate": {
    #       "rate": 8,
    #       "rateCount": 1
    #     },
    #     "sheba": "640170000000000000000007"
    #   },
    #   "invoiceItemSrvs": [
    #     {
    #       "id": 66516,
    #       "amount": 50000,
    #       "description": "محصول اول در پایتون",
    #       "quantity": 1,
    #       "discount": 0,
    #       "voucherUsageSrvs": []
    #     }
    #   ],
    #   "guildSrv": {
    #     "id": 561,
    #     "name": "سرویس دهندگان",
    #     "code": "API_GUILD"
    #   },
    #   "closed": False,
    #   "verificationNeeded": False,
    #   "safe": False,
    #   "postVoucherEnabled": True,
    #   "referenceNumber": "71887608",
    #   "issuerSrv": {
    #     "id": 16128,
    #     "name": "شرکت رضا زارع",
    #     "ssoId": "11963175",
    #     "ssoIssuerCode": 1,
    #     "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #   },
    #   "willBeBlocked": False,
    #   "willBePaid": False,
    #   "unsafeCloseTimeOut": 0,
    #   "edited": False,
    #   "waiting": False,
    #   "subInvoice": False
    # }

    vouchers = [
        {
            "name": "تخفیف 5000",
            "amount": 5000,
            "count": 1,
            "description": "Discount 5000 Rials"
        }
    ]
    voucher = pod_voucher.define_discount_amount_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                                         expire_date="1420/12/01")

    print(pod_voucher.apply_voucher(invoice_id=invoice["id"], voucher_hash=voucher[0]["hash"]))

    # OUTPUT
    # {
    #   "id": 61489,
    #   "totalAmountWithoutDiscount": 50000,
    #   "delegationAmount": 0,
    #   "totalAmount": 45000,
    #   "payableAmount": 49050,
    #   "vat": 4050,
    #   "issuanceDate": 1579517705964,
    #   "deliveryDate": 0,
    #   "paymentBillNumber": "1049210",
    #   "uniqueNumber": "56b0d97a3aec1034",
    #   "description": "تست اعمال کد تخفیف بر روی فاکتور بعد از صدور فاکتور",
    #   "paymentDate": 0,
    #   "payed": False,
    #   "serial": 0,
    #   "canceled": False,
    #   "cancelDate": 0,
    #   "business": {
    #     "id": 7867,
    #     "name": "شرکت رضا",
    #     "numOfProducts": 395,
    #     "rate": {
    #       "rate": 8,
    #       "rateCount": 1
    #     },
    #     "sheba": "640170000000000000000007"
    #   },
    #   "invoiceItemSrvs": [
    #     {
    #       "id": 66516,
    #       "amount": 50000,
    #       "description": "محصول اول در پایتون",
    #       "quantity": 1,
    #       "discount": 5000,
    #       "voucherUsageSrvs": [
    #         {
    #           "hash": "3YGKO6CTPFIZ",
    #           "consumDate": 1579517706905,
    #           "usedAmount": 5000,
    #           "canceled": False
    #         }
    #       ]
    #     }
    #   ],
    #   "guildSrv": {
    #     "id": 561,
    #     "name": "سرویس دهندگان",
    #     "code": "API_GUILD"
    #   },
    #   "closed": False,
    #   "verificationNeeded": False,
    #   "safe": False,
    #   "postVoucherEnabled": True,
    #   "referenceNumber": "71887608",
    #   "issuerSrv": {
    #     "id": 16128,
    #     "name": "شرکت رضا زارع",
    #     "ssoId": "11963175",
    #     "ssoIssuerCode": 1,
    #     "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #   },
    #   "willBeBlocked": False,
    #   "willBePaid": False,
    #   "unsafeCloseTimeOut": 0,
    #   "edited": False,
    #   "waiting": False,
    #   "subInvoice": False
    # }

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
