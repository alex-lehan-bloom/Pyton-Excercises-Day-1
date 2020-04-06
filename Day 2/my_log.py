
import datetime


def my_log():
    try:
        f = open("log.txt", "a+")
    except Exception as e:
        print(e)
    date = datetime.datetime.now()
    f.write(date.strftime("%y/%m/%Y, %H:%M:%S") + " This is a new log message line\n")
    f.close()
    print("Successfully created new log entry.")


my_log()
my_log()