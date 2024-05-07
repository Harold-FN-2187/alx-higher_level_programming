#!/bin/bash
# get size of HTTP response of give URL in bytes
curl -s "$1" | wc -c