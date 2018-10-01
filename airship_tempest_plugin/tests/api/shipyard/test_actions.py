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

from airship_tempest_plugin.tests.api.shipyard import base

from tempest.lib import decorators


class ActionsTest(base.BaseShipyardTest):

    def _get_action_id(self):
        resp = self.shipyard_actions_client.list_actions()
        self.assertTrue(len(resp[1]) > 0,
                        'No actions available, nothing to test')
        # get the response body
        return resp[1]['id']

    def _get_action_step_id(self):
        resp = self.shipyard_actions_client.list_actions()
        self.assertTrue(len(resp[1]) > 0,
                        'No actions available, nothing to test')
        return resp[1]['id'], resp[1]['steps'][0]['id']

    @decorators.idempotent_id('94901561-7ad1-4e9c-8df8-afe3a7f63c09')
    def test_list_actions(self):
        """List of actions, Successful with response status 200"""
        resp = self.shipyard_actions_client.list_actions()
        self.assertTrue(len(resp[1]) > 0,
                        'No actions available, nothing to test')
        self.assertEqual(resp.response['status'], '200')

    @decorators.idempotent_id('b0d4c23a-d3a4-4a12-8e10-ac6f8a98d33e')
    def test_get_action(self):
        action_id = self._get_action_id()
        """Get actions, Successful with response status 200"""
        resp = self.shipyard_actions_client.get_action(action_id)
        self.assertEqual(resp.response['status'], '200')

    @decorators.idempotent_id('a8bc9e6b-bfa3-4635-a1ec-0b9ddc9cb03f')
    def test_get_action_step(self):
        """Get actions step, Successful with response status 200"""
        action_id, step_id = self._get_action_step_id()
        resp = self.shipyard_actions_client.get_action_step(action_id, step_id)
        self.assertEqual(resp.response['status'], '200')
