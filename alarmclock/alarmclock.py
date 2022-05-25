from datetime import datetime
from playsound import playsound

def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! please try again.."
    else:
        if int(alarm_time[:2]) > 12:
            return "Invalid hour format! please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid minute format! please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid second format! please try again..."
        else:
            return "ok"
while True:
    alarm_time = input("Enter your alarm time: ")

    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"setting alarm for {alarm_time}")
        break

alarm_hour = alarm_time[:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:]

while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_min:
                if alarm_second == current_sec:
                    print("wake up!!")
                    playsound("F:/python-beginner-dev-short-guide/alarmclock/alarm.wav")
                    break