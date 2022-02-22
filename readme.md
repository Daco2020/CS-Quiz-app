# 컴퓨터 사이언스 퀴즈 웹 서비스
</br>

## 기존 CS 학습의 문제점

첫 번째, 직접 설명하는 식이 아닌 암기식으로 학습하게 된다. </br>
두 번째, 이것이 지금 내게 중요한 내용인지 판단하기 어렵다. </br>
세 번째, 혼자 주입식으로 학습하니 재미가 없다. </br>
</br>

## 왜 '퀴즈'인가?

'퀴즈'는 자신의 지식을 직접 설명해야 한다.</br>
가장 많은 답변이 달린 '퀴즈'를 보며 어떤 지식이 중요한지 자연스럽게 알게 된다.</br>
혼자가 아닌 함께 학습하고 내가 놓치고 있던 다른 사람의 지식까지 습득할 수 있게 된다.</br>
</br>

## 프로젝트 목적
- 주니어 개발자들이 CS을 재미있게 익힐 수 있는 웹 서비스를 제공하기 위함.
- 서비스를 제작하면서 나 스스로도 CS를 공부하기 위함.
- 질문과 답변을 통해 스스로 답을 찾게 만들기 위함.
</br>

## 목차
[사용 기술](#사용-기술)</br>
[구현 기능](#구현-기능)</br>
[문제 해결 과정](#문제-해결-과정)</br>
[API 명세](#API-명세)</br>
[ERD](#ERD)</br>
[추가-구현(예정)](#추가-구현(예정))</br>
[랭킹시스템(예정)](#랭킹시스템(예정))</br>


</br>

## 사용 기술
- 언어 : Python 3.8
- 프레임워크 : Django 4.0, DRF
- 데이터베이스 : MySQL
</br>

## 현재 구현 기능
1. 유저에게 퀴즈 3개를 반환합니다.
    - Query Params에 'category', 'level' 값을 넣을 수 있으며 해당되는 퀴즈를 받을 수 있습니다.
    - Params 값이 없다면 퀴즈를 랜덤하게 반환합니다.
2. 유저는 퀴즈 1개를 선택할 수 있습니다.
3. 유저는 답변을 작성 후 제출 할 수 있습니다.
    - 답변 뿐 아니라 참고한 레퍼런스 자료를 url 형태로 추가할 수 있습니다.
4. 유저는 답변 제출 후 다른 사람들의 답변을 확인할 수 있습니다.
</br>


## 문제 해결 과정
> GenericView와 serializer 사용하면 클라이언트가 원하는 키값과 맞지 않는 경우가 있었음 (ex. '태그명'이 필요한데 '태그id'로 반환하는 경우)
- serializer 커스텀할 수 있는 방법을 찾아 키값 형태를 수정하였음.
> 퀴즈의 답변들을 반환할 때, 해당 퀴즈 뿐만 아니라 전체 퀴즈의 답변들이 반환되는 문제가 있었음
- Views에서 해당되는 퀴즈id의 값만 반환되도록 커스텀 하였음.
> 유저가 퀴즈를 선택하면 해당 퀴즈의 답변 숫자를 표기하여 유저들의 흥미를 유도하고 싶었음
- models field에는 명시되어 있지 않기 때문에 serializer 커스텀하여 count 필드를 추가 반환하였음.
</br>

![진행과정 이미지](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ef5baac1-dae7-4d6c-899d-2a9d8d0c3942/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220219T050255Z&X-Amz-Expires=86400&X-Amz-Signature=27fb6ef9d472a103aa3dc0393ba6673b08cbe3d699dd2c351444fc99c759a78b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
</br>
</br>

## API 명세 
[포스트맨 다큐먼트 링크](https://documenter.getpostman.com/view/18513651/UVkiSdi1)
</br>
</br>


## ERD
![ERD 이미지](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f2bf078c-141d-417d-b6dd-a487b49dadb6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220219T045100Z&X-Amz-Expires=86400&X-Amz-Signature=289dab35d9e0710e9cf1956927d988a92567b1f6029a214d883ba9cc5ea6f5a8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

</br>
</br>

## 추가 진행(예정)

- [x] 유저 로그인 기능 구현
- [ ] Django templates을 이용한 프론트단 구현
- [ ] 기존 코드 로직 점검 및 1차 리펙토링
- [ ] unit test 진행
- [ ] 마음에 드는 답변이 있다면 ‘맞아요’버튼을 누를 수 있다.
- [ ] 틀린 답변이 있다면 ‘틀려요'버튼을 누르고 코멘트를 남길 수 있다.
- [ ] 유저가 직접 CS 퀴즈를 추가할 수 있다. 
- [ ] 유저는 본인이 답변한 퀴즈에 대해서 받지 않도록 선택 할 수 있다.
- [ ] 유저는 자신이 푼 퀴즈를 볼 수 있다.
- [ ] 유저는 자신이 푼 퀴즈를 다른 유저에게 퀴즈로 전달할 수 있다.
- [ ] 유저는 다른 유저로부터 받은 퀴즈를 풀 수 있다.
- [ ] 유저는 웹 서비스에 전반에 대한 피드백을 남길 수 있다.
</br>

## 랭킹시스템(예정)

- 유저가 답변을 제출하면 퀴즈의 난이도 별로 랭킹 포인트를 받는다.
- 유저가 답한 답변이 ‘맞아요’를 받을 수록 랭킹 포인트가 올라간다.
- 유저가 답한 답변이 ‘틀려요'를 받을 수록 랭킹 포인트가 줄어든다.
- 랭킹 포인트에 따라 티어를 나눈다
</br>

## 리펙토링 진행상황

### 2022년

- 2월 20일 : quiz > views > 'queryset'로직 내 불필요한 query요청 삭제 및 분기처리 추가
- 2월 21일 : django-allauth 라이브러리를 사용하여 소셜 로그인(google) 구현
