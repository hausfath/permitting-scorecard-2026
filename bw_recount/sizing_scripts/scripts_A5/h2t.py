import re,sys,html
t=open(sys.argv[1],encoding='utf8',errors='ignore').read()
t=re.sub(r'<(script|style).*?</\1>','',t,flags=re.S)
t=re.sub(r'</(p|tr|li|h\d|div)>','\n',t); t=re.sub(r'</t[dh]>',' | ',t)
t=html.unescape(re.sub(r'<[^>]+>','',t)); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
print(t)
