#!/bin/zsh -f

cat filelist.txt             \
  | ./bin/fzf -f "$1"        \
  | head -n9                 \
  | ./bin/sed -e 's/"/\\&/g' \
  | ./bin/sed -e 's/\r$//g'  \
  > matches.txt

# add an empty first object, so that
# each following object can start with a comma
echo '{"items": [{}'

while IFS='' read -r relpath || [ -n "${relpath}" ]; do
  abspath="$searchdir/$relpath"
  filename="$(basename "$relpath")"
  cat <<EOF
  ,{
     "title": "$filename",
     "subtitle": "$relpath",
     "arg": "$abspath",
     "type": "file:skipcheck",
     "icon": {"path": "$abspath", "type": "fileicon"}
  }
EOF
done < matches.txt

echo ']}'
