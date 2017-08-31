from stakkr import docker_actions
from stakkr import stakkr_compose

def connect_container_to_proxy(self):
    services = stakkr_compose.get_enabled_services(stakkr_compose.get_configured_services())
    if 'nginx-proxy-slave' in services:
        network = self.project_name + '_proxy-tier'
        docker_actions.add_container_to_network('nginx',network)
        docker_actions.add_container_to_network('nginx-gen', network)
        docker_actions.restart_container('{}_{}'.format(self.project_name,'apache'))
