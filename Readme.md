# Repository Contents

### 1. Extract_and_Transform : Reads raw CSV files and cleans data. Saves clean dataframes as new CSV
### 2. Load : Uses SQLAlchemy to load clean dataframes into MySQL database.
### 3. Reset : Drops all tables in remote database, to avoid errors when re-running Load
### 4. Test : Retrieves tables from MySQL server to test that they're correct
### 5. Project_Report : Word document describing ETL process
### 6. WW2_Missions : Folder containing raw THOR data
### 7. Weather : Folder containing raw NCEI weather data
### 8. CSV : Folders containing cleaned CSV files as intermediary step to database export
