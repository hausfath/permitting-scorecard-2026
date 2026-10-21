import re,sys
t=open(sys.argv[1],errors='ignore').read()
t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'&#\d+;|&nbsp;|&[a-z]+;',' ',t); t=re.sub(r'\s+',' ',t)
pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 400
for m in re.finditer(pat,t,re.I):
    print('...',t[max(0,m.start()-w):m.end()+w],'\n')
