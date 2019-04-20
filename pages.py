from abc import ABCMeta, abstractmethod

class DashPage(metaclass=ABCMeta):

    def __init__(self):
        self.layout = self._layout()
        self.callbacks = self._callbacks()

    @abstractmethod
    def _layout(self):
        pass

    @abstractmethod
    def _callbacks(self):
        pass
