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
from argparse import Namespace

import management.commands.save as commands
from korth_spirit.instance import Instance
from management.commands import Aggregate as AggregateCommand
from management.protocols import Invoker


def register(invoker: Invoker, instance: Instance, args: Namespace):
    """
    Registers load commands.

    Args:
        invoker (LocalInvoker): The invoker to register the commands with.
        instance (ReceiverInstance): The instance to use for the commands.
        args (Namespace): The arguments to use for the commands.
    """

    kwargs = {
        "instance": instance,
        "file_name": args.file,
        "binary_mode": args.binary
    }
    invoker\
        .register(
            "SAVE ATRRIBUTES",
            commands.SaveAttributes(**kwargs)
        )\
        .register(
            "SAVE OBJECTS",
            commands.SaveObjects(**kwargs)
        ).register(
            "SAVE TERRAIN",
            commands.SaveTerrain(**kwargs)
        )

    file_name = args.file
    kwargs.pop("file_name")
    invoker\
        .register(
            "SAVE ALL",
            AggregateCommand(
                commands.SaveAttributes(**kwargs, file_name=f"attributes_{file_name}"),
                commands.SaveObjects(**kwargs, file_name=f"objects_{file_name}"),
                commands.SaveTerrain(**kwargs, file_name=f"terrain_{file_name}")
            )
        )
