#!/bin/bash

curl "http://localhost:8000/city-builder/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
