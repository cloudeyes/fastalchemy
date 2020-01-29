from contextvars import ContextVar
from typing import Callable, Dict, Optional, Union
import importlib
import threading
import types

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp
from starlette.requests import Request

from sqlalchemy.orm import Session, Query, sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import DeclarativeMeta
import sqlalchemy

_Session: sessionmaker = None
_SessionContext: ContextVar[Optional[Session]] = ContextVar("_session", default=None)

class Database:
    '''For typing.'''
    engine: Engine
    Base: DeclarativeMeta

database: Database = None

class SessionInitializationError(Exception):
    pass


class SQLAlchemyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, 
            db_module: Union[types.ModuleType, str]='database',
            models_module: Union[types.ModuleType, str]='models'):
        global _Session
        global database

        super().__init__(app)

        if type(db_module) == str and database is None:
            database = importlib.import_module(db_module)
        else:
            database = db_module

        if type(models_module) == str:
            models = importlib.import_module(models_module)
        else:
            models = models_module

        database.Base.metadata.create_all(bind=database.engine)
        _Session = sessionmaker(bind=database.engine)


    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        with db():
            response = await call_next(request)

        return response

class DBSessionMeta(type):
    @property
    def session(self):
        return self.get_sesion()

    def query(self, *entitles, **kwargs) -> Callable[..., Query]:
        return self.get_session().query(*entitles, **kwargs)

    def add(self, instance: DeclarativeMeta):
        session = self.get_session()
        session.add(instance)
        return session

    def commit(self):
        self.get_session().commit()

    def truncate_all(self):
        meta = database.Base.metadata
        session = self.get_session()
        for table in reversed(meta.sorted_tables):
            session.execute(table.delete())
        session.commit()

    def get_session(self) -> Session:
        if _Session is None:
            raise SessionInitializationError

        session = _SessionContext.get()

        if session is None:
            raise SessionInitializationError

        return session


class DBSession(metaclass=DBSessionMeta):
    def __init__(self, kwargs: Dict=None):
        self.token = None
        self.kwargs = kwargs or {}

    def __enter__(self):
        if not isinstance(_Session, sessionmaker):
            raise SessionInitializationError

        self.token = _SessionContext.set(_Session(**self.kwargs))
        return type(self)

    def __exit__(self, exc_type, exc_value, traceback):
        sess = _SessionContext.get()
        if exc_type is not None:
            sess.rollback()
        else:
            sess.commit()

        sess.close()
        _SessionContext.reset(self.token)

db: DBSession = DBSession
