#! /bin/python3

import pydbus
from gi.repository import GLib, Notify
import cv2
import os
import time

def notify_user():
    pass

def take_pic():
    """Take a picture with default camera and store it.
    """
    camera = cv2.VideoCapture(0)
    for _ in range(3):  # snap 3 times in a row
        ret_val, frame = camera.read()
        pic_path = os.path.join(
            os.path.expanduser("~/facesnaps"),
            "capture_{}.png".format(time.time()))
        cv2.imwrite(pic_path, frame)

    camera.release()


def _event_handler(*args):
    if isinstance(args[1], dict) and not args[1].get('LidIsClosed', True):
        time.sleep(1)  # wait 1 sec before snapping
        take_pic()


def main():
    loop = GLib.MainLoop()
    bus = pydbus.SystemBus()
    lid_proxy = bus.get("org.freedesktop.UPower", "/org/freedesktop/UPower")
    lid_proxy.onPropertiesChanged = _event_handler
    loop.run()


if __name__ == '__main__':
    main()
