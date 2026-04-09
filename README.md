# URL Shortener

A simple URL shortener project built step-by-step with FastAPI, PostgreSQL, and Redis.  
This roadmap guides you through each milestone, from a basic health check endpoint to a fully cached redirect flow.

---

## 🚀 Milestones

### **Milestone 1 — Hello Server**

- [X] Start a FastAPI server locally
- [X] Implement `GET /health` → returns `{ "status": "ok" }`
- [X] Verify via browser or `curl`

---

### **Milestone 2 — Shorten a URL (No DB Yet)**

- [X] Add `POST /shorten`
    - Accepts a long URL
    - Returns a **fake short code** (hard-coded for now)
    - Store mappings in an in-memory Python dictionary
- [X] Add `GET /{code}`
    - Looks up the code in the dictionary
    - Returns the long URL
- [X] Test both endpoints with `curl`

---

### **Milestone 3 — Add PostgreSQL**

- [X] Replace the dictionary with a PostgreSQL database
- [X] Design a minimal table (e.g., `id`, `short_code`, `long_url`, timestamps)
- [X] Use SQLAlchemy or raw `psycopg2`
- [X] Write your own **Base62 encoder** (do not copy from libraries)
- [X] Store and fetch URL mappings from the DB

---

### **Milestone 4 — Add Redis Caching**

- [X] Integrate Redis into the `GET /{code}` lookup process
- [X] On each request:
    1. Check Redis first
    2. If **hit**, return the stored long URL
    3. If **miss**, query the DB and write the result back to Redis
- [X] Add a TTL for cache entries and justify your choice

---

## 🧠 Milestone 1 Tasks

### **TASK 1.1 — Understand the Concepts**

#### Redis

- [X] [Redis in 100 Seconds](https://www.youtube.com/watch?v=G1rOthIU-uo)
- [X] [Redis Crash Course](https://www.youtube.com/watch?v=jgpVdJB2sKQ)

#### Web Backend

- [ ] [FastAPI Tutorial](https://www.youtube.com/watch?v=0sOvCWFmrtA)
- [ ] Read HTTP status codes:  
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status

#### Docker

- [ ] [Docker in 100 Seconds](https://www.youtube.com/watch?v=Gjnup-PuquQ)
- [ ] Run Redis locally:
  ```bash
  docker run -d -p 6379:6379 redis

## **TASK 1.2 — FastAPI Setup**

- [ ] Create a minimal FastAPI app
- [ ] Implement:
    ```python 
  GET /health → {"status": "ok"}

- [ ]Test in browser or using:
```bash
curl http://localhost:8000/health