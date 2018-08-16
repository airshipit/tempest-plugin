# Copyright 2018 AT&T Corp
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from airship_tempest_plugin.tests.api.shipyard.rbac import rbac_base

from patrole_tempest_plugin import rbac_rule_validation

from tempest.common import utils
from tempest.lib import decorators
from tempest.lib.common.utils import data_utils
from tempest.lib.common.utils import test_utils

from tempest.api.identity import base

class ActionsRbacTest(rbac_base.BaseShipyardRbacTest):

    @rbac_rule_validation.action(service="shipyard",
                                 rules=["get_actions"])
    @decorators.idempotent_id('183dd007-8a97-4070-afc3-9318401ebad7')
    def test_get_actions(self):
        with self.rbac_utils.override_role(self):
            self.shipyard_actions_client.get_actions()
