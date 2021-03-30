import time_parser
from io import StringIO
import subprocess as sp
import os
import sys
import os.path
import datetime
import pytz
import random

test_times_valid_format = [
"2021-03-19T20:37:22+02:00",
"2022-09-09T02:32:41+05:00",
"2012-10-23T20:47:45+08:00",
"1989-11-15T20:17:25+12:00",
"2024-03-18T20:27:34+0300",
"1924-05-12T20:52:44-0400",
"1987-08-10T20:32:12-0600",
"1999-12-03T20:55:25+0700",
"1989-01-06T20:59:45+0800",
"2005-07-25T20:33:25-0900"
]

test_times_valid_format_results = [
"2021-03-19T18:37:22+0000",
"2022-09-08T21:32:41+0000",
"2012-10-23T12:47:45+0000",
"1989-11-15T08:17:25+0000",
"2024-03-18T17:27:34+0000",
"1924-05-13T00:52:44+0000",
"1987-08-11T02:32:12+0000",
"1999-12-03T13:55:25+0000",
"1989-01-06T12:59:45+0000",
"2005-07-26T05:33:25+0000"
]

test_times_invalid_strings = [
"aaaaaaaaaaa",    
"The brown dog jumps over the lazy fox",    
"1999-23-22222222222222",
"-1",
"January 11th",
"9999999999999999999999999999999999999999999999999999999999999999999999999",
"-999999999999999999999999999999999999999999999999999999999999999999999999",
"1/0"
]

test_times_invalid_dates = [
"2021-13-19T20:37:22+02:00",    #invalid month
"2022-09-59T02:32:41+05:00",    #invalid day
"2012-23-123T20:47:45+08:00"    #invalid month and day
]

test_times_invalid_times = [
"2021-13-19T99999999:37:22+02:00",    #invalid hour
"2022-09-59T02:678:41+05:00",    #invalid minutes
"2012-23-123T20:47:61+08:00",   #invalid seconds
"2012-23-123T20:47:61+99:00"    #invalid timezone
]

test_times_negative_values = [
"2021-03-19T18:-37:22+0000",
"2022-09--08T21:32:41+0000",
"2012-10-23T-12:47:45+0000",
]

    
def test_convert_valid_dates():
    position = 0
    for i in test_times_valid_format:
        results = time_parser.convert_time(test_times_valid_format[position])
        assert results == test_times_valid_format_results[position]
        position = position + 1

def test_convert_invalid_strings():
    position = 0
    for i in test_times_invalid_strings:
        result = time_parser.convert_time(test_times_invalid_strings[position])
        assert result == "This is the incorrect date string format. (Example format 2021-03-29T20:37:45+02:00)\n"
        position = position + 1

def test_convert_invalid_dates():
    position = 0
    for i in test_times_invalid_dates:
        result = time_parser.convert_time(test_times_invalid_dates[position])
        assert result == "This is the incorrect date string format. (Example format 2021-03-29T20:37:45+02:00)\n"
        position = position + 1

def test_convert_invalid_times():
    position = 0
    for i in test_times_invalid_times:
        result = time_parser.convert_time(test_times_invalid_times[position])
        assert result == "This is the incorrect date string format. (Example format 2021-03-29T20:37:45+02:00)\n"
        position = position + 1

def test_convert_negative_values():
    position = 0
    for i in test_times_negative_values:
        result = time_parser.convert_time(test_times_negative_values[position])
        assert result == "This is the incorrect date string format. (Example format 2021-03-29T20:37:45+02:00)\n"
        position = position + 1

def test_store_values():
    values_file = open("time_values.txt", "w")
    values_file.close()
    format = "%Y-%m-%dT%H:%M:%S%z"
    test_1 = datetime.datetime.strptime("2005-07-25T20:33:25-1111", format)
    test_2 = datetime.datetime.strptime("2005-07-25T20:33:25-2222", format)
    time_parser.store_time(test_1, test_2)
    values_file = open("time_values.txt", "rt")
    values_file_list = []
    for i in values_file.readlines():
        values_file_list.append(i.strip())
    assert values_file_list[0] == "2005-07-25T20:33:25-1111 >>>>>>>>> 2005-07-25T20:33:25-2222"
    values_file.close()
    values_file = open("time_values.txt", "w")
    values_file.close()

def test_view_stored_values():
    values_file = open("time_values.txt", "w")
    values_file.writelines("This is the test!")
    values_file.close()
    run_view_values = time_parser.view_time()
    assert run_view_values == ['This is the test!']
    values_file = open("time_values.txt", "w")
    values_file.close()
    
def test_clear_times():
    values_file = open("time_values.txt", "w")
    values_file.writelines("This is the test!")
    values_file.close()
    time_parser.clear_times()
    assert os.stat("time_values.txt").st_size == 0








    

