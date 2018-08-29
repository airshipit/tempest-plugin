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

import logging

from airship_tempest_plugin.tests.api.shipyard.rbac import rbac_base

from patrole_tempest_plugin import rbac_rule_validation

from tempest import config
from tempest.lib import decorators
from tempest.lib import exceptions

CONF = config.CONF
LOG = logging.getLogger(__name__)


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
            # and NotFound exception
            try:
                self.shipyard_actions_client.create_action()
            except (exceptions.BadRequest, exceptions.NotFound):
                pass

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:action_deploy_site"])
    @decorators.idempotent_id('e69687da-8d4e-413b-a566-c0e56b5d1087')
    def test_deploy_site(self):
        with self.rbac_utils.override_role(self):
            LOG.warn("In this scenario, `workflow_orchestrator:create_action` "
                     "is enforced first and if permission is denied, then "
                     "there is no additional enforcement. If permission is "
                     "allowed to `workflow_orchestrator:create_action`, then "
                     "`workflow_orchestrator:action_deploy_site` is enforced. "
                     " If this test fails, check permissions of both actions.")
            try:
                self.shipyard_actions_client.create_action(
                    action="deploy_site")
            # Ignore exceptions besides Forbidden
            except (exceptions.BadRequest, exceptions.NotFound):
                pass

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:action_update_site"])
    @decorators.idempotent_id('95f3b377-99ae-4ac2-8ce3-1e52ca081abc')
    def test_update_site(self):
        with self.rbac_utils.override_role(self):
            LOG.warn("In this scenario, `workflow_orchestrator:create_action` "
                     "is enforced first and if permission is denied, then "
                     "there is no additional enforcement. If permission is "
                     "allowed to `workflow_orchestrator:create_action`, then "
                     "`workflow_orchestrator:action_update_site` is enforced. "
                     " If this test fails, check permissions of both actions.")
            try:
                self.shipyard_actions_client.create_action(
                    action="update_site")
            # Ignore exceptions besides Forbidden
            except (exceptions.BadRequest, exceptions.NotFound):
                pass

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:action_update_software"])
    @decorators.idempotent_id('18fae927-e759-4a60-bceb-81807b9f2c10')
    def test_update_software(self):
        with self.rbac_utils.override_role(self):
            LOG.warn("In this scenario, `workflow_orchestrator:create_action` "
                     "is enforced first and if permission is denied, then "
                     "there is no additional enforcement. If permission is "
                     "allowed to `workflow_orchestrator:create_action`, then "
                     "`workflow_orchestrator:action_update_software` is "
                     "enforced. If this test fails, check permissions of both "
                     "actions.")
            try:
                self.shipyard_actions_client.create_action(
                    action="update_software")
            # Ignore exceptions besides Forbidden
            except (exceptions.BadRequest, exceptions.NotFound):
                pass

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:action_redeploy_server"])
    @decorators.idempotent_id('bba1eb77-c350-4c3b-b62d-3eea8bc13110')
    def test_redeploy_server(self):
        with self.rbac_utils.override_role(self):
            LOG.warn("In this scenario, `workflow_orchestrator:create_action` "
                     "is enforced first and if permission is denied, then "
                     "there is no additional enforcement. If permission is "
                     "allowed to `workflow_orchestrator:create_action`, then "
                     "`workflow_orchestrator:action_redeploy_server` is "
                     "enforced. If this test fails, check permissions of both "
                     "actions.")
            try:
                self.shipyard_actions_client.create_action(
                    action="redeploy_server")
            # Ignore exceptions besides Forbidden
            except (exceptions.BadRequest, exceptions.NotFound):
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

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:get_action_validation"])
    @decorators.idempotent_id('a5156dcd-2674-4295-aa6a-d8db1bd4cf4b')
    def test_get_action_validation(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a NotFound exception
            try:
                self.shipyard_actions_client.get_action_validation()
            except exceptions.NotFound:
                pass

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

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:invoke_action_control"])
    @decorators.idempotent_id('4f6b6564-ff1d-463a-aee8-ed2d51e2a286')
    def test_invoke_action_control(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a NotFound exception
            try:
                self.shipyard_actions_client.invoke_action_control()
            except exceptions.NotFound:
                pass
