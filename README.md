# README.md
# Agriculture Education Platform

## Overview
This project is a microservice-based agriculture education platform built with FastAPI (backend) and Vue3 (frontend). It provides user authentication, course listing, and real‑time Q&A chat.

## Backend
- **Framework**: FastAPI
- **Auth**: OAuth2 with JWT
- **WebSocket**: Real‑time Q&A
- **Database**: In‑memory (placeholder for PostgreSQL)

## Frontend
- **Framework**: Vue3
- **Components**: CourseList, QnAChat

## Running
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```
