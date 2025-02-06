import datetime

def passed_time(year: int, month: int, day: int) -> str:
    """ """
    b_year = year # Birth year
    b_month = month # Birth month
    b_day = day # Birth day
    b_date = datetime.date(year, month, day) # Birth date
    today = datetime.date.today() # Today

    if (today-b_date).days <= 365: # For baby under 1 year
        return f"Siz tug'ilganigizga {(today-b_date).days} bo'ldi."
    
    elif today.month > b_month:
        year = today.year - b_year
        day = today-datetime.date(today.year, b_month, b_day)
        return f"Siz tug'ilganigizga {(today-b_date).days} bo'ldi."
    
    elif today.month == b_month:
        if today.day < b_day:
            year = today.year - b_year-1
            day = today-datetime.date(today.year-1, b_month, b_day)
            return f"Siz tug'ilganingizga {year}-yilu, {day.days} kun bo'ldi"
        
        elif today.day == b_day:
            year = today.year - b_year
            return f"Siz bugun {year} yoshga to'ldingiz. Tabriklaymiz!"
        
        else:
            year = today.year - b_year-1
            day = today-datetime.date(today.year-1, b_month, b_day)
            return f"Siz tug'ilganingizga {year}-yilu, {day.days} kun bo'ldi"
            


    else:
        year = today.year - b_year-1
        day = today-datetime.date(today.year-1, b_month, b_day)
        return f"Siz tug'ilganingizga {year}-yilu, {day.days} kun bo'ldi"
        


q_year = int(input("Tug'ilgan kiriting: "))
q_month = int(input("Tug'ilgan oyingizni kiriting: "))
q_day = int(input("Tug'ilgan kuningizni kiriting: "))

user = passed_time(q_year, q_month, q_day)
print(user)