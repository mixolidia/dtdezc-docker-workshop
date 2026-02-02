import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine('postgresql://postgres:postgres@localhost:5432/ny_taxi')

print("="*60)
print("QUESTION 3: Counting short trips")
print("="*60)
query_3 = """
SELECT COUNT(*) as trip_count
FROM green_taxi_data
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
"""
result_3 = pd.read_sql(query_3, engine)
print(f"Answer: {result_3['trip_count'][0]:,}")
print()

print("="*60)
print("QUESTION 4: Longest trip for each day")
print("="*60)
query_4 = """
SELECT DATE(lpep_pickup_datetime) as pickup_day,
       MAX(trip_distance) as max_distance
FROM green_taxi_data
WHERE trip_distance < 100
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY max_distance DESC
LIMIT 1;
"""
result_4 = pd.read_sql(query_4, engine)
print(f"Answer: {result_4['pickup_day'][0]}")
print(f"Max distance: {result_4['max_distance'][0]:.2f} miles")
print()

print("="*60)
print("QUESTION 5: Biggest pickup zone on Nov 18")
print("="*60)
query_5 = """
SELECT z."Zone", SUM(g.total_amount) as total
FROM green_taxi_data g
JOIN taxi_zone_lookup z ON g."PULocationID" = z."LocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total DESC
LIMIT 5;
"""
result_5 = pd.read_sql(query_5, engine)
print("Top 5 zones:")
print(result_5)
print(f"\nAnswer: {result_5['Zone'][0]}")
print()

print("="*60)
print("QUESTION 6: Largest tip from East Harlem North")
print("="*60)
query_6 = """
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
LIMIT 5;
"""
result_6 = pd.read_sql(query_6, engine)
print("Top 5 dropoff zones by tip:")
print(result_6)
print(f"\nAnswer: {result_6['Zone'][0]}")