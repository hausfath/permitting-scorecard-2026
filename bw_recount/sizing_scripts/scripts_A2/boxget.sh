#!/bin/zsh
# usage: boxget.sh f_ID OUTFILE
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
curl -sL -A "$UA" -o "$2" "https://usfs-public.app.box.com/index.php?rm=box_download_shared_file&vanity_name=PinyonPublic&file_id=$1"
file -b "$2" | cut -c1-50
