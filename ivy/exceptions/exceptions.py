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
Created on Mar 4, 2014

author: jakeret
'''


class IllegalAccessException(Exception):
    """Raised when an immutable struct is tried to be modified"""
    pass

class NotImplementedException(Exception):
    """Raised when a methods of an ABC are not overwritten"""
    pass

class InvalidAttributeException(Exception):
    """Raised when attributes are not valid"""
    pass

class UnsupportedPluginTypeException(Exception):
    """Raised when a plugin cannot be found or be instanciated"""
    pass

class InvalidLoopException(Exception):
    """Raised when a loop cannot be executed properly"""
    pass
