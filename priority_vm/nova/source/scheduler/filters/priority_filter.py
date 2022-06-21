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

from oslo_log import log as logging

from nova import objects
from nova.objects import fields
from nova.scheduler import filters
from nova.virt import hardware

LOG = logging.getLogger(__name__)


class PriorityFilter(filters.BaseHostFilter):

    def host_passes(self, host_state, spec_obj):
        if not host_state.priority:
            return False
        spec_obj = spec_obj.obj_clone()
        ram_ratio = host_state.ram_allocation_ratio
        cpu_ratio = host_state.cpu_allocation_ratio
        requested_topology = spec_obj.numa_topology
        host_topology = host_state.numa_topology
        pci_requests = spec_obj.pci_requests

        network_metadata = None
        if 'network_metadata' in spec_obj:
            network_metadata = spec_obj.network_metadata

        if pci_requests:
            pci_requests = pci_requests.requests

        flavor_priority = spec_obj.flavor.extra_specs.get(
            'hw:cpu_priority')
        hint_priority = spec_obj.get_scheduler_hint('priority')
        if not (flavor_priority in fields.CPUPriorityPolicy.ALL
                or hint_priority in fields.CPUPriorityPolicy.ALL):
            return True

        if requested_topology and host_topology:
            limits = objects.NUMATopologyLimits(
                cpu_allocation_ratio=cpu_ratio,
                ram_allocation_ratio=ram_ratio)
            if network_metadata:
                limits.network_metadata = network_metadata

            instance_topology = (hardware.numa_fit_instance_to_host(
                        host_topology, requested_topology,
                        limits=limits,
                        pci_requests=pci_requests,
                        pci_stats=host_state.pci_stats))
            if not instance_topology:
                LOG.debug("%(host)s, %(node)s fails NUMA topology "
                          "requirements. The instance does not fit on this "
                          "host.", {'host': host_state.host,
                                    'node': host_state.nodename},
                          instance_uuid=spec_obj.instance_uuid)
                return False
            host_state.limits['numa_topology'] = limits
            return True
        elif requested_topology:
            LOG.debug("%(host)s, %(node)s fails NUMA topology requirements. "
                      "No host NUMA topology while the instance specified "
                      "one.",
                      {'host': host_state.host, 'node': host_state.nodename},
                      instance_uuid=spec_obj.instance_uuid)
            return False
        else:
            return True
