from setuptools import setup

setup(
    name='StakkrNginxProxy',
    version='3.5',
    packages=['nginx_proxy'],
    entry_points='''
        [stakkr.plugins]
        nginx_proxy=nginx_proxy.core:nginx_proxy
    '''
)
