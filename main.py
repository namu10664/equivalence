from Equivalence_pkg.check import *

R={(1, 1), (1, 3), (2, 2), (3, 3),(3, 1), (3, 4), (4, 4), (4, 3)}

print('집합 {}의 동치를 확인합니다.\n'.format(R))

print('추이적인지 확인 : ',Equivalence.check_transitive(R))
print('대칭적인지 확인 : ',Equivalence.check_symmetric(R))
print('반사적인지 확인 : ',Equivalence.check_reflexive(R))
print('동치인가?       : ', Equivalence.check_equivalance(R))
