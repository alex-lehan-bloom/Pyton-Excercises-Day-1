
import datetime


def my_log(msg, path):
    try:
        f = open(path, "a+")
    except OSError as e:
        print("something went wrong: " + e.strerror)
    date = datetime.datetime.now()
    f.write(date.strftime("%y/%m/%Y, %H:%M:%S") + " {} \n".format(msg))
    f.close()
    print("Successfully created new log entry.")


my_log("This is a log message from Alex", "log.txt")
