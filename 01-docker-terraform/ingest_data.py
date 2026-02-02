import pandas as pd
from sqlalchemy import create_engine
import pyarrow.parquet as pq

# Database connection
engine = create_engine('postgresql://postgres:postgres@localhost:5432/ny_taxi')

# Load parquet file
print("Loading green taxi data...")
df_green = pd.read_parquet('green_tripdata_2025-11.parquet')

# Load to database
print("Inserting green taxi data into database...")
df_green.to_sql('green_taxi_data', engine, if_exists='replace', index=False, chunksize=10000)
print(f"Inserted {len(df_green)} rows into green_taxi_data table")

# Load zone lookup
print("Loading zone lookup data...")
df_zones = pd.read_csv('taxi_zone_lookup.csv')

print("Inserting zone data into database...")
df_zones.to_sql('taxi_zone_lookup', engine, if_exists='replace', index=False)
print(f"Inserted {len(df_zones)} rows into taxi_zone_lookup table")

print("Data ingestion complete!")