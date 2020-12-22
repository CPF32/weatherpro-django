#!/bin/bash

curl "http://localhost:8000/city-builder" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
