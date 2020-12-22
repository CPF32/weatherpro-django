#!/bin/#!/usr/bin/env bash

curl "http://localhost:8000/city-builder" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "city": {
      "name": "'"${NAME}"'",
      "favorite": "'"${FAVORITE}"'"
    }
  }'

echo
