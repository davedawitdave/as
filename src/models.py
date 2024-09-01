# src/models.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SurveyData(Base):
    __tablename__ = 'survey_data'
    
    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    survey_date = Column(Date)
    unique_id = Column(String)
    country_name = Column(String)
    region_name = Column(String)
    bda_name = Column(String)
    cohort = Column(String)
    program = Column(String)
    client_name = Column(String)
    client_id_manifest = Column(String)
    location = Column(String)
    phone = Column(String)
    phone_smart_feature = Column(String)
    gender = Column(String)
    age = Column(Integer)
    nationality = Column(String)
    strata = Column(String)
    disability = Column(Boolean)
    education = Column(String)
    client_status = Column(String)
    sole_income_earner = Column(Boolean)
    responsible_people = Column(Integer)
    business_status = Column(String)
    biz_operating = Column(Boolean)
    submission_time = Column(DateTime)
    geolocation = Column(String)  # Can be changed to Geography type if using PostGIS

# Database setup
engine = create_engine('postgresql://username:password@localhost/dbname')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
