#!/usr/bin/env python3

from ruuvitag_sensor.ruuvitag import RuuviTag
import json, sys, re

def run(mac):
    sensor = RuuviTag(mac)
    sensor.update()
    return sensor.state

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 get_tag_data.py <MAC Address of the RuuviTag>")
    elif re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", sys.argv[1].lower()):
        state = run(sys.argv[1])
        print(json.dumps(state))
    else:
        print("Invalid MAC address %s" % sys.argv[1])
        

