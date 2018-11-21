from abc import ABC, abstractmethod


class BaseLogHandler(ABC):

    @abstractmethod
    def get_next_log(self):
        pass
