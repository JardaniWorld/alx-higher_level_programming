#!/bin/bash
# This script displays the number of bytes in Location

curl -s "$1" | wc -c
