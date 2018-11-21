from abc import ABC, abstractmethod


class BaseLogWriter(ABC):

    @abstractmethod
    def append_log(self, log):
        pass

    @abstractmethod
    def end_unification(self):
        pass
