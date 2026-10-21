import re, sys, collections
txt = open(sys.argv[1], encoding='utf-8', errors='replace').read().splitlines()
cnt = collections.defaultdict(collections.Counter)
first = {}
for i, l in enumerate(txt):
    m = re.match(r'^\s*([GY]?\d{5})\s+1\s', l)
    if m and i + 1 < len(txt):
        l2 = txt[i+1]
        if re.match(r'^\s+2\s', l2):
            toks = l2.split()
            st = next((t for t in toks if t in ('PROD','PRIMRY','UNIT','RELINQ','EXPIR','TERMIN','SOP','SOO','OPERNS','CANCEL','NO-EXE','DSO','REJECT','ADMIN')), None)
            if st is None:
                st = '?'
            sale = toks[-1]
            cnt[sale][st] += 1
want = sys.argv[2].split(',')
for s in want:
    c = cnt.get(s)
    print(s, sum(c.values()) if c else 0, dict(c) if c else {})
