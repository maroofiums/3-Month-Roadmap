## Month 3: ML + System Design + Integrated Projects  
**Duration:** 18 Jan – 14 Feb 2026  

### 🎯 Overall Goal
Build a strong foundation in **Machine Learning**, learn **production-level API integration**, understand **system design basics**, and finally design a **custom async backend framework prototype (Velox)**.

This month focuses on **thinking like a backend + ML engineer**, not just writing isolated code.

---

## Week 9 (18 Jan – 24 Jan) → ML Basics

**Goal:**  
Learn how ML models are trained, how data is prepared, and how features affect model performance.  
This week builds the **ML foundation** for future APIs.

| Day | Focus | Tasks / Mini Project |
|---|---|---|
| Mon | NumPy Basics | Arrays, slicing, reshaping, broadcasting |
| Tue | Pandas Basics | DataFrames, reading CSV/Excel, missing values |
| Wed | Feature Engineering | Scaling, encoding categorical variables |
| Thu | Logistic Regression | Train/test split, model fitting, evaluation |
| Fri | Decision Tree | Train model, visualize tree, interpret results |
| Sat | KNN | Distance metrics, choosing `k`, evaluation |
| Sun | Mini ML Project | Train on Titanic or Iris dataset, save model using `joblib` |

**Tip:**  
Keep datasets **small and simple**. Focus on *why* preprocessing and features matter more than accuracy.

---

## Week 10 (25 Jan – 31 Jan) → ML API Integration

**Goal:**  
Expose trained ML models through **async APIs**, and make them more **production-ready** using caching and testing.

| Day | Focus | Tasks / Mini Project |
|---|---|---|
| Mon | FastAPI Basics | Setup project, create first API endpoint |
| Tue | Serve ML Model | Load `joblib` model, create `/predict` endpoint |
| Wed | Async Endpoints | Convert routes to `async def`, understand async flow |
| Thu | Redis Caching | Cache repeated prediction requests |
| Fri | API Testing | Test using Postman / curl, handle errors |
| Sat | Mini Project | ML Prediction API with async + Redis caching |
| Sun | Documentation | Write README, endpoint docs, usage examples |

**Tip:**  
Think of **async + caching** as optimization layers that turn a basic ML script into a real backend service.

---

## Week 11 (1 Feb – 7 Feb) → System Design Lite

**Goal:**  
Understand how scalable systems are designed and how backend components work together.

| Day | Focus | Tasks / Mini Project |
|---|---|---|
| Mon | Database Indexing | B-Tree vs Hash index, when to use indexing |
| Tue | Sharding Basics | Horizontal vs vertical sharding concepts |
| Wed | Queue Basics | Redis Queue or RabbitMQ (async processing) |
| Thu | Rate Limiting | Implement per-user request limit |
| Fri | URL Shortener | DB design, indexes, optional queue |
| Sat | Notification System | Async notifications using queue |
| Sun | System Design Diagrams | Draw architecture diagrams for GitHub |

**Tip:**  
Simple **diagrams + small working prototype** are more valuable than over-engineered systems.

---

## Week 12 (8 Feb – 14 Feb) → Velox Framework Prep

**Goal:**  
Design and implement the **first working prototype** of a custom async backend framework (**Velox**) using Sanic + SQLModel.

Velox is not meant to replace FastAPI — it demonstrates **framework-level thinking**.

| Day | Focus |
|---|---|
| Day 1 | Framework vision + Sanic core |
| Day 2 | Routing system (basic hello route) |
| Day 3 | SQLModel integration + builtin SQLite DB |
| Day 4 | Framework config + app factory pattern |
| Day 5 | CLI tool (`velox makeproject app`) |
| Day 6 | CLI polish + `velox run` command |
| Day 7 | Cleanup, README, diagrams, public GitHub release |

**Tip:**  
Velox does **not need to be complete**.  
A minimal, working framework with CLI + DB + routing is more impressive than a half-finished big idea.

---

## 📌 Monthly Summary

1. **Week 9:** ML foundations — data, features, models  
2. **Week 10:** ML → async APIs with caching  
3. **Week 11:** System design fundamentals + mini systems  
4. **Week 12:** Integration week + Velox framework prototype  

---
