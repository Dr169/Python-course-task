# get the year between '1900' and '3000'
while True:
    current_year = int(input('Enter Year: '))

    if current_year > 3000 or current_year < 1900 :      
        print("You should give a number between '1900' and '3000'")
        continue
    if current_year <= 3000 and current_year >= 1900 :
        print("Your current year is {}".format(current_year))
        break

if current_year % 4 == 0 :
    # List of tuples for Months and date ranges in leap year
    calendar = [('1','january', 31),('2','feburary', 29),('3','march', 31),
                ('4','april', 30),('5','may', 31),('6','june', 30),
                ('7','july', 31),('8','august', 31),('9','september', 30),
                ('10','october', 31),('11','november', 30),('12','december', 31)]
    leap_year = True
    print("You are in a leap year")

else:
    # List of tuples for Months and date ranges in normal year
    calendar = [('1','january', 31),('2','feburary', 28),('3','march', 31),
                ('4','april', 30),('5','may', 31),('6','june', 30),
                ('7','july', 31),('8','august', 31),('9','september', 30),
                ('10','october', 31),('11','november', 30),('12','december', 31)]
    leap_year = False

# get the month between '1' and '12'
while True:
    current_month_number = input('Enter month: ')

    if int(current_month_number) > 12 or int(current_month_number) < 1 :      
        print("You should give a number between '1' and '12'")
        continue
    else:
        for i in range(12):
            if current_month_number == calendar[i][0] :
                current_month_name = calendar[i][1]
                print("Your current month is {}".format(calendar[i][1]))
    break

# get the day for each month
while True:
    current_day = input('Enter day: ')

    for i in range(12):
        if current_month_number == calendar[i][0] :
            if int(current_day) < 1 or int(current_day) > calendar[i][2]:
                print("You should give a number between '1' and '{}'".format(calendar[i][2]))
        continue
            
    if int(current_day) > 1 and int(current_day) < calendar[i][2]:
        print("Your current day is {}".format(current_day))
        break

week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

past_days = 0
for i in range(12):
    if current_month_number != calendar[i][0]:
        past_days +=  calendar[i][2]

    else:
        past_days += int(current_day)
        break

current_day_index = past_days % 7
current_day_name = week[current_day_index]

print("-------------<current date>-------------")
print("{}/{}/{}".format(current_year,current_month_number,current_day))
print("{}-{}-{}".format(current_day,current_month_name,current_year))
print("{}-{}-{}-{}".format(current_day_name,current_day,current_month_name,current_year))

def sum_calendar(number_of_sum):
    future_days = past_days + number_of_sum

    try:
        new_day_name = week[current_day_index + (future_days % 7)]

    except:
        new_day_name = week[current_day_index + (future_days % 7) - 7]

    new_year = current_year
    while future_days > 365:
        if  new_year % 4 == 0:
            future_days -= 366
            new_year += 1

        elif new_year % 4 != 0:
            future_days -= 365
            new_year += 1

    new_month_number = 1
    for i in range(12):
        if new_year % 4 == 0:
            calendar = [('1','january', 31),('2','feburary', 29),('3','march', 31),
                ('4','april', 30),('5','may', 31),('6','june', 30),
                ('7','july', 31),('8','august', 31),('9','september', 30),
                ('10','october', 31),('11','november', 30),('12','december', 31)]
            if future_days > calendar[i][2]:
                future_days -= calendar[i][2]
                new_month_number +=1

        if new_year % 4 != 0:
            calendar = [('1','january', 31),('2','feburary', 28),('3','march', 31),
                ('4','april', 30),('5','may', 31),('6','june', 30),
                ('7','july', 31),('8','august', 31),('9','september', 30),
                ('10','october', 31),('11','november', 30),('12','december', 31)]
            if future_days > calendar[i][2]:
                future_days -= calendar[i][2]
                new_month_number +=1

    new_month_name = ""
    for i in range(12):
        if str(new_month_number) == calendar[i][0]:
            new_month_name += calendar[i][1]

    print("-------------<future date>-------------")
    print("{}/{}/{}".format(new_year,new_month_number,future_days))
    print("{}-{}-{}".format(future_days,new_month_name,new_year))
    print("{}-{}-{}-{}".format(new_day_name,future_days,new_month_name,new_year))


sum_calendar(10)