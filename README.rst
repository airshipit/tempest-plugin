===============================================
Tempest Integration of airship-tempest-plugin
===============================================

The purpose of this plugin is to provide automated tests
for all OpenStack Airship components.

DISCALIMER:
This initial implementation is just to meet the first use case which is RBAC
testing. For RBAC testing, we only need to hit the API endpoint and check
role permission to the API being tested. Some of the REST clients will need to be
rewritten if functional testing is desired. Those that need to be rewritten
are documented in each service client code.

