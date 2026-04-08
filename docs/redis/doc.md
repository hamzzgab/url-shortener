# Redis Notes

## Overview

**Redis** (Remote Dictionary Server) is an in-memory key-value store known for its extremely fast reads and writes. It supports multiple data types — strings, lists, sets, hashes, streams, and more — making it a versatile multi-model store.

It is primarily used as a **cache** rather than a primary data store, often sitting in front of a database like PostgreSQL. It's ideal for data that doesn't change frequently, where repeated cache hits significantly improve performance.

> By default, Redis is **volatile** (non-persistent). Persistence must be explicitly configured.

---

## Installation (macOS)

```bash
brew install redis
```

---

## Core Commands

### Basic Key Operations

```bash
SET age 25        # Store a code
GET age           # → "25"
DEL age           # → (integer) 1
EXISTS name       # → (integer) 1 if key exists
KEYS *            # List all keys
FLUSHALL          # Delete everything
```

### Expiry / TTL

```bash
TTL name             # Check remaining TTL (-1 = no expiry, -2 = key gone)
EXPIRE name 10       # Set expiry of 10 seconds on existing key
SETEX name 10 hamza  # Set key with code AND expiry in one command
```

---

## Data Types

### Strings
The default type. Used with `SET` / `GET` / `SETEX` as shown above.

---

### Lists
Ordered, allow duplicates. Support push/pop from both ends.

```bash
LPUSH friends hamza       # Push to the left (front)
RPUSH friends ali         # Push to the right (back)
LRANGE friends 0 -1       # Get all elements → 1) "hamza" 2) "ali"
LPOP friends              # Remove & return from the left
RPOP friends              # Remove & return from the right
```

---

### Sets
Unordered, **no duplicates**.

```bash
SADD hobbies "guitar"     # Add member
SMEMBERS hobbies          # List all members
SREM hobbies "guitar"     # Remove member
```

---

### Hashes
Key-value pairs nested under a single key — like a mini object/record.

```bash
HSET person name kyle     # Set a field
HGET person name          # → "kyle"
HGETALL person            # Get all fields and values
HSET person age 26        # Add another field
HDEL person age           # Delete a field
HEXISTS person name       # → 1 if field exists, 0 if not
```

---

## Quick Reference Summary

| Command       | Description                          |
|---------------|--------------------------------------|
| `SET` / `GET` | Store and retrieve a string value    |
| `DEL`         | Delete a key                         |
| `EXISTS`      | Check if a key exists                |
| `EXPIRE`      | Set a TTL on a key                   |
| `SETEX`       | Set key with value and TTL at once   |
| `TTL`         | Check remaining time on a key        |
| `LPUSH/RPUSH` | Add to front/back of a list          |
| `LRANGE`      | Read a range of list elements        |
| `SADD`        | Add to a set                         |
| `SMEMBERS`    | List all set members                 |
| `HSET/HGET`   | Set/get a field in a hash            |
| `HGETALL`     | Get all fields and values in a hash  |
| `FLUSHALL`    | Wipe the entire Redis store          |