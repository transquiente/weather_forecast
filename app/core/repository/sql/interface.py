from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

EntityDC = TypeVar("EntityDC")


class IBaseRepository(ABC, Generic[EntityDC]):
    @abstractmethod
    def get(self, entity_id: UUID, **kwargs) -> EntityDC:
        raise NotImplementedError

    @abstractmethod
    def get_many(self, ids: set[UUID], raise_not_found: bool = True, **kwargs) -> list[EntityDC]:
        raise NotImplementedError

    @abstractmethod
    def add(self, entity: EntityDC, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_many(self, entities: list[EntityDC], **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity: EntityDC) -> None:
        raise NotImplementedError
