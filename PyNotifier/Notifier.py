import time as t
from pynotifier import Notification

while True:
    t.sleep(3600)
    Notification(
        title = "Get UP & Drink water",
        description = "It's been an hour have a quick Break",
        icon_path = r'C:\Users\Aditya\Documents\[P]Projects\PyNotifier\Frame 1.ico',
        duration = 30,
        urgency = Notification.URGENCY_CRITICAL
    ).send()