# coding=utf-8
from __future__ import unicode_literals

import unittest

from pod_base import InvalidDataException, APIException
from random import randint
from pod_billing import PodSettlement, StatusSettlement, ToolCodeSettlement
from tests.config import *


class TestPodSettlement(unittest.TestCase):
    __slots__ = "__settlement"

    def setUp(self):
        self.__settlement = PodSettlement(api_token=API_TOKEN, server_type=SERVER_MODE)

    def test_01_request_wallet_settlement(self):
        result = self.__settlement.request_wallet_settlement(amount=10000)
        self.assertIsInstance(result, dict, msg="request wallet settlement : check instance")

    def test_01_request_wallet_settlement_all_params(self):
        params = {
            "wallet": "PODLAND_WALLET",
            "firstName": "رضا",
            "lastName": "زارع",
            "sheba": SHEBA_NUMBER,
            "currencyCode": "IRR",
            "uniqueId": str(randint(10000, 99999999)),
            "description": "درخواست برداشت وجه با پایتون",
        }
        result = self.__settlement.request_wallet_settlement(amount=10000, **params)
        self.assertIsInstance(result, dict, msg="request wallet settlement (all params): check instance")

    def test_01_request_wallet_settlement_required_param(self):
        with self.assertRaises(TypeError, msg="request wallet settlement : required param"):
            self.__settlement.request_wallet_settlement()

    def test_01_request_wallet_settlement_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="request wallet settlement : validation error"):
            self.__settlement.request_wallet_settlement(amount="10000")

    def test_02_request_guild_settlement(self):
        result = self.__settlement.request_guild_settlement(amount=10000, guild_code=GUILD_CODE)
        self.assertIsInstance(result, dict, msg="request guild settlement : check instance")

    def test_02_request_guild_settlement_all_params(self):
        params = {
            "wallet": "PODLAND_WALLET",
            "firstName": "رضا",
            "lastName": "زارع",
            "sheba": SHEBA_NUMBER,
            "currencyCode": "IRR",
            "uniqueId": str(randint(10000, 99999999)),
            "description": "درخواست برداشت وجه با پایتون"
        }
        result = self.__settlement.request_guild_settlement(amount=10000, guild_code=GUILD_CODE, **params)
        self.assertIsInstance(result, dict, msg="request guild settlement (all params): check instance")

    def test_02_request_guild_settlement_required_param(self):
        with self.assertRaises(TypeError, msg="request guild settlement : required param"):
            self.__settlement.request_guild_settlement()

    def test_02_request_guild_settlement_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="request guild settlement : validation error"):
            self.__settlement.request_guild_settlement(amount="10000", guild_code=123456)

    def test_03_request_settlement_by_tool(self):
        result = self.__settlement.request_settlement_by_tool(amount=10000, guild_code=GUILD_CODE,
                                                              tool_code=ToolCodeSettlement.PAYA, tool_id=SHEBA_NUMBER)
        self.assertIsInstance(result, dict, msg="request settlement by tool : check instance")

    def test_03_request_settlement_by_tool_all_params(self):
        params = {
            "wallet": "PODLAND_WALLET",
            "firstName": "رضا",
            "lastName": "زارع",
            # "currencyCode": "IRR",
            # "uniqueId": str(randint(10000, 99999999)),
            "description": "درخواست برداشت وجه با پایتون"
        }
        result = self.__settlement.request_settlement_by_tool(amount=10000, guild_code=GUILD_CODE,
                                                              tool_code=ToolCodeSettlement.PAYA, tool_id=SHEBA_NUMBER,
                                                              **params)
        self.assertIsInstance(result, dict, msg="request settlement by tool (all params): check instance")

    def test_03_request_settlement_by_tool_required_param(self):
        with self.assertRaises(TypeError, msg="request settlement by tool : required param"):
            self.__settlement.request_settlement_by_tool()

    def test_03_request_settlement_by_tool_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="request settlement by tool : validation error"):
            self.__settlement.request_settlement_by_tool(amount="10000", guild_code=123456, tool_code="asdasd",
                                                         tool_id="")

    def test_04_list_settlements(self):
        result = self.__settlement.list_settlements()
        self.assertIsInstance(result, list, msg="list settlements : check instance")

    def test_04_list_settlements_all_params(self):
        params = {
            "id": 8071,  # شناسه درخواست
            "statusCode": StatusSettlement.DONE,  # کد وضعیت درخواست
            "currencyCode": "IRR",  # کد ارز
            "fromAmount": 100.0,  # حد پایین مبلغ درخواست شده
            "toAmount": 999,  # حد بالای مبلغ درخواست شده
            "fromDate": "1398/11/22",  # حد پایین تاریخ درخواست شمسی yyyy/mm/dd
            "toDate": "1398/12/01",  # حد بالای تاریخ درخواست شمسی yyyy/mm/dd
            "uniqueId": "64973000",  # شناسه یکتا
            "firstName": "رضا",  # نام صاحب حساب
            "lastName": "زارع",  # نام خانوادگی صاحب حساب
            "toolCode": ToolCodeSettlement.CARD,  # نوع ابزار برای تسویه کارت به کارت،پایا،ساتنا
            "toolId": CARD_NUMBER,  # شماره ابزاری که تسویه به آن واریز گردیده
            "invoiceId": 1  # شماره فاکتور
        }
        result = self.__settlement.list_settlements(**params)
        self.assertIsInstance(result, list, msg="list settlements (all params): check instance")

    def test_04_list_settlements_validation_error(self):
        params = {
            "id": "8071",
            "statusCode": "ABCD",
            "fromAmount": "100.0",
            "toAmount": "999",
            "fromDate": "1398_11_22",
            "toDate": "1398_12_01",
            "uniqueId": "64973000",
            "firstName": "رضا",
            "lastName": "زارع",
            "toolCode": "BAJSKDHJASd",
            "toolId": "12345",
            "invoiceId": "1"
        }
        with self.assertRaises(InvalidDataException, msg="list settlements : validation error"):
            self.__settlement.list_settlements(**params)

    def test_05_add_auto_settlement(self):
        try:
            result = self.__settlement.add_auto_settlement(guild_code=GUILD_CODE)
            self.assertEqual(result, True, msg="add auto settlement : check instance")
        except APIException as e:
            self.assertEqual(e.message, "این حساب شما در حال حاضر دارای تسویه حساب خودکار می باشد",
                             msg="add auto settlement : check instance")

    def test_05_add_auto_settlement_all_params(self):
        try:
            result = self.__settlement.add_auto_settlement(guild_code=GUILD_CODE, currencyCode="IRR")
            self.assertEqual(result, True, msg="add auto settlement (all params): check instance")
        except APIException as e:
            self.assertEqual(e.message, "این حساب شما در حال حاضر دارای تسویه حساب خودکار می باشد",
                             msg="add auto settlement : check instance")

    def test_05_add_auto_settlement_required_params(self):
        with self.assertRaises(TypeError, msg="add auto settlement : required params"):
            self.__settlement.add_auto_settlement()

    def test_06_remove_auto_settlement(self):
        try:
            result = self.__settlement.remove_auto_settlement(guild_code=GUILD_CODE)
            self.assertEqual(result, True, msg="remove auto settlement : check instance")
        except APIException as e:
            self.assertEqual(e.message, "درخواست تسویه حساب  یافت نشد", msg="remove auto settlement : check instance")

    def test_06_remove_auto_settlement_all_params(self):
        try:
            result = self.__settlement.remove_auto_settlement(guild_code=GUILD_CODE, currencyCode="IRR")
            self.assertEqual(result, True, msg="remove auto settlement (all params): check instance")
        except APIException as e:
            self.assertEqual(e.message, "درخواست تسویه حساب  یافت نشد", msg="remove auto settlement : check instance")

    def test_06_remove_auto_settlement_required_params(self):
        with self.assertRaises(TypeError, msg="remove auto settlement : required params"):
            self.__settlement.remove_auto_settlement()
