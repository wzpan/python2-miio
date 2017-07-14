# -*- coding: UTF-8 -*-
import logging
import click
import ast
import sys

import miio  # noqa: E402

_LOGGER = logging.getLogger(__name__)
pass_dev = click.make_pass_decorator(miio.device)


@click.group(invoke_without_command=True)
@click.option('--ip', envvar="MIIO_DEV_IP", required=False)
@click.option('--token', envvar="MIIO_DEV_TOKEN", required=False)
@click.option('-d', '--debug', default=False, count=True)
@click.pass_context
def cli(ctx, ip, token, debug):
    """A tool to command miio device."""
    if debug:
        logging.basicConfig(level=logging.DEBUG)
        _LOGGER.info("Debug mode active")
    else:
        logging.basicConfig(level=logging.INFO)

    # if we are scanning, we do not try to connect.
    if ctx.invoked_subcommand == "discover":
        return

    if ip is None or token is None:
        click.echo("You have to give ip and token!")
        sys.exit(-1)

    dev = miio.device(ip, token, debug)
    _LOGGER.debug("Connecting to %s with token %s", ip, token)

    ctx.obj = dev

    if ctx.invoked_subcommand is None:
        ctx.invoke(status)


@cli.command()
def discover():
    """Search for robots in the network."""
    miio.device.discover()

@cli.command()
@click.argument('cmd', required=True)
@click.argument('parameters', required=False)
@pass_dev
def raw_command(dev, cmd, parameters):
    """Run a raw command."""
    params = []
    if parameters:
        params = ast.literal_eval(parameters)
    click.echo("Sending cmd %s with params %s" % (cmd, params))
    click.echo(dev.raw_command(cmd, params))


if __name__ == "__main__":
    cli()
