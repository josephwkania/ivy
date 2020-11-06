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


from abc import ABCMeta
from ivy.exceptions.exceptions import NotImplementedException

class BasePlugin(object, metaclass=ABCMeta):
    '''
    Abstract base class for all the plugins providing standardized
    interfaces
    '''

    def __init__(self, ctx, **kwargs):
        self.ctx = ctx
        self.ctx.update(kwargs)
        
    def __str__(self):
        raise NotImplementedException()

    def __call__(self):
        raise NotImplementedException()