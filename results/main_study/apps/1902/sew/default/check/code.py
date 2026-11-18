class  Ddict:
    def  __init__(self):
        self.dicts = dict()
    def  add(self,key):
        d = self.dicts
        for i in key:
            if  i not  in d:
                d[i]=dict()
            d = d[i]
        d[' '] = ''
    def  find(self,key):
        if key=='':
            return '',''
        d=self.dicts
        q=[]
        h = [key[0]]
        for i in key:
            if  i not  in d:
                if  ' ' in  d and  len(d)==1:
                    return ''.join(q),''.join(h)
                return ('','')
            q.append(i)
            if  1!=len(d):
                h=q[:]
            d = d[i]
        if ' ' in d and len(d)==1:
            return ''.join(q),''.join(h)
        return ('','')
words = Ddict()
ans=0
while  1:
    try:
        x = input()
        if  len(x) == 0:
            break
    except:
        break
    ans += 1+len(x)
    ws = [[]]
    for  i in  x:
        if not i in '.,?!\'- ':
            ws[-1].append(i)
        else:
            if ws[-1]:
                ws.append([])
    ws = list([''.join(e) for  e in  ws])
    for  w in  ws:
        next_word,helped_word=words.find(w)
        if  next_word and  next_word!=helped_word:
            ans -= len(next_word) - len(helped_word) - 1
        words.add(w)
print(ans)