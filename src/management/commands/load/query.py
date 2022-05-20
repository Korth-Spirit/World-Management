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

from common.file import load
from common.func import on_each
from korth_spirit import Instance
from korth_spirit.query import QueryEnum


class LoadQuery:
    def __init__(
        self,
        instance: Instance,
        query_type: QueryEnum,
        load_function: callable,
        file_name: str = 'backup.json',
        binary_mode: bool = False
    ):
        """
        Initializes the Load Query command.

        Args:
            instance (Instance): The instance.
            query_type (QueryEnum): The type of query to perform.
            load_function (callable): The function to use to load the data.
            file_name (str): The file name.
            binary_mode (bool): Whether or not to load the data in binary mode
        """        
        self._instance = instance
        self._query = query_type
        self._file_name = file_name
        self._binary_mode = binary_mode
        self._load_function = load_function
    
    def execute(self):
        """
        Executes the command.
        """
        logging.info(f'Loading {self._query} from {self._file_name}')
        def _receive(data: dict):
            self._load_function(data)

        on_each(
            load(
                self._file_name,
                self._binary_mode
            ),
            _receive
        ) 
