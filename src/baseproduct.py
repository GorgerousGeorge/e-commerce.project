from ABC import abc, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
