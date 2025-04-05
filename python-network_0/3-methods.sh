#!/bin/bash
# Displays all HTTP methods the server will accept
curl -sI "$1" | grep -i "Allow:" | awk -F "Allow: " '{print $2}'
