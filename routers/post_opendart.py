from fastapi import APIRouter, Depends
from typing import Optional
from config import get_secret
from fastapi.encoders import jsonable_encoder
import requests
import schemas
import models
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import pandas as pd


models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/재무재표/{code}/{year}/{report}/{type}", tags=["OPENDART"], summary="기업별재무재표 조회 및 DB 다운로드")
def create(code: str, year: str, report: str, type: str, request: schemas.Statement, db: Session = Depends(get_db)):
    '''
    ## 대표적인 조회조건 예시
    - **주요 기업 고유번호(code)** : 현대중공업지주 "01205709" 한국조선해양 "00164830" 삼성전자 "00126380" 현대두산인프라코어 "00344287" 현대건설기계 "01205842" 현대제뉴인 "01535840"
    - **year** : "2021"
    - **report** : "11013": "1분기보고서", "11012": "반기보고서","11014": "3분기보고서", "11011": "사업보고서"
    - **type** : "CFS": "연결재무제표", "OFS":"재무제표"
    - 조회데이터는 DB에 저장됨

    '''

    OPEN_DART_API = get_secret("OPEN_DART_API")
    BASE_URL = "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json"
    Full_URL = BASE_URL + \
        f"?crtfc_key={OPEN_DART_API}&corp_code={code}&bsns_year={year}&reprt_code={report}&fs_div={type}"
    resp = requests.get(Full_URL)
    dict = resp.json()["list"]

    for row in dict:
        print(row)
        new_record = models.StateModel(**row)
        db.add(new_record)
    db.commit()
    return
