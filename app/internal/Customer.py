from .Person import Person

class Customer(Person):
    def __init__(self, firstname, lastname, country, province, zip_code, birthday, phone_number, account):
        super().__init__(firstname, lastname, country, province, zip_code, birthday, phone_number, account)
        self.__credit_card = None
        self.__booking_list = []
    
    def get_credit_card(self):
        return self.__credit_card
    
    def get_booking_list(self):
        return self.__booking_list

    def add_credit_card(self, credit_card):
        # Validation
        self.__credit_card = credit_card

    def add_booking(self, booking):
        # validation
        self.__booking_list.append(booking)

    def get_personal_information(self):
        return {"firstname": self.__firstname,
                "lastname": self.__lastname,
                "email": self.__account.get_email(),
                "country": self.__country,
                "province": self.__province,
                "zip_code": self.__zip_code,
                "birthday": self.__birthday,
                "phone_number": self.__phone_number}
    
    def booking(self):
        pass

    def cancle_booking(self):
        pass
    