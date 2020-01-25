# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException, InvalidDataException
from examples.config import *
from pod_billing import PodBilling
from random import randint

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)

    preferred_tax_rate = 0.10

    bill_number = "Py_reduce_{}".format(randint(1, 100000000))
    customer_invoice = [
        {
            "productId": 0,
            "price": 500,
            "quantity": 2,
            "description": "محصول اول - مشتری"
        }
        , {
            "productId": 0,
            "price": 300,
            "quantity": 1,
            "description": "محصول دوم - مشتری"
        }
    ]

    main_invoice = {
        "invoiceItemVOs": [{
            "productId": 0,
            "price": 350,
            "quantity": 2,
            "description": "محصول اول - کسب و کار مالک فاکتور"
        }, {
            "productId": 0,
            "price": 100,
            "quantity": 1,
            "description": "محصول دوم - کسب و کار مالک فاکتور"
        }
        ],
        "guildCode": GUILD_CODE
    }

    sub_invoices = [
        {
            "businessId": DEALER_BUSINESS_IDs[0],
            "guildCode": GUILD_CODE,
            "invoiceItemVOs": [
                {
                    "productId": 0,
                    "price": 50,
                    "quantity": 2,
                    "description": "پورسانت - کسب و کار {} ذینفع اول فاکتور".format(DEALER_BUSINESS_IDs[0])
                }
            ]
        }, {
            "businessId": DEALER_BUSINESS_IDs[0],
            "guildCode": GUILD_CODE,
            "invoiceItemVOs": [
                {
                    "productId": 0,
                    "price": 30,
                    "quantity": 2,
                    "description": "کارمزد بازاریابی - کسب و کار {} ذینفع اول فاکتور".format(DEALER_BUSINESS_IDs[0])
                }
            ]
        }, {
            "businessId": DEALER_BUSINESS_IDs[1],
            "guildCode": GUILD_CODE,
            "invoiceItemVOs": [
                {
                    "productId": 0,
                    "price": 70,
                    "quantity": 2,
                    "description": "سهم از محصول اول - کسب و کار {} ذینفع دوم فاکتور".format(DEALER_BUSINESS_IDs[1])
                }
                ,
                {
                    "productId": 0,
                    "price": 200,
                    "quantity": 1,
                    "description": "سهم از محصول دوم - کسب و کار {} ذینفع دوم فاکتور".format(DEALER_BUSINESS_IDs[1])
                }
            ]
        }
    ]

    other_params = {
        "customerDescription": "این توضیحات در فاکتور مشتری نمایش داده می شود",  # Optional
        "preferredTaxRate": preferred_tax_rate  # Optional
    }

    invoice = pod_billing.issue_multi_invoice(main_invoice=main_invoice, customer_invoice=customer_invoice,
                                              sub_invoices=sub_invoices, **other_params)

    main_invoice_updated = {
        "id": invoice["id"],
        "reduceInvoiceItemVOs": [{
            "id": invoice["invoiceItemSrvs"][0]["id"],
            "price": 350,
            "quantity": 1,
            "description": "محصول اول - کسب و کار مالک فاکتور - کاهش تعداد از 2 به 1"
        }, {
            "id": invoice["invoiceItemSrvs"][1]["id"],
            "price": 100,
            "quantity": 1,
            "description": "محصول دوم - کسب و کار مالک فاکتور"
        }]
    }
    customer_invoice_updated = [
        {
            "id": invoice["customerInvoice"]["invoiceItemSrvs"][0]["id"],
            "price": 500,
            "quantity": 1,
            "description": "محصول اول - مشتری - کاهش تعداد از 2 به 1"
        }
        , {
            "id": invoice["customerInvoice"]["invoiceItemSrvs"][1]["id"],
            "price": 250,
            "quantity": 1,
            "description": "محصول دوم - مشتری - کاهش قیمت از 300 به 250"
        }]

    sub_invoices_updated = [
        {
            "id": invoice["subInvoices"][0]["id"],
            "reduceInvoiceItemVOs": [
                {
                    "id": invoice["subInvoices"][0]["invoiceItemSrvs"][0]["id"],
                    "price": 50,
                    "quantity": 1,
                    "description": "پورسانت - کسب و کار {} ذینفع اول فاکتور - کاهش تعداد از 2 به 1".format(
                        DEALER_BUSINESS_IDs[0])
                }
            ]
        }, {
            "id": invoice["subInvoices"][1]["id"],
            "reduceInvoiceItemVOs": [
                {
                    "id": invoice["subInvoices"][1]["invoiceItemSrvs"][0]["id"],
                    "price": 30,
                    "quantity": 1,
                    "description": "کارمزد بازاریابی - کسب و کار {} ذینفع اول فاکتور - کاهش تعداد از 2 به 1".format(
                        DEALER_BUSINESS_IDs[0])
                }
            ]
        }, {
            "id": invoice["subInvoices"][2]["id"],
            "reduceInvoiceItemVOs": [
                {
                    "id": invoice["subInvoices"][2]["invoiceItemSrvs"][0]["id"],
                    "price": 70,
                    "quantity": 1,
                    "description": "سهم از محصول اول - کسب و کار {} ذینفع دوم فاکتور - کاهش تعداد از 2 به 1".format(
                        DEALER_BUSINESS_IDs[1])
                },
                {
                    "id": invoice["subInvoices"][2]["invoiceItemSrvs"][1]["id"],
                    "price": 150,
                    "quantity": 1,
                    "description": "سهم از محصول دوم - کسب و کار {} ذینفع دوم فاکتور".format(DEALER_BUSINESS_IDs[1])
                }
            ]
        }
    ]

    result = pod_billing.reduce_multi_invoice_and_cash_out(preferred_tax_rate=preferred_tax_rate,
                                                           main_invoice=main_invoice_updated,
                                                           customer_invoice=customer_invoice_updated,
                                                           sub_invoices=sub_invoices_updated,
                                                           toolCode="SETTLEMENT_TOOL_SATNA")

    print(result)
    # OUTPUT
    # {
    #   "id": 62419,
    #   "totalAmountWithoutDiscount": 450,
    #   "delegationAmount": 0,
    #   "totalAmount": 450,
    #   "payableAmount": 491,
    #   "vat": 41,
    #   "issuanceDate": 1579947664808,
    #   "deliveryDate": 0,
    #   "paymentBillNumber": "1049721",
    #   "uniqueNumber": "e251c6ceae447852",
    #   "paymentDate": 0,
    #   "payed": false,
    #   "serial": 0,
    #   "canceled": false,
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
    #       "id": 67562,
    #       "amount": 350,
    #       "description": "محصول اول - کسب و کار مالک فاکتور - کاهش تعداد از 2 به 1",
    #       "quantity": 1,
    #       "discount": 0,
    #       "voucherUsageSrvs": []
    #     },
    #     {
    #       "id": 67563,
    #       "amount": 100,
    #       "description": "محصول دوم - کسب و کار مالک فاکتور",
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
    #   "closed": false,
    #   "verificationNeeded": false,
    #   "editedInvoiceId": 62414,
    #   "customerInvoice": {
    #     "id": 62418,
    #     "totalAmountWithoutDiscount": 750,
    #     "delegationAmount": 0,
    #     "totalAmount": 750,
    #     "payableAmount": 818,
    #     "vat": 68,
    #     "issuanceDate": 1579947664798,
    #     "deliveryDate": 0,
    #     "paymentBillNumber": "1049721",
    #     "uniqueNumber": "bae7e742cd529637",
    #     "description": "این توضیحات در فاکتور مشتری نمایش داده می شود",
    #     "paymentDate": 0,
    #     "payed": false,
    #     "serial": 0,
    #     "canceled": false,
    #     "cancelDate": 0,
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 395,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000007"
    #     },
    #     "invoiceItemSrvs": [
    #       {
    #         "id": 67560,
    #         "amount": 500,
    #         "description": "محصول اول - مشتری - کاهش تعداد از 2 به 1",
    #         "quantity": 1,
    #         "discount": 0,
    #         "voucherUsageSrvs": []
    #       },
    #       {
    #         "id": 67561,
    #         "amount": 250,
    #         "description": "محصول دوم - مشتری - کاهش قیمت از 300 به 250",
    #         "quantity": 1,
    #         "discount": 0,
    #         "voucherUsageSrvs": []
    #       }
    #     ],
    #     "guildSrv": {
    #       "id": 561,
    #       "name": "سرویس دهندگان",
    #       "code": "API_GUILD"
    #     },
    #     "closed": false,
    #     "verificationNeeded": false,
    #     "safe": false,
    #     "postVoucherEnabled": false,
    #     "referenceNumber": "72426946",
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
    #     "edited": false,
    #     "waiting": false,
    #     "subInvoice": false
    #   },
    #   "subInvoices": [
    #     {
    #       "id": 62420,
    #       "totalAmountWithoutDiscount": 50,
    #       "delegationAmount": 0,
    #       "totalAmount": 50,
    #       "payableAmount": 55,
    #       "vat": 5,
    #       "issuanceDate": 1579947664810,
    #       "deliveryDate": 0,
    #       "paymentBillNumber": "1049721",
    #       "uniqueNumber": "415bbfbe4de82f52",
    #       "paymentDate": 0,
    #       "payed": false,
    #       "serial": 0,
    #       "canceled": false,
    #       "cancelDate": 0,
    #       "business": {
    #         "id": 9343,
    #         "name": "کسب و کار حمید",
    #         "numOfProducts": 12,
    #         "rate": {
    #           "rate": 0,
    #           "rateCount": 0
    #         },
    #         "sheba": "500570000000000000000001"
    #       },
    #       "invoiceItemSrvs": [
    #         {
    #           "id": 67564,
    #           "amount": 50,
    #           "description": "پورسانت - کسب و کار 9343 ذینفع اول فاکتور - کاهش تعداد از 2 به 1",
    #           "quantity": 1,
    #           "discount": 0,
    #           "voucherUsageSrvs": []
    #         }
    #       ],
    #       "guildSrv": {
    #         "id": 561,
    #         "name": "سرویس دهندگان",
    #         "code": "API_GUILD"
    #       },
    #       "closed": false,
    #       "verificationNeeded": false,
    #       "safe": false,
    #       "postVoucherEnabled": false,
    #       "referenceNumber": "72426946",
    #       "issuerSrv": {
    #         "id": 16128,
    #         "name": "شرکت رضا زارع",
    #         "ssoId": "11963175",
    #         "ssoIssuerCode": 1,
    #         "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #       },
    #       "willBeBlocked": false,
    #       "willBePaid": false,
    #       "unsafeCloseTimeOut": 0,
    #       "edited": false,
    #       "waiting": false,
    #       "subInvoice": true
    #     },
    #     {
    #       "id": 62421,
    #       "totalAmountWithoutDiscount": 30,
    #       "delegationAmount": 0,
    #       "totalAmount": 30,
    #       "payableAmount": 33,
    #       "vat": 3,
    #       "issuanceDate": 1579947664811,
    #       "deliveryDate": 0,
    #       "paymentBillNumber": "1049721",
    #       "uniqueNumber": "71f8f9ffe02c7eb4",
    #       "paymentDate": 0,
    #       "payed": false,
    #       "serial": 0,
    #       "canceled": false,
    #       "cancelDate": 0,
    #       "business": {
    #         "id": 9343,
    #         "name": "کسب و کار حمید",
    #         "numOfProducts": 12,
    #         "rate": {
    #           "rate": 0,
    #           "rateCount": 0
    #         },
    #         "sheba": "500570000000000000000001"
    #       },
    #       "invoiceItemSrvs": [
    #         {
    #           "id": 67565,
    #           "amount": 30,
    #           "description": "کارمزد بازاریابی - کسب و کار 9343 ذینفع اول فاکتور - کاهش تعداد از 2 به 1",
    #           "quantity": 1,
    #           "discount": 0,
    #           "voucherUsageSrvs": []
    #         }
    #       ],
    #       "guildSrv": {
    #         "id": 561,
    #         "name": "سرویس دهندگان",
    #         "code": "API_GUILD"
    #       },
    #       "closed": false,
    #       "verificationNeeded": false,
    #       "safe": false,
    #       "postVoucherEnabled": false,
    #       "referenceNumber": "72426946",
    #       "issuerSrv": {
    #         "id": 16128,
    #         "name": "شرکت رضا زارع",
    #         "ssoId": "11963175",
    #         "ssoIssuerCode": 1,
    #         "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #       },
    #       "willBeBlocked": false,
    #       "willBePaid": false,
    #       "unsafeCloseTimeOut": 0,
    #       "edited": false,
    #       "waiting": false,
    #       "subInvoice": true
    #     },
    #     {
    #       "id": 62422,
    #       "totalAmountWithoutDiscount": 220,
    #       "delegationAmount": 0,
    #       "totalAmount": 220,
    #       "payableAmount": 240,
    #       "vat": 20,
    #       "issuanceDate": 1579947664812,
    #       "deliveryDate": 0,
    #       "paymentBillNumber": "1049721",
    #       "uniqueNumber": "e8b9612554884db6",
    #       "paymentDate": 0,
    #       "payed": false,
    #       "serial": 0,
    #       "canceled": false,
    #       "cancelDate": 0,
    #       "business": {
    #         "id": 12006,
    #         "name": "Fanap",
    #         "numOfProducts": 15,
    #         "rate": {
    #           "rate": 0,
    #           "rateCount": 0
    #         },
    #         "sheba": "210150000001568301414110"
    #       },
    #       "invoiceItemSrvs": [
    #         {
    #           "id": 67566,
    #           "amount": 70,
    #           "description": "سهم از محصول اول - کسب و کار 12006 ذینفع دوم فاکتور - کاهش تعداد از 2 به 1",
    #           "quantity": 1,
    #           "discount": 0,
    #           "voucherUsageSrvs": []
    #         },
    #         {
    #           "id": 67567,
    #           "amount": 150,
    #           "description": "سهم از محصول دوم - کسب و کار 12006 ذینفع دوم فاکتور",
    #           "quantity": 1,
    #           "discount": 0,
    #           "voucherUsageSrvs": []
    #         }
    #       ],
    #       "guildSrv": {
    #         "id": 561,
    #         "name": "سرویس دهندگان",
    #         "code": "API_GUILD"
    #       },
    #       "closed": false,
    #       "verificationNeeded": false,
    #       "safe": false,
    #       "postVoucherEnabled": false,
    #       "referenceNumber": "72426946",
    #       "issuerSrv": {
    #         "id": 16128,
    #         "name": "شرکت رضا زارع",
    #         "ssoId": "11963175",
    #         "ssoIssuerCode": 1,
    #         "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #       },
    #       "willBeBlocked": false,
    #       "willBePaid": false,
    #       "unsafeCloseTimeOut": 0,
    #       "edited": false,
    #       "waiting": false,
    #       "subInvoice": true
    #     }
    #   ],
    #   "safe": false,
    #   "postVoucherEnabled": false,
    #   "referenceNumber": "72426946",
    #   "issuerSrv": {
    #     "id": 16128,
    #     "name": "شرکت رضا زارع",
    #     "ssoId": "11963175",
    #     "ssoIssuerCode": 1,
    #     "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #   },
    #   "willBeBlocked": false,
    #   "willBePaid": false,
    #   "unsafeCloseTimeOut": 0,
    #   "edited": false,
    #   "waiting": false,
    #   "subInvoice": false
    # }
except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except InvalidDataException as e:
    print("Validation Exception: ", e.message)
except PodException as e:
    print("Pod Exception: ", e.message)
