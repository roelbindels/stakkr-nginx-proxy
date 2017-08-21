from stakkr import docker
from stakkr import stakkr_compose

def connect_container_to_proxy(self):
    services = stakkr_compose.get_enabled_services(stakkr_compose.get_configured_services())
    if 'nginx-proxy-slave' in services:
        network = self.project_name + '_proxy-tier'
        docker.add_container_to_network('nginx',network)
        docker.add_container_to_network('nginx-gen', network)
        docker.restart_container('{}_{}'.format(self.project_name,'apache'))
