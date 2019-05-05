#!/usr/bin/env python3


# Form: https://github.com/ttu/ruuvitag-sensor
from ruuvitag_sensor.ruuvi import RuuviTagSensor
import json, sys, re


def run(mac, timeout=3):
    # This can handle more than one MAC address
    return RuuviTagSensor.get_data_for_sensors([mac], timeout)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 get_tag_data.py <MAC Address of the RuuviTag>")
    elif re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", sys.argv[1].lower()):
        MAC = sys.argv[1]
        if len(sys.argv) > 2 and sys.argv[2].isdigit():
            timeout = int(sys.argv[2]) 
            data = run(MAC, timeout)
        else:
            data = run(MAC)

        print(json.dumps(data.get(MAC, {})))
    else:
        print("Invalid MAC address %s" % sys.argv[1])
        

