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

"""
https://github.com/openstack/airship-shipyard/blob/master/docs/source/API.rst#site-statuses-api
"""

from oslo_serialization import jsonutils as json

from tempest.lib.common import rest_client


class SiteStatusesClient(rest_client.RestClient):
    api_version = "v1.0"

    # Note: add support of query filters if testing beyond RBAC is desired
    def get_site_statuses(self):
        resp, body = self.get('site_statuses')
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)
