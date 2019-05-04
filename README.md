# node-red-dalinwk
This project consists of Node-RED nodes for Dalhousie's INWK IoT lab exerices.

## Ruuvi nodes


### ruuvi-scan
Queries a Ruuvi sensor and outputs its data to msg.payload as JSON-Formatted string.

The node depends on a Python script to run; therefore, Python (2 or 3) must be installed
Also the following module "ruuvitag_sensor" using downloaded from [github](https://github.com/ttu/ruuvitag-sensor)


### ruuvi-adapter
Receives SON-Formatted string that contains ruuvi sensor data and splits the data into five outputs:
 - Temperature: Celcius
 - Humidity: RH-%
 - Pressure: Pascal
 - Acceleration: milli-G
 - Battery: mV


## Version
Currently version 0.1.0.

## Installing
Clone the repository to you computer. Then in your node red directory (typically ~/.node-red) run
```
cd ~/.node-red
npm install ~/node-red-dalinwk

```

