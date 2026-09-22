# --------------------------------
# Name : Matthew Rumph
# Date : 9/17/2026
# Purpose : Foot and inch converter class
# Term : FALL 2026
# Class : CSC 221
# Filename: foot_measure.py
# --------------------------------


class FootMeasure:
    def __init__(self, feet=0, inches=0):
        self.__feet = feet
        self.__inches = inches
        self.__convert()
        self.in_inches = self.in_inches()

    def __str__(self):
        """
        returns the string value of our FootMeasure object
        :return: string value of our FootMeasure object
        """
        if self.__inches == 0 and self.__feet > 0:
            return f"{self.__feet} ft."
        elif self.__inches == 0 and self.__feet == 0:
            return f"{self.__feet} ft. {self.__inches} in."
        elif self.__feet == 0 and self.__inches > 0:
            return f"{self.__inches} in."
        else:
            return f"{self.__feet} ft. {self.__inches} in."

    def __convert(self):
        """
        converts all feet to inches to get 1 consistent unit and then converts all inches to feet and inches for consistency.
        :return:
        """
        self.__inches += 12*self.__feet
        self.__feet = 0

        self.__feet = self.__inches // 12
        self.__inches = self.__inches % 12

    def in_inches(self):
        """
        returns the total inches value of our FootMeasure object
        :return: int feet in inches + inches
        """
        result = self.__inches + self.__feet*12
        return result

    def get_feet(self):
        """
        gets and returns the feet value of our FootMeasure object
        :return: int feet
        """
        return self.__feet

    def get_inches(self):
        """
        gets and returns the inches value of our FootMeasure object
        :return: int inches
        """
        return self.__inches

    def set_feet(self, value):
        """
        sets the feet value of our FootMeasure object to a given value
        :return:
        """
        self.__feet = value

    def set_inches(self, value):
        """
        sets the inches value of our FootMeasure object to a given value
        :return:
        """
        self.__inches = value


    def __add__(self, other):
        """
        adds two FootMeasure objects
        :param other: right-side operand
        :return: sum of two FootMeasure objects
        """
        a = self.in_inches
        b = other.in_inches

        return FootMeasure(inches=a+b)

    def __eq__(self, other):
        """
        compares two FootMeasure objects and if they're equal
        :param other: right-side operand
        :return: boolean comparison of two FootMeasure objects
        """
        return self.in_inches == other.in_inches

    def __ne__(self, other):
        """
        compares two FootMeasure objects and if they're not equal
        :param other: right-side operand
        :return: bool comparison of two FootMeasure objects
        """
        return self.in_inches != other.in_inches

    def __gt__(self, other):
        """
        compares two FootMeasure objects and if the first is greater than the second
        :param other: right-side operand
        :return: bool comparison of two FootMeasure objects
        """
        return self.in_inches > other.in_inches

    def __lt__(self, other):
        """
        compares two FootMeasure objects and if the first is less than the second
        :param other: right-side operand
        :return: bool comparison of two FootMeasure objects
        """
        return self.in_inches < other.in_inches

    def __ge__(self, other):
        """
        compares two FootMeasure objects and if the first is greater than or equal to the second
        :param other: right-side operand
        :return: bool comparison of two FootMeasure objects
        """
        return self.in_inches >= other.in_inches

    def __le__(self, other):
        """
        compares two FootMeasure objects and if the first is less than or equal to the second
        :param other: right-side operand
        :return: bool comparison of two FootMeasure objects
        """
        return self.in_inches <= other.in_inches

