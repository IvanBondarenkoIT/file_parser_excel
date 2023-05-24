import re

VALIDATION_PATTERNS = {
    "First Name": r'[A-Za-z]+',
    "Last Name": r'[A-Za-z]+',
    "SSN": r'\d{3}-\d{2}-\d{4}',
    "Address": r'.+',
    "Company": r'.+',
    "Department": r'.+',
    "Position": r'.+',
    "Zip": r'\d{5}(-\d{4})?',
    "tel": r'\d?-?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
}


class DataInterpreter:
    def __init__(self):
        self.__result_dict = []
        self.__current_row = None
        self.__not_valid_data = []

    def add_data(self, data):
        self.__current_row = data
        self.__result_dict.append({
            "name": self.validate("First Name"),
            "address": self.validate("Address"),
            "user_fullname": f'{self.validate("First Name")} '
                             f'{self.validate("Last Name")}',
            "user_additional_info": f'{self.validate("SSN")}|'
                                    f'{self.validate("Company")}|'
                                    f'{self.validate("Department")}|'
                                    f'{self.validate("Position")}|',

            "zip": self.validate("Zip"),
            "tel": self.validate("Mobile number"),
            })

    def validate(self, kay):
        """Return valid values or empty string"""
        if re.match(pattern=r'[A-Za-z]+', string=str(self.__current_row.get(kay))):
            return self.__current_row.get(kay)
        else:
            self.__not_valid_data.append(self.__current_row.get(kay))
            return ""

    def get_final_values(self):
        return self.__result_dict

    def get_not_valid_data(self):
        return self.__not_valid_data
