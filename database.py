from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os


load_dotenv()
connection_string=os.getenv('DB_CONNECTION_STRING')
engine = create_engine(connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    # Execute the query and store the result in a variable
    result = conn.execute(text("select * from jobs"))
    
    result_all=result.all()
    #print(type(result.all()))
    #result.all() is of type list
    jobs = []
    
    # Iterate over each row
    for row in result_all:
      # Convert each row to a dictionary using the _mapping attribute
      row_dict = dict(row._mapping)
      jobs.append(row_dict)
    return jobs

