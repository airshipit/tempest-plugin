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
http://airship-shipyard.readthedocs.io/en/latest/API.html#document-staging-api
"""

from oslo_serialization import jsonutils as json

from tempest.lib.common import rest_client

# NOTE(rb560u): The following will need to be rewritten in the future if
# functional testing is desired:
#  - 'def post_configdocs`
#  - `def get_configdocs_within_collection`
#  - 'def post_commitconfigdocs'
# This initial implementation is just to meet the first use case which is RBAC
# testing. For RBAC testing, we only need to hit the API endpoint and check
# role permission to that API.


class DocumentStagingClient(rest_client.RestClient):
    api_version = "v1.0"

    def get_configdocs_status(self):
        resp, body = self.get('configdocs')
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)

    def create_configdocs(self):
        url = "configdocs/1"
        post_body = json.dumps({})
        resp, body = self.post(url, post_body)
        self.expected_success(201, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)

    def get_configdocs(self):
        resp, body = self.get('configdocs/1')
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)

    def get_renderedconfigdocs(self):
        resp, body = self.get('renderedconfigdocs')
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)

    def commit_configdocs(self):
        post_body = json.dumps({})
        resp, body = self.post("commitconfigdocs", post_body)
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)
