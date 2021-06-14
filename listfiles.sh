#!/bin/zsh -f

filelist="$(pwd)/filelist.txt"
fd="$(pwd)/bin/fd"

cd "${searchdir/#\~/$HOME}"

# --follow: follow symlinks
# --hidden: include hidden files and folders
"$fd" --follow --hidden '.' '.' > "$filelist"

# print the number of files listed above
wc -l < "$filelist" | tr -d " " | tr -d "\n"
