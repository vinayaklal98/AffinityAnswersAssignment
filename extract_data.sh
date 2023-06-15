#!/bin/bash

# This url is used to download the text file containing all the data
input_url="https://www.amfiindia.com/spages/NAVAll.txt"

# Output File to which the Scheme Data and Assest Value is written to
output_file="output.tsv"

# To download the input file
curl -o "$output_file" "$input_url"

# Extract Scheme Name and Asset Value fields using awk
#
awk -F';' '{print $4 "\t" $5}' "$output_file" > "$output_file.tmp"

# Remove lines with headers and empty fields
grep -vE "^Scheme\sName\tAsset\sValue$" "$output_file.tmp" > "$output_file"

# Remove temporary file
rm "$output_file.tmp"