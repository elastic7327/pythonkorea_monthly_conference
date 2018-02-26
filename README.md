# 수정중 

## pythonkorea_montly_conference // Flask + Sqlalchemy + Alembic +Zappa Integration + @ 
## 2018 3월10일에 홍대 한빛 미디어에서 발표할 파이선 격월세미나 전용 리포입니다. 

## Flask + SqlAlchemy + Alembic + Zappa Integration Example
## 플라스크를 장고처럼 익숙하게 만들어서, 사용하기


```
본인도 몇년동안 Django 또는 Beego 등의 조금 덩치가 있는 프레임워크를 사용하다보니.
하는 것에만 익숙해지고, 예전에 텀프로젝트 그리고 현재 있는 팀에서 FSA를 사용하면서, 
구글에 있는 다양한 블로깅에서 설명해주지않은 핵심만 몇개 간추려서 발표를 준비했습니다. 

Flask를 좀더 장고처럼 비슷하게 그리고 익숙한 느낌으로 사용하기 위해서 발표를 준비했습니다.
이 프로젝트 역시 테스트가 매우 중요한 역활을 합니다. 

마지막으로는 저희 팀에서 서비스에 지금 사용하고 있는 Zappa라는 프레임워크를 사용해서,
3분만에 AWS Lambda에 작성한 Flask 프로젝트를 람다로 디플로이 해봅니다. 


python3

1. Hello Flask 
    장고보다 조금 쉬워보이는 Hello World
    virtualenv -p python3 Path.
    pip install flask 

2. Test & command
    장고처럼 Test
    unittest
    pip install pytest
    장고처럼 Command

3. Views
    함수형 뷰

    클래스형 뷰

4. Sqlalchemy and Alembic -> like Django migration
    장고처럼 ORM 
    pip install sqlalchemy
    pip install alembic

    alembic init migrations
    alembic revision --autogenerate -m "added user . . . ."
    alembic revision --autogenerate -m "create user table"
    alembic upgrade head

5. Deploy Zappa 
    람다로 가볍게 올려보자
    pip install zappa
    Async 비동기처리
    PS . 장고도 람다로 올릴수가 있다.!

```
