import sys
import os.path
import datetime
import pytz
import random

def convert_time(date):
    format = "%Y-%m-%dT%H:%M:%S%z"
    try:
      date_time_obj = datetime.datetime.strptime(date, format)
      date_time_obj_utc = date_time_obj.astimezone(pytz.utc)
      print("The entered time {} has been converted to UTC and resulted in {} \n".format(date_time_obj.strftime(format), date_time_obj_utc.strftime(format)))
      store_time(date_time_obj, date_time_obj_utc)
      return date_time_obj_utc.strftime(format)
    except ValueError:
      error_string = "This is the incorrect date string format. (Example format 2021-03-29T20:37:45+02:00)\n"
      print(error_string)
      return error_string

def input_time(var):
    if var == "manual":
        date_input = input("Input the new date (Example format 2021-03-29T20:37:45+02:00):")
    elif var == "random":
        random_timezone = '%0*d' % (2, random.randint(1, 9))
        random_number_sign = random.randint(1, 2)
        if random_number_sign == 1:
            random_sign = "+"
        elif random_number_sign == 2:
            random_sign = "-"
        date_input = "{}-{}-{}T{}:{}:{}{}{}:00".format(random.randint(1900,2025), random.randint(1,12), random.randint(1,28), random.randint(0,23), random.randint(0,59), random.randint(0, 59), random_sign, random_timezone)
        print("The randomly chosen date is {}\n".format(date_input))
    convert_time(date_input)
    return

def store_time(time, time_utc):
    values_file = open("time_values.txt", "a")
    format = "%Y-%m-%dT%H:%M:%S%z"
    values_file.writelines("{} >>>>>>>>> {}\n".format(time.strftime(format), time_utc.strftime(format)))
    values_file.close()
    return
    
def view_time():
    if os.path.isfile('time_values.txt') and os.stat("time_values.txt").st_size != 0:
        print("Viewing conversion history:")
        values_file = open("time_values.txt", "rt")
        values_file_list = []
        for i in values_file.readlines():
            values_file_list.append(i.strip())
        for i in values_file_list:
            print("{}".format(i))
        values_file.close()
        print("\n")
        return values_file_list
    else:
        print ("You have not yet stored any values! \n")

def clear_times():
    if os.path.isfile('time_values.txt') and os.stat("time_values.txt").st_size != 0:
        values_file = open("time_values.txt", "w")
        values_file.close()
        print("Conversion history has been cleared! \n \n")
        return
    else:
        print ("You have not yet stored any values! \n")
    return

def main():
    user_input = input("Choose one option: \n n = Input new time and date manually \n r = Input random new time and date \n v = View conversion history \n c = Clear inputted times\n e = Exit program \n")
    if (user_input == "v"):
        view_time()
        main()
    if (user_input == "n"):
        input_time("manual")
        main()
    if (user_input == "r"):
        input_time("random")
        main()
    if (user_input == "c"):
        clear_times()
        main()
    if (user_input == "e"):
        print ("Thanks for using this program! \n")
        sys.exit()
    else:
        print("Invalid command, please try again! \n")
        main()
    
if __name__ == "__main__":
    main()
