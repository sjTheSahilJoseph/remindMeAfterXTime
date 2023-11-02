# Imports
from notifypy import Notify
import time

# Variables
title = "Title"
message = "Message"
icon = "assets/icons/appIcon.ico"
applicationName = "remindMeAfterXTime"
notificationSound = "assets/sounds/notificationSound.wav"
interval = 30  # Interval in seconds

# Remind Me Function
def remindMe(title: str, message: str, icon: str, applicationName: str, notificationSound: str):
    """Remind Me is a function which just populates the notification based on the arguments.

    Args:
        title (str): Title of Notification
        message (str): Main Message of Notification
        icon (str): Application Icon that displays on notification
        applicationName (str): Which App is sending the notification?
        notificationSound (str): A sound that will play when the notification happens
    """
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.icon = icon
    notification.application_name = applicationName
    notification.audio = notificationSound
    notification.send()

# Remind me After X Time Function
def remindMeAfterXTime(interval: int):
    """RemindMeAfterXTime reminds you after an interval of time again and again.

    Args:
        interval (int): Interval Time in seconds
    """
    afterXTime = (60 * 60 * interval)
    while True:
        remindMe(title, message, icon, applicationName, notificationSound)
        time.sleep(afterXTime)

if __name__ == "__main__":
    remindMeAfterXTime(interval)