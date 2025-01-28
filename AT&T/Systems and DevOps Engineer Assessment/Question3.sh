#!/usr/bin/env bash

# Read input from stdin
read my_variable </dev/stdin

# Replace 'replaceme' with 'processed' and output the result
echo "$my_variable" | sed 's/replaceme/processed/g'

exit 0
