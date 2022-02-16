import datetime
import time
import winsound

alarm_time_hours = input("enter hours: ")
alarm_time_mins = input("enter minutes: ")
alarm_time_secs = input("enter secs: ")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == f"{alarm_time_hours}:{alarm_time_mins}:{alarm_time_secs}":
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

    print(current_time)
    time.sleep(1)
