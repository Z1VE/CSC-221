#------------------------------
# NAME : Matthew
# DATE : 9/8/26
# TERM : FALL 2026
# COURSE : CSC 221
# PROJECT : Fraction Class Lab
# FILENAME : fraction.py
#------------------------------

class Fraction:
    def __init__(self,numerator, denominator):
        if not isinstance(numerator,int) and isinstance(denominator,int):
            raise TypeError("Your numerator and or denominator are not integers")
        if denominator == 0:
            raise ZeroDivisionError

        self.__numerator = numerator
        self.__denominator = denominator
        self.__reduce()

    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        if self.__denominator < 0:
            if self.__denominator == -1:
                return f"{-self.__numerator}"
            return f"{-self.__numerator}/{self.__denominator}"
        return f'{self.__numerator}/{self.__denominator}'

    def get_numerator(self):
        """
        Returns numerator of fraction object
        :return: int numerator
        """
        return self.__numerator

    def get_denominator(self):
        """
        Returns denominator of fraction object
        :return: int denominator
        """
        return self.__denominator

    def set_denominator(self,value):
        """
        Sets denominator of the fraction object to given value
        :param value: int value to set denominator to
        :return: None
        """
        if not isinstance(value, int):
            raise TypeError("Your denominator is not an integer")
        if value == 0:
            raise ZeroDivisionError
        self.__denominator = value

    def set_numerator(self,value):
        """
        Sets numerator of the fraction object to given value
        :param value: int value to set numerator to
        :return: None
        """
        if not isinstance(value, int):
            raise TypeError("Your denominator is not an integer")

        self.__numerator = value


    def __reduce(self):
        """
        Reduce fraction object to its smallest form
        :return:
        """
        gcd = self.__calc_gcd()

        self.__numerator //= gcd
        self.__denominator //= gcd

    def __calc_gcd(self):

        a = max(abs(self.__numerator), abs(self.__denominator))
        b = min(abs(self.__numerator), abs(self.__denominator))

        while b != 0:
            temp = b
            b = a % b
            a = temp

        return a


    def __neg__(self):
        """
        Returns fraction object negated
        :return: Fraction object result of negation
        """
        return Fraction(-self.__numerator, self.__denominator)

    def __add__(self, other):
        """
        Adds fraction objects together
        :param other: second fraction on the right side of operator
        :return: Fraction object result sum of both fractions
        """
        if not isinstance(other, Fraction):
            raise TypeError("Right-side operand must be of type Fraction")
        numerator = elf.__numserator * other.get_denominator() + other.get_numerator() * self.__denominator
        denominator = self.__denominator * other.get_denominator()

        return Fraction(numerator,denominator)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        """
        Multiplies two fraction objects
        :param other: Fraction object on right side of operator
        :return: Fraction object result of the product of left and right side operands
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"Right-side operand must be of type Fraction")
        numerator = self.__numerator * other.get_numerator()
        denominator = self.__denominator * other.get_denominator()

        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError(f"Right-side operand must be of type Fraction")
        if other.get_denominator() == 0:
            raise ZeroDivisionError
        numerator = self.__numerator / other.get_numerator()
        denominator = self.__denominator / other.get_denominator()

    def __eq__(self, other):
