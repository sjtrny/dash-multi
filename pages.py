from abc import ABCMeta, abstractmethod

class DashPage(metaclass=ABCMeta):

    @abstractmethod
    def layout(self):
        pass

    @abstractmethod
    def callbacks(self):
        pass
