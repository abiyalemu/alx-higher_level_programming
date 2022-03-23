#!/bin/bash
# Sends a delete request to URL and displays body of response
curl -s "$1" -X DELETE
