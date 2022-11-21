from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    engine = create_engine("postgresql://root:password@postgres:5432/assignment?sslmode=disable", pool_pre_ping=True, echo=True, future=True)
except Exception as e:
    print(e)
    exit(1)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)