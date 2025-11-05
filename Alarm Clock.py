import datetime
import os
import time
import platform

def set_alarm(alarm_time, sound_file):
    """
    Set an alarm to go off at a specified time.

    :param alarm_time: The time to set the alarm for (in 24-hour format, e.g. "14:30").
    :param sound_file: The file path to the sound file to play when the alarm goes off.
    """
    print(f"Alarm set for {alarm_time}...")
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake Up!")
            play_sound(sound_file)  # Play the sound file
            break
        time.sleep(1)  # Check every second

def play_sound(sound_file):
    """
    Play the sound file.

    :param sound_file: The file path to the sound file to play.
    """
    if platform.system() == "Windows":
        os.system(f'start {sound_file}')
    elif platform.system() == "Darwin":  # macOS
        os.system(f'afplay {sound_file}')
    elif platform.system() == "Linux":
        os.system(f'aplay {sound_file}')
    else:
        print("Unsupported OS")

def main():
    while True:
        alarm_time = input("Enter the time to set the alarm for (in 24-hour format, e.g. 14:30): ")
        try:
            datetime.datetime.strptime(alarm_time, "%H:%M")
            break
        except ValueError:
            print("Invalid time format. Please enter the time in 24-hour format (e.g., 14:30).")

    sound_file = input("Enter the file path to the sound file to play when the alarm goes off: ")
    set_alarm(alarm_time, sound_file)

if __name__ == "__main__":
    main()
