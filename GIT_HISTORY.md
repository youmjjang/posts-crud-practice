# Git 작업 이력

이 저장소는 Git으로 구현 과정과 구조 변경을 커밋했으며, 각 커밋 메시지에서 작업 내용을 확인할 수 있다.

대표 커밋:

- `d328dfa7` — **Add modular posts CRUD implementation**
  - 게시글 CRUD를 `routes/posts.py`, `repositories/posts.py`, `post_rules.py`, `request_logging.py`로 역할별 분리
- `b4b824e6` — **Add board templates and styles**
  - 목록·상세·작성·수정·삭제·오류 화면과 공통 CSS 추가
- `c431281c` — **Preserve SQL setup and practice files**
  - PostgreSQL 준비 SQL과 기존 실습 파일 유지
- `ee6bf79d` — **Preserve monitoring service**
  - `monitor/backend` 감시 서비스 구조와 수집 기능 유지
- `6ccd938f` — **Document setup and CRUD routes**
  - 실행 방법, 폴더 구조, CRUD 주소와 HTTP 처리 규칙을 README에 문서화

GitHub의 저장소 **Commits** 화면에서도 위 커밋 SHA와 메시지를 직접 확인할 수 있다.

Repository: https://github.com/youmjjang/posts-crud-practice
Commits: https://github.com/youmjjang/posts-crud-practice/commits/main
