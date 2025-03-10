from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

load_dotenv()
connection_string=os.getenv('DB_CONNECTION_STRING')


db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

timeout = 10

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")



def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all=result.all()
    #print(type(result.all()))
    #result.all() is of type list
    jobs = []
    for row in result_all:
      # Convert each row to a dictionary using the _mapping attribute
      row_dict = dict(row._mapping)
      jobs.append(row_dict)
    return jobs



def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
       text(f"SELECT * FROM jobs WHERE id={id}")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return row
 

 
Session = sessionmaker(bind=engine)
session = Session()
def add_application_to_db(job_id, data):
    try:
        query = text("""
            INSERT INTO applications (
                job_id,
                full_name,
                email,
                linkedin_url,
                education,
                work_experience,
                resume_url
            ) VALUES (
                :job_id,
                :full_name,
                :email,
                :linkedin_url,
                :education,
                :work_experience,
                :resume_url
            )
        """)
        session.execute(query, {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],  # Corrected key
            'resume_url': data['resume_url']
        })
        session.commit()
        print("Data committed successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()
