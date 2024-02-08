from datetime import datetime

def age_checker(date_of_birth):
    
    try:
        converted_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
        date_today = datetime.now()
        difference = date_today - converted_date
        total_days = difference.days
        age = int(total_days // 365.25)

        if age < 16:
            return f"Access denied! Your age is {age}, you need to be 16 for access"
        else:
            return "Access granted!"
        
    except ValueError:
        raise ValueError("Invalid format, please input date of birth in the following format: YYYY-MM-DD")

    
# the following code is for when we use the function datetime.strptime to capture the exception for incorrect format

    # converted_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
    # date_today = datetime.now()
    # difference = date_today - converted_date
    # total_days = difference.days
    # age = int(total_days // 365.25)

    # if age < 16:
    #     return f"Access denied! Your age is {age}, you need to be 16 for access"
    # else:
    #     return "Access granted!"
        




#print(age_checker("1987/09/15"))