from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from . import models


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# TODO: make selection using environment vars

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# temporary, for testing
def initBase(db: Session):
    engine = db.get_bind()
    try:
        models.SampleModel.__table__.drop(engine)
    except:
        pass
    models.SampleModel.__table__.create(engine)
    db_sample = [models.SampleModel(
        id = 0,
        name = "A card",
        remark = None
    )]
    db.add_all(db_sample)
    db.commit()
    db.close()



def get_sample(db: Session, id: int) -> Optional[models.Sample]:
    sample = db.query(models.SampleModel).filter(models.SampleModel.id == id).first()
    if sample:
        return models.Sample(**sample.__dict__)
    return None
