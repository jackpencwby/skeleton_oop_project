from ..internal.Hotel import Hotel
from ..internal.Room import Room
from ..internal.Location import Location
from ..internal.Opinion import Opinion
from ..internal.Interval import Interval
from datetime import date

location1 = Location(country="Thailand", province="Bangkok")
location2 = Location(country="England", province="London")
location3 = Location(country="United States", province="Warshington D.C")

room1_hotel1 = Room(room_no="1", type="small", price=1000)
room2_hotel1 = Room(room_no="2", type="small", price=1000)
room3_hotel1 = Room(room_no="3", type="small", price=1000)
room4_hotel1 = Room(room_no="4", type="medium", price=1500)
room5_hotel1 = Room(room_no="5", type="medium", price=1500)
room6_hotel1 = Room(room_no="6", type="large", price=2000)

room1_hotel2 = Room(room_no="1", type="small", price=2000)
room2_hotel2 = Room(room_no="2", type="small", price=2000)
room3_hotel2 = Room(room_no="3", type="small", price=2000)
room4_hotel2 = Room(room_no="4", type="medium", price=3000)
room5_hotel2 = Room(room_no="5", type="medium", price=3000)
room6_hotel2 = Room(room_no="6", type="large", price=4000)

room1_hotel3 = Room(room_no="1", type="small", price=3000)
room2_hotel3 = Room(room_no="2", type="small", price=3000)
room3_hotel3 = Room(room_no="3", type="small", price=3000)
room4_hotel3 = Room(room_no="4", type="medium", price=4500)
room5_hotel3 = Room(room_no="5", type="medium", price=4500)
room6_hotel3 = Room(room_no="6", type="large", price=6000)

room1_hotel4 = Room(room_no="1", type="small", price=4000)
room2_hotel4 = Room(room_no="2", type="small", price=4000)
room3_hotel4 = Room(room_no="3", type="small", price=4000)
room4_hotel4 = Room(room_no="4", type="medium", price=6000)
room5_hotel4 = Room(room_no="5", type="medium", price=6000)
room6_hotel4 = Room(room_no="6", type="large", price=8000)

room1_hotel5 = Room(room_no="1", type="small", price=5000)
room2_hotel5 = Room(room_no="2", type="small", price=5000)
room3_hotel5 = Room(room_no="3", type="small", price=5000)
room4_hotel5 = Room(room_no="4", type="medium", price=7500)
room5_hotel5 = Room(room_no="5", type="medium", price=7500)
room6_hotel5 = Room(room_no="6", type="large", price=10000)

room1_hotel6 = Room(room_no="1", type="small", price=5000)
room2_hotel6 = Room(room_no="2", type="small", price=5000)
room3_hotel6 = Room(room_no="3", type="small", price=5000)
room4_hotel6 = Room(room_no="4", type="medium", price=8000)
room5_hotel6 = Room(room_no="5", type="medium", price=8000)
room6_hotel6 = Room(room_no="6", type="large", price=12000)

hotel1 = Hotel(name="hotel1", location=location1, hotel_email="hotel1@gmail.com")
hotel2 = Hotel(name="hotel2", location=location1, hotel_email="hotel2@gmail.com")
hotel3 = Hotel(name="hotel3", location=location2, hotel_email="hotel3@gmail.com")
hotel4 = Hotel(name="hotel4", location=location2, hotel_email="hotel4@gmail.com")
hotel5 = Hotel(name="hotel5", location=location3, hotel_email="hotel5@gmail.com")
hotel6 = Hotel(name="hotel6", location=location3, hotel_email="hotel6@gmail.com")

hotel1.add_room(room1_hotel1)
hotel1.add_room(room2_hotel1)
hotel1.add_room(room3_hotel1)
hotel1.add_room(room4_hotel1)
hotel1.add_room(room5_hotel1)
hotel1.add_room(room6_hotel1)

hotel2.add_room(room1_hotel2)
hotel2.add_room(room2_hotel2)
hotel2.add_room(room3_hotel2)
hotel2.add_room(room4_hotel2)
hotel2.add_room(room5_hotel2)
hotel2.add_room(room6_hotel2)

hotel3.add_room(room1_hotel3)
hotel3.add_room(room2_hotel3)
hotel3.add_room(room3_hotel3)
hotel3.add_room(room4_hotel3)
hotel3.add_room(room5_hotel3)
hotel3.add_room(room6_hotel3)

hotel4.add_room(room1_hotel4)
hotel4.add_room(room2_hotel4)
hotel4.add_room(room3_hotel4)
hotel4.add_room(room4_hotel4)
hotel4.add_room(room5_hotel4)
hotel4.add_room(room6_hotel4)

hotel5.add_room(room1_hotel5)
hotel5.add_room(room2_hotel5)
hotel5.add_room(room3_hotel5)
hotel5.add_room(room4_hotel5)
hotel5.add_room(room5_hotel5)
hotel5.add_room(room6_hotel5)

hotel6.add_room(room1_hotel6)
hotel6.add_room(room2_hotel6)
hotel6.add_room(room3_hotel6)
hotel6.add_room(room4_hotel6)
hotel6.add_room(room5_hotel6)
hotel6.add_room(room6_hotel6)

# room1_hotel1.add_reserved_interval(Interval(date(2024,4,1), date(2024,4,3)))
# room2_hotel1.add_reserved_interval(Interval(date(2024,4,1), date(2024,4,3)))
# room3_hotel1.add_reserved_interval(Interval(date(2024,4,1), date(2024,4,3)))