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


class ActionsRbacTest(rbac_base.BaseShipyardRbacTest):

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:list_actions"])
    @decorators.idempotent_id('183dd007-8a97-4070-afc3-9318401ebad7')
    def test_list_actions(self):
        with self.rbac_utils.override_role(self):
            self.shipyard_actions_client.list_actions()

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:create_action"])
    @decorators.idempotent_id('fff43c6f-b6ed-44dd-b47b-02c45d7bdb8c')
    def test_create_action(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a BadRequest exception
            try:
                self.shipyard_actions_client.create_action()
            except exceptions.BadRequest:
                pass

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:get_action"])
    @decorators.idempotent_id('68e2f10f-0676-41bb-8f47-bc695e1aa536')
    def test_get_action(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a NotFound exception
            try:
                self.shipyard_actions_client.get_action()
            except exceptions.NotFound:
                pass

    ''' NEEDS REWORK AS SHIPYARD NOT DOING POLICY ENFORCEMENT FIRST
    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:get_action_validation"])
    @decorators.idempotent_id('a5156dcd-2674-4295-aa6a-d8db1bd4cf4b')
    def test_get_action_validation(self):
        with self.rbac_utils.override_role(self):
            self.shipyard_actions_client.get_action_validation()
    '''

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:get_action_step"])
    @decorators.idempotent_id('6243d2ff-f88e-41cf-8169-140a551834a4')
    def test_get_action_step(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a NotFound exception
            try:
                self.shipyard_actions_client.get_action_step()
            except exceptions.NotFound:
                pass

    ''' NEEDS REWORK AS SHIPYARD NOT DOING POLICY ENFORCEMENT FIRST
    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:invoke_action_control"])
    @decorators.idempotent_id('4f6b6564-ff1d-463a-aee8-ed2d51e2a286')
    def test_invoke_action_control(self):
        with self.rbac_utils.override_role(self):
            self.shipyard_actions_client.invoke_action_control()
    '''
