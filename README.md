Automated Scraping and Storage System 
 The extracted data is stored in a MongoDB database for easy querying and further analysis.The system uses advanced scraping techniques with BeautifulSoup and requests libraries to parse web pages and identify key elements such as the title, subject, description, word count, read time, and downloadable resources. The scraper ensures data uniqueness by leveraging MongoDB’s upsert functionality, which prevents duplication and maintains a clean dataset.
Data extraction is highly structured, utilizing HTML tags and classes to target relevant sections like Introduction Guidance, Mathematical Processes, and Academic Honesty guidelines. Each section is systematically captured and normalized to ensure consistency across all entries. For instance, file links are validated, text content is cleaned to remove unnecessary whitespace, and missing fields are handled gracefully.
The uniqueness of this system lies in its ability to dynamically adjust to the website's structure, ensuring robust performance even if minor changes occur in the webpage layout. By employing MongoDB’s document-oriented storage, the system maintains flexibility, allowing storage of complex and hierarchical dats. This approach ensures scalability, making the system capable of handling large datasets while preserving data integrity and accessibility.
4o


Features
Scrapes structured data, including title, subject, description, sections, file links, and more.
Cleans and normalizes the extracted data.
Stores data in MongoDB with upsert functionality to prevent duplication.
Implements logging and error handling for smooth operation.

Prerequisites
Before running the project, ensure you have the following installed:
1.Python (Version 3.7 or above)
2.MongoDB (Running locally or via a cloud service like MongoDB Atlas)
3.Necessary Python libraries (see Dependencies)

Installation and Setup
Step 1: Clone the Repository
git clone https://github.com/Suresh807/Automated-Scraping-and-Storage-System-Using-MongoDB.git
cd nailib-scraper
Step 2: Set Up MongoDB
Install MongoDB if not already installed. Download MongoDB.
Start MongoDB server: 
mongod

Alternatively, set up a MongoDB Atlas cloud instance.
Step 3: Install Dependencies
Create a virtual environment and install the required libraries:
 Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate   For macOS/Linux
venv\Scripts\activate      For Windows

 Install dependencies
pip install -r requirements.txt
Step 4: Update URLs
In the script app.py, update the base_urls list with the actual URLs of the Nailib pages you want to scrape.
Step 5: Run the Script
Execute the script to scrape and store data:
python app.py
Step 6: Verify MongoDB Storage
Check the stored data in MongoDB:
 Open MongoDB shell
mongo

 Check the database
use nailib_data
db.ia_samples.find().pretty()

Directory Structure
nailib-scraper/
│
├── app.py                Main script for scraping and saving data
├── requirements.txt      Python dependencies
├── README.md             Project documentation
└── .gitignore            Git ignore file

Dependencies
The project uses the following Python libraries:
requests: For fetching web pages.
BeautifulSoup (bs4): For HTML parsing and data extraction.
pymongo: For connecting to MongoDB.
logging: For logging the execution process.
Install all dependencies using:
pip install -r requirements.txt

MongoDB Schema
The data is stored in the nailib_data database under the ia_samples collection with the following schema:
{
  "title": "Sample IA Title",
  "subject": "Math AI SL",
  "description": "Checklist for IA",
  "sections": {
    "Introduction Guidance": "Content here...",
    "Mathematical Information usage": "Content here..."
  },
  "word_count": 2112,
  "read_time": "11 mins",
  "file_link": "https://nailib.com/resource.pdf",
  "publication_date": "YYYY-MM-DD"
}

