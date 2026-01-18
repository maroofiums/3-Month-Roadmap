
## **Month 3: ML + System Design + Integrated Projects (18 Jan – 22 Feb 2026)**

---

### **Week 9 (18 Jan – 24 Jan) → ML Basics**

**Goal:** Train small ML models, prep data, understand feature engineering

| Day | Focus               | Tasks / Mini Project                                 | Tips                                            |
| --- | ------------------- | ---------------------------------------------------- | ----------------------------------------------- |
| Mon | Numpy basics        | Arrays, slicing, reshaping, broadcasting             | Practice with small arrays to understand shapes |
| Tue | Pandas basics       | DataFrames, reading CSV/Excel, missing values        | Try cleaning Titanic dataset                    |
| Wed | Feature Engineering | Scaling, encoding categorical variables              | Use `StandardScaler`, `LabelEncoder`            |
| Thu | Logistic Regression | Train/test split, model fitting, evaluation          | Use sklearn, track accuracy & confusion matrix  |
| Fri | Decision Tree       | Visualize tree, interpret results                    | Focus on overfitting vs underfitting            |
| Sat | KNN                 | Distance metrics, neighbor selection                 | Try on small datasets (Iris)                    |
| Sun | Mini ML Project     | Train a model on Titanic or Iris, save with `joblib` | This model will later be served in Week 10      |

**Tip:** Keep datasets small, focus on **learning how to prepare data and train models**. This is your foundation for APIs.

---

### **Week 10 (25 Jan – 31 Jan) → ML API Integration**

**Goal:** Serve ML models via FastAPI, async, and caching

| Day | Focus           | Tasks / Mini Project                                   | Tips                                         |
| --- | --------------- | ------------------------------------------------------ | -------------------------------------------- |
| Mon | FastAPI Basics  | Setup FastAPI project, create first endpoint           | Use uvicorn to run locally                   |
| Tue | Serve ML Model  | Load `joblib` model, create `/predict` endpoint        | Input validation is key                      |
| Wed | Async Endpoints | Use `async def` in routes                              | Improves response time for multiple requests |
| Thu | Redis Caching   | Cache repeated predictions                             | Use `redis-py`, set expiry time (ex=60s)     |
| Fri | Test API        | Postman / curl tests, handle errors                    | Make robust input checking                   |
| Sat | Mini Project    | ML Prediction API (Titanic or Iris) with async + cache | Push code to GitHub                          |
| Sun | Docs & README   | Document endpoints, add usage example                  | Visual diagrams for request flow             |

**Tip:** Treat caching & async as **optimization layers**; they make your ML API “production-ready”.

---

### **Week 11 (1 Feb – 7 Feb) → System Design Lite**

**Goal:** Understand how to design scalable APIs and databases

| Day | Focus                  | Tasks / Mini Project                 | Tips                                        |
| --- | ---------------------- | ------------------------------------ | ------------------------------------------- |
| Mon | DB Indexing            | Learn B-Tree, Hash index             | Index primary and frequently queried fields |
| Tue | Sharding Basics        | Horizontal vs vertical sharding      | Use diagrams to visualize                   |
| Wed | Queue Basics           | Redis Queue or RabbitMQ              | Simple producer-consumer example            |
| Thu | Rate Limiter           | Implement per-user request limit     | Use Redis for tracking requests             |
| Fri | URL Shortener Project  | DB design + index + queue (optional) | Focus on minimal, working system            |
| Sat | Notification System    | Async delivery using queues          | Test with multiple requests                 |
| Sun | System Design Diagrams | Draw architecture for GitHub         | Show DB, API, caching, queue                |

**Tip:** Diagrams + simple working prototype > perfect system. Keep it lightweight.

---

### **Week 12 (8 Feb – 22 Feb) → Integrated Projects + Velox Prep**

**Goal:** Combine ML, async backend, caching, and system design; start Velox planning

| Day | Focus                    | Tasks / Mini Project                                      | Tips                                     |
| --- | ------------------------ | --------------------------------------------------------- | ---------------------------------------- |
| Mon | ML API + Async + Cache   | Integrate Week 10 model into backend with async endpoints | Ensure caching works with repeated calls |
| Tue | Backend Project          | Todo or User Management with async, middleware, DB, Redis | Use modular code structure               |
| Wed | Backend + ML Integration | Call ML API from backend project                          | Test end-to-end flow                     |
| Thu | Velox Prep               | Define routing & middleware design                        | Think modular + easy to extend           |
| Fri | Velox ORM + DB           | Simple CRUD operations with async                         | Use SQLite or Postgres for now           |
| Sat | Velox + Async Routing    | Combine routing + ORM + middleware                        | Test with small demo project             |
| Sun | Final Project Push       | Push all projects to GitHub with README + diagrams        | Include flow diagrams and explanations   |

**Tip:** Week 12 is **all about integration**. Velox doesn’t need to be complete—just a working minimal framework that demonstrates your concept.

---

### **Summary Week by Week**

1. **Week 9:** Solid ML basics, train & save models
2. **Week 10:** ML → FastAPI, async endpoints, caching
3. **Week 11:** System design concepts, DB optimization, queues, rate limiting, mini projects
4. **Week 12:** Integrate everything; start Velox mini framework; push polished projects to GitHub
