import click
import os

from clint.textui import colored, puts
from nginx_proxy import utils


@click.command(help='Connect to nginx proxy', name='nginx-proxy')
@click.pass_context
def nginx_proxy(ctx):
    utils.connect_container_to_proxy(ctx.obj['STAKKR'])