#!/bin/bash
# senda a GET request to the url and diplays tne body of the response
curl -sx GET "$1" -H "X-CodingSchool-User-Id:98"
