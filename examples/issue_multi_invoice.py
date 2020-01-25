# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException, InvalidDataException
from examples.config import *
from pod_billing import PodBilling
from random import randint

try:
    pod_billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)

    bill_number = "Py_{}".format(randint(1, 100000000))
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
        "guildCode": GUILD_CODE,
        "billNumber": bill_number,       # Optional
        "metadata": {       # Optional
            "multi_invoice": True,
            "customer": {
                "name": "رضا",
                "family": "زارع"
            }
        },
        "description": "توضیحات فاکتور - نمایش در پنل مالک فاکتور"       # Optional
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
            ],
            "billNumber": bill_number+"_sub"+str(DEALER_BUSINESS_IDs[0]),       # Optional
            "metadata": {       # optional
                "key_1": "value_1",
                "key_2": 2
            },
            "description": "توضیحات فاکتور - نمایش در پنل {} به عنوان ذینفع اول فاکتور".format(
                DEALER_BUSINESS_IDs[0])       # Optional
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
            ],
            "billNumber": bill_number+"_marketer_sub"+str(DEALER_BUSINESS_IDs[0]),       # Optional
            "metadata": {       # optional
                "key_1": "value_1",
                "key_2": 2
            },
            "description": "توضیحات فاکتور - نمایش در پنل {} به عنوان ذینفع اول فاکتور".format(
                DEALER_BUSINESS_IDs[0])       # Optional
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
            ],
            "billNumber": bill_number+"_sub"+str(DEALER_BUSINESS_IDs[1]),    # optional
            "metadata": {       # optional
                "products": [
                    {
                        "id": 0,
                        "share": 35
                    },
                    {
                        "id": 0,
                        "share": 45
                    }
                ]
            },
            "description": "توضیحات فاکتور - نمایش در پنل {} به عنوان ذینفع دوم فاکتور".format(
                DEALER_BUSINESS_IDs[1])       # Optional
        }
    ]

    other_params = {
        "redirectURL": "http://google.com",       # Optional
        "userId": USER_ID,       # Optional
        "currencyCode": "IRR",       # Optional
        "preferredTaxRate": 0.10,       # Optional
        "verificationNeeded": False,       # Optional
        "customerDescription": "این توضیحات در فاکتور مشتری نمایش داده می شود",       # Optional
        "customerMetadata": {       # Optional
            "time": "1398/12/01 10:48:59",
            "os": "XUbuntu/ Linux 64bit"
        }
    }

    invoice = pod_billing.issue_multi_invoice(main_invoice=main_invoice, customer_invoice=customer_invoice,
                                              sub_invoices=sub_invoices, **other_params)
    print(invoice)
    # OUTPUT
    # {
    #   "id": 61965,
    #   "totalAmountWithoutDiscount": 800,
    #   "delegationAmount": 0,
    #   "totalAmount": 800,
    #   "payableAmount": 880,
    #   "vat": 80,
    #   "issuanceDate": 1579673363604,
    #   "deliveryDate": 0,
    #   "billNumber": "Py_69274901",
    #   "paymentBillNumber": "1049539",
    #   "uniqueNumber": "564e734413d78db4",
    #   "description": "توضیحات فاکتور - نمایش در پنل مالک فاکتور",
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
    #       "id": 67040,
    #       "amount": 350,
    #       "description": "محصول اول - کسب و کار مالک فاکتور",
    #       "quantity": 2,
    #       "discount": 0,
    #       "voucherUsageSrvs": []
    #     },
    #     {
    #       "id": 67041,
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
    #   "userSrv": {
    #     "id": 16849,
    #     "name": "رضا زارع",
    #     "ssoId": "11923337",
    #     "ssoIssuerCode": 1,
    #     "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #   },
    #   "cellphoneNumber": "09370000941",
    #   "closed": false,
    #   "verificationNeeded": false,
    #   "metadata": "{\"multi_invoice\": true, \"customer\": {\"name\": \"\\u0631\\u0636\\u0627\", \"family\": \"\\u0632\\u0627\\u0631\\u0639\"}}",
    #   "customerInvoice": {
    #     "id": 61964,
    #     "totalAmountWithoutDiscount": 1300,
    #     "delegationAmount": 0,
    #     "totalAmount": 1300,
    #     "payableAmount": 1430,
    #     "vat": 130,
    #     "issuanceDate": 1579673363597,
    #     "deliveryDate": 0,
    #     "paymentBillNumber": "1049539",
    #     "uniqueNumber": "46dda161afe014c",
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
    #         "id": 67038,
    #         "amount": 500,
    #         "description": "محصول اول - مشتری",
    #         "quantity": 2,
    #         "discount": 0,
    #         "voucherUsageSrvs": []
    #       },
    #       {
    #         "id": 67039,
    #         "amount": 300,
    #         "description": "محصول دوم - مشتری",
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
    #     "userSrv": {
    #       "id": 16849,
    #       "name": "رضا زارع",
    #       "ssoId": "11923337",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "cellphoneNumber": "09370000941",
    #     "closed": false,
    #     "verificationNeeded": false,
    #     "metadata": "{\"time\": \"1398/12/01 10:48:59\", \"os\": \"XUbuntu/ Linux 64bit\"}",
    #     "safe": false,
    #     "postVoucherEnabled": false,
    #     "referenceNumber": "72105352",
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
    #       "id": 61966,
    #       "totalAmountWithoutDiscount": 100,
    #       "delegationAmount": 0,
    #       "totalAmount": 100,
    #       "payableAmount": 110,
    #       "vat": 10,
    #       "issuanceDate": 1579673363607,
    #       "deliveryDate": 0,
    #       "billNumber": "Py_69274901_sub9343",
    #       "paymentBillNumber": "1049539",
    #       "uniqueNumber": "19dd8ed72cc2ca3f",
    #       "description": "توضیحات فاکتور - نمایش در پنل 9343 به عنوان ذینفع اول فاکتور",
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
    #           "id": 67042,
    #           "amount": 50,
    #           "description": "پورسانت - کسب و کار 9343 ذینفع اول فاکتور",
    #           "quantity": 2,
    #           "discount": 0,
    #           "voucherUsageSrvs": []
    #         }
    #       ],
    #       "guildSrv": {
    #         "id": 561,
    #         "name": "سرویس دهندگان",
    #         "code": "API_GUILD"
    #       },
    #       "userSrv": {
    #         "id": 16849,
    #         "name": "رضا زارع",
    #         "ssoId": "11923337",
    #         "ssoIssuerCode": 1,
    #         "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #       },
    #       "cellphoneNumber": "09370000941",
    #       "closed": false,
    #       "verificationNeeded": false,
    #       "metadata": "{\"key_1\": \"value_1\", \"key_2\": 2}",
    #       "safe": false,
    #       "postVoucherEnabled": false,
    #       "referenceNumber": "72105352",
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
    #       "id": 61967,
    #       "totalAmountWithoutDiscount": 60,
    #       "delegationAmount": 0,
    #       "totalAmount": 60,
    #       "payableAmount": 66,
    #       "vat": 6,
    #       "issuanceDate": 1579673363609,
    #       "deliveryDate": 0,
    #       "billNumber": "Py_69274901_marketer_sub9343",
    #       "paymentBillNumber": "1049539",
    #       "uniqueNumber": "dad1f72f1ebd51f0",
    #       "description": "توضیحات فاکتور - نمایش در پنل 9343 به عنوان ذینفع اول فاکتور",
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
    #           "id": 67043,
    #           "amount": 30,
    #           "description": "کارمزد بازاریابی - کسب و کار 9343 ذینفع اول فاکتور",
    #           "quantity": 2,
    #           "discount": 0,
    #           "voucherUsageSrvs": []
    #         }
    #       ],
    #       "guildSrv": {
    #         "id": 561,
    #         "name": "سرویس دهندگان",
    #         "code": "API_GUILD"
    #       },
    #       "userSrv": {
    #         "id": 16849,
    #         "name": "رضا زارع",
    #         "ssoId": "11923337",
    #         "ssoIssuerCode": 1,
    #         "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #       },
    #       "cellphoneNumber": "09370000941",
    #       "closed": false,
    #       "verificationNeeded": false,
    #       "metadata": "{\"key_1\": \"value_1\", \"key_2\": 2}",
    #       "safe": false,
    #       "postVoucherEnabled": false,
    #       "referenceNumber": "72105352",
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
    #       "id": 61968,
    #       "totalAmountWithoutDiscount": 340,
    #       "delegationAmount": 0,
    #       "totalAmount": 340,
    #       "payableAmount": 374,
    #       "vat": 34,
    #       "issuanceDate": 1579673363610,
    #       "deliveryDate": 0,
    #       "billNumber": "Py_69274901_sub12006",
    #       "paymentBillNumber": "1049539",
    #       "uniqueNumber": "f4ae7f2948d3d237",
    #       "description": "توضیحات فاکتور - نمایش در پنل 12006 به عنوان ذینفع دوم فاکتور",
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
    #         "sheba": "210150000000000000000000"
    #       },
    #       "invoiceItemSrvs": [
    #         {
    #           "id": 67044,
    #           "amount": 70,
    #           "description": "سهم از محصول اول - کسب و کار 12006 ذینفع دوم فاکتور",
    #           "quantity": 2,
    #           "discount": 0,
    #           "voucherUsageSrvs": []
    #         },
    #         {
    #           "id": 67045,
    #           "amount": 200,
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
    #       "userSrv": {
    #         "id": 16849,
    #         "name": "رضا زارع",
    #         "ssoId": "11923337",
    #         "ssoIssuerCode": 1,
    #         "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #       },
    #       "cellphoneNumber": "09370000941",
    #       "closed": false,
    #       "verificationNeeded": false,
    #       "metadata": "{\"products\": [{\"id\": 0, \"share\": 35}, {\"id\": 0, \"share\": 45}]}",
    #       "safe": false,
    #       "postVoucherEnabled": false,
    #       "referenceNumber": "72105352",
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
    #   "referenceNumber": "72105352",
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
