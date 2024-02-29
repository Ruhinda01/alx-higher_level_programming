#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -s -L -X OPTIONS "$1"
