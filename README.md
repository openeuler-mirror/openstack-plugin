# openstack-plugin

本仓库用来存放openstack sig开发的openstack插件代码。仓库分支用来区分OpenStack的适配版本。`master`分支暂不存放任何代码。请切换分支查看相关特性。

## 目录结构

顶层目录为`特性名称`，每个特性目录包含两个子目录`source`和`patch`， source是openstack代码，基线是上游社区指定版本，由于gitee的git仓库容量有限，移除了git历史。`patch`是该特性的git patch文件，用来制作RPM包。

## 说明

### 项目基线
- Neutron: 15.3.4
- Neutron-lib: 1.29.2

## 特性说明

