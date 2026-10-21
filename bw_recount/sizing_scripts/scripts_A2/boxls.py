import re,sys,json,subprocess
fid=sys.argv[1]
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
h=subprocess.run(["curl","-sL","-A",UA,f"https://usfs-public.app.box.com/v/PinyonPublic/folder/{fid}"],capture_output=True,text=True).stdout
i=h.find('"items":[')
arr,_=json.JSONDecoder().raw_decode(h[i+8:])
for it in arr:
    print(it['typedID'], it['name'], it.get('itemSize'))
