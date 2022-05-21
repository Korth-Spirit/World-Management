# Copyright (c) 2022 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import argparse
import logging

from management.instance import ReceiverInstance
from management.invoker import LocalInvoker


def main() -> None:
    """
    The main function.
    """
    argument_parser = argparse.ArgumentParser(
        prog="backup",
        description="Korth Spirit World Backup Utility for Activeworlds"
    )

    argument_parser.add_argument(
        'file',
        help="File to use",
        type=str,
    )

    argument_parser.add_argument(
        '-b', '--binary',
        help="If specified, files will be written in binary mode",
        default=False,
        action="store_true"
    )

    argument_parser.add_argument(
        '-c', '--config',
        help="Configuration file to use",
        default="configuration.json",
        type=str
    )

    argument_parser.add_argument(
        '-t', '--type',
        help="Query type to use. Prefixed with <value>_",
        default="all",
        type=str,
        choices=["all", "terrain", "objects", "attributes"]
    )

    argument_parser.add_argument(
        '-v', '--verbose',
        help="If specified, debug logging will be enabled",
        default=False,
        action="store_true"
    )

    exclusive_group = argument_parser.add_mutually_exclusive_group()
    exclusive_group.add_argument(
        '-l', '--load',
        help="If specified, the instance will begin loading the specified --file",
        default=False,
        action="store_true"
    )
    exclusive_group.add_argument(
        '-d', '--delete',
        help="If specified, the instance will begin deleting the specified --type",
        default=False,
        action="store_true"
    )

    arguments = argument_parser.parse_args()

    if arguments.verbose:
        logging.basicConfig(level=logging.DEBUG)

    with ReceiverInstance() as instance:
        actor = LocalInvoker.create_loaded(instance, arguments)

        action = 'LOAD' if arguments.load else 'SAVE'
        action = 'DELETE' if arguments.delete else action

        actor.invoke(f"{action} {arguments.type.upper()}")
