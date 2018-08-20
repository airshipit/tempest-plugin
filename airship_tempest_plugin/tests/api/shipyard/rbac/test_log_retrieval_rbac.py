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

from tempest.lib import decorators
from tempest.lib import exceptions


class LogRetrievalRbacTest(rbac_base.BaseShipyardRbacTest):

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:get_action_step_logs"])
    @decorators.idempotent_id('5fd2c572-a226-482d-bdce-70d3ffcd7495')
    def test_get_action_step_logs(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a BadRequest exception
            try:
                self.shipyard_log_retrieval_client.get_action_step_logs()
            except exceptions.BadRequest:
                pass
