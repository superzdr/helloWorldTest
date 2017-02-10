import numpy as np
import math
from DayAverage import cacuPV

class CompareXn(object):
    def comparetwo(self,arrayn,p1,p2):
        scacuPV = cacuPV()
        arrayp1 = scacuPV.cacuDA(arrayn,p1)
        arrayp2 = scacuPV.cacuDA(arrayn,p2)
        predictn = np.array(arrayp1) - np.array(arrayp2)

        arrayn2 = arrayn[1:].tolist()
        arrayn2.append(arrayn[-1])
        arrayn2n = np.array(arrayn2)
        realn = arrayn2n - arrayn

        resultn = predictn * realn
        resultn[:p2-1] = 0

        return resultn

    def cacuscore(self,arrayn):
        score = [0,0,0]
        for xs in arrayn:
            if xs >0:
                score[0] = score[0] + 1
                score[1] = score[1] + 1
                score[2] = score[2] + math.pow(10,score[1])
            elif xs < 0:
                score[0] = score[0] - 1
                if score[2] > 0.0:
                    score[2] = score[2] - math.pow(10, score[1])
                if score[1] > 0.0:
                    score[1] = score[1] - 1
        return score

    def comparearytwo(self,arrayn,arrayn1,arrayn2,p1,p2):
        p = max(p1,p2)
        pricen = np.array(arrayn)
        pn1 = np.array(arrayn1)
        pn2 = np.array(arrayn2)
        pn1[:p]=0
        pn2[:p]=0
        predictn = pn1 - pn2

        pricen2 = pricen[1:].tolist()
        pricen2.append(pricen[-1])
        pricen2n = np.array(pricen2)
        realn = pricen2n - pricen

        resultn = predictn * realn

        return resultn




'''
cx = CompareXn()

a = np.array([1,9,3,4,5,5,7])

resulta = cx.comparetwo(a,1,3)

print resulta

scorea = cx.cacuscore(resulta)
print scorea
'''
