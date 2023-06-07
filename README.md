# equivalence
## 이 모듈은 관계 R의 동치를 확인니다.
 (설치 방법: !git clone https://github.com/namu10664/equivalence.git)
 
 (위치 이동: %cd /content/equivalence/)
 
 (모듈을 설치하고 equivalence파일로 이동 한 후,) 
 
 우선, 입력창에 !python main.py 을 입력하면,

> 미리 주어진 집합 R = {(1, 1), (1, 3), (2, 2), (3, 3),(3, 1), (3, 4), (4, 4), (4, 3)} 가 동치인지 True, False로 알려줍니다.

  Equivalence_pkg.check에서 다음과 같은 기능을 따로 불러올 수 있습니다.
  
>  check_transitive(R): R이 추이적인지 판단합니다.
>  
>  check_symmetric(R):R이 대칭적인지 판단합니다.
>  
>  heck_reflexive(R):R이 반사적인지 판단합니다.
>  
>  check_equivalance(R):R이 동치인지 판단합니다.

 즉, R을 새로 정의하여 동치를 알고싶다면,

> 입력창에 from Equivalence_pkg.check import * 를 실행하고, (R을 새로 정의하고,) check_equivalance(R)를 입력하면 됩니다.
