import abc


class AbstractCRUD(abc.ABC):

    @abc.abstractmethod
    def get_one(self, collection, criteria):
      pass

    @abc.abstractmethod
    def insert_one(self, model):
      pass

    @abc.abstractmethod
    def update_one(self, model):
        pass
