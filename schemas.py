from pydantic import BaseModel


class Unsold(BaseModel):
    시군구: str
    구분: str
    미분양현황: int
    date: str

class Statement(BaseModel):
    rcept_no: str
    reprt_code: str
    bsns_year: str
    corp_code: str
    sj_div: str
    sj_nm: str
    account_id: str
    account_nm: str
    account_detail: str
    thstrm_nm: str
    thstrm_amount: str
    thstrm_add_amount: str
    frmtrm_q_nm: str
    frmtrm_q_amount: str
    frmtrm_nm: str
    frmtrm_amount: str
    frmtrm_add_amount: str
    bfefrmtrm_nm: str
    bfefrmtrm_amount: str
    ord: str
    currency: str





