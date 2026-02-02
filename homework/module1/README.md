# Data Engineering Zoomcamp 2026 - Module 1 Homework

## Question 1: Understanding Docker images

**Command:**
```bash
docker run -it --entrypoint bash python:3.13
pip --version
```

**Answer:** 24.3.1

---

## Question 2: Understanding Docker networking

Given the docker-compose.yaml, pgadmin should connect using:

**Answer:** db:5432

**Explanation:** Within the Docker network, containers use the service name (`db`) and the internal container port (5432), not the host-mapped port.

---

## Question 3: Counting short trips

**SQL Query:**
```sql
SELECT COUNT(*) as trip_count
FROM green_taxi_data
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
```

**Answer:** 8007

---

## Question 4: Longest trip for each day

**SQL Query:**
```sql
SELECT DATE(lpep_pickup_datetime) as pickup_day,
       MAX(trip_distance) as max_distance
FROM green_taxi_data
WHERE trip_distance < 100
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY max_distance DESC
LIMIT 1;
```

**Answer:** 2025-11-14

---

## Question 5: Biggest pickup zone

**SQL Query:**
```sql
SELECT z."Zone", SUM(g.total_amount) as total
FROM green_taxi_data g
JOIN taxi_zone_lookup z ON g."PULocationID" = z."LocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total DESC
LIMIT 1;
```

**Answer:** East Harlem North

---

## Question 6: Largest tip

**SQL Query:**
```sql
SELECT dropoff_zone."Zone", MAX(g.tip_amount) as max_tip
FROM green_taxi_data g
JOIN taxi_zone_lookup pickup_zone 
  ON g."PULocationID" = pickup_zone."LocationID"
JOIN taxi_zone_lookup dropoff_zone 
  ON g."DOLocationID" = dropoff_zone."LocationID"
WHERE pickup_zone."Zone" = 'East Harlem North'
  AND g.lpep_pickup_datetime >= '2025-11-01'
  AND g.lpep_pickup_datetime < '2025-12-01'
GROUP BY dropoff_zone."Zone"
ORDER BY max_tip DESC
LIMIT 1;
```

**Answer:** Yorkville West

---

## Question 7: Terraform Workflow

**Answer:** terraform init, terraform apply -auto-approve, terraform destroy

**Explanation:**
1. `terraform init` - Downloads provider plugins and sets up backend
2. `terraform apply -auto-approve` - Generates proposed changes and auto-executes the plan
3. `terraform destroy` - Removes all resources managed by terraform

---

## Setup Instructions

### Files in this repository:
- `docker-compose.yaml` - Docker setup for Postgres
- `ingest_data.py` - Script to load parquet and CSV data into Postgres
- `sql_queries.py` - Script to execute SQL queries and get answers
- `.gitignore` - Excludes data files from repository

### How to run:
```bash
# Start Postgres
docker-compose up -d

# Download data
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv

# Install dependencies
pip install pandas sqlalchemy psycopg2-binary pyarrow

# Ingest data
python ingest_data.py

# Run queries to get answers
python sql_queries.py
```
