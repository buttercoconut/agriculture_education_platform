# Agriculture Education Platform

## Project Structure

```
agriculture_education_platform/
├── backend/
│   ├── api/
│   │   ├── user.py
│   │   ├── course.py
│   │   └── community.py
│   ├── models/
│   │   ├── user.py
│   │   ├── course.py
│   │   └── community.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── course_service.py
│   │   └── community_service.py
│   ├── main.py
│   └── README.md
├── frontend/
│   ├── components/
│   │   ├── CourseList.vue
│   │   └── QAChat.vue
│   ├── views/
│   │   ├── Home.vue
│   │   ├── Course.vue
│   │   └── QA.vue
│   ├── App.vue
│   ├── main.js
│   ├── router.js
│   └── README.md
└── README.md
```

## Running the Backend

```bash
cd backend
uvicorn main:app --reload
```

## Running the Frontend

```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

- `POST /users/token` – 로그인
- `POST /users/register` – 회원가입
- `GET /users/me` – 현재 사용자 정보
- `GET /courses/` – 모든 코스 목록
- `POST /courses/` – 코스 생성
- `GET /courses/{id}` – 코스 상세
- `GET /community/posts` – 커뮤니티 포스트 목록
- `POST /community/posts` – 커뮤니티 포스트 생성

## Notes

- 현재는 인메모리 저장소를 사용하고 있으므로 재시작 시 데이터가 사라집니다.
- 실제 운영 환경에서는 PostgreSQL, Redis, RabbitMQ 등으로 교체해야 합니다.

---

This repository is a minimal prototype for the Agriculture Education Platform.
