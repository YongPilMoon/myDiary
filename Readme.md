# myDiary
생각을 깊게 할 수 있도록 도와주는 일기장을 만들고 싶습니다.

### 개발환경 세팅

- 파이썬 가상환경
  - [x] pyenv
	- [x] python
	- [x] django
	- [x] html, css, javascript, sass

### 서비스 기능
- calendar 기능 
	- 작성한 일기 calendar에 표시
	- calendar의 날짜 클릭 시 작성 일기 확인
	 
	
- 일기 작성 기능
	- 작성
	- 수정
	- 삭제
	
- 로그인
	- 페이스북 로그인
	- 구글 로그인	
### 개발 과정

-  개발 시작: 2016-10-30

#### 기능 구현

- calendar 구현
	 - [x] 기본 calendar class를 활용한 calendar구현
		- main page에 달력 그려주기
	- [x] 기본 일기 작성 구현
		- 달력 날짜 클릭시 장성 form으로 이동
	- [x] calendar에 일기 작성된 날짜 표시
		- 일기를 작성하면 해당 날짜에 초록색을 표시
	
- 로그인 구현
	- [x] 일반로그인	
	- [x] 페이스북 로그인
	- [x] 구글 로그인
		- social auth library 이용
- 회원가입

- 비밀번호 찾기
	- 가입 email로 hash된 token을 포함한 link를 보내줌			
- 일기 공유 기능

- 일기 암호화

- 일기 도움말 서비스	
