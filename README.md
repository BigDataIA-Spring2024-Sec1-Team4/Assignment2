
## Project Title
Development of a Structured Database and Text Extraction System for Finance Professional Development Resources
 

 





## Problem Statement

The project aims to organize and streamline access to finance professional development resources. It involves compiling 224 refresher readings and topic outlines from the CFA Institute into two key datasets. These datasets will serve as tools for improving the skills of finance professionals. The end objective is to build an intelligent application that utilizes these datasets to offer personalized learning experiences for finance professionals.
## Project Goals

### 1. Web Scraping and Dataset Creation

- **Objective:** Extract information from the provided webpage starting with CFA Institute’s website.
- **Tools:** Utilize web scraping tools such as Beautiful Soup or Scrapy.
- **Output:** Structure the extracted data into a CSV file with the following schema: 
  `{Name of the topic, Year, Level, Introduction Summary, Learning Outcomes, Link to the Summary Page, Link to the PDF File}`.

### 2. PDF Extraction

- **Objective:** Extract text from the provided PDF files (Topic outlines).
- **Tools:** Use PyPDF2 and Grobid for text extraction.
- **Output:** Organize extracted text into text files following the naming convention:
  - `Grobid_RR_{Year}_{Level}_combined.txt`
  - `PyPDF_RR_{Year}_{Level}_combined.txt`


### 3. Database Upload

- **Objective:** Upload structured data from step 1 into a Snowflake database.
- **Tools:** Utilize SQLAlchemy for database interaction.


### 4. Cloud Storage Integration

- **Objective:** Upload structured data (CSV) and extracted text files (from both Grobid and PyPDF) into an AWS S3 bucket.
- **Tools:** Write a Python function for uploading data to AWS S3 bucket. Utilize SQLAlchemy to upload structured metadata (Grobid) into a Snowflake database.

## Technologies Used

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Snowflake](https://img.shields.io/badge/Snowflake-387BC3?style=for-the-badge&logo=snowflake&logoColor=light)](https://www.snowflake.com/)
[![Amazon S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)](https://aws.amazon.com/s3/)
[![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-59666C?style=for-the-badge&logo=python&logoColor=blue)](https://www.crummy.com/software/BeautifulSoup/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Grobid](https://img.shields.io/badge/Grobid-007396?style=for-the-badge&logo=java&logoColor=white)](https://github.com/kermitt2/grobid)
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)](https://airflow.apache.org/)




## Data Source

1. CFA Institute’s website . 
(https://www.cfainstitute.org/membership/professional-development/refresher-readings)

2. PDFs Provided

##  Prerequisites 


Prerequisites of Software for the Project: 

### 1. Python Environment
Ensure Python is installed on the system. The project is developed using the Python programming language.

### 2. Python Libraries
- **Selenium**: For web scraping and interacting with dynamic elements on websites.
- **Beautiful Soup**: For parsing HTML content and extracting relevant information from web pages.
- **PyPDF2**: For extracting text from PDF files.
- **SQLAlchemy**: For interacting with databases using Python.
- **Boto3**: For interacting with AWS services such as S3.
- **Grobid**: For additional PDF text extraction capabilities.

### 3. Web Browser Driver
Selenium requires a web browser driver (e.g., ChromeDriver, GeckoDriver) compatible with the browser version installed on the system.

### 4. Snowflake Account
Access to a Snowflake account is necessary for database operations. This includes creating databases, tables, and establishing connections.

### 5. AWS Account
Access to an AWS account is required for utilizing AWS S3 storage services.

### 6. Visual Studio Code
Integrated Development Environment (IDE) or text editor for writing and running Python scripts.

 

 

 

 

 

 

 

 

 
## Project Structure



## Architectural Diagram


![Diagram Description](./diagrams/diagram.png)
## How to run Application locally


To run the application locally from scratch, follow these steps:

1. **Clone the Repository**: Clone the repository onto your local machine.

   ```bash
   git clone <repository_url>
   ```

2. **Create a Virtual Environment**: Set up a virtual environment to isolate project dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**: Activate the virtual environment.

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **Unix or MacOS**:

     ```bash
     source venv/bin/activate
     ```
4. **Host Grobid Server**: Open Docker Desktop and host the Grobid server.

   ```bash
    git clone https://github.com/kermitt2/grobid_client_python
    cd grobid_client_python
    python3 setup.py install
    docker run -t --rm -p localhost:8070 lfoppiano/grobid:0.8.0
   ```

5. **Install Requirements**: Install the required dependencies listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Notebook Script**: Execute the `run_notebook.sh` shell script to run the application.

   ```bash
   bash run_notebook.sh
   ```

By following these steps, you will be able to run the application locally from scratch. Ensure that Docker Desktop is installed and running before hosting the Grobid server.
## Team Information and Contribution 

Name           | Contribution %| Contributions |
---------------|---------------| --- |
Anirudh Joshi  | 34%           |      |
Nitant Jatale  | 33%           |      |
Rutuja More    | 33%           |      |