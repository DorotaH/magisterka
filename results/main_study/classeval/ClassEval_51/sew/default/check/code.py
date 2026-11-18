import  numpy as  np


class  KappaCalculator:

    @staticmethod
    def kappa(testData, k):
        dataMat, P0 = np.mat(testData), 0.0
        for  i in  range(0, k):
            P0 = P0 + dataMat[i, i] * 1.0
        xsum, ysum = np.sum(dataMat, axis=1), np.sum(dataMat, axis=0)
        sum=np.sum(dataMat)
        Pe=float(xsum * ysum)/sum/sum
        P0=float(P0/sum*1.0)
        cohens_coefficient=float((P0-Pe)/(1-Pe))
        return cohens_coefficient
    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        dataMat, oneMat = np.mat(testData, float), np.ones((k, 1))
        sum = 0.0
        P0 = 0.0
        for  i in  range(0, N):
            temp = 0.0
            for  j in  range(k):
                sum += dataMat[i, j]
                temp += 1.0 * dataMat[i, j] ** 2
            temp = temp - n
            temp /= (n - 1) * n
            P0 = P0 + temp
        P0=P0 * 1.0/N
        ysum=np.sum(dataMat, axis=0)
        for  i in  range(0, k):
            ysum[0, i] = pow((ysum[0, i] / sum), 2)
        Pe=oneMat * ysum*1.0
        ans=(P0-Pe)/(1-Pe)
        return ans[0, 0]