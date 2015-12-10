from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pytest
import numpy as np

from pyrst.utils import rlencode, rldecode


class Test_rlencode:
    def test_example(self):
        A = np.array([
            [1,2,3,4],
            [1,2,3,4],
            [3,4,5,6],
            [3,3,3,3],
            [3,3,4,5],
            [3,3,4,5]])
        A_rl, n = rlencode(A, 0)
        assert np.array_equal(A_rl.shape, np.array([4, 4]))
        assert n.size == 4
        assert np.array_equal(A_rl, np.array([
            [1,2,3,4],
            [3,4,5,6],
            [3,3,3,3],
            [3,3,4,5]]))
        assert np.array_equal(n, np.array([2,1,1,2]))

    def test_example_transposed(self):
        A = np.array([
            [1,1,3,3,3,3],
            [2,2,4,3,3,3],
            [3,3,5,3,4,4],
            [4,4,6,3,5,5]])
        A_rl, n = rlencode(A, 1)
        assert np.array_equal(A_rl.shape, np.array([4, 4]))
        assert n.size == 4
        assert np.array_equal(A_rl, np.array([
            [1,3,3,3],
            [2,4,3,3],
            [3,5,3,4],
            [4,6,3,5]]))
        assert np.array_equal(n, np.array([2,1,1,2]))

    def test_1d_array(self):
        A = np.array([1,1,1,1,4,4,5])
        A_rl, n = rlencode(A)
        assert np.array_equal(A_rl, np.array([1,4,5]))
        assert np.array_equal(n, np.array([4,2,1]))

class Test_rldecode:
    pass