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
from korth_spirit import Instance
from korth_spirit.data import ObjectLoadData
from korth_spirit.query import QueryEnum
from korth_spirit.sdk import aw_object_load

from .query import LoadQuery


class LoadObjects(LoadQuery):
    def __init__(
        self,
        instance: Instance,
        file_name: str = 'backup.json',
        binary_mode: bool = False
    ):
        """
        Initializes the Load Objects command.

        Args:
            instance (Instance): The instance to load the objects into.
            file_name (str): The file name to load the objects from.
            binary_mode (bool): Whether or not to load the data in binary mode
        """
        def _receive(data: dict):
            data.pop('id', None)
            data.pop('number', None)

            aw_object_load(
                ObjectLoadData(
                    **data
                )
            )

        super().__init__(
            instance,
            QueryEnum.OBJECT,
            _receive,
            file_name,
            binary_mode
        )
