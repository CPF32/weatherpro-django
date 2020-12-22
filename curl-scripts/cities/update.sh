#!/bin/bash

curl "http://localhost:8000/city-builder/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "city": {
      "name": "'"${NAME}"'",
      "favorite": "'"${favorite}"'"
    }
  }'

echo
