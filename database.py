from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Настройки БД
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


# ==========================================
# ПРАКТИКА №1: Создание таблицы
# Мы будем писать модель Book прямо здесь
# ==========================================

# class Book(Base):
# ... код напишем вместе ...




class Book(Base):
    __tablename__ = "books"


    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(String)

def create_db():
    Base.metadata.create_all(bind=engine)
