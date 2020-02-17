# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_billing import PodSettlement

try:
    pod_settlement = PodSettlement(api_token=API_TOKEN, server_type=SERVER_MODE)

    print(pod_settlement.add_auto_settlement(guild_code=GUILD_CODE, currencyCode="IRR"))

    # OUTPUT
    # True

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
