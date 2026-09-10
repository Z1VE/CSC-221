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
        if not isinstance(numerator,int) or not isinstance(denominator,int):
            raise TypeError("Your numerator and or denominator are not integers")
        if denominator == 0:
            raise ZeroDivisionError

        self.__numerator = numerator
        self.__denominator = denominator
        self.__reduce()

    def __str__(self):
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
        self.__reduce()

    def set_numerator(self,value):
        """
        Sets numerator of the fraction object to given value
        :param value: int value to set numerator to
        :return: None
        """
        if not isinstance(value, int):
            raise TypeError("Your numerator is not an integer")

        self.__numerator = value
        self.__reduce()


    def __reduce(self):
        """
        Reduce fraction object to its smallest form
        :return:
        """
        gcd = self.__calc_gcd()

        self.__numerator //= gcd
        self.__denominator //= gcd

        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

    def __calc_gcd(self):
        """
        calculates greatest common divisor
        :return: greatest common divisor
        """
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
        numerator = self.__numerator * other.get_denominator() + other.get_numerator() * self.__denominator
        denominator = self.__denominator * other.get_denominator()

        return Fraction(numerator,denominator)

    def __sub__(self, other):
        """
        subtracts one fraction object from another
        :param other: second fraction on the right side of operator
        :return: Fraction object result of difference of both fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Right-side operand must be of type Fraction")
        return self + (-other)

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
        """
        Divides 2 fractions by one another
        :param other: right side operand
        :return: quotient
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"Right-side operand must be of type Fraction")
        if other.get_denominator() == 0:
            raise ZeroDivisionError

        numerator = self.__numerator * other.get_denominator()
        denominator = self.__denominator * other.get_numerator()

        return Fraction(numerator,denominator)

    def __eq__(self, other):
        """
        Checks if left and right side fraction objects are equal
        :param other: right side fraction object
        :return: boolean
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"Right-side operand must be of type Fraction")

        return self.get_numerator() * other.get_denominator() == other.get_numerator() * self.get_denominator()

    def __ne__(self, other):
        """
        Checks if left and right side fraction objects are not equal
        :param other: right side fraction object
        :return: boolean
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"Right-side operand must be of type Fraction")

        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Checks if left side fraction object is less than right-side
        :param other: right side fraction object
        :return: boolean
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"Right-side operand must be of type Fraction")

        a = self.get_numerator() * other.get_denominator()
        b = other.get_numerator() * self.get_denominator()

        if a < b:
            return True
        else:
            return False

    def __le__(self,other):
        """
        Checks if left side fraction object is less than or equal to the right side fraction object
        :param other: right side fraction object
        :return: boolean
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"Right-side operand must be of type Fraction")

        if self.__lt__(other) or self.__eq__(other):
            return True

        else:
            return False


    def __gt__(self, other):
        """
        Checks if left side fraction object is greater than the right side fraction object
        :param other: right side fraction object
        :return: boolean
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"Right-side operand must be of type Fraction")

        return not self.__le__(other)

    def __ge__(self, other):
        """
        Checks if left side fraction object is greater than or equal to the right side fraction object
        :param other: right side fraction object
        :return:
        """
        if not isinstance(other, Fraction):
            raise TypeError(f"Right-side operand must be of type Fraction")
        return not self.__lt__(other)