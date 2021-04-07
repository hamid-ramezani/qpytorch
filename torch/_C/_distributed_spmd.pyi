from typing import List

from ._distributed_c10d import ProcessGroup

from torch import Tensor

class EventHandler: ...

class AllReduceComm(EventHandler):
    def __init__(self, process_group: ProcessGroup): ...

class DefaultBucketer(EventHandler): ...

class DefaultTrigger(EventHandler): ...

class Engine:
    def __init__(self, handlers: List[EventHandler]): ...
    def prepare_module(self, params: List[Tensor]): ...