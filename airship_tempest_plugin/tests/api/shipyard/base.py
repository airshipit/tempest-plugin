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

from airship_tempest_plugin.services.shipyard.json.actions_client import ActionsClient
from airship_tempest_plugin.services.shipyard.json.document_staging_client import DocumentStagingClient
from airship_tempest_plugin.services.shipyard.json.airflow_monitoring_client import AirflowMonitoringClient

from tempest import config
from tempest import test

from patrole_tempest_plugin import rbac_utils

CONF = config.CONF

class BaseShipyardTest(test.BaseTestCase):
    """Base class for Shipyard tests."""
    credentials = ['primary', 'admin']

    @classmethod
    def skip_checks(cls):
        super(BaseShipyardTest, cls).skip_checks()
        if not CONF.service_available.shipyard:
            raise cls.skipException("Shipyard is not enabled in the deployment")

    @classmethod
    def setup_clients(cls):
        super(BaseShipyardTest, cls).setup_clients()
        cls.auth_provider = cls.os_primary.auth_provider

        cls.shipyard_actions_client = ActionsClient(
            cls.auth_provider,
            CONF.shipyard.catalog_type,
            CONF.identity.region,
            CONF.shipyard.endpoint_type)
        cls.shipyard_document_staging_client = DocumentStagingClient(
            cls.auth_provider,
            CONF.shipyard.catalog_type,
            CONF.identity.region,
            CONF.shipyard.endpoint_type)
        cls.shipyard_airflow_monitoring_client = AirflowMonitoringClient(
            cls.auth_provider,
            CONF.shipyard.catalog_type,
            CONF.identity.region,
            CONF.shipyard.endpoint_type)
