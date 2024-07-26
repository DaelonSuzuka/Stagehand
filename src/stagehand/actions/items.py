from qtstrap import *
from abc import abstractmethod


class ActionItem(QWidget):
    @classmethod
    def get_subclasses(cls):
        return {c.name: c for c in cls.__subclasses__()}

    @classmethod
    def get_item(cls, name):
        return cls.get_subclasses()[name]

    @abstractmethod
    def set_data(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    def get_data(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    def reset(self):
        pass


class TriggerItem(QWidget):
    @classmethod
    def get_subclasses(cls):
        return {c.name: c for c in cls.__subclasses__()}

    @classmethod
    def get_item(cls, name):
        return cls.get_subclasses()[name]

    @abstractmethod
    def set_data(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    def get_data(self) -> dict:
        raise NotImplementedError

    def reset(self):
        pass


class FilterStackItem(QWidget):
    @classmethod
    def get_subclasses(cls):
        return {c.name: c for c in cls.__subclasses__()}

    @classmethod
    def get_item(cls, name):
        return cls.get_subclasses()[name]

    @abstractmethod
    def set_data(self, data: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_data(self) -> dict:
        raise NotImplementedError

    def reset(self) -> None:
        pass

    @abstractmethod
    def check(self) -> bool:
        raise NotImplementedError
