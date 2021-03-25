# 4796번 캠핑

case = 1
while True:
    caseValue = 0
    L, P, V = map(int, input().split())
    if L == 0:
        break
    else:
        while True:
            if V - P >= 0:
                caseValue += L
                V -= P
            else:
                if V > L:
                    caseValue += L
                else:
                    caseValue += V
                print(f"Case {case}: {caseValue}")
                case += 1
                break