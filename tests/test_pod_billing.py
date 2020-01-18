# coding=utf-8
from __future__ import unicode_literals

import unittest

from pod_export import PodExport

try:
    from urlparse import urlparse
    from urlparse import parse_qs
except ImportError:
    from urllib.parse import urlparse
    from urllib.parse import parse_qs

from pod_base import InvalidDataException, APIException

from pod_billing import PodBilling
from tests.config import *


def get_products():
    return [
        {
            "productId": 0,
            # مبلغ بند فاکتور. برای استفاده از قیمت محصول وارد شده از مقدار auto استفاده نمایید
            "price": 100,
            # تعداد محصول
            "quantity": 1,
            # توضیحات
            "productDescription": "محصول اول",
        },
        {
            "productId": 0,
            "price": 800,
            "quantity": 5,
            "productDescription": "محصول دوم",
        }
    ]


def get_products_for_reduce():
    return [
        {
            # مبلغ بند فاکتور. برای استفاده از قیمت محصول وارد شده از مقدار auto استفاده نمایید
            "price": 80,
            # تعداد محصول
            "quantity": 1,
            # توضیحات
            "itemDescription": "محصول اول - مبلغ از 100 به 80 کاهش داده شد",
        },
        {
            "price": 800,
            "quantity": 1,
            "itemDescription": "محصول دوم - تعداد از 5 به 1 کاهش پیدا کرد",
        }
    ]


class TestPodBilling(unittest.TestCase):
    __slots__ = "__billing"

    def setUp(self):
        self.__billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)

    def test_1_issue_invoice(self):
        products = get_products()

        result = self.__billing.issue_invoice(products=products, guild_code=GUILD_CODE)
        self.assertIsInstance(result, dict, msg="issue invoice : check instance")
        self.assertEqual(len(result["invoiceItemSrvs"]), 2, msg="issue invoice : check count product")
        self.assertEqual(result["guildSrv"]["code"], GUILD_CODE, msg="issue invoice : check guild code")

    def test_1_issue_invoice_all_params(self):
        products = get_products()

        params = {
            "redirectURL": "http://www.google.com",
            "userId": USER_ID,
            "billNumber": "1234587",
            "description": "تست صدور فاکتور در پایتون",
            "deadline": "1420/12/05",
            "currencyCode": "IRR",  # default : IRR
            # "addressId": 0,
            # "voucherHash" : [""],
            "preferredTaxRate": 0.09,
            "verificationNeeded": True,
            "verifyAfterTimeout": True,
            "preview": True,
            "safe": True,
            "postVoucherEnabled": True,
            "hasEvent": True,
            "eventTitle": "unit test event title",
            "eventTimeZone": "Asia/Tehran",
            "eventDescription": "تست توضیحات رویداد",
            "metadata": {"env": "Python 2.7/Unit Test", "os": "Linux 64bit"},
            "eventMetadata": {"name": "event", "type": "Notification", "Time": "15 min"},
            "eventReminders": [
                {"id": 1, "minute": 15, "alarmType": "Notification"}
            ],
        }

        result = self.__billing.issue_invoice(products=products, guild_code=GUILD_CODE, **params)
        self.assertIsInstance(result, dict, msg="issue invoice (all params) : check instance")
        self.assertEqual(len(result["invoiceItemSrvs"]), 2, msg="issue invoice (all params) : check count product")
        self.assertEqual(result["guildSrv"]["code"], GUILD_CODE, msg="issue invoice (all params) : check guild code")
        self.assertEqual(result["userSrv"]["id"], USER_ID, msg="issue invoice (all params) : check customer user id")

    def test_1_issue_invoice_validation_error(self):
        products = get_products()

        params = {
            'redirectURL': 'https://karthing.ir/test.php',  # should start with http(s)://
            'deadline': '1398-12-11'  # correct format yyyy/mm/dd
        }

        with self.assertRaises(InvalidDataException, msg="issue invoice : validation error"):
            self.__billing.issue_invoice(products=products, guild_code=GUILD_CODE, **params)

    def __issue_invoice(self, **kwargs):
        products = get_products()

        return self.__billing.issue_invoice(products=products, guild_code=GUILD_CODE, **kwargs)

    def test_2_pay_invoice(self):
        invoice = self.__issue_invoice()
        self.assertEqual(self.__billing.pay_invoice(invoice["id"]), True, msg="pay invoice : successful")
        with self.assertRaises(APIException, msg="pay invoice : already pay"):
            self.__billing.pay_invoice(invoice["id"])

    def test_2_pay_invoice_required_params(self):
        with self.assertRaises(TypeError, msg="pay invoice : required param"):
            self.__billing.pay_invoice()

    def test_2_pay_invoice_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="pay invoice : validation error"):
            self.__billing.pay_invoice("abcd")

    def test_3_pay_invoice_by_credit(self):
        invoice = self.__issue_invoice_by_other_business()
        self.assertEqual(self.__billing.pay_invoice_by_credit(invoice["id"]), True, msg="pay invoice : successful")
        with self.assertRaises(APIException, msg="pay invoice : already pay"):
            self.__billing.pay_invoice_by_credit(invoice["id"])

    def test_3_pay_invoice_by_credit_required_params(self):
        with self.assertRaises(TypeError, msg="pay invoice : required param"):
            self.__billing.pay_invoice_by_credit()

    def test_3_pay_invoice_by_credit_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="pay invoice : validation error"):
            self.__billing.pay_invoice_by_credit("abcd")

    def test_4_get_invoice_list(self):
        invoices = self.__billing.get_invoice_list()
        self.assertIsInstance(invoices, list, msg="get invoice list : check instance")

    def test_4_get_invoice_list_all_params(self):
        params = {
            "page": 1,
            "size": 10,
            "id": 123456,
            "guildCode": GUILD_CODE,
            'billNumber': '12345',  # شماره قبض که به تنهایی با آن می توان جستجو نمود
            'uniqueNumber': '123456',  # شماره کد شده ی قبض که به تنهایی با آن می توان جستجو نمود
            'trackerId': 11,
            'fromDate': '1398/01/01 00:00:00',  # تاریخ شمسی صدور فاکتور yyyy/mm/dd hh:mi:ss
            'toDate': '1398/12/29 00:00:00',  # تاریخ شمسی صدور فاکتور yyyy/mm/dd hh:mi:ss
            'isCanceled': True,
            'isPayed': True,
            'isClosed': True,
            'isWaiting': True,
            'referenceNumber': 'put reference number',  # شماره ارجاع
            'userId': USER_ID,  # شناسه کاربری مشتری
            'issuerId': [12121],  # شناسه کاربری صادر کننده فاکتور
            'query': 'web',  # عبارت برای جستجو
            'productIdList': [0],  # لیست شماره محصولات
        }

        invoices = self.__billing.get_invoice_list(**params)
        self.assertIsInstance(invoices, list, msg="get invoice list ( all params ) : check instance")

    def test_4_get_invoice_list_first_id(self):
        params = {
            "firstId": 0
        }

        invoices = self.__billing.get_invoice_list(**params)
        self.assertIsInstance(invoices, list, msg="get invoice list ( first id ) : check instance")

    def test_4_get_invoice_list_last_id(self):
        params = {
            "lastId": 0
        }

        invoices = self.__billing.get_invoice_list(**params)
        self.assertIsInstance(invoices, list, msg="get invoice list ( last id ) : check instance")

    def test_4_get_invoice_list_validation_error(self):
        params = {
            "lastId": 0,
            "firstId": 0
        }
        with self.assertRaises(InvalidDataException, msg="get invoice list (validation error) : set first id, last id"):
            self.__billing.get_invoice_list(**params)

    def test_5_get_invoice_list_by_metadata(self):
        meta_query = {"field": "name", "is": "reza"}
        invoices = self.__billing.get_invoice_list_by_metadata(meta_query=meta_query)
        self.assertIsInstance(invoices, list, msg="get invoice list by metadata : check instance")

    def test_5_get_invoice_list_by_metadata_validation_error_meta_query(self):
        meta_query = "{\"field\": \"name\", \"is\": \"reza\"}"

        with self.assertRaises(InvalidDataException,
                               msg="get invoice list by metadata : validation error meta_query"):
            self.__billing.get_invoice_list_by_metadata(meta_query=meta_query)

    def test_5_get_invoice_list_by_metadata_validation_error_params(self):
        meta_query = {"field": "name", "is": "reza"}
        params = {
            "isPayed": "true",
            "isClose": "true",
        }
        with self.assertRaises(InvalidDataException,
                               msg="get invoice list by metadata : validation error params"):
            self.__billing.get_invoice_list_by_metadata(meta_query=meta_query, **params)

    def test_5_get_invoice_list_by_metadata_required_params(self):
        with self.assertRaises(TypeError, msg="get invoice list by metadata : required params"):
            self.__billing.get_invoice_list_by_metadata()

    def test_6_get_invoice_list_as_file(self):
        params = {
            "lastNRows": 0
        }

        result = self.__billing.get_invoice_list_as_file(**params)
        self.assertIsInstance(result, dict, msg="get invoice list as file : check instance")
        self.assertEqual(result["service"], "/nzh/biz/getInvoiceList/", msg="get invoice list as file : check service")

    def test_6_get_invoice_list_as_file_all_params(self):
        params = {
            "lastNRows": 0,
            "offset": 0,
            "size": 10,
            "toDate": "1420/12/12 10:10:10",  # تاریخ شمسی صدور فاکتور yyyy/mm/dd hh:mi:ss
            "fromDate": "1420/01/01 10:10:10",  # تاریخ شمسی صدور فاکتور yyyy/mm/dd hh:mi:ss
            "guildCode": GUILD_CODE,  # کد صنف
            "id": 55434,
            "billNumber": "12345",  # شماره قبض که به تنهایی با آن می توان جستجو نمود
            "uniqueNumber": "123456",  # شماره کد شده ی قبض که به تنهایی با آن می توان جستجو نمود
            "trackerId": 123,
            "isCanceled": False,
            "isPayed": False,
            "isClosed": False,
            "isWaiting": False,
            "referenceNumber": "put reference number",  # شماره ارجاع
            "userId": USER_ID,  # شناسه کاربری مشتری
            "query": "test",  # عبارت برای جستجو
            "productIdList": [0],  # لیست شماره محصولات
            "callbackUrl": "https://karthing.ir/test.php",  # آدرس فراخوانی پس از اتمام تولید گزارش
        }

        result = self.__billing.get_invoice_list_as_file(**params)
        self.assertIsInstance(result, dict, msg="get invoice list as file (all params) : check instance")
        self.assertEqual(result["service"], "/nzh/biz/getInvoiceList/",
                         msg="get invoice list as file (all params) : check service")

    def test_6_get_invoice_list_as_file_required_params(self):
        with self.assertRaises(InvalidDataException, msg="get invoice list as file : required params"):
            self.__billing.get_invoice_list_as_file()

    def test_6_get_invoice_list_as_file_validation_error(self):
        params = {
            "lastNRows": 0,
            "toDate": "1398-12-12 10:20",
            "fromDate": "13981212"
        }
        with self.assertRaises(InvalidDataException, msg="get invoice list as file : validation error"):
            self.__billing.get_invoice_list_as_file(**params)

    def test_7_verify_invoice_required_params(self):
        with self.assertRaises(TypeError, msg="verify invoice : required params"):
            self.__billing.verify_invoice()

    def test_7_verify_invoice_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="verify invoice : validation error"):
            self.__billing.verify_invoice("invoice id")

    def test_8_verify_invoice_by_bill_number_required_params(self):
        with self.assertRaises(TypeError, msg="verify invoice by bill_number : required params"):
            self.__billing.verify_invoice_by_bill_number()

    def test_8_verify_invoice_by_bill_number_not_exists(self):
        with self.assertRaises(APIException, msg="verify invoice by bill_number : not exists bill number"):
            self.__billing.verify_invoice_by_bill_number("invoice 4564564_id")

    def test_8_verify_invoice_by_bill_number_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="verify invoice by bill_number : validation error"):
            self.__billing.verify_invoice_by_bill_number(123)

    def test_9_verify_and_close_invoice_required_params(self):
        with self.assertRaises(TypeError, msg="verify and close invoice : required params"):
            self.__billing.verify_and_close_invoice()

    def test_9_verify_and_close_invoice_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="verify and close invoice : validation error"):
            self.__billing.verify_and_close_invoice("invoice id")

    def test_10_close_invoice(self):
        invoice = self.__issue_invoice()
        self.__billing.pay_invoice(invoice["id"])
        self.assertEqual(self.__billing.close_invoice(invoice_id=invoice["id"]), True, msg="close invoice")

    def test_10_close_invoice_required_params(self):
        with self.assertRaises(TypeError, msg="close invoice : required params"):
            self.__billing.close_invoice()

    def test_10_close_invoice_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="close invoice : validation error"):
            self.__billing.close_invoice(invoice_id="123456")

    def test_11_cancel_invoice(self):
        invoice = self.__issue_invoice()
        self.assertEqual(self.__billing.cancel_invoice(invoice_id=invoice["id"]), True, msg="cancel invoice")

    def test_11_cancel_invoice_required_params(self):
        with self.assertRaises(TypeError, msg="cancel invoice : required params"):
            self.__billing.cancel_invoice()

    def test_11_cancel_invoice_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="cancel invoice : validation error"):
            self.__billing.cancel_invoice(invoice_id="123456")

    def test_12_send_invoice_payment_sms(self):
        params = {
            "userId": USER_ID
        }
        invoice = self.__issue_invoice(**params)
        self.assertEqual(self.__billing.send_invoice_payment_sms(invoice_id=invoice["id"]), True, msg="send sms")

    def test_12_send_invoice_payment_sms_all_params(self):
        params = {
            "userId": USER_ID
        }
        invoice = self.__issue_invoice(**params)

        params = {
            "wallet": WALLET,
            "callbackUri": "https://karthing.ir/test.php?callback=true&invoice_id={}".format(invoice["id"]),
            "redirectUri": "https://karthing.ir/test.php?redierct=true&invoice_id={}".format(invoice["id"]),
            "delegationId": [],
            "forceDelegation": True,
        }

        self.assertEqual(self.__billing.send_invoice_payment_sms(invoice_id=invoice["id"], **params), True,
                         msg="send sms (all params)")

    def test_12_send_invoice_payment_sms_validation_error(self):
        invoice_id = "10"
        params = {
            "wallet": 123456,
            "callbackUri": "karthing.ir/test.php?callback=true&invoice_id={}".format(invoice_id),
            "redirectUri": "karthing.ir/test.php?redierct=true&invoice_id={}".format(invoice_id),
            "delegationId": "[]",
            "forceDelegation": "True",
        }
        with self.assertRaises(InvalidDataException, msg="send sms : validation error"):
            self.__billing.send_invoice_payment_sms(invoice_id=invoice_id, **params)

    def test_12_send_invoice_payment_sms_required_param(self):
        with self.assertRaises(TypeError, msg="send sms : required params"):
            self.__billing.send_invoice_payment_sms()

    def test_13_get_invoice_payment_link(self):
        params = {
            "userId": USER_ID
        }

        invoice = self.__issue_invoice(**params)
        result = self.__billing.get_invoice_payment_link(invoice_id=invoice["id"])

        self.assertIsInstance(result, str, msg="get invoice payment_link : check instance")

    def test_13_get_invoice_payment_link_all_params(self):
        params = {
            "userId": USER_ID
        }

        invoice = self.__issue_invoice(**params)
        redirect_url = "https://google.com"  # should start with http(s)://
        call_url = "https://yahoo.com"  # should start with http(s)://
        gateway = "PEP"
        result = self.__billing.get_invoice_payment_link(invoice_id=invoice["id"], redirect_url=redirect_url,
                                                         call_url=call_url, gateway=gateway)

        self.assertIsInstance(result, str, msg="get invoice payment_link (all params) : check instance")
        parsed = urlparse(result)
        parsed_qs = parse_qs(parsed.query)
        self.assertEqual(parsed_qs["redirectUri"][0], redirect_url,
                         msg="get invoice payment_link (all params) : redirect url")
        self.assertEqual(parsed_qs["callUri"][0], call_url, msg="get invoice payment_link (all params) : call url")
        self.assertEqual(parsed_qs["gateway"][0], gateway, msg="get invoice payment_link (all params) : gateway")

    def test_13_get_invoice_payment_link_validation_error(self):
        params = {
            "userId": USER_ID
        }

        invoice = self.__issue_invoice(**params)
        redirect_url = "google.com"  # should start with http(s)://
        call_url = "yahoo.com"  # should start with http(s)://
        with self.assertRaises(InvalidDataException, msg="get invoice payment_link : validation error"):
            self.__billing.get_invoice_payment_link(invoice_id=invoice["id"], redirect_url=redirect_url,
                                                    call_url=call_url)

    def test_13_get_invoice_payment_link_required_param(self):
        with self.assertRaises(TypeError, msg="get invoice payment_link : required params"):
            self.__billing.get_invoice_payment_link()

    def test_14_get_export_list(self):
        exports = self.__billing.export.get_export_list()
        self.assertIsInstance(exports, list, msg="get export list : check instance")

    def test_14_get_export_list_all_params(self):
        params = {
            "page": 1,
            "size": 10,
            "statusCode": PodExport.EXPORT_SERVICE_STATUS_CREATED,
            "serviceUrl": "/nzh/biz/getInvoiceList/"
        }
        exports = self.__billing.export.get_export_list(**params)
        self.assertIsInstance(exports, list, msg="get export list (all params): check instance")

    def test_14_get_export_list_validation_error(self):
        params = {
            "statusCode": "ABCD",
            "serviceUrl": 123456
        }
        with self.assertRaises(InvalidDataException, msg="get export list : validation error"):
            self.__billing.export.get_export_list(**params)

    def test_15_get_pay_invoice_by_wallet_link(self):
        params = {
            "userId": USER_ID
        }

        invoice = self.__issue_invoice(**params)

        result = self.__billing.get_pay_invoice_by_wallet_link(invoice_id=invoice["id"])
        self.assertIsInstance(result, str, msg="get pay invoice by wallet link (all params) : check instance")
        parsed = urlparse(result)
        parsed_qs = parse_qs(parsed.query)
        self.assertEqual(parsed_qs["invoiceId"][0], str(invoice["id"]),
                         msg="get pay invoice by wallet link (all params) : check invoice id")

    def test_15_get_pay_invoice_by_wallet_link_all_params(self):
        params = {
            "userId": USER_ID
        }

        invoice = self.__issue_invoice(**params)

        redirect_url = "http://google.com"
        call_url = "http://yahoo.com"

        result = self.__billing.get_pay_invoice_by_wallet_link(invoice_id=invoice["id"], redirect_url=redirect_url,
                                                               call_url=call_url)
        self.assertIsInstance(result, str, msg="get pay invoice by wallet link (all params) : check instance")
        parsed = urlparse(result)
        parsed_qs = parse_qs(parsed.query)
        self.assertEqual(parsed_qs["invoiceId"][0], str(invoice["id"]),
                         msg="get pay invoice by wallet link (all params) : check invoice id")
        self.assertEqual(parsed_qs["redirectUri"][0], redirect_url,
                         msg="get pay invoice by wallet link (all params) : check redirect url")
        self.assertEqual(parsed_qs["callUri"][0], call_url,
                         msg="get pay invoice by wallet link (all params) : check call url")

    def test_15_get_pay_invoice_by_wallet_link_required_param(self):
        with self.assertRaises(TypeError, msg="get pay invoice by wallet link : required param"):
            self.__billing.get_pay_invoice_by_wallet_link()

    def test_15_get_pay_invoice_by_wallet_link_validation_error(self):
        invoice_id = "123"

        redirect_url = "google.com"
        call_url = "yahoo.com"

        with self.assertRaises(InvalidDataException, msg="get pay invoice by wallet link : validation error"):
            self.__billing.get_pay_invoice_by_wallet_link(invoice_id=invoice_id, redirect_url=redirect_url,
                                                          call_url=call_url)

    def test_16_get_pay_invoice_by_unique_number_link(self):
        unique_number = "ancdd"
        result = self.__billing.get_pay_invoice_by_unique_number_link(unique_number=unique_number)

        self.assertIsInstance(result, str, msg="get invoice by unique number link : check instance")
        parsed = urlparse(result)
        parsed_qs = parse_qs(parsed.query)
        self.assertEqual(parsed_qs["uniqueNumber"][0], unique_number,
                         msg="get invoice by unique number link : unique number")

    def test_16_get_pay_invoice_by_unique_number_link_all_params(self):
        unique_number = "abcdd"

        redirect_url = "https://google.com"  # should start with http(s)://
        call_url = "https://yahoo.com"  # should start with http(s)://
        gateway = "PEP"
        result = self.__billing.get_pay_invoice_by_unique_number_link(unique_number=unique_number,
                                                                      redirect_url=redirect_url, call_url=call_url,
                                                                      gateway=gateway)

        self.assertIsInstance(result, str, msg="get invoice by unique number link (all params) : check instance")
        parsed = urlparse(result)
        parsed_qs = parse_qs(parsed.query)
        self.assertEqual(parsed_qs["redirectUri"][0], redirect_url,
                         msg="get invoice by unique number link (all params) : redirect url")
        self.assertEqual(parsed_qs["callUri"][0], call_url,
                         msg="get invoice by unique number link (all params) : call url")
        self.assertEqual(parsed_qs["gateway"][0], gateway,
                         msg="get invoice by unique number link (all params) : gateway")
        self.assertEqual(parsed_qs["uniqueNumber"][0], unique_number,
                         msg="get invoice by unique number link (all params) : unique number")

    def test_16_get_pay_invoice_by_unique_number_link_validation_error(self):
        unique_number = "abcdd"
        redirect_url = "google.com"  # should start with http(s)://
        call_url = "yahoo.com"  # should start with http(s)://
        with self.assertRaises(InvalidDataException, msg="get invoice by unique number link : validation error"):
            self.__billing.get_pay_invoice_by_unique_number_link(unique_number=unique_number, redirect_url=redirect_url,
                                                                 call_url=call_url)

    def test_16_get_pay_invoice_by_unique_number_link_required_param(self):
        with self.assertRaises(TypeError, msg="get invoice by unique number link : required params"):
            self.__billing.get_pay_invoice_by_unique_number_link()

    @staticmethod
    def __issue_invoice_by_other_business():
        products = get_products()
        billing = PodBilling(api_token=OTHER_BUSINESS_API_TOKEN, server_type=SERVER_MODE)
        return billing.issue_invoice(products=products, guild_code=OTHER_BUSINESS_GUILD_CODE,
                                     userId=USER_ID_YOUR_BUSINESS)

    def test_17_pay_invoice_in_future_by_guild_code(self):
        invoice = self.__issue_invoice_by_other_business()
        date = "1420/12/10"
        self.assertEqual(self.__billing.pay_invoice_in_future(invoice_id=invoice["id"], date=date,
                                                              guild_code=GUILD_CODE), True,
                         msg="pay invoice in future (by guild code)")

    def test_17_pay_invoice_in_future_by_wallet(self):
        invoice = self.__issue_invoice_by_other_business()
        date = "1420/12/10"
        self.assertEqual(self.__billing.pay_invoice_in_future(invoice_id=invoice["id"], date=date, wallet=WALLET), True,
                         msg="pay invoice in future (by wallet)")

    def test_17_pay_invoice_in_future_validation_error(self):
        invoice = {"id": "123"}
        date = "14201210"
        with self.assertRaises(InvalidDataException, msg="pay invoice in future : validation error"):
            self.__billing.pay_invoice_in_future(invoice_id=invoice["id"], date=date, guild_code=GUILD_CODE)

    def test_17_pay_invoice_in_future_required_params(self):
        with self.assertRaises(TypeError, msg="pay invoice in future : required params"):
            self.__billing.pay_invoice_in_future()

    def test_18_pay_invoice_in_future_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="pay invoice by invoice : validation error"):
            self.__billing.pay_invoice_by_invoice("123", "456")

    def test_18_pay_invoice_in_future_required_params(self):
        with self.assertRaises(TypeError, msg="pay invoice by invoice : required params"):
            self.__billing.pay_invoice_by_invoice()

    def test_19_pay_invoice_by_credit(self):
        invoice = self.__issue_invoice_by_other_business()
        self.assertEqual(self.__billing.pay_invoice_by_credit(invoice_id=invoice["id"]), True,
                         msg="pay invoice by credit")

    def test_19_pay_invoice_by_credit_required_params(self):
        with self.assertRaises(TypeError, msg="pay invoice by credit : required params"):
            self.__billing.pay_invoice_by_credit()

    def test_19_pay_invoice_by_credit_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="pay invoice by credit : required params"):
            self.__billing.pay_invoice_by_credit("45645")

    def test_20_reduce_invoice(self):
        invoice = self.__issue_invoice()
        preferred_tax_rate = 0.09
        items = get_products_for_reduce()
        items[0]["invoiceItemId"] = invoice["invoiceItemSrvs"][0]["id"]
        items[1]["invoiceItemId"] = invoice["invoiceItemSrvs"][1]["id"]
        result = self.__billing.reduce_invoice(invoice_id=invoice["id"], items=items,
                                               preferred_tax_rate=preferred_tax_rate)
        self.assertIsInstance(result, dict, msg="reduce invoice : check instance")

    def test_test_20_reduce_validation_error(self):
        invoice = self.__issue_invoice()
        preferred_tax_rate = 0.09
        items = get_products_for_reduce()
        items[0]["invoiceItemId"] = invoice["invoiceItemSrvs"][0]["id"]
        items[1]["invoiceItemId"] = invoice["invoiceItemSrvs"][1]["id"]
        items[0]["price"] = "456"

        with self.assertRaises(InvalidDataException, msg="reduce invoice : validation error"):
            self.__billing.reduce_invoice(invoice_id=invoice["id"], items=items, preferred_tax_rate=preferred_tax_rate)

    def test_test_20_reduce_required_params(self):
        with self.assertRaises(TypeError, msg="reduce invoice : required params"):
            self.__billing.reduce_invoice()
