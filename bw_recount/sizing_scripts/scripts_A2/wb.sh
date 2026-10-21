#!/bin/zsh
# usage: wb.sh URL OUTFILE  -> fetch closest Wayback raw copy, convert pdf to txt
curl -sL -o "$2" "http://web.archive.org/web/2019id_/$1"
if file "$2" | grep -q PDF; then pdftotext -layout "$2" "${2%.pdf}.txt" 2>/dev/null; echo "OK $(wc -c < ${2%.pdf}.txt) chars"; else echo "NOT PDF: $(file -b $2 | cut -c1-60)"; fi
