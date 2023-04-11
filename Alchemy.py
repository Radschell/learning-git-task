from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# create an engine to connect to the database
engine = create_engine('sqlite:///mydatabase.db')

# create a base class for declarative models
Base = declarative_base()

# define the clean_stations table
class CleanStations(Base):
    __tablename__ = 'clean_stations'
    station = Column(String, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    name = Column(String)
    country = Column(String)
    state = Column(String)
    clean_measure = relationship('CleanMeasure', backref='clean_stations')

# define the clean_measure table
class CleanMeasure(Base):
    __tablename__ = 'clean_measure'
    station = Column(String, ForeignKey('clean_stations.station'), primary_key=True)
    date = Column(String, primary_key=True)
    precip = Column(Float)
    tobs = Column(Float)

# create the tables in the database
Base.metadata.create_all(engine)

import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module import CleanStation

# create an engine to connect to the database
engine = create_engine('sqlite:///mydatabase.db')

# create a session maker
Session = sessionmaker(bind=engine)
session = Session()

# specify the path to the CSV file
csv_file_path = '/C:/Users/HOME/Desktop/Kodilla/learning-git-task/clean_stations.csv'

with open(csv_file_path, 'r') as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        # create a new instance of CleanStation for each row of data
        station = CleanStation(station=row[0], latitude=float(row[1]), longitude=float(row[2]), 
                               elevation=float(row[3]), name=row[4], country=row[5], state=row[6])
        session.add(station)

# commit the changes and close the session
session.commit()
session.close()

import sqlite3

def get_stations_data(sql_statement):
    # create a connection to the database
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # execute the SQL statement and retrieve the data
    cursor.execute(sql_statement)
    data = cursor.fetchall()

    # close the connection and return the data
    conn.close()
    return data
