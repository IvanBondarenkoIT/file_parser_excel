import re

VALIDATION_PATTERNS = {
    "First Name": r'[A-Za-z]+',
    "Last Name": r'[A-Za-z]+',
    "SSN": r'\d{3}-?\d{2}-?\d{4}',
    "Address": r'.+',
    "Company": r'.+',
    "Department": r'.+',
    "Position": r'.+',
    "Zip": r'\d{2,5}-?(\d{4})?',
    "Mobile number": r'\d?-?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
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
            "user_additional_info": self.build_user_additional_info("SSN", "Company", "Department","Position"),
            "zip": self.validate("Zip"),
            "tel": self.validate("Mobile number"),
            })

    def validate(self, kay):
        """Return valid values or empty string"""
        if re.match(pattern=VALIDATION_PATTERNS.get(kay), string=str(self.__current_row.get(kay))):
            return self.__current_row.get(kay)
        else:
            self.__not_valid_data.append(f"{self.__current_row.get(kay)}")
            return ""

    def build_user_additional_info(self, *args):
        result = []
        for arg in args:
            validate_data = self.validate(arg)
            if validate_data:
                result.append(validate_data)
        return "|".join(result)

    @property
    def get_final_values(self):
        return self.__result_dict

    @property
    def get_not_valid_data(self):
        return self.__not_valid_data
