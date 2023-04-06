-- settings.sql
CREATE DATABASE garden;
CREATE USER gardenuser WITH PASSWORD 'garden';
GRANT ALL PRIVILEGES ON DATABASE garden TO gardenuser;