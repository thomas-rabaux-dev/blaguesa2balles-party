#!/bin/bash
# Script to try downloading missing navigation images from various Internet Archive snapshots

BASE_URL="http://web.archive.org/web"
TIMESTAMPS=(
    "20040902025339"
    "20040930144807"
    "20041202104907"
    "20050204160516"
    "20050414033429"
    "20050908093121"
)

MISSING_IMAGES=(
    "index_01.gif"
    "index_02.gif"
    "index_03.gif"
    "index_04.gif"
    "index_13.gif"
    "index_14.gif"
    "index_16.gif"
    "index_17.gif"
)

cd images

for timestamp in "${TIMESTAMPS[@]}"; do
    echo "Trying snapshot: $timestamp"
    for img in "${MISSING_IMAGES[@]}"; do
        echo "  Downloading $img..."
        curl -sL "${BASE_URL}/${timestamp}id_/http://users.skynet.be/bk337183/images/$img" -o "${img}.try"
        size=$(wc -c < "${img}.try")
        if [ $size -gt 2000 ]; then
            echo "    ✓ Found! (${size} bytes)"
            mv "${img}.try" "$img"
        else
            echo "    ✗ Not available"
            rm "${img}.try"
        fi
    done
done

echo "Done! Check which images were recovered."
