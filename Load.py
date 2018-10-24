#!/usr/bin/env python

import csv
from sqlalchemy import create_engine, inspect
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Station(Base):
    __tablename__='station'
    station_id=Column(Integer, primary_key=True)
    name=Column(String(255))
    state=Column(String(255))
    elevation=Column(Float)
    latitude=Column(Float)
    longitude=Column(Float)
    
class Weather(Base):
    __tablename__='weather'
    weather_id=Column(Integer, primary_key=True)
    station_id=Column(Integer)
    precipitation=Column(Float)
    max_temp=Column(Float)
    min_temp=Column(Float)
    mean_temp=Column(Float)
    snowfall=Column(Float)
    date=Column(Integer)
    
class Aircraft(Base):
    __tablename__='aircraft'
    aircraft_id=Column(Integer, primary_key=True)
    aircraft=Column(String(255))
    name=Column(String(255))
    full_name=Column(String(255))
    aircraft_type=Column(String(255))
    hyperlink=Column(String(255))
    
class Weapon(Base):
    __tablename__='weapon'
    weapon_id=Column(Integer, primary_key=True)
    country=Column(String(255))
    name=Column(String(255))
    alt_name=Column(String(255))
    description=Column(String(255))

class Mission(Base):
    __tablename__='mission'
    mission_id=Column(Integer, primary_key=True)
    country=Column(String(255))
    target=Column(String(255))
    latitude=Column(Float)
    longitude=Column(Float)
    aircraft=Column(String(255))
    number_of_he=Column(Float)
    type_of_he=Column(String(255))
    lbs_of_he=Column(Float)
    number_of_ic=Column(Float)
    type_of_ic=Column(String(255))
    lbs_of_ic=Column(Float)
    number_of_frag=Column(Float)
    type_of_frag=Column(String(255))
    lbs_of_frag=Column(Float)
    date=Column(Integer)

engine = create_engine('mysql://group07:KnuUyh4WWRqHDxNY@cwru-data-project02.ciuevunbeloh.us-east-2.rds.amazonaws.com:3306/group07')
con = engine.connect()
session = Session(bind=engine)

Base.metadata.create_all(engine)

#with open('CSV/stations.csv',newline='') as file:
#    reader=csv.reader(file)
#    next(reader)
#    for row in reader:
#        entry=Station(station_id=row[0],name=row[1],state=row[2],elevation=row[3],latitude=row[4],longitude=row[5])
#        session.add(entry)
#        session.commit()

l=0

with open('CSV/weather.csv',newline='') as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        entry=Weather(station_id=row[0],precipitation=row[1],max_temp=row[2],min_temp=row[3],mean_temp=row[4],snowfall=row[5],date=row[6]\
		weather_id=row[7])
		print(entry)
		l=l+1
		if l==5: break
       # session.add(entry)
       #session.commit()

        


# In[ ]:




