from lib import docker

def connect_container_to_proxy(self):
    services = [service for service in self.user_config_main.get('services', '').split(',') if service != '']
    if 'nginx-proxy-slave' in services:
        network = self.project_name + '_proxy-tier'
        docker.add_container_to_network('nginx',network)
        docker.add_container_to_network('nginx-gen', network)
        docker.restart_container('{}_{}'.format(self.project_name,'apache'))
