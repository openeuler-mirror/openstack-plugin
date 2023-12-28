# openstack-plugin

本仓库用来存放openstack sig开发的openstack插件代码。仓库分支用来区分OpenStack的适配版本。`master`分支暂不存放任何代码。请切换分支查看相关特性。

## 目录结构

顶层目录为`特性名称`，每个特性目录包含两个子目录`source`和`patch`， source是openstack代码，基线是上游社区指定版本，由于gitee的git仓库容量有限，移除了git历史。`patch`是该特性的git patch文件，用来制作RPM包。

## 说明

### 项目基线
- ironic: 13.0.7
- neutron: 15.3.4
- neutron-lib: 1.29.2
- nova: 20.6.1
- os-vif: 1.17.0
- python-neutronclient: 6.14.1
- python-openstackclient: 4.0.2
- python-openstacksdk: 0.36.5

### 特性
- 流量分散 neutron为[15.3.4](https://opendev.org/openstack/neutron/src/tag/15.3.4)、neutron-lib为[1.29.2](https://opendev.org/openstack/neutron-lib/src/tag/1.29.2)。neutron还涉及entry point的修改，在子包中完成。特性spec请阅读相关[文档](https://gitee.com/openeuler/openstack/blob/master/docs/spec/distributed-traffic.md)。
- 支持纳管带DPU卸载的裸金属节点。一共包含3个patch，其中：
  - nova-offload-support-baremetal-with-dpu-ctrl.patch 应用于裸机管理节点的nova项目
  - ironic-offload-support-baremetal-with-dpu.patch 应用于裸机管理节点的ironic项目
  - nova-offload-support-baremetal-with-dpu-agent.patch 应用于DPU上的nova项目
- 支持纳管网络vDPA设备（virtio-net）。一共包含6个patch，其中：
  - nova-offload-support-generic-vdpa-of-smartnic-20231129.patch 应用于控制节点和计算节点的nova项目
  - os-vif-offload-support-generic-vdpa-of-smartnic-20231129.patch 应用于控制节点和计算节点的os-vif项目
  - neutron-offload-support-generic-vdpa-of-smartnic-20231129.patch 应用于控制节点和计算节点的neutron项目
  - neutron-lib-offload-support-generic-vdpa-of-smartnic-20231129.patch 应用于控制节点的neutron-lib项目
  - python-neutronclient-offload-support-generic-vdpa-of-smartnic-20231129.patch 应用于控制节点的python-neutronclient项目
  - python-openstackclient-offload-support-generic-vdpa-of-smartnic-20231129.patch 应用于控制节点的python-openstackclient项目
