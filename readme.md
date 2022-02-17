# DRF 초기세팅 파일 입니다.
### 다음 사항이 세팅되어 있습니다.
- cors 세팅
- pymysql 세팅
- logging 세팅
- 기본 app으로 'users' 세팅
- app의 경우 apps 디렉토리 하위 위치(파일을 app별로 관리하기 위함)


### 다음 순서를 따라해주세요.
1. 레포를 깃 클론 받아주세요.
2. 가상환경을 만들어주세요. (파이썬 3.8 권장)
3. requirements.txt 를 이용하여 라이브러리를 설치해주세요.
4. project_name/settings.py 에서 DATABASE 에 데이터베이스 이름을 넣어주세요. (데이터 베이스가 없다면 생성 후 이름을 기재해주세요)
5. python manage.py runserver 으로 서버를 열어주세요.
6. http://127.0.0.1:8000/users/ping  해당 url에서 반환메시지(pong)가 정상적으로 나오는지 확인해주세요.
7. 서버가 정상작동한다면 'project_name'의 이름을 본인의 프로젝트 명으로 바꿔주세요!
   (VSC기준, shift + command + f 를 누르면 모든 파일의 'project_name'을 찾아서 바꾸실 수 있습니다!)

- 설치된 라이브러리는 requirements를 참고해주세요.
- 추가하면 좋은 공통 라이브러리는 추가 후 PR요청해주세요.

### 권장 사항
- swagger를 사용한다면 drf-yasg을 추가로 설치해주세요.
- permission의 경우 settings 내부에 설정하는 방법과 permissions.py를 만드는 방법이 있습니다. 원하는 방법으로 추가하여 진행해주세요.


### 업데이트 이력
2022년 2월 12일
- settings.py -> INSTALLED_APPS에 'rest_framework', 추가.
- 'users' app에 serializers.py 파일 추가.
- util 폴더 apps 폴더 하위로 이동.
