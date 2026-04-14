## 🛒 Amazon Sales ETL Pipeline 
An end-to-end ETL pipeline built using Python, Pandas, and SQL Server to extract, transform, and load Amazon sales data into a structured database
for analytics and visualization.

## 📌 Overview
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline:

- Load Raw CSV Data to SQL Server (staging layer).
- Extracts raw CSV data from SQL Server.
- Transforms and cleans using Pandas.
- Loads structured data into SQL Server (final table).
- Ready for Power BI visualization.

## 🏗️ Architecture

CSV Files → SQL Server (Raw Tables) → Python (Pandas Processing) → SQL Server (Clean Tables) → Power BI

## 📂 Project Structure

```bash
Sales_Pipeline/
│── Data/                    
│   │── DataLoadToSql.py 
│   │── Setup.py 
│   │── Amazon_RawData.csv 
│── src/                      
│   │── Extract.py           
│   │── Transform.py         
│   │── load.py               
│       # Handles database insertion logic
│
│── Main_Pipeline.py         
│── config.py                
│── .env                     
│── .gitignore                
│── README.md
```
## 🔄 ETL Workflow

- **Initial Load (CSV → SQL Server):**  
  Raw CSV data is inserted into SQL Server (staging/raw tables)

- **Extract:**  
  Data is extracted from SQL Server into Python using SQLAlchemy

- **Transform:**  
  Data cleaning (handling nulls, formatting, type conversion)  
  Data normalization and structuring

- **Load:**  
  Cleaned data is loaded back into SQL Server (final tables)
