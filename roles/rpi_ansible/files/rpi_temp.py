#!/usr/bin/env python3

import json

try:
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        content = f.readline().strip('\n')
        temp_float = round(float(content)/1000, 1)
        print(json.dumps({"temperature_celcius": temp_float}))
except FileNotFoundError:
    print(json.dumps({"error": "Unable to read file with temperature reading!"}))
    raise SystemExit()
