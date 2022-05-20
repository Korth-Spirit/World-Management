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


def append_to(file: str, data: str | bytes) -> None:
    """
    Appends the data to the file.
    If the data is a bytes, the file will be opened in binary mode.

    Args:
        file (str): The name of the file to append to.
        data (str or bytes): The data to append.
    """
    mode = "ab+" if type(data) == bytes else "a+"

    with open(file, mode) as f:
        logging.debug(f"Appending {data} to {file}")
        f.write(data)

        if type(data) == bytes:
            f.write(b"\n")
        else:
            f.write("\n")

def load(file: str, binary_mode: bool = False) -> dict:
    """
    Loads the file.

    Args:
        file (str): The name of the file to load.
        binary (bool): Whether to open the file in binary mode.

    Returns:
        dict: The data loaded from the file.
    """
    mode = "rb" if binary_mode else "r"

    with open(file, mode) as f:
        for line in f:
            if binary_mode:
                line = line.decode("utf-8")
            yield json.loads(line)
