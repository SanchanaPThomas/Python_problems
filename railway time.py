def railway_time(s):
   
    period=s[-2:]#AM/PM
    hour,minute,second = map(int,s[:-2].split(':')) #splits the hour,min and sec

    if period=='AM':
        if hour==12:
            hour=0 #12AM to 00  
    else:  
        if hour!=12:
            hour+=12 #add 12 for PM except 12PM 

    return f"{hour:02d}:{minute:02d}:{second:02d}" #final time in the "HH:MM:SS" 24-hour format
#02d:
#0-pad with zeros if the number has fewer digits
#2-ensure the number is atleast 2 digits wide
#d-format as a decimal integer


s=input("enter time ")#input format-07:05:45PM
print(railway_time(s))  
