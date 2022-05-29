from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class UnsoldModel(Base):
    __tablename__ = "unsold_house"

    id = Column(Integer, primary_key=True, index=True)
    시군구 = Column(String, index=True)
    구분 = Column(String, index=True)
    미분양현황 = Column(Integer, index=True)
    date = Column(String, index=True)


class StateModel(Base):
    __tablename__ = "statement"

    id = Column(Integer, primary_key=True, index=True)
    rcept_no = Column(String, index=True)
    reprt_code = Column(String, index=True)
    bsns_year = Column(String, index=True)
    corp_code = Column(String, index=True)
    sj_div = Column(String, index=True)
    sj_nm = Column(String, index=True)
    account_id = Column(String, index=True)
    account_nm = Column(String, index=True)
    account_detail = Column(String, index=True)
    thstrm_nm = Column(String, index=True)
    thstrm_amount = Column(String, index=True)
    thstrm_add_amount = Column(String, index=True)
    frmtrm_q_nm = Column(String, index=True)
    frmtrm_q_amount = Column(String, index=True)
    frmtrm_nm = Column(String, index=True)
    frmtrm_amount = Column(String, index=True)
    frmtrm_add_amount = Column(String, index=True)
    bfefrmtrm_nm = Column(String, index=True)
    bfefrmtrm_amount = Column(String, index=True)
    ord = Column(String, index=True)
    currency = Column(String, index=True)
