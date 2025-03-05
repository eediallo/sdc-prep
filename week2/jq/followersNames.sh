#!/bin/bash

# Step 1: Fetch the followers_url from myGitHubInfo.json
followers_url=$(cat myGitHubInfo.json | jq -r '.followers_url')

# Step 2: Fetch the data from the followers_url
followers_data=$(curl -s "$followers_url")

# Step 3: Extract URLs from the fetched data and fetch them
echo "$followers_data" | jq -r '.[].url' | while read -r url; do
  if [ -n "$url" ]; then
    curl -s "$url"
    
  fi
done