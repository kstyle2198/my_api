from fastapi import APIRouter, Depends
from config import get_secret
from fastapi.encoders import jsonable_encoder
import requests
import schemas
import models
from sqlalchemy.orm import Session
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


국토교통_API = get_secret("HOUSE_API")
BASE_URL = " http://stat.molit.go.kr/portal/openapi/service/rest/"


@router.post("/미분양/{yearmonth}", tags=["국토교통"])
def create(yearmonth: str, request: schemas.Unsold, db: Session = Depends(get_db)):
    '''
    시군구별 미분양현황
    - 2010년 12월 ~ 2022년 3월  (yearmonth 형식 : YYYYMM)
    - 2006년까지는 12월 데이터만 있음 (세부 시군 레벨 데이터는 없음)

    '''

    targetURL = BASE_URL+"getList.do?key="+국토교통_API + \
        "&form_id=2082&style_num=128&start_dt="+yearmonth+"&end_dt="+yearmonth
    response = requests.get(targetURL)
    response = response.json()['result_data']['formList']

    for row in response:
        print(row)
        new_record = models.UnsoldModel(**row)
        db.add(new_record)
    db.commit()
    return
