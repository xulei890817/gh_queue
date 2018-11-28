from abc import ABCMeta, abstractmethod


class BaseQueue(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def push_left(self):
        pass

    @abstractmethod
    def push_array_left(self):
        pass

    @abstractmethod
    def push_right(self):
        pass

    @abstractmethod
    def push_array_right(self):
        pass

    @abstractmethod
    def pop_left(self):
        pass

    @abstractmethod
    def pop_right(self):
        pass

    @property
    @abstractmethod
    def qsize(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def get_nowait(self):
        pass

    @abstractmethod
    def get_batch_nowait(self):
        pass

    @abstractmethod
    def put_nowait(self):
        pass
