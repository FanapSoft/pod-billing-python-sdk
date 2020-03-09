# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodDirectWithdraw

try:
    pod_settlement = PodDirectWithdraw(api_token=API_TOKEN, server_type=SERVER_MODE)

    print(pod_settlement.revoke_direct_withdraw(id=323))

    # OUTPUT
    # True

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
