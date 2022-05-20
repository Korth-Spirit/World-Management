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
from typing import Callable, Generator, Iterable, Tuple


def on_each(iterable: Iterable[Tuple], callback: Callable, ignore_exceptions: bool = False) -> None:
    """
    Iterates over all parameters in an iterable and passes them to a callback.

    Args:
        iterable (Iterable[Tuple]): A list of parameter for the callback.
        callback (Callable): The callback to call for each parameter.
        ignore_exceptions (bool): Whether to ignore exceptions.
    """
    for each in iterable:
        try:
            callback(each)
        except Exception as e:
            if not ignore_exceptions:
                raise e

def and_do(funcs: Iterable[Callable], *args: Tuple, **kwargs: Tuple) -> None:
    """
    Creates a function that calls all the functions in the iterable.

    Args:
        funcs (Iterable[Callable]): The functions to call.
        *args (Tuple): The arguments to pass to the functions.
        **kwargs (Tuple): The keyword arguments to pass to the functions.

    Yields:
        Generator: The return value of the functions.
    """
    for each in funcs:
        yield each(*args, **kwargs)

def every_x(func: Callable, iterable: Iterable, x: int = 5):
    """
    Calls the function on every subset of x elements in the iterable.

    Args:
        func (Callable): The function to call.
        iterable (Iterable): The iterable to iterate over.
        x (int): The number of times to call the function.

    Yields:
        Generator: The return value of the function per x elements.
    """
    store: list = list()
    for index, value in enumerate(iterable, start = 1):
        store.append(value)
        if index % x == 0:
            yield func(store)
            store.clear()

    if len(store) > 0:
        yield func(store)
