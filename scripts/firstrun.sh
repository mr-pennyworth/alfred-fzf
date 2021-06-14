#!/bin/bash

xattr -d com.apple.quarantine ./bin/fd
xattr -d com.apple.quarantine ./bin/fzf
xattr -d com.apple.quarantine ./bin/sed

sed -i '' 's/firstrun.sh/listfiles.sh/g' ./info.plist
./scripts/listfiles.sh
