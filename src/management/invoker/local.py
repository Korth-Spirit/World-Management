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
from management.protocols import Command


class LocalInvoker:
    def __init__(self):
        """
        Initializes a new instance of the LocalInvoker class.
        """
        self._history: list[Command] = list()
        self._commands: dict[str, Command] = dict()

    @property
    def history(self) -> list:
        """
        Gets the history of commands.

        Returns:
            list: The history of commands.
        """
        return self._history

    def unregister(self, name: str) -> "LocalInvoker":
        """
        Unregisters a command.

        Args:
            name (str): The name of the command to unregister.

        Returns:
            LocalInvoker: The current instance.
        """
        self._commands.pop(name)

        return self

    def register(self, name: str, command: Command) -> "LocalInvoker":
        """
        Registers a command.

        Args:
            name (str): The name of the command to register.
            command (Command): The command to register.

        Returns:
            LocalInvoker: The current instance.
        """
        self._commands[name] = command

        return self
    
    def invoke(self, name: str) -> "LocalInvoker":
        """
        Executes a command.

        Args:
            name (str): The name of the command to execute.

        Returns:
            LocalInvoker: The current instance.
        """
        command = self._commands.get(name)

        if not command:
            raise KeyError(f"Command '{name}' not found.")

        command.execute()
        self._history.append(command)

        return self
