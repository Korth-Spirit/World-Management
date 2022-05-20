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
import json
import logging
from dataclasses import asdict

from common.file import append_to
from common.func import on_each
from korth_spirit import Instance
from korth_spirit.query import QueryEnum


class Save:
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
    
    def execute(self):
        """
        Executes the command.
        """
        def _receive(data):
            data = json.dumps(asdict(data), skipkeys=True, default=str)

            if self._binary_mode:
                data = data.encode('utf-8')

            append_to(self._file_name, data)

        logging.info(f'Saving {self._type} to {self._file_name}')
        
        on_each(
            self._instance.query(self._query),
            _receive,
            ignore_exceptions=True
        ) 
