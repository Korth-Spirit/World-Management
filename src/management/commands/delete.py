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

from korth_spirit.query import QueryEnum
from korth_spirit.sdk import (aw_delete_all_objects, aw_terrain_delete_all,
                              aw_world_attributes_reset)


class Delete:
    def __init__(
        self,
        query_type: str
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

        self._type = query_type
        self._query = QueryEnum[_query]
    
    def execute(self):
        """
        Executes the command.
        """
        logging.info(f'Deleting {self._type}')
        
        if self._query == QueryEnum.OBJECT:
            aw_delete_all_objects()
        elif self._query == QueryEnum.TERRAIN:
            aw_terrain_delete_all()
        elif self._query == QueryEnum.WORLD:
            aw_world_attributes_reset()
