from fastapi import APIRouter
from ..instance.company import company
from ..model.hotel import HotelModel, IntervalModel
from datetime import date as Date

router = APIRouter(prefix="/reservation", tags=["reservation"], responses={404: {"description": "Not Found"}})

@router.get('/rateListMenu')
async def view_rate(data: dict) -> dict:  #hotel_name:str, checkin:str, checkout:str, amount:int
    return company.view_rate_from_hotel(data['hotel_name'], [data['checkin'], data['checkout']], data['amount'])    #change to classroom ex.

@router.get('/reviewDetails')       #if logged in, it will show pay method, else show 'continue' and login first then go guestInfo
async def select(hotel_name:str, checkin:str, checkout:str, amount:int, room_type:str):
    return company.select_room(hotel_name, [checkin, checkout], amount, room_type)

@router.get('/guestInfo')
async def book():
    pass
    