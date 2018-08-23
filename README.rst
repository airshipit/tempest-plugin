===============================================
Tempest Integration of airship-tempest-plugin
===============================================

Purpose:
--------
The purpose of this plugin is to provide automated tests
for all OpenStack Airship components.

DISCALIMER:
-----------
This initial implementation is just to meet the first use case which is RBAC
testing. For RBAC testing, we only need to hit the API endpoint and check
role permission to the API being tested. Some of the REST clients will need to be
rewritten if functional testing is desired. Those that need to be rewritten
are documented in each service client code.

Environment Information:
------------------------
Testing can be done in a airship-in-a-bottle environment. Please refer to [0] and [1].
Tempest and Tempest plugin installation can be done in a Python virtual environment.

FAQ:
----
- Where do the REST clients exist?
  https://github.com/att-comdev/airship-tempest-plugin/tree/master/airship_tempest_plugin/services
- Where do the tests exists? [3]
  https://github.com/att-comdev/airship-tempest-plugin/tree/master/airship_tempest_plugin/tests/api
- Example of where/how the REST clients are instantiated.
  https://github.com/att-comdev/airship-tempest-plugin/blob/master/airship_tempest_plugin/tests/api/shipyard/base.py
- Where do we define expected results (requirements)?
  https://github.com/att-comdev/airship-tempest-plugin/blob/master/airship_tempest_plugin/tests/api/common/rbac_roles.yaml
- Where do we add configuration to support another Airship component?
  https://github.com/att-comdev/airship-tempest-plugin/blob/master/airship_tempest_plugin/config.py
- Where do we run the test from?
  After the plugin is installed, run it from the tempest directory
- Example of how to run all the RBAC tests for Shipyard:
  'tempest run --regex airship_tempest_plugin.tests.api.shipyard.rbac'
- What is Patrole?
  https://github.com/openstack/patrole/blob/master/README.rst
- What is a Tempest plugin? [8]
  https://docs.openstack.org/tempest/latest/plugin.html

Patrole Supporting Documentation:
---------------------------------
Patrole documentation for requirements driven approach that is used: https://github.com/openstack/patrole/blob/master/doc/source/framework/requirements_authority.rst
Patrole role-overriding: https://github.com/openstack/patrole/blob/master/doc/source/framework/rbac_utils.rst#role-overriding
Patrole under-permission exception: https://github.com/openstack/patrole/blob/master/patrole_tempest_plugin/rbac_exceptions.py#L51
Patrole over-permission exception: https://github.com/openstack/patrole/blob/master/patrole_tempest_plugin/rbac_exceptions.py#L44

Future Considerations:
---------------------
Will the airship-tempest-plugin continue to live here: https://github.com/att-comdev/airship-tempest-plugin or will it be moved under OpenStack?
Will there exist a RBAC gate for all Airship projects? 

Referenced Links:
-----------------
[0] https://github.com/openstack/airship-in-a-bottle
[1] https://www.airshipit.org/
