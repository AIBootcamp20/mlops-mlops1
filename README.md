[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/xoFPmgXs)
## 👨‍🏫 프로젝트 소개
## TMDB 데이터를 활용한 영화 평점 예측 서비스 & MLOps Flow 이해하기 <br> <br>
## Team
<table>
  <tr>
    <td> <div align=center> 👑 </div> </td>
    <td> <div align=center> 🙍 </div> </td>
    <td> <div align=center> 🙍 </div> </td>
    <td> <div align=center> 🙍 </div> </td>
  </tr>
  <tr>
    <td> <div align=center> <b>이진성</b> </div> </td>
    <td> <div align=center> <b>고아연</b> </div> </td>
    <td> <div align=center> <b>윤소정</b> </div> </td>
    <td> <div align=center> <b>한혜숙</b> </div> </td>
  </tr>
  <tr>
    <td> <div align=center> <img width="1024" height="1024" alt="Image" src="https://github.com/user-attachments/assets/0630c3b4-e9e8-40e9-8909-650aa91ca71e" /> </td> <!--이진성-->
    <td> <div align=center> <img width="1024" height="1024" alt="Image" src="https://github.com/user-attachments/assets/1f42b6d4-7d84-453b-ac51-e5439f420303" /> </td> <!--고아연-->
    <td> <div align=center> <img width="1024" height="1024" alt="Image" src="https://github.com/user-attachments/assets/749df542-8d79-4512-abe5-c98abb13b31f" /> </td> <!--윤소정-->
    <td> <div align=center> <img width="1024" height="1024" alt="Image" src="https://github.com/user-attachments/assets/f0ffe120-6645-4ff5-8de0-329a624906b5" /> </td> <!--한혜숙-->
  </tr>
  <tr>
    <td> <div align=center> <a href="https://github.com/wlstjd6524"> <img alt="Github" src ="https://img.shields.io/badge/Github-181717.svg?&style=plastic&logo=Github&logoColor=white"/> </a> </div> </td>
    <td> <div align=center> <a href="https://github.com/ayoun88"> <img alt="Github" src ="https://img.shields.io/badge/Github-181717.svg?&style=plastic&logo=Github&logoColor=white"/> </a> </div> </td>
    <td> <div align=center> <a href="https://github.com/Lucia128"> <img alt="Github" src ="https://img.shields.io/badge/Github-181717.svg?&style=plastic&logo=Github&logoColor=white"/> </a> </div> </td>
    <td> <div align=center> <a href="https://github.com/lxlfoo"> <img alt="Github" src ="https://img.shields.io/badge/Github-181717.svg?&style=plastic&logo=Github&logoColor=white"/> </a> </div> </td>
    </tr>
</table>

## 💻 개발환경 및 도구
- Python 3.10.0
- Pytonn Library
  - Pandas
  - Scikit-learn
  - LightGBM 
- Amazon S3 (Simple Storage Service)
- Amazon Web Service (AWS) EC2
- Apache Airflow
- Docker
- FastAPI


## 📏 프로젝트 목적
MLOps PipeLine 구조와 TMDB 데이터를 활용한 영화 평점 예측 시스템 프로젝트 입니다.

TMDB (The Movies DataBase) 데이터를 기반으로 앞으로 개봉할 새로운 영화에 대한 평점을 예측하여 반환하여 사용자에게 해당 결과를 제공하는 것을 목표로 설정했습니다.

## 📁 프로젝트 구조
```text
mlops/
├─ airflow_pipeline/
│  ├─ airflow/
│  │  ├─ dags/
│  │  │  └─ model_train_dag.py
│  │  │     # 모델 학습 · 평가 · S3 저장을 담당하는 메인 DAG
│  │  │
│  │  ├─ logs/
│  │  │  ├─ dag_id=model_training/
│  │  │  │  └─ run_id=manual__2025-12-30T08_03_08.073557+00_00/
│  │  │  │     # DAG 실행 이력 (모델 학습 버전 관리 및 추적 목적)
│  │  │  │
│  │  │  ├─ dag_processor_manager/
│  │  │  │  └─ dag_processor_manager.txt
│  │  │  │
│  │  │  └─ scheduler/
│  │  │     ├─ 2025-12-30/
│  │  │     │  └─ model_train_dag.py
│  │  │     └─ latest/
│  │  │        └─ model_train_dag.py
│  │  │
│  │  ├─ plugins/            # (확장 대비용, 현재는 비어 있음)
│  │  ├─ src/                # (Airflow 내부 로직 확장 대비 디렉토리)
│  │  ├─ .env
│  │  ├─ .env.common
│  │  ├─ Dockerfile
│  │  ├─ entrypoint
│  │  ├─ env.common.template
│  │  └─ requirements-airflow.txt
│  │
│  ├─ train/
│  │  ├─ src/
│  │  │  └─ model/
│  │  │     ├─ data_loader.py
│  │  │     ├─ features.py
│  │  │     ├─ train_model.py
│  │  │     ├─ evaluate.py
│  │  │     ├─ save.py
│  │  │     ├─ train_orchestration.py
│  │  │     ├─ utils.py
│  │  │     ├─ main.py
│  │  │     └─ __init__.py
│  │  │     # 실제 모델 학습 · 평가 · S3 저장 로직
│  │  │
│  │  ├─ Dockerfile
│  │  └─ requirements-train.txt
│  │
│  └─ webserver_config.py
│     # Airflow 웹서버 설정
│
├─ data-prepare/
│  ├─ dags/
│  │  └─ collector_dag.py
│  │  │  # 데이터 수집 및 전처리 파이프라인 DAG
│  │  │
│  ├─ data_prepare/
│  │  ├─ collector.py
│  │  ├─ preprocessor.py
│  │  ├─ load_test.py
│  │  └─ main.py
│  │
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ .env.template
│
├─ modeling/
│  ├─ src/
│  │  └─ ...                # train/src/model 구조와 동일 (실험용)
│  │
│  ├─ Dockerfile
│  ├─ docker-compose.yml
│  ├─ requirements.txt
│  ├─ run_experiment.py
│  ├─ .dockerignore
│  └─ .gitignore
│
└─ serving/
   ├─ app/
   │  ├─ main.py
   │  ├─ model_service.py
   │  ├─ s3_io.py
   │  ├─ schemas.py
   │  └─ templates/
   │     └─ results.html
   │     # FastAPI 기반 모델 서빙 애플리케이션
   │
   ├─ models/
   │  ├─ metadata.json
   │  ├─ metrics.json
   │  └─ model_bundle.joblib
   │  # S3에서 동기화된 최신 모델 번들
   │
   ├─ Dockerfile
   ├─ docker-compose.yml
   ├─ requirements.txt
   └─ .env
```

## 🔨 프로젝트 시스템 아키텍처

## ✍ 구현 기능
### 1. 데이터 자동 수집 과 전처리

### 2. TMDB Data 를 기반으로 한 추천 모델
- 선정모델 : LightGBM
- 모델 선정 이유 :
- 모델 학습 구조 :
- 평가 지표 :

### 3. AutomatedPipeLine

### 4. 모델 서빙

## 🚨 문제 및 인사이트 도출
### 1. Team MLOps Flow 의 잘못된 파악으로 역할군 정의 지연 문제

### 2. 모델링 저장 확장자 관련 규칙 정의 문제

### 3. FastAPI 입력데이터 Load 방식 문제

### 4. 추론 Predict 값이 비정상적으로 튀는 문제

## 🔎 프로젝트 한계 및 개선사항

## 📍 회고
👑 이진성 : 

🙍 고아연 : 

🙍 윤소정 : 

🙍 한혜숙 : 

## 🌐 기술스택
[Fast API] : https://fastapi.tiangolo.com/ko/tutorial/first-steps/
