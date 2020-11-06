# IVY is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# IVY is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with IVY.  If not, see <http://www.gnu.org/licenses/>.


'''
Tests for `ivy.utils` module.

author: jakeret
'''


import pytest

from ivy.exceptions.exceptions import IllegalAccessException
from ivy.utils.struct import ImmutableStruct
from ivy.utils.struct import Struct


class TestStruct(object):

    def test_struct(self):
        
        a = Struct()
        a['x'] = 1
        assert a.x == 1
        
        a.y = 2
        assert a['y'] == 2

    def test_init(self):
        a = Struct(z=3)
        assert a['z'] == 3
        assert a.z == 3

    def test_copy(self):
        a = Struct(z=3)
        b = a.copy()
        assert b.z == 3
        
        
    def test_immutableStruct(self):
        a = ImmutableStruct()
        try:
            a['x'] = 1
            pytest.fail("Not mutation allowd on immutable", False)
        except IllegalAccessException:
            assert True
            
