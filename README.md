# posts-crud-practice

SKT ALEPH Day3 실습 과제용 Flask + PostgreSQL 게시판이다. 기존 mini-watch의 일반 서비스와 감시 서비스를 유지하면서 게시글 CRUD를 역할별 모듈로 분리했다.

## 구조

```text
general/
├─ app.py
├─ db.py
├─ post_rules.py
├─ request_logging.py
├─ requirements.txt
├─ repositories/
│  ├─ __init__.py
│  └─ posts.py
├─ routes/
│  ├─ __init__.py
│  └─ posts.py
├─ templates/
│  ├─ index.html
│  ├─ detail.html
│  ├─ new.html
│  ├─ edit.html
│  ├─ delete.html
│  └─ error.html
├─ static/
│  └─ style.css
└─ sql/

monitor/backend/
└─ 기존 감시 서비스
```

## 1. PostgreSQL 준비

`general/.env.example`을 참고해 `general/.env`를 만든다. 실제 `.env`는 Git에 올리지 않는다.

```text
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=general_db
DB_USER=postgres
DB_PASSWORD=YOUR_POSTGRES_PASSWORD
```

수업에서 만든 기존 `general_db`와 `posts` 테이블을 그대로 사용할 수 있다. 새로 준비하는 경우 `general/sql/`의 SQL을 수업 순서에 맞게 실행하고 `post_ids.sql`까지 적용해 게시글 번호 시퀀스를 설정한다.

## 2. 일반 서비스 실행

Windows CMD에서 `general` 폴더를 연다.

```text
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

브라우저에서 `http://127.0.0.1:5100/`에 접속한다.

## 3. 감시 서비스 실행

별도 CMD에서 `monitor/backend` 폴더를 연다.

```text
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

감시 서비스는 `http://127.0.0.1:5200`에서 실행되며 일반 서비스의 요청 기록을 `/api/events`로 수집한다.

## CRUD 주소

- 목록: `GET /`
- 상세: `GET /board/<post_id>`
- 작성: `GET, POST /board/new`
- 수정: `GET, POST /board/<post_id>/edit`
- 삭제 확인/처리: `GET, POST /board/<post_id>/delete`

작성·수정 입력은 서버에서 `strip()` 후 공통 검사한다. 잘못된 입력은 400, 없는 게시글은 404, 저장·수정·삭제 성공 후 이동은 303을 사용한다.
