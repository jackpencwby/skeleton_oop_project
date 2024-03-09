from .Room import Room
from .Opinion import Opinion
from fastapi import HTTPException, status

class Hotel:
    def __init__(self, name, location, hotel_email, balance=0):
        self.__name = name
        self.__location = location
        self.__hotel_email = hotel_email
        self.__balance = balance
        self.__status = None
        self.__room_list = []
        self.__opinion_list = []

    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location

    def get_hotel_email(self):
        return self.__hotel_email
    
    def get_balance(self):
        return self.__balance
    
    def get_status(self):
        return self.__status
    
    def change_status(self, status):
        # Validation
        self.__status = status

    def get_room_list(self):
        return self.__room_list
    
    def get_opinion(self):
        return self.__opinion_list
    
    def add_room(self, room):
        # Validation
        self.__room_list.append(room)

    def add_opinion(self, opinion):
        if isinstance(opinion, Opinion):
            self.__opinion_list.append(opinion)
            return 'done'
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
                            detail = {"message": "Invalid opinion"})
                
    def set_balance(self,balance):
        if isinstance(balance,int):
            self.__balance = balance
            return  "Hotel balance setting success"
        return  "Hotel balance setting error"
        
    def get_available_room(self, interval, amount):     #Fluk
        if not isinstance(amount, int) or amount > 3 or amount < 1:
            raise Exception('Invalid amount of room')
        all_available_room = []
        type_amount = {'small':0, 'medium':0, 'large':0}
        for room in self.__room_list:
            if room.is_available_at(interval):
                type_amount[room.get_type()] += 1
                all_available_room.append(room)
        available_room = []
        for type, a in type_amount.items():
            if a >= amount:      
                for room in all_available_room:
                    if room.get_type() == type:
                        available_room.append(room) 
                        break
        return available_room
    
    def select_room(self, interval, amount, room_type):     #fluk
        room_list = []
        if room_type not in ['small', 'medium', 'large']:
            raise Exception('Invalid Room Type!')
        for room in self.__room_list:
            if room.get_type() == room_type and room.is_available_at(interval):
                amount -= 1
                room_list.append(room)
            if amount == 0:
                break
        if amount == 0:
            [room.add_pending_interval(interval) for room in room_list]
            return 'done'
        raise Exception(f'Rooms are not enought!?!')

    def get_room_by_type(self, type):
        for room in self.__room_list:
            if room.get_type() == type:
                return room
        raise Exception('Error to get room!')


                


    
    