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


"""
Tests for `ivy.loop ` module.

author: jakeret
"""


from pickle import dumps
from pickle import loads

from ivy import context
from ivy.loop import Loop
from ivy.plugin.parallel_plugin_collection import ParallelPluginCollection
from ivy.utils.struct import Struct
from ivy.context import ctx
from ivy.workflow_manager import WorkflowManager
from ivy.loop import ListIter


PLUGIN_NAME = "test.plugin.simple_plugin"

class TestPickle(object):
 
    def test_loop_pickle(self):
        loop = Loop([PLUGIN_NAME, PLUGIN_NAME])
        p = next(loop)
        
        sLoop = dumps(loop)
        loop2 = loads(sLoop)
        
        for p in loop2:
            p()

        loop.reset()
        
        sLoop = dumps(loop)
        loop2 = loads(sLoop)
        
        for p in loop2:
            p()


    def test_struct_pickle(self):
        struct = Struct(value1=1)
        struct.params = Struct(backend="multiprocessing")
        
        sStruct = dumps(struct)
        struct2 = loads(sStruct)


    def test_parallel_plugin_collection_pickle(self):
        ctx = context.ctx()
           
        parallelPluginCollection = ParallelPluginCollection(
                                    "ivy.plugin.simple_map_plugin",
                                    ["ivy.plugin.simple_square_plugin"], 
                                    "ivy.plugin.simple_reduce_plugin")
        
        sParallelPluginCollection = dumps(parallelPluginCollection)
        parallelPluginCollectio2 = loads(sParallelPluginCollection)

    def test_context_pickle(self):
        lCtx = ctx()
        sLCtx = dumps(lCtx)
        lCtx2 = loads(sLCtx)        

    def test_workflow_context_pickle(self):
        args = ["--backend=multiprocessing",
        "--cpu-count=1",
        "test.config.workflow_config_parallel"]
           
        mgr = WorkflowManager(args)
          
        lCtx = ctx()
        sLCtx = dumps(lCtx)
        lCtx2 = loads(sLCtx)        

    def test_ListIter_pickle(self):
        listIter = ListIter(["a", "b", "c"])
        item = next(listIter)
        
        sListIter = dumps(listIter)
        listIter2 = loads(sListIter)
        
        for p in listIter2:
            pass


if __name__ == '__main__':
#     pytest.main()
    test = TestPickle()
    test.test_loop_pickle()