
from sqlalchemy.engine import create_engine

from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///:memory:')
ENGINE = create_engine("mysql://root:MyNewPass@localhost/local_test")
          # convert_unicode=False,
          # isolation_level="READ UNCOMMITTED")

session = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=ENGINE))

def init_db():
    from src.models.user import Base
    Base.metadata.create_all(ENGINE)
