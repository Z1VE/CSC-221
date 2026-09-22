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

    def __str__(self):
        """
        returns the string value of our FootMeasure object
        :return:
        """
        pass

    def __convert(self):
        """
        converts all feet to inches to get 1 consistent unit
        :return:
        """
        self.__inches += 12*self.__feet

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

    def set_feet(self):
        """
        sets and sets the feet value of our FootMeasure object
        :return:
        """
        pass


    def set_inches(self):
        """
        sets and sets the inches value of our FootMeasure object
        :return:
        """
        pass
