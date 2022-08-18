from google.cloud import bigquery as bq
import os
import glob

# Specify environments
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = glob.glob("*.json")[0]
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'hannstar-first-3467ba8870b5.json'

project_id = 'hannstar-first'   # uplowcase sensitive
client = bq.Client(project=project_id)
print(client)

# SQL language
sql = client.query('''
  SELECT 
    year
  FROM 
    `bigquery-public-data.noaa_gsod.gsod1929`
  LIMIT
    10
    ''')

# Output result
for row in sql.result():
    print(row)

