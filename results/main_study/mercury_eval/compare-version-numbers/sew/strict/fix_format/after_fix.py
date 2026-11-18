class  Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if  version1.count('.') > version2.count('.'):
            for i in range(0, version1.count('.')):
                version2 += ".0"
        elif  version2.count('.')>version1.count('.'):
            for  i in  range(version2.count('.')):
                version1 += ".0"
        v1, v2=[int(x) for x in version1.split(".")], [int(x) for x in version2.split(".")]
        if  v2[0]<v1[0]:
            res = 1
        elif  v1[0]<v2[0]:
            res = -1
        else:
            for  i,j in  zip(v1,v2):
                if  j==i:
                    res=0
                elif  i>j:
                    res = 1
                    break
                elif  j>i:
                    res = -1
                    break

        return  res
