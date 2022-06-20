import os

import docker


class DockerRuntime(object):
    def __init__(self):
        try:
            docker_kwargs = docker.utils.kwargs_from_env()
            self.client = docker.APIClient(version="auto", **docker_kwargs)
        except docker.errors.DockerException:
            raise InitException

    def images(self, name=None, quiet=None):
        return self.client.images(name=name, quiet=quiet)

    def volumes(self, name=None):
        return self.client.volumes(name=name)

    def containers(self, name=None):
        return self.client.containers(name=name)

    def inspect_image(self, image_tag):
        return self.client.history(image_tag)

    def inspect_container(self, container_name):
        # args: container_name(str)
        return self.client.inspect_container(container_name)
    
    def history(self, name):
        return self.client.history(name)

    def build(
        self,
        path=None,
        tag=None,
        nocache=None,
        rm=None,
        decode=None,
        network_mode=None,
        pull=None,
        forcerm=None,
        buildargs=None,
    ):
        return self.client.build(
            path=path,
            tag=tag,
            nocache=nocache,
            rm=rm,
            decode=decode,
            network_mode=network_mode,
            pull=pull,
            forcerm=forcerm,
            buildargs=buildargs,
        )

    def push(self, name, **kwargs):
        return self.client.push(name, **kwargs)

    def pull(self, image, tag):
        return self.client.pull(repository=image, tag=tag, stream=True)

    def login(self, username, password, server, image_type):
        return self.client.login(username, password, server, image_type)
        
class IsulaRuntime(object):
    def __init__(self):
        from isula import client
        try:
            self.builder_client = client.init_builder_client()
            self.isulad_client = client.init_isulad_client()
        except Exception:
            raise InitException

    def images(self, name=None, quiet=None):
        return self.builder_client.list_images(image_name=name)
    
    def volumes(self):
        return self.isulad_client.list_volumes()
    
    def containers(self, filters=None):
        return self.isulad_client.list_containers(filters=filters)

    def inspect_image(self, image_tag):
        # TODO(wxy): This API doesn't work now. Correct it.
        #return self.isulad_client.inspect_image(image_tag)
        raise NotImplementedError
    
    def inspect_container(self,container_id):
        return self.isulad_client.inspect_container(container_id)

    def history(self, name):
        # isula doesn't support this API.
        raise NotImplementedError

    def build(
        self,
        path=None,
        tag=None,
        nocache=None,
        rm=None,
        decode=None,
        network_mode=None,
        pull=None,
        forcerm=None,
        buildargs=None,
    ):
        docker_file = os.path.join(path, 'Dockerfile')
        output = 'isulad:' + tag
        image_format = 'oci'
        return self.builder_client.build_image(docker_file, output,
            image_format, path, nocache=nocache)

    def push(self, name, **kwargs):
        return self.builder_client.push_image(name, "oci")
    
    def pull(self, image, tag):
        return self.builder_client.pull_image(image)

    def login(self,username, password, server):
        return self.isulad_client.login(username, password, server)


class RuntimeAdapter(object):
    def __init__(self, base_runtime):
        if base_runtime == "docker":
            self.runtime = DockerRuntime()
        elif base_runtime == "isula":
            self.runtime = IsulaRuntime()

    def images(self, name=None, quiet=None):
        return self.runtime.images(name=name, quiet=quiet)

    def inspect_image(self, image_tag):
        return self.runtime.inspect_image(image_tag)

    def history(self, name):
        return self.runtime.history(name)

    def build(
        self,
        path=None,
        tag=None,
        nocache=None,
        rm=None,
        decode=None,
        network_mode=None,
        pull=None,
        forcerm=None,
        buildargs=None,
    ):
        return self.runtime.build(
            path=path,
            tag=tag,
            nocache=nocache,
            rm=rm,
            decode=decode,
            network_mode=network_mode,
            pull=pull,
            forcerm=forcerm,
            buildargs=buildargs,
        )

    def push(self, name, **kwargs):
        return self.runtime.push(name, **kwargs)


class InitException(Exception):
    def __init__(self):
        super(InitException, self).__init__()