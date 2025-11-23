from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Настройки БД
DATABASE_URL = "sqlite:///./quotes.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


# ==========================================
# ПРАКТИКА №1: Создание таблицы
# Мы будем писать модель Book прямо здесь
# ==========================================

# class Quote(Base):
# ... код напишем вместе ...




class Quote(Base):
    __tablename__ = "quotes"


    id = Column(Integer, primary_key=True)
    text = Column(String)
    author = Column(String)

def create_db():
    Base.metadata.create_all(bind=engine)
