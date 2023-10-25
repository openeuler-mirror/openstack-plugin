# All rights reserved.
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

from neutron_lib.api import converters
from neutron_lib.api.definitions import network
from neutron_lib.api.definitions import network_mtu


MTU = 'mtu'

# The alias of the extension.
ALIAS = 'net-mtu-writable'

# Whether or not this extension is simply signaling behavior to the user
# or it actively modifies the attribute map.
IS_SHIM_EXTENSION = False

# Whether the extension is marking the adoption of standardattr model for
# legacy resources, or introducing new standardattr attributes. False or
# None if the standardattr model is adopted since the introduction of
# resource extension.
# If this is True, the alias for the extension should be prefixed with
# 'standard-attr-'.
IS_STANDARD_ATTR_EXTENSION = False

# The name of the extension.
NAME = 'Network MTU (writable)'

# A prefix for API resources. An empty prefix means that the API is going
# to be exposed at the v2/ level as any other core resource.
API_PREFIX = ''

# The description of the extension.
DESCRIPTION = (
    "Provides a writable MTU attribute for a network resource.")

# A timestamp of when the extension was introduced.
UPDATED_TIMESTAMP = "2017-07-12T00:00:00-00:00"


RESOURCE_ATTRIBUTE_MAP = {
    network.COLLECTION_NAME: {
        MTU: {'allow_post': True, 'allow_put': True, 'is_visible': True,
              'is_filter': True, 'is_sort_key': True,
              'validate': {'type:non_negative': None}, 'default': 0,
              'convert_to': converters.convert_to_int},
    },
}

# The subresource attribute map for the extension. It adds child resources
# to main extension's resource. The subresource map must have a parent and
# a parameters entry. If an extension does not need such a map, None can
# be specified (mandatory).
SUB_RESOURCE_ATTRIBUTE_MAP = {}

# The action map: it associates verbs with methods to be performed on
# the API resource.
ACTION_MAP = {}

# The action status.
ACTION_STATUS = {
}

# The list of required extensions.
REQUIRED_EXTENSIONS = [network_mtu.ALIAS]

# The list of optional extensions.
OPTIONAL_EXTENSIONS = []
