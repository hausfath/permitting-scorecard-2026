#!/bin/zsh
# usage: wb.sh OUTFILE URL [timestamp]
out=$1; url=$2; ts=${3:-2018}
for i in 1 2 3 4; do
  curl -m 300 -sL -o "$out" "https://web.archive.org/web/${ts}id_/$url"
  if file "$out" | grep -q PDF; then pdftotext -layout "$out" "${out%.pdf}.txt" 2>/dev/null; echo "OK $(ls -la $out | awk '{print $5}') $(wc -l < ${out%.pdf}.txt) lines"; exit 0; fi
  sleep 5
done
echo "FAIL: $(file $out | cut -c1-100)"; head -c 300 "$out" | tr -d '\0' | grep -o '<title>[^<]*' 
