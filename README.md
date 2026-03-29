# URL Shortener

A simple URL shortener project built step-by-step with FastAPI, PostgreSQL, and Redis.  
This roadmap guides you through each milestone, from a basic health check endpoint to a fully cached redirect flow.

---

## 🚀 Milestones

### **Milestone 1 — Hello Server**
- [ ] Start a FastAPI server locally  
- [ ] Implement `GET /health` → returns `{ "status": "ok" }`  
- [ ] Verify via browser or `curl`

---

### **Milestone 2 — Shorten a URL (No DB Yet)**
- [ ] Add `POST /shorten`  
  - Accepts a long URL  
  - Returns a **fake short code** (hard-coded for now)  
  - Store mappings in an in-memory Python dictionary  
- [ ] Add `GET /{code}`  
  - Looks up the code in the dictionary  
  - Returns the long URL  
- [ ] Test both endpoints with `curl`

---

### **Milestone 3 — Add PostgreSQL**
- [ ] Replace the dictionary with a PostgreSQL database  
- [ ] Design a minimal table (e.g., `id`, `short_code`, `long_url`, timestamps)  
- [ ] Use SQLAlchemy or raw `psycopg2`  
- [ ] Write your own **Base62 encoder** (do not copy from libraries)  
- [ ] Store and fetch URL mappings from the DB

---

### **Milestone 4 — Add Redis Caching**
- [ ] Integrate Redis into the `GET /{code}` lookup process  
- [ ] On each request:
  1. Check Redis first  
  2. If **hit**, return the stored long URL  
  3. If **miss**, query the DB and write the result back to Redis  
- [ ] Add a TTL for cache entries and justify your choice

---

## 🧠 Milestone 1 Tasks

### **TASK 1.1 — Understand the Concepts**

#### Redis
- [ ] [Redis in 100 Seconds](https://www.youtube.com/watch?v=G1rOthIU-uo)  
- [ ] [Redis Crash Course](https://www.youtube.com/watch?v=jgpVdJB2sKQ)

#### Web Backend
- [ ] [FastAPI Tutorial](https://www.youtube.com/watch?v=0sOvCWFmrtA)  
- [ ] Read HTTP status codes:  
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status

#### Docker
- [ ] [Docker in 100 Seconds](https://www.youtube.com/watch?v=Gjnup-PuquQ)  
- [ ] Run Redis locally:  
  ```bash
  docker run -d -p 6379:6379 redis