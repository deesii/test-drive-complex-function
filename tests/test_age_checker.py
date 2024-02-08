from lib.age_checker import *
import pytest


#Given a date of birth that is over 16 it will return access granted as a string

def test_over_sixteen():
    result = age_checker("1987-09-15") 
    assert result == "Access granted!"

#Given a date of birth that is under 16 it will return access denited as a string

def test_under_sixteen():
    result = age_checker("2008-11-08") 
    assert result == "Access denied! Your age is 15, you need to be 16 for access"


#Given an invalid input (wrong format date), it will return an exception stating "Invalid format, please input date of birth in the following format: YYYY-MM-DD"

def test_wrong_format_date():

    with pytest.raises(ValueError) as e:
        age_checker("16/03/2009")
    error_message = str(e.value)
    assert error_message == "Invalid format, please input date of birth in the following format: YYYY-MM-DD"
    
# def test_wrong_format_date():
#     assert age_checker("16/03/2009") == ""