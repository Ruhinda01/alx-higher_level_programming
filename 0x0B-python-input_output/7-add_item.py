#!/usr/bin/python3
import sys
import json
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

if not os.path.exists(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("[]")

if len(sys.argv) > 1:
    data = load_from_json_file(filename)
    for j in range(len(sys.argv[1:])):
        data.append(sys.argv[j+1])
    save_to_json_file(data, filename)
