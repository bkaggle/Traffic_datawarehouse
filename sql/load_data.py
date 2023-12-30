from sqlalchemy import create_engine
import pandas as pd
from sql.process_data import process_traffic_data
# Update the connection string with your PostgreSQL credentials and database information
engine = create_engine('postgresql://postgres:postgres@localhost:5432/week2')

input_file = '../data/traffic.csv'

df_track, df_trajectory = process_traffic_data(input_file)
# Define your table names and schemas
table1 = 'track'
table2 = 'trajectory'
schema1 = 'timed_vehicle_schema.sql'
schema2 = 'trajectory_schema.sql'

# Write the dataframes to the PostgreSQL database with schemas
df_track.to_sql(name=table1, con=engine, index=False, if_exists='replace', schema=schema1)
df_trajectory.to_sql(name=table2, con=engine, index=False, if_exists='replace', schema=schema2)
