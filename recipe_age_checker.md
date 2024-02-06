# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

``` python

#when user is over 16 , access is granted

```
As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

``` python

# when the user is under 16, access is denied and tell them their current and the required age (18)

```
As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.


As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.

``` python

# when there is an invalid entry, access is denied , stating invalid format, and format according to spec

```
## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def age_checker(date_of_birth):
    """
    parameter : string containing a date (e.g "2013-10-02")

    returns: 

        over 16:  string "access granted!" 
        under 16: string "access denied, your ages is XX , you need to be 16 for access"
        invalid entry: string "invalid format, please input date of birth in the following format: YYYY-MM-DD"

    pass # 
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a date of birth that is over 16 it will return access granted as a string
"""
age_checker("1987-09-15") => "Access granted!"

"""
Given a date of birth that is under 16 it will return access denited as a string
"""
age_checker("2008-11-08") => "Access denied! Your age is 15, you need to be 16 for access""

"""
Given an invalid input (wrong format date), it will return an exception stating "Invalid format, please input date of birth in the following format: YYYY-MM-DD"
"""
age_checker("16/03/2009") => exception with string "Invalid format, please input date of birth in the following format: YYYY-MM-DD"

"""
Given an invalid input (empty string), it will return an exception stating "Invalid format, please input date of birth in the following format: YYYY-MM-DD"
"""
age_checker("") => exception with string "Invalid format, please input date of birth in the following format: YYYY-MM-DD"

"""

"""

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

Refer to test_age_checker.py


