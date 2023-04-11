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
