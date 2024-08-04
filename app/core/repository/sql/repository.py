from typing import ClassVar, TypeAlias
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm.interfaces import ORMOption

from app.core.repository.sql.error import ObjectNotFound
from app.core.repository.sql.interface import IBaseRepository


class BaseRepository(IBaseRepository):
    model: ClassVar[TypeAlias] = NotImplemented
    base_options: list[ORMOption] = []

    def __init__(self, session: Session) -> None:
        self.session = session

    def _get(
        self,
        entity_id: UUID,
        load_refreshed: bool = False,
        _options: list[ORMOption] | None = None,
    ) -> model:
        instance = self.session.get(
            self.model, entity_id, options=_options or self.base_options, populate_existing=load_refreshed
        )
        if instance is None:
            raise ObjectNotFound(f"{self.model.__name__} with id {entity_id} not found")
        return instance

    def _get_many(
        self,
        ids: set[UUID],
        _options: list[ORMOption] | None = None,
        populate_existing: bool = False,
        raise_not_found: bool = True,
    ) -> list[model]:
        _options = _options or []
        stmt = (
            select(self.model)
            .options(*_options)
            .where(self.model.id.in_(ids))
            .execution_options(populate_existing=populate_existing)
        )
        result = self.session.execute(stmt)
        instances = list(result.unique().scalars())
        if raise_not_found and len(ids) > len(instances):
            not_found_ids = set(ids) - set([i.id for i in instances])  # noqa: C401, C403
            raise ObjectNotFound(
                f"Some ids are not presented in the system: {[str(obj) for obj in sorted(not_found_ids)]}"
            )
        return instances

    def get(self, entity_id: UUID, load_refreshed: bool = False, **kwargs) -> model:
        options = kwargs.get("options")
        return self._get(entity_id, load_refreshed, options if options is not None else self.base_options, **kwargs)

    def get_many(self, ids: set[UUID], raise_not_found: bool = True, **kwargs) -> list[model]:
        return self._get_many(ids, raise_not_found=raise_not_found, **kwargs)

    def add(self, entity: model, merge: bool = False, **kwargs) -> None:
        if merge:
            entity = self.session.merge(entity, options=self.base_options)
        self.session.add(entity)

    def add_many(self, entities: list[model], **kwargs) -> None:
        self.session.add_all(entities)

    def delete(self, entity: model) -> None:
        self.session.delete(entity)
