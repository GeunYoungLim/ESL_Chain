# ESL Chain ( Electronic Shelf Chain + Block Chain )

ESL과 블록체인을 결합한 시스템.

## Prerequisites

파이썬 3.5버전 이상, pip3 9.0 이상

## Installing

프로젝트에서 필요한 pip 패키지를 먼저 설치한다. (requirments.txt 파일 사)

    pip install -r requirments.txt

## Running the test

처음 실행한다면 관리자 계정을 설정해야한다

    python3 manage.py init // 초기화
    python3 manage.py migrate // 마이그레이션
    python3 manage.py createsuperuser // 관리자 계정 설정

개발하고 디버그, 테스트를 진행 할 경우 장고 내장서버로 실행한다.

    python3 manage.py runserver
    // 문제 없이 실행 되었다면 아래 같은 메시지들이 출력됨.
    Performing system checks...

    System check identified no issues (0 silenced).
    April 07, 2018 - 12:00:06
    Django version 1.11.12, using settings 'esl_chain.settings'
    Starting development server at http://[로컬주소]:8000/
    Quit the server with CONTROL-C.

브라우저로 접속 한 뒤 확인해볻다.

    1. http://[로컬주소]:8000/admin       << 관리자 페이지
    2. http://[로컬주소]:8000/api/manual  << rest swagger 페이지
    3. http://[로컬주소]:8000/api/example << RESTful API 예제

## Project Structure


    ├── README.md             //리드 미 파일
    ├── esl_chain
    │   ├── esl_chain
    │   │   ├── __init__.py
    │   │   ├── settings.py   // 장고 서버 세팅
    │   │   ├── urls.py       // URL 정의
    │   │   ├── views.py      // view 구현 (example 예제코드 여기 있음)
    │   │   └── wsgi.py       // 웹서버 연동 (나중에 아파치랑 연동할 때 사용
    │   ├── manage.py         // 장고 프로젝트 매니저
    └── requirments.txt       // 필요 패키지


### Acknowledgments

*  [프로젝트 디렉토리]\esl_chain\secrets.json 파일은 git으로 관리하지 않음(보안을 위해...  .gitignore에 추가 됨).
*  [프로젝트 디렉토리]\esl_chain\secrets.json 파일은 manage.py 스크립트가 실행 될 때 자동으로 생성 됨.


