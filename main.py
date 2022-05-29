from fastapi import Depends, FastAPI
from routers import get_weather, post_opendart, post_미분양_시군구별, get_opendart, get_미분양_시군구별
import schemas, models
from sqlalchemy.orm import Session
from database import engine, SessionLocal

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


app.include_router(get_weather.router)
app.include_router(post_미분양_시군구별.router)
app.include_router(get_미분양_시군구별.router)
app.include_router(post_opendart.router)
app.include_router(get_opendart.router)


# @app.post('/unsold', tags=["POST"])
# def create(request: schemas.Unsold, db: Session = Depends(get_db)):
#     new_record = models.Unsold(region=request.region, clf=request.clf,
#                                unsold_num=request.unsold_num, date=request.date)
#     db.add(new_record)
#     db.commit()
#     db.refresh(new_record)
#     return new_record
