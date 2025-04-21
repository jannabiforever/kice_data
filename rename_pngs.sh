#!/bin/zsh

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <folder_name>"
  echo "Example: $0 2025_11"
  exit 1
fi

folder="./png/$1"

if [[ ! -d "$folder" ]]; then
  echo "Error: Folder '$folder' does not exist."
  exit 1
fi

cd "$folder"

for file in *.png; do
  newname="${file/페이지/p}"
  if [[ "$file" != "$newname" ]]; then
    mv "$file" "$newname"
    echo "Renamed: $file -> $newname"
  fi
done
