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
import common.func
import pytest


@pytest.mark.parametrize("params, expected", [
    ([(1, 2, 3)], [1]),
    ([(1, 2, 3), (4, 5, 6)], [1, 4]),
    ([(1, 2, 3), (4, 5, 6), (7, 8, 9)], [1, 4, 7]),
])
def test_on_each(params: list[tuple], expected: list) -> None:
    def callback(param: tuple):
        return param[0]
    assert list(
        common.func.on_each(
            params,
            callback
        )
    ) == expected

@pytest.mark.parametrize("funcs, args, expected", [
    (
        [
            lambda x, y: x + y,
            lambda x, y: x * y,
            lambda x, y: x - y,
            lambda x, y: x / y,
        ],
        [1, 2],
        [3, 2, -1, 0.5]
    ),
])
def test_and_do(funcs: list, args: tuple, expected: list) -> None:
    """
    Tests that the and_do function calls multiple functions.

    Args:
        funcs (list): The functions to call.
        args (list): The arguments to pass to the functions.
        kwargs (list): The keyword arguments to pass to the functions.
        expected (list): The expected return values of the functions.
    """
    assert list(
        common.func.and_do(
            funcs,
            *args,
        )
    ) == expected

@pytest.mark.parametrize("iterable, x, expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 4, 7]),
    ([1, 2, 3, 4, 5, 6, 7, 8], 3, [1, 4, 7]),
])
def test_every_x(iterable: list, x: int, expected: list) -> None:
    """
    Tests that the every_x function calls a function on every subset of x elements in the iterable.

    Args:
        iterable (list): The iterable to iterate over.
        x (int): The number of times to call the function.
        expected (list): The expected return values of the functions.
    """
    assert list(
        common.func.every_x(
            lambda x: x[0],
            iterable,
            x,
        )
    ) == expected
