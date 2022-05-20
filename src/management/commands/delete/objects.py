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
import logging

from common.func import on_each
from korth_spirit import Instance
from korth_spirit.data import ObjectDeleteData
from korth_spirit.query import QueryEnum
from korth_spirit.sdk import aw_object_delete
from management.commands.iterator import Iterator


class DeleteObjects(Iterator):
    def __init__(self, instance: Instance):
        """
        Initializes the Delete Objects command.

        Args:
            instance (Instance): The instance.
        """
        self._instance = instance

        super().__init__(
            self._instance.query(QueryEnum.OBJECT),
            lambda data: aw_object_delete(
                ObjectDeleteData(data.number, data.x, data.z)
            )
        )
