name = input("Enter file:")
handle = open(name)
hr = list()
count = 0
for id in handle:
    if not id.startswith('From '):
        continue
    mails = id.split()  
    thm = mails[5]
    time = thm.split(':')
    hour = time[0]
    hr.append(hour)
dic = dict()
for i in hr:
    dic[i] = dic.get(i,0) + 1
lit = list()
for k,v in dic.items():
    nlit = (k,v)
    lit.append(nlit)
lit = sorted(lit,reverse=False)
for a,b in lit:
    print(a,b)
