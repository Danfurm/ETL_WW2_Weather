# Files Explanation

### 1. Extract_and_Transform : Reads raw CSV files and cleans data. Save clean dataframes as new CSV
### 2. Load : Uses SQLAlchemy to load clean dataframes into MySQL database.
### 3. Reset : Drops all tables in remote database, to avoid errors when re-running Load
### 4. Test : Retrieves tables from MySQL server to test that they're correct
