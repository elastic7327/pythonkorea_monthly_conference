# 수정중 

## T.D.D를 통한 Flask API 개발
## 2018 3월10일에 홍대 한빛 미디어에서 발표할 파이선 격월세미나 전용 리포입니다.  Flask + SqlAlchemy + Alembic + Zappa Integration Example

```
Feed Back 으로 인해서 테스트 쪽으로 좀더 중점적으로 가려고 합니다.

본인도 몇년동안 Django 또는 Beego 등의 조금 덩치가 있는 많은 것들이 갖춰있는 프레임워크를 사용하다보니.
하는 것에만 익숙해지고, 예전에 텀프로젝트 그리고 현재 있는 팀에서 Flask SqlAlchemy alembic 를 사용하면서, 
구글에 있는 다양한 블로깅에서 설명해주지않은 핵심만 몇개 간추려서 발표를 준비했습니다. 

Flask를 T.D.D 기반으로 좀더 장고처럼 비슷하게 그리고 익숙한 느낌으로 사용하기 위해서 발표를 준비했습니다.
이 프로젝트 역시 테스트가 매우 중요한 역활을 합니다. 

마지막으로는 저희 팀에서 서비스에 지금 사용하고 있는 Zappa라는 프레임워크를 사용해서,
3분만에 AWS Lambda에 작성한 Flask 프로젝트를 람다로 디플로이 해봅니다. 

python3

1. Hello Flask 
    Hello World with Test
    virtualenv -p python3 Path.
    pip install flask 

2 테스트를 하는 방법
    - 모듈, 모델(db model), 뷰 (func/auth/status)

    1. 유닛테스트를 합니다. 모듈 테스트를 합니다. 
        가령 제가 함수를 만들었다고 한다면.. 그 함수 또는 정말 간단한 수식을 테스트합니다. assertion 

    2. 해당 유닛을 뷰로 옮겨봅니다. 뷰로 옮기게 되면서, 400 error 500 error 다양한 에러가 발생할 수 있습니다. 여기서 status_code에 맞게 적절하게 
        예외처리를 넣어줍니다. 

    3. 뷰 처리에서 깔끔하게 201, 또는 200이 나온다면 그 다음 인증(Auth) 테스트를 합니다.
        사실 인증관련 모듈, 패키지 등은 다시 유닛테스트에 작성해서, 적절하게 동작을 하는지 확인합니다.
        다시 해당 모듈을 @데코레이터화 해서, 원하는 뷰에 적용을 합니다. 
        뷰에 적용이후 뷰 테스트를 시작합니다.
        
        P.S 이것은 개인적인 성향이 많이 따르기 때문에.. 처음부터 인증(Auth) 403 error 관련

    1 - 3 번을 좀더 재미있게 표현을 한다면..
        가령 대포를 만드는 과정이랑 비슷 한 것 같습니다.
        대포를 만들기위해서 대장간에서, 어느정도 만들고, 야전환경과 비슷한 곳에서 테스트를 하고 해당 무기를 전방에 배치를한다..? 그리고 테스트로 사격을 좀 해본다좀 재미있지만. 아무도 바로 성벽위에서 대포를 설치하면서 만들지 않죠. (물론 staging, prod 환경을 나눈다 하더라도..)

        실질적으로 게임에서는 대포는..드래드엔 드롭 또는 클릭 한방으로 만들기 때문에.. 사실 생각해보면 많은 분들께서 드래그엔 드롭 보다는...
        직접 뷰 위에서, chrome 또는 safari 또는 익스플로러로 한땀 한땀 확인해보면서 .. API를 개발한다는.. 사실 또는 포스트맨(postman) 으로 한땀 한땀.. 포스트맨은 양반

    4. 프로젝트 구조 전체를 리팩토링 하고 싶은경우, 지속적으로 테스트를 하면서,
       가령 서브 디렉토리에 있는 models.py 의 경로를 옮기고 싶은경우, 지속적으로 테스트를 하면서 옮겨보세요.
       누구도 한번에 머릿속으로 정확한 PATH를 알고 from ... import 를 작성 하지는 않는 것 같습니다. (가끔씩 원숭이도 나무에서 떨어질 떄가 있습니다.)

3. custom command and useful plugins

    커맨드(command)는 뷰에 올려놓고 사용하기에는 부담스러운 테스트를커맨드로 지정해서 하는 방법도 좋은 방법입니다. (Sentry)
    조금 오래걸리는 배치(Batch) 작업 등을 하기에 적절합니다.
    테스트를 좀더 테스트답게 쉽게 도와주는 빛과 소금 패키지
    Pytest, Mixer, unit-test

4. Views
    개인적인 취향일뿐.. 어느것을 선택하는것은 개발자의 자유입니다.
    개인적으로 클래스뷰를 선호합니다.. (장고의 영향..)

    함수형 뷰?
    클래스형 뷰? (플러그인 소개, 플러그인 없이도 가능)

5. Models 
    모델 테스트(test)와 마이그레이션(migration) 그리고 ORM을 위한 SqlAlchemy
    Sqlalchemy and Alembic -> like Django migration
    pip install sqlalchemy
    pip install alembic
    alembic init migrations
    alembic revision --autogenerate -m "added user . . . ."
    alembic revision --autogenerate -m "create user table"
    alembic upgrade head

6. Flask 이기에 좀더 자유로운 것들..
    모든 모듈들을 테스트화 해서, 필요할때 붙혀서 쓰면 됩니다.
    위에 3에서 했던 방법대로, 한다면 큰 무리없이 해당 모듈들을
    적절하게 Flask에 이식 할 수가 있을 것 입니다.

    Flask Unit Test with ElasticSearch  DSL Flask Unit Test with Sentry   - sentry Flask Unit Test with JWT -  json web token Flask Unit Test with Oauth2 - aka oauth2 Flask Unit Test with GraphQL - graphene 

    플라스크(Flask)는 Session 세션 또는 Auth 인증처리만 적절하게 처리한다면,

7. Deploy Zappa 
    람다(aws Lambda)로 가볍게 올려보자
    pip install zappa
    Async 비동기처리
    PS . 장고도 람다로 올릴수가 있다.!

8. 마치며.. 
    웹에서의 파이썬
```
