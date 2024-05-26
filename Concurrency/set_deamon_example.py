import threading


def background_task():
    while True:
        print("Running background task...")
        time.sleep(1)


def main_task():
    print("Main task is running...")
    time.sleep(5)
    print("Main task is done.")


# ایجاد یک نخ برای وظیفه پس‌زمینه
background_thread = threading.Thread(target=background_task)
# تنظیم نخ به حالت daemon
background_thread.setDaemon(True)
# شروع نخ
background_thread.start()

# اجرای وظیفه اصلی
main_task()

print("Program is ending...")

###################################################مثال دوم#######################################

import threading
import time


def background_task():
    while True:
        print("Running background task...")
        time.sleep(1)


def main_task():
    print("Main task is running...")
    time.sleep(5)
    print("Main task is done.")


# ایجاد یک نخ برای وظیفه پس‌زمینه
background_thread = threading.Thread(target=background_task)
# تنظیم نخ به حالت daemon با استفاده از خاصیت daemon
background_thread.daemon = True
# شروع نخ
background_thread.start()

# اجرای وظیفه اصلی
main_task()

print("Program is ending...")
