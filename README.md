# URL Shortener

## Milestones
- [ ] Milestone 1 — Hello server\
    Get a FastAPI server running locally with one endpoint: `GET /health` that returns `{"status": "ok"}`. That's it. You're done when you can hit it in your browser or curl and see the response.
- [ ] Milestone 2 — Shorten a URL (no DB yet)\
    Add `POST /shorten` that accepts a long URL and returns a fake short code (hardcode it, store it in a Python dictionary for now). Add `GET /{code}` that looks up the dictionary and returns the long URL. Test it with curl. No database yet — just prove the logic works.
- [ ] Milestone 3 — Add PostgreSQL\
  Replace the dictionary with a real database. You'll need to design your table (hint: look at what data you actually need to store). Use SQLAlchemy or just raw psycopg2 — your choice. Write your own Base62 encoder — look up how Base62 works and implement it yourself, don't copy one.
- [ ] Milestone 4 — Add Redis caching\
  Add Redis to your redirect flow. Check Redis first on every `GET /{code}` request. Only hit the database on a cache miss, then store the result in Redis. Add a TTL. Ask yourself: what TTL makes sense and why?


### Milestone 1 
#### TASK 1.1 : Understanding Concepts
- [ ] Redis
  - [ ] [Redis](https://www.youtube.com/watch?v=G1rOthIU-uo) 100 seconds
  - [ ] [Redis Crash course](https://www.youtube.com/watch?v=jgpVdJB2sKQ)
- [ ] Web Based
  - [ ] [FastAPI](https://www.youtube.com/watch?v=0sOvCWFmrtA) tutorial
  - [ ] HTTP status code understanding ([doc](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status))
- [ ] [Docker in 100 seconds](https://www.youtube.com/watch?v=Gjnup-PuquQ) : `docker run -d -p 6379:6379 redis` to get redis running

#### TASK 1.2 : FastAPI setup
- [ ] Run FastAPI with just a single endpoint `GET /health` > `{"status": "ok"}`
- [ ] Try to view it from the browser, or curl and see the response