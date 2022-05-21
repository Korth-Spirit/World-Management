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
from abc import ABC

from korth_spirit import Instance
from korth_spirit.query import QueryEnum


class FileABC(ABC):
    def __init__(
        self,
        instance: Instance,
        query_type: str,
        file_name: str = 'backup.json',
        binary_mode: bool = False
    ):
        """
        Initializes the Save Query command.

        Args:
            instance (Instance): The instance.
            query_type (str): The type of query to perform. { "attributes", "objects", "terrain" }
            file_name (str): The file name.
            binary_mode (bool): Whether or not to save the data in binary mode.
        """
        _query = query_type\
            .upper()\
            .removesuffix('S')\
            .replace('ATTRIBUTE', 'WORLD')

        self._instance = instance
        self._type = query_type
        self._query = QueryEnum[_query]
        self._file_name = file_name
        self._binary_mode = binary_mode
