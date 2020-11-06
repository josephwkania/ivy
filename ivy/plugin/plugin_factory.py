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
Created on Mar 5, 2014

author: jakeret
'''

from ivy.exceptions.exceptions import UnsupportedPluginTypeException
import importlib


class PluginFactory(object):
    """
    Simple factory creating instances of plugins
    """

    @staticmethod
    def createInstance(pluginName, ctx):
        """
        Instantiates the given plugin. Expects that the given module contains a class
        
        with the name 'Plugin'
        
        :param pluginName: name of the plugin to instanciate
        
        :return plugin: an instance of the plugin
        
        :raises: UnsupportedPluginTypeException
        """
        try:
            module = importlib.import_module(pluginName)
            plugin = module.Plugin(ctx)
            return plugin
        except ImportError as ex:
            raise UnsupportedPluginTypeException("Module '%s' could not be loaded" % pluginName, ex)
        except AttributeError as ex:
#             print("Module '%s' has no class definition 'Plugin'" % pluginName)
#             print("Old skool 'plugin' is deprecated! Adapt your implementation")
#             try:
#                 plugin = module.plugin()
#                 return plugin
#             except AttributeError:
                raise UnsupportedPluginTypeException("Module '%s' has no class definition 'Plugin(ctx)'" % pluginName)
            
        except Exception as ex:
            raise UnsupportedPluginTypeException("Module '%s' could not be instantiated'" % pluginName, ex)
        