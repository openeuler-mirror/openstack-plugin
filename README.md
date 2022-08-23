# openstack-plugin

本仓库用来存放openstack sig开发的openstack插件代码。仓库分支用来区分OpenStack的适配版本。`master`分支暂不存放任何代码。请切换分支查看相关特性。

## 目录结构

顶层目录为`项目名称`，每个目录包含两个子目录`source`和`patch`， source是openstack代码，基线是上游社区指定版本，由于gitee的git仓库容量有限，移除了git历史。`patch`是该特性的git patch文件，用来制作RPM包。

## 说明

### 项目基线

- Nova: 25.0.0
- OpenStack-helm: ced30abead0bddb528d0c5fb7c1627dd8f1e22ba
- OpenStack-helm-infra: ff70971009d29a37619e8e82080663a9ab76d57b
- Kolla: 14.2.0
- Kolla-ansible: 14.2.0

### 特性 

- 虚拟机高低优先级
    nova为[25.0.0](https://opendev.org/openstack/nova/src/tag/25.0.0)、placement为[7.0.0](https://opendev.org/openstack/placement/src/tag/7.0.0)，特性spec请阅读相关[文档](https://gitee.com/openeuler/openstack/blob/master/docs/spec/priority_vm.md)
