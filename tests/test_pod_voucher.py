# coding=utf-8
from __future__ import unicode_literals

import unittest

from pod_base import InvalidDataException
from random import randrange
from pod_billing import PodBilling
from pod_billing import PodVoucher
from tests.config import *


class TestPodVoucher(unittest.TestCase):
    __slots__ = ("__voucher", "__billing")

    def setUp(self):
        self.__voucher = PodVoucher(api_token=API_TOKEN, server_type=SERVER_MODE)
        self.__billing = PodBilling(api_token=API_TOKEN, server_type=SERVER_MODE)

    def test_1_define_credit_voucher(self):
        vouchers = [{
            "name": "کد اعتبار 1 ریالی تست پایتون",
            "amount": 1,
            "count": 1,
            "description": "این کد اعتبار به صورت تستی و با پایتون ثبت شده است "
        }]
        expire_date = "1420/12/01"
        result = self.__voucher.define_credit_voucher(vouchers=vouchers, guild_code=GUILD_CODE, expire_date=expire_date)
        self.assertIsInstance(result, list, msg="define credit voucher (all params) : check instance")
        self.assertEqual(len(result), 1, msg="define credit voucher (all params) : check len")

    @staticmethod
    def __generate_random_voucher(prefix=""):
        return "{}{}".format(prefix, randrange(1000, 2000000))

    def test_1_define_credit_voucher_all_params(self):
        vouchers = [{
            "name": "کد اعتبار 1 ریالی تست پایتون",
            "amount": 1,
            "count": 2,
            "description": "این کد اعتبار به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("CREDIT-"), self.__generate_random_voucher("CREDIT-")]
        }, {
            "name": "کد اعتبار 2 ریالی تست پایتون",
            "amount": 2,
            "count": 1,
            "description": "این کد اعتبار به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("CREDIT-")]
        }]
        expire_date = "1420/12/01"
        result = self.__voucher.define_credit_voucher(vouchers=vouchers, guild_code=GUILD_CODE, expire_date=expire_date,
                                                      limited_consumer_id=USER_ID, currency_code="IRR")
        self.assertIsInstance(result, list, msg="define credit voucher (all params) : check instance")
        self.assertEqual(len(result), 3, msg="define credit voucher (all params) : check len")

    def test_1_define_credit_voucher_invalid_hash_length(self):
        vouchers = [{
            "name": "کد اعتبار 1 ریالی تست پایتون",
            "amount": 1,
            "count": 3,  # changed
            "description": "این کد اعتبار به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("CREDIT-"), self.__generate_random_voucher("CREDIT-")]
        }, {
            "name": "کد اعتبار 2 ریالی تست پایتون",
            "amount": 2,
            "count": 1,
            "description": "این کد اعتبار به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("CREDIT-")]
        }]
        expire_date = "1420/12/01"

        with self.assertRaises(InvalidDataException, msg="define credit voucher : invalid hash length"):
            self.__voucher.define_credit_voucher(vouchers=vouchers, guild_code=GUILD_CODE, expire_date=expire_date,
                                                 limited_consumer_id=USER_ID, currency_code="IRR")

    def test_1_define_credit_voucher_validation_error(self):
        vouchers = [{
            "name": "کد اعتبار 1 ریالی تست پایتون",
            "amount": "1",  # should be int
            "count": "3",  # should be int
            "description": "این کد اعتبار به صورت تستی و با پایتون ثبت شده است "
        }, {
            "name": "کد اعتبار 1 ریالی تست پایتون",
            "amount": "1",  # should be int
            "count": "1",  # should be int
            "description": "این کد اعتبار به صورت تستی و با پایتون ثبت شده است "
        }]
        expire_date = "1420-12-01"  # correct format yyyy/mm/dd
        limited_consumer_id = "123"  # should be int
        with self.assertRaises(InvalidDataException, msg="define credit voucher : validation error"):
            self.__voucher.define_credit_voucher(vouchers=vouchers, guild_code=GUILD_CODE, expire_date=expire_date,
                                                 limited_consumer_id=limited_consumer_id, currency_code="IRR")

    def test_1_define_credit_voucher_required_params(self):
        with self.assertRaises(TypeError, msg="define credit voucher : required params"):
            self.__voucher.define_credit_voucher()

    def test_2_define_discount_amount_voucher(self):
        vouchers = [{
            "name": "کد تخفیف 1 ریالی تست پایتون",
            "amount": 1,
            "count": 2,
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است "
        }, {
            "name": "کد تخفیف 1 ریالی تست پایتون",
            "amount": 1,
            "count": 1,
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است "
        }]
        expire_date = "1420/12/01"
        result = self.__voucher.define_discount_amount_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                                               expire_date=expire_date)

        self.assertIsInstance(result, list, msg="define discount amount voucher (all params) : check instance")
        self.assertEqual(len(result), 3, msg="define discount amount voucher (all params) : check len")

    def test_2_define_discount_amount_voucher_all_params(self):
        vouchers = [{
            "name": "کد تخفیف 1 ریالی تست پایتون",
            "amount": 1,
            "count": 2,
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS1-"), self.__generate_random_voucher("DIS1-")]
        }, {
            "name": "کد تخفیف 1 ریالی تست پایتون",
            "amount": 1,
            "count": 1,
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS2-")]
        }]
        expire_date = "1420/12/01"
        product_list = PRODUCT_IDs
        dealer_business_id_list = DEALER_BUSINESS_IDs
        result = self.__voucher.define_discount_amount_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                                               expire_date=expire_date, limited_consumer_id=USER_ID,
                                                               currency_code="IRR", product_id=product_list,
                                                               dealer_business_id=dealer_business_id_list)

        self.assertIsInstance(result, list, msg="define discount amount voucher (all params) : check instance")
        self.assertEqual(len(result), 3, msg="define discount amount voucher (all params) : check len")

    def test_2_define_discount_amount_voucher_invalid_hash_len(self):
        vouchers = [{
            "name": "کد تخفیف 1 ریالی تست پایتون",
            "amount": 1,
            "count": 3,  # changed
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS1-"), self.__generate_random_voucher("DIS1-")]
        }, {
            "name": "کد تخفیف 1 ریالی تست پایتون",
            "amount": 1,
            "count": 1,
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS2-")]
        }]
        expire_date = "1420/11/01"
        with self.assertRaises(InvalidDataException, msg="define discount amount voucher : invalid hash len"):
            self.__voucher.define_discount_amount_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                                          expire_date=expire_date, limited_consumer_id=USER_ID,
                                                          currency_code="IRR")

    def test_2_define_discount_amount_voucher_validation_error(self):
        vouchers = [{
            "name": "کد تخفیف 1 ریالی تست پایتون",
            "amount": "1",  # should be int
            "count": "3",  # should be int
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS1-"), self.__generate_random_voucher("DIS1-")]
        }, {
            "name": "کد تخفیف 1 ریالی تست پایتون",
            "amount": "1",  # should be int
            "count": "1",  # should be int
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS2-")]
        }]
        expire_date = "1420-11-01"  # correct format yyyy/mm/dd
        with self.assertRaises(InvalidDataException, msg="define discount amount voucher : validation error"):
            self.__voucher.define_discount_amount_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                                          expire_date=expire_date, limited_consumer_id=USER_ID,
                                                          currency_code="IRR")

    def test_2_define_discount_amount_voucher_required_params(self):
        with self.assertRaises(TypeError, msg="define discount amount voucher : required params"):
            self.__voucher.define_discount_amount_voucher()

    def test_3_define_discount_percentage_voucher(self):
        vouchers = [{
            "name": "کد تخفیف 1 درصدی تست پایتون",
            "discountPercentage": 1,
            "amount": 100,
            "count": 2,
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است "
        }, {
            "name": "کد تخفیف 2 درصدی تست پایتون",
            "discountPercentage": 2,
            "amount": 200,
            "count": 1,
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است "
        }]
        expire_date = "1420/12/01"
        discount_type = PodVoucher.DISCOUNT_TYPE_ONE_TIME_INVOICE
        result = self.__voucher.define_discount_percentage_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                                                   expire_date=expire_date, discount_type=discount_type)

        self.assertIsInstance(result, list, msg="define discount percentage voucher (all params) : check instance")
        self.assertEqual(len(result), 3, msg="define discount percentage voucher (all params) : check len")

    def test_3_define_discount_percentage_voucher_all_params(self):
        vouchers = [{
            "name": "کد تخفیف 1 درصدی تست پایتون",
            "discountPercentage": 1,
            "amount": 100,
            "count": 2,
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS1-"), self.__generate_random_voucher("DIS1-")]
        }, {
            "name": "کد تخفیف 2 درصدی تست پایتون",
            "discountPercentage": 2,
            "amount": 200,
            "count": 1,
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS2-")]
        }]
        expire_date = "1420/12/01"
        product_list = PRODUCT_IDs
        dealer_business_id_list = DEALER_BUSINESS_IDs
        discount_type = PodVoucher.DISCOUNT_TYPE_ONE_TIME_INVOICE
        result = self.__voucher.define_discount_percentage_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                                                   expire_date=expire_date, limited_consumer_id=USER_ID,
                                                                   currency_code="IRR", product_id=product_list,
                                                                   dealer_business_id=dealer_business_id_list,
                                                                   discount_type=discount_type)

        self.assertIsInstance(result, list, msg="define discount percentage voucher (all params) : check instance")
        self.assertEqual(len(result), 3, msg="define discount percentage voucher (all params) : check len")

    def test_3_define_discount_percentage_voucher_invalid_hash_len(self):
        vouchers = [{
            "name": "کد تخفیف 1 درصدی تست پایتون",
            "discountPercentage": 1,
            "amount": 100,
            "count": 3,  # changed
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS1-"), self.__generate_random_voucher("DIS1-")]
        }, {
            "name": "کد تخفیف 2 درصدی تست پایتون",
            "discountPercentage": 2,
            "amount": 200,
            "count": 1,
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS2-")]
        }]
        expire_date = "1420/11/01"
        discount_type = PodVoucher.DISCOUNT_TYPE_ONE_TIME_INVOICE
        with self.assertRaises(InvalidDataException, msg="define discount percentage voucher : invalid hash len"):
            self.__voucher.define_discount_percentage_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                                              expire_date=expire_date, limited_consumer_id=USER_ID,
                                                              currency_code="IRR", discount_type=discount_type)

    def test_3_define_discount_percentage_voucher_validation_error(self):
        vouchers = [{
            "name": "کد تخفیف 1 درصدی تست پایتون",
            "discountPercentage": "1",
            "amount": "100",  # should be int
            "count": "3",  # should be int
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS1-"), self.__generate_random_voucher("DIS1-")]
        }, {
            "name": "کد تخفیف 2 درصدی تست پایتون",
            "discountPercentage": "2",
            "amount": "200",  # should be int
            "count": "1",  # should be int
            "description": "این کد تخفیف به صورت تستی و با پایتون ثبت شده است ",
            "hash": [self.__generate_random_voucher("DIS2-")]
        }]
        expire_date = "1420-11-01"  # correct format yyyy/mm/dd
        discount_type = 3  # one of PodVoucher.DISCOUNT_TYPE_ONE_TIME_ITEM or PodVoucher.DISCOUNT_TYPE_ONE_TIME_INVOICE
        # or PodVoucher.DISCOUNT_TYPE_UNLIMITED

        with self.assertRaises(InvalidDataException, msg="define discount percentage voucher : validation error"):
            self.__voucher.define_discount_percentage_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                                              expire_date=expire_date, limited_consumer_id=USER_ID,
                                                              currency_code="IRR", discount_type=discount_type)

    def test_3_define_discount_percentage_voucher_required_params(self):
        with self.assertRaises(TypeError, msg="define discount percentage voucher : required params"):
            self.__voucher.define_discount_percentage_voucher()

    def __get_invoice(self, **kwargs):
        kwargs["products"] = [
            {
                "productId": 0,
                "price": 50000,
                "quantity": 1,
                "productDescription": "محصول اول در پایتون"
            }
        ]
        kwargs["guild_code"] = GUILD_CODE
        kwargs["description"] = "تست اعمال کد تخفیف بر روی فاکتور بعد از صدور فاکتور - پایتون تست"
        return self.__billing.issue_invoice(**kwargs)

    def __get_voucher(self):
        vouchers = [
            {
                "name": "تخفیف 5000",
                "amount": 5000,
                "count": 1,
                "description": "Discount 5000 Rials"
            }
        ]
        voucher = self.__voucher.define_discount_amount_voucher(vouchers=vouchers, guild_code=GUILD_CODE,
                                                                expire_date="1420/12/01")
        return voucher[0]

    def test_4_apply_voucher(self):
        invoice = self.__get_invoice(postVoucherEnabled=True)
        voucher = self.__get_voucher()
        result = self.__voucher.apply_voucher(invoice_id=invoice["id"], voucher_hash=voucher["hash"])

        self.assertIsInstance(result, dict, msg="apply voucher : check instance")
        self.assertEqual(result["invoiceItemSrvs"][0]["discount"], voucher["creditAmount"],
                         msg="apply voucher : check amount")

    def test_4_apply_voucher_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="apply voucher : validation error"):
            self.__voucher.apply_voucher(invoice_id="123456", voucher_hash="ABCDE")

    def test_4_apply_voucher_required_params(self):
        with self.assertRaises(TypeError, msg="apply voucher : required params"):
            self.__voucher.apply_voucher()

    def test_5_get_voucher_list(self):
        params = {
            "page": 1,
            "size": 50
        }
        result = self.__voucher.get_voucher_list(**params)
        self.assertIsInstance(result, list, msg="get voucher list : check instance")

    def test_5_get_voucher_list_all_params(self):
        params = {
            "page": 1,
            "size": 50,
            "type": PodVoucher.DISCOUNT_TYPE_ONE_TIME_INVOICE | PodVoucher.DISCOUNT_TYPE_ONE_TIME_ITEM |
                    PodVoucher.DISCOUNT_TYPE_UNLIMITED,
            "consumerId": 123456,
            "hash": "",
            "name": "",
            "guildCode": ["API_GUILD", "CLOTHING_GUILD"],
            "currencyCode": "IRR",
            "amountFrom": 0,
            "amountTo": 2000,
            "discountPercentageFrom": 5,
            "discountPercentageTo": 10,
            "expireDateFrom": "1398/12/01",
            "expireDateTo": "1399/01/01",
            "productId": [1234, 4567],
            "consumDateFrom": "1398/12/15",
            "consumDateTo": "1398/12/17",
            "usedAmountFrom": 10000,
            "usedAmountTo": 200000,
            "active": True,
            "used": False
        }

        result = self.__voucher.get_voucher_list(**params)
        self.assertIsInstance(result, list, msg="get voucher list (all params) : check instance")

    def test_5_get_voucher_list_validation_error(self):
        params = {
            "page": 1,
            "size": 50,
            "type": "1",    # should be int
            "consumerId": "123456",    # should be int
            "hash": 123,    # should be str
            "name": 123,
            "guildCode": ["API_GUILD", "CLOTHING_GUILD"],
            "currencyCode": "IRR",
            "amountFrom": 0,
            "amountTo": 2000,
            "discountPercentageFrom": 5,
            "discountPercentageTo": 10,
            "expireDateFrom": "1398-12-01",    # should be format yyyy/mm/dd
            "expireDateTo": "1399-01-01",    # should be format yyyy/mm/dd
            "productId": [1234, 4567],
            "consumDateFrom": "1398-12-15",    # should be format yyyy/mm/dd
            "consumDateTo": "1398-12-17",    # should be format yyyy/mm/dd
            "usedAmountFrom": "10000",    # should be int
            "usedAmountTo": "200000",    # should be int
            "active": "True",    # should be boolean
            "used": "False"    # should be boolean
        }
        with self.assertRaises(InvalidDataException, msg="get voucher list : validation error"):
            self.__voucher.get_voucher_list(**params)

    def test_6_activate_voucher(self):
        voucher = self.__get_voucher()

        result = self.__voucher.activate_voucher(voucher["id"])
        self.assertIsInstance(result, dict, msg="activate voucher : check instance")
        self.assertEqual(result["active"], True, msg="activate voucher : check status")

    def test_6_activate_voucher_required_params(self):
        with self.assertRaises(TypeError, msg="activate voucher : required param"):
            self.__voucher.activate_voucher()

    def test_6_activate_voucher_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="activate voucher : validation error"):
            self.__voucher.activate_voucher(voucher_id="123456")

    def test_7_deactivate_voucher(self):
        voucher = self.__get_voucher()

        result = self.__voucher.deactivate_voucher(voucher["id"])
        self.assertIsInstance(result, dict, msg="deactivate voucher : check instance")
        self.assertEqual(result["active"], False, msg="deactivate voucher : check status")

    def test_7_deactivate_voucher_required_params(self):
        with self.assertRaises(TypeError, msg="deactivate voucher : required param"):
            self.__voucher.deactivate_voucher()

    def test_7_deactivate_voucher_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="deactivate voucher : validation error"):
            self.__voucher.deactivate_voucher(voucher_id="123456")
