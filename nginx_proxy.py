import click
import os

from clint.textui import colored, puts
from plugins.nginx_proxy.lib import nginx_proxy_utils


@click.command(help='Connect to nginx proxy', name='nginx-proxy')
@click.pass_context
def nginx_proxy(ctx):
    nginx_proxy_utils.connect_container_to_proxy(ctx.obj['LAMP'])