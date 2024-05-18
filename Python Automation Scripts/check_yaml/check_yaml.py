#!/usr/bin/env python3

import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r") as file:
            yaml.safe_load(file.read())
        print("Validate YAML!")
    else:
        print(f"{sys.argv[1]} not found")
else:
    print("Usage: checkyaml.py <file>")
