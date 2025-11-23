import uvicorn
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal, create_db, Quote
from parser import get_quotes_from_web

# Импортируем настройки (Quote импортируем позже, когда напишем)
from database import SessionLocal, create_db, Quote
from parser import get_quotes_from_web

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Создаем таблицы (если они описаны)
create_db()

# Получение сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================================
# ПРАКТИКА №3: Роуты и Связывание
# ==========================================


@app.get("/")
def home(request: Request, db:Session = Depends(get_db)):
    all_quotes = db.query(Quote).all() # Взяли все записи из таблицы книги и передли их

    # Задача: Достать книги из БД и передать в шаблон
    return templates.TemplateResponse("index.html", {"request": request, "Qoute": all_quotes})

# Спарсить данные и подгрузить на страницу
@app.get("/parser")
def load_books(db:Session = Depends(get_db)):
    # Задача: Спарсить и сохранить в БД

    data = get_quotes_from_web()

    for quote in data:
        new_quote = Quote(
            title = quote["text"],
            author = quote["author"]
            )
        db.add(new_quote)

    db.commit()
    
    return RedirectResponse(url="/", status_code=303) # переадресация


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
