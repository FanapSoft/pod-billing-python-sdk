# coding=utf-8
from __future__ import unicode_literals

import unittest

from pod_base import InvalidDataException, APIException
from pod_billing import PodDirectWithdraw
from tests.config import *


class TestPodDirectWithdraw(unittest.TestCase):
    __slots__ = "__direct_withdraw"

    def setUp(self):
        self.__direct_withdraw = PodDirectWithdraw(api_token=API_TOKEN, server_type=SERVER_MODE)

    @staticmethod
    def __load_private_key():
        with open(PRIVATE_KEY_PATH, "r") as private_key_file:
            return private_key_file.read()

    def test_1_define_direct_withdraw(self):
        try:
            result = self.__direct_withdraw.define_direct_withdraw(username=USERNAME_BANK,
                                                                   private_key=self.__load_private_key(),
                                                                   deposit_number=DEPOSIT_NUMBER,
                                                                   wallet="PODLAND_WALLET", on_demand=True,
                                                                   min_amount=0, max_amount=1000)
            self.assertIsInstance(result, dict, msg="define direct withdraw : check instance")
            self.assertEqual(result["onDemand"], True, msg="define direct withdraw : check on demand")
            self.assertEqual(result["maxAmount"], 1000, msg="define direct withdraw : check max amount")
        except APIException as e:
            self.assertEqual(e.error_code, 170, msg="define direct withdraw : check error code 170"
                                                    "[already active]")

    def test_1_define_direct_withdraw_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="define direct withdraw : validation error"):
            self.__direct_withdraw.define_direct_withdraw(username="", private_key="",
                                                          deposit_number=DEPOSIT_NUMBER, wallet="PODLAND_WALLET",
                                                          on_demand="True", min_amount="0", max_amount="1000")

    def test_1_define_direct_withdraw_required_params(self):
        with self.assertRaises(TypeError, msg="define direct withdraw : required params"):
            self.__direct_withdraw.define_direct_withdraw()

    def test_2_direct_withdraw_list(self):
        params = {
            "wallet": "PODLAND_WALLET"
        }
        result = self.__direct_withdraw.direct_withdraw_list(**params)

        self.assertIsInstance(result, list, msg="direct withdraw list : check instance")

    def test_3_update_direct_withdraw(self):
        result = self.__direct_withdraw.direct_withdraw_list()
        if len(result) == 0:
            self.skipTest("define direct withdraw: There are no active permissions")

        try:
            result = self.__direct_withdraw.update_direct_withdraw(id=result[0]["id"], username=USERNAME_BANK,
                                                                   private_key=self.__load_private_key(),
                                                                   deposit_number=DEPOSIT_NUMBER,
                                                                   wallet="PODLAND_WALLET", on_demand=True,
                                                                   min_amount=0, max_amount=20000)
            self.assertIsInstance(result, dict, msg="define direct withdraw : check instance")
            self.assertEqual(result["onDemand"], True, msg="define direct withdraw : check on demand")
            self.assertEqual(result["maxAmount"], 20000, msg="define direct withdraw : check max amount")
        except APIException as e:
            self.assertEqual(e.error_code, 170, msg="define direct withdraw : check error code 170 [already active]")

    def test_3_update_direct_withdraw_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="define direct withdraw : validation error"):
            self.__direct_withdraw.update_direct_withdraw(id="456", username="", private_key="",
                                                          deposit_number=DEPOSIT_NUMBER, wallet="PODLAND_WALLET",
                                                          on_demand="True", min_amount="0", max_amount="1000")

    def test_3_update_direct_withdraw_required_params(self):
        with self.assertRaises(TypeError, msg="define direct withdraw : required params"):
            self.__direct_withdraw.update_direct_withdraw()

    def test_4_revoke_direct_withdraw(self):
        result = self.__direct_withdraw.direct_withdraw_list()
        if len(result) == 0:
            self.skipTest("define direct withdraw: There are no active permissions")

        result = self.__direct_withdraw.revoke_direct_withdraw(id=result[0]["id"])

        self.assertIsInstance(result, bool, msg="revoke direct withdraw : check instance")
        self.assertEqual(result, True, msg="revoke direct withdraw : check result")

    def test_4_revoke_direct_withdraw_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="revoke direct withdraw : validation error"):
            self.__direct_withdraw.revoke_direct_withdraw(id="456")

    def test_4_revoke_direct_withdraw_required_params(self):
        with self.assertRaises(TypeError, msg="revoke direct withdraw : required params"):
            self.__direct_withdraw.revoke_direct_withdraw()
