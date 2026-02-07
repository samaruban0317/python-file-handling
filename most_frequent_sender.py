name = input("Enter file name: ")
handle = open(name)
email = dict()
for words in handle:
    word = words.rstrip()
    if not word.startswith('From '):
        continue
    if word.startswith('From '):
        mails = words.split()
        for id in mails:
            if '@' in id:
                email[id] = email.get(id,0) + 1
bigword = None
bigvalue = None
for word,value in email.items():
    if bigword == None or value>bigvalue:
        bigword = word
        bigvalue = value
print(bigword,bigvalue)
