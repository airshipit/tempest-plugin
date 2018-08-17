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
from tempest.lib import exceptions
from tempest.lib.common.utils import data_utils
from tempest.lib.common.utils import test_utils

from tempest.api.identity import base

class DocumentStagingRbacTest(rbac_base.BaseShipyardRbacTest):

    @rbac_rule_validation.action(service="shipyard",
                                 rules=["get_configdocs"])
    @decorators.idempotent_id('0ab53b15-bce9-494f-9a11-34dd2c44d699')
    def test_get_configdocs(self):
        with self.rbac_utils.override_role(self):
            self.shipyard_document_staging_client.get_configdocs()

    @rbac_rule_validation.action(service="shipyard",
                                 rules=["post_configdocs"])
    @decorators.idempotent_id('1a0daf92-9dba-470c-a317-66b41c0b3df7')
    def test_post_configdocs(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a BadRequest exception
            try:
                self.shipyard_document_staging_client.post_configdocs()
            except exceptions.BadRequest:
                pass

    @rbac_rule_validation.action(service="shipyard",
                                 rules=["get_configdocs_within_collection"])
    @decorators.idempotent_id('d64cfa75-3bbe-4688-8849-db5a54ce98ea')
    def test_get_configdocs_within_collection(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a NotFound exception
            try:
                self.shipyard_document_staging_client.get_configdocs_within_collection()
            except exceptions.NotFound:
                pass

    @rbac_rule_validation.action(service="shipyard",
                                 rules=["get_renderedconfigdocs"])
    @decorators.idempotent_id('0ab53b15-bce9-494f-9a11-34dd2c44d699')
    def test_get_renderedconfigdocs(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a NotFound exception
            try:
                self.shipyard_document_staging_client.get_renderedconfigdocs()
            except exceptions.NotFound:
                pass

    @rbac_rule_validation.action(service="shipyard",
                                 rules=["post_commitconfigdocs"])
    @decorators.idempotent_id('200d1cbf-ca11-4b92-9cfd-6cd2a90bc919')
    def test_post_commitconfigdocs(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a Conflict exception
            try:
                self.shipyard_document_staging_client.post_commitconfigdocs()
            except exceptions.Conflict:
                pass
