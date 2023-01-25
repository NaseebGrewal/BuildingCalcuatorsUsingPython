def add_time(start, duration, day = ""):

  answer = ""
  name_of_days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
  
  cur_h, y = start.split(':')
  cur_m , am_pm = y.split()

  cur_h = int(cur_h)
  cur_m = int(cur_m)
  am_pm = am_pm.upper()
  # if am_pm == ''

  hour, min = duration.split(':')
  min = int(min)
  days = int(hour) // 24
  hours = int(hour) % 24


  # starting with minutes
  # value of current minutes
  if cur_m + min > 60:
    hours += 1
    cur_m += min - 60 
  else:
    cur_m += min

  # update days as hours changed by 1 
    if hours == 24:
      days+=1
      hours = 0

# finding the right value of current hours
  # initial_12 = cur_h//12
  # final_12 = (cur_h + hours)//12
  # cur_h = (cur_h + hours)%12
  # num = final_12 - initial_12
  new_cur_h = cur_h%12
  if am_pm == 'PM':
    new_cur_h += 12

  new_cur_h += hours
  if new_cur_h >= 24:
    days += 1
  
  new_cur_h = new_cur_h % 24
  
  # print(new_cur_h)
  
  # if num == 0:
    
    
  
  
  if new_cur_h >=12: 
    if new_cur_h != 12: 
      answer += str(new_cur_h%12) + ":" 
    else: 
      answer += str(new_cur_h) + ":"
      
    if cur_m < 10:
      answer += '0'+ str(cur_m)+" PM"
    else:
      answer += str(cur_m)+ " PM"
  
  else:
    if new_cur_h == 0:
      new_cur_h = 12
    answer += str(new_cur_h) + ":"
    if cur_m < 10:
      answer += '0'+ str(cur_m)+" AM"
    else:
      answer += str(cur_m)+" AM"
  

  

  
    
  # answer+= " ({x} days later)".format(x = days)
  
  # finding the right day
  if day!="":
    rem_days = days%7
    idx_cur_day = name_of_days.index(day.lower()) + rem_days

    name_day = name_of_days[idx_cur_day].capitalize()
    answer+= ","
    answer+= " {x}".format(x = name_day )

  
  if days == 1:
      answer+= " (next day)"
  elif days > 1:
    answer+= " ({x} days later)".format(x = days)
  
  return answer 
    
  # print(answer)

  
  # print(cur_h, hours)
  
   
  # print(new_cur_h%12,cur_m,"PM" if new_cur_h>12 else "AM")
    

  # print(rem_days)
  # print(idx_cur_day)
  # print(name_of_days[idx_cur_day].capitalize())
  # working fine till now...

  
      
# actual = add_time("8:16 PM", "466:02", "tuesday")
# expected = "6:18 AM, Monday (20 days later)"

# print(actual == expected)

# actual = add_time("11:59 PM", "24:05", "Wednesday")
# expected = "12:04 AM, Friday (2 days later)"
    
# print(actual == expected)

# actual = add_time("2:59 AM", "24:00", "saturDay")
# expected = "2:59 AM, Sunday (next day)"
# print(actual == expected)

# actual = add_time("3:30 PM", "2:12", "Monday")
# expected = "5:42 PM, Monday"
# print(actual == expected)     
# actual = add_time("5:01 AM", "0:00")
# expected = "5:01 AM"  
# print(actual == expected)     
# actual = add_time("8:16 PM", "466:02")
# expected = "6:18 AM (20 days later)"    
# print(actual == expected)
# actual = add_time("11:59 PM", "24:05")
# expected = "12:04 AM (2 days later)"
# print(actual == expected)

# actual = add_time("2:59 AM", "24:00")
# expected = "2:59 AM (next day)"
# print(actual == expected)
# actual = add_time("11:40 AM", "0:25")
# expected = "12:05 PM"
# print(actual == expected)

# actual = add_time("9:15 PM", "5:30")
# expected = "2:45 AM (next day)"
# print(actual == expected)
# actual = add_time("11:55 AM", "3:12")
# expected = "3:07 PM"
# print(actual == expected)
# actual = add_time("3:30 PM", "2:12")
# expected = "5:42 PM"
# print(actual == expected)


# return new_time
  

# add_time("12:16 AM", "25:02",'tueSday')
# x = "abcd"
# y = x.lower()
# print(x.upper(),y)
