from fastapi import APIRouter, Depends
from config import get_secret
from fastapi.encoders import jsonable_encoder
import requests
import schemas
import models
from sqlalchemy.orm import Session
from database import engine, SessionLocal


router = APIRouter()

국토교통_API = get_secret("HOUSE_API")
BASE_URL = " http://stat.molit.go.kr/portal/openapi/service/rest/"


@router.get("/미분양/{yearmonth}", tags=["국토교통"])
async def get_unsold(yearmonth: str):
    '''
    시군구별 미분양현황
    - 2010년 12월 ~ 2022년 3월   (yearmonth 형식 : YYYYMM)
    - 2006년까지는 12월 데이터만 있음 (세부 시군 레벨 데이터는 없음)

    '''
    targetURL = BASE_URL+"getList.do?key="+국토교통_API + \
        "&form_id=2082&style_num=128&start_dt="+yearmonth+"&end_dt="+yearmonth
    response = requests.get(targetURL)
    response = response.json()["result_data"]["formList"]
    return response

    # data1 = response["result_data"]["formList"]

    # 시군구리스트 =[]
    # 미분양리스트 = []
    # 연월리스트 =[]

    # for i in data1:
    #     print(i)
    #     시군구 = i["시군구"]

    #     if "미분양현황" in i.keys():
    #         미분양건수 = i["미분양현황"]
    #     else:
    #         미분양건수 = 0
    #     연월 = i["date"]
    #     시군구리스트.append(시군구)
    #     미분양리스트.append(미분양건수)
    #     연월리스트.append(연월)

    # result = []
    # result.append(["regionname", 시군구리스트])
    # result.append(["unsold", 미분양리스트])
    # result.append(["date", 연월리스트])
    # return jsonable_encoder(result)
