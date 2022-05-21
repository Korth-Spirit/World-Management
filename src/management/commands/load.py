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

from common.file import load
from common.func import on_each
from korth_spirit.data import ObjectLoadData, TerrainNodeData
from korth_spirit.query import QueryEnum, WorldAttributeEnum
from korth_spirit.sdk import aw_object_load, aw_terrain_load_node
from korth_spirit.sdk.write_data import write_data

from .file_abc import FileABC


class Load(FileABC):
    def _load_function(self, data: dict):
        """
        Loads the data based on the query type.

        Args:
            data (dict): The data to load.
        """
        if self._query_type == QueryEnum.OBJECT:
            aw_object_load(ObjectLoadData(**data))
        elif self._query_type == QueryEnum.TERRAIN:
            aw_terrain_load_node(TerrainNodeData(**data))
        elif self._query_type == QueryEnum.WORLD:
            write_data(
                WorldAttributeEnum[data['name']].value,
                data['value']
            )
        
    
    def execute(self):
        logging.info(f'Loading {self._type} from {self._file_name}')
        
        def _receive(data: dict):
            data.pop('id', None)
            data.pop('number', None)
            self._load_function(data)

        on_each(
            load(
                self._file_name,
                self._binary_mode
            ),
            _receive
        )
