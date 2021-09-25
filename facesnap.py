#! /bin/python

import pydbus
from gi.repository import GLib
import cv2
import os
import time

def take_pic():
  camera = cv2.VideoCapture(0)
  for _ in range(3):
    ret_val, frame = camera.read()    
    pic_path = os.path.join(
      os.path.expanduser("~/facesnaps"), "capture_{}.png".format(time.time()))
    cv2.imwrite(pic_path, frame)

  camera.release()

def _event_handler(*args):
  if isinstance(args[1], dict) and not args[1].get('LidIsClosed', True):
    time.sleep(1)
    take_pic()


def main():
  loop = GLib.MainLoop()
  bus = pydbus.SystemBus()
  lid_proxy = bus.get("org.freedesktop.UPower", "/org/freedesktop/UPower")
  lid_proxy.onPropertiesChanged = _event_handler
  loop.run()
  
if __name__ == '__main__':
  main()
