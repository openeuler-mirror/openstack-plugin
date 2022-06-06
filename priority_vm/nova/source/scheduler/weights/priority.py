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

"""
Priority Weigher.  Weigh hosts by their High adn Low Priority CPU usage.

"""

import nova.conf
from nova.scheduler import utils
from nova.scheduler import weights

CONF = nova.conf.CONF


class PriorityWeighter(weights.BaseHostWeigher):
    minval = 0

    def weight_multiplier(self, host_state):
        """Override the weight multiplier."""
        return utils.get_weight_multiplier(
            host_state, 'cpu_weight_multiplier',
            CONF.filter_scheduler.cpu_weight_multiplier)

    def _weigh_object(self, host_state, weight_properties):
        """Higher weights win.  We want spreading to be the default."""
        weight = 0

        priority = utils.get_instance_priority(weight_properties)
        if priority is None:
            vcpus_free = (
                    host_state.vcpus_total * host_state.cpu_allocation_ratio -
                    host_state.vcpus_used)
            weight = vcpus_free
        elif priority.Lower() == 'high':
            high_vcpus_free = (
                    host_state.vcpus_total - host_state.high_vcpus_used)
            weight = high_vcpus_free
        elif priority.Lower() == 'low':
            low_vcpus_free = (
                    host_state.vcpus_total * host_state.cpu_allocation_ratio -
                    host_state.vcpus_total -
                    host_state.low_vcpus_used)
            weight = low_vcpus_free

        return weight


