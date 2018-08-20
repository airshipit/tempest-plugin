# Copyright 2015
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
from oslo_config import cfg

service_available_group = cfg.OptGroup(name="service_available",
                                       title="Available Airship Services")

ServiceAvailableGroup = [
    cfg.BoolOpt("shipyard",
                default=True,
                help="Whether or not Shipyard is expected to be available."),
]

shipyard_group = cfg.OptGroup(name='shipyard',
                              title='Shipyard service options')

ShipyardGroup = [
    cfg.StrOpt('endpoint_type',
               default='internal',
               choices=['public', 'admin', 'internal'],
               help="The endpoint type to use for the Shipyard service"),
    cfg.StrOpt('catalog_type',
               default='shipyard',
               help="Catalog type of the Shipyard service"),
]


def get_opt_lists(self, conf):
    """Get a list of options for sample config generation"""
    return [
        (service_available_group, ServiceAvailableGroup),
        (shipyard_group, ShipyardGroup)
    ]
