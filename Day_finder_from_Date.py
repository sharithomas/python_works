# code for checking leap year
def is_leap_yr(year): 
    flag =False
    if (year%4==0 and year%100!=0) or year%400==0:
      flag=True
    return flag

#method to get number of days considering the whole years
def get_year_days(year):
    diff_year = year - year_ref
    days_total=0
    #if year is negative consider next year to ref year. eg if year = 2018 Dec 1 consider year 2019 only
    if diff_year < 0 :
        year_gap_flag =-1
        for yr in range (year+1 , year_ref) : 
            if is_leap_yr(yr) is True:
                days_total = days_total +366
            else:
                 days_total = days_total + 365     
    #if year is positive consider years till ref year(except ref yr). eg if year = 2022 Dec 1 consider year 2020 , 2021        
    else:
        year_gap_flag =1
        for yr in range (year_ref , year) :
            if is_leap_yr(yr) is True:
                days_total = days_total + 366
            else:
                days_total = days_total + 365     
    return year_gap_flag ,days_total 
    
def get_month_days(month , year ,year_gap_flag):
    days_total=0
    if year_gap_flag == 1 :
        for mnth in range (1 , month) :#considers  one month less that the input month
            days_total = days_total + month_day_dict[mnth]            
        if month >= 3 and is_leap_yr(year) is True:
                days_total = days_total+1
    if year_gap_flag == -1 :
        for mnth in range ( month+1, 13) : #considers days months from given month to dec
            days_total = days_total + month_day_dict[mnth] 
        if month == 1:#for Jan check if Feb has 29 days (leap year)
            if is_leap_yr(year) is True:
                days_total = days_total+1   
    return days_total

def get_remaining_days(day ,month , year ,year_gap_flag):
    days_total=0
    if year_gap_flag == 1 :
        days_total = day -1       
    if year_gap_flag == -1 :  
        leap_day =0#for extra day in case Feb month has 29 days
        if month == 2 and is_leap_yr(year) is True :
            leap_day = 1 
        days_total = month_day_dict[month] + leap_day - day +1 
    return days_total

def day_calculator(days_count,year_gap_flag):
    rem_days = days_count%7
    if year_gap_flag>0:
        day_string = rem_day_dictionary_positive[rem_days]
    else:
        day_string = rem_day_dictionary_negative[rem_days]
    return day_string
    
    
#set reference year - month - day as 01-01-2020 which is a Wednesday
year_ref=2020
month_ref=1
day_ref=1

#month day count dictionary
month_day_dict = {1 : 31, 2 : 28 , 3 : 31 , 4 : 30 , 5 : 31 , 6 : 30 , 7 : 31 , 8 : 31 , 9 : 30 , 10 : 31 , 11 : 30 , 12 : 31} 
#remaining day dictionary wrt referenc date 01-01-2020 Wednesday
rem_day_dictionary_positive = {0:'Wednesday' , 1:'Thursday' , 2:'Friday' , 3:'Saturday' , 4:'Sunday' , 5:'Monday' , 6:'Tuesday' , }
rem_day_dictionary_negative = {0:'Wednesday' , 6:'Thursday' , 5:'Friday' , 4:'Saturday' , 3:'Sunday' , 2:'Monday' , 1:'Tuesday' , }

year =int(input(" enter year"))
month=int(input("month"))
day=int(input("date"))

year_gap_flag ,year_days  = get_year_days(year)
year_month_days = year_days + get_month_days(month , year ,year_gap_flag)
total_days = year_month_days+get_remaining_days(day ,month , year ,year_gap_flag)
day = day_calculator(total_days,year_gap_flag)
print ("Final Result...Total days =" ,total_days, '\nDay is ' ,day)