# Broskies-Hub-Task-3
Broskies Hub Task 3

📰 News Headline Web Scraper
This project is a simple Python script that scrapes news headlines from a news website (e.g., BBC News) using requests and BeautifulSoup. The extracted headlines are saved into a .txt file for offline viewing or further processing.

📌 Features
Fetches HTML content using requests

Parses <h2> and <title> tags using BeautifulSoup

Extracts headlines and saves them into news_headlines.txt

🚀 Getting Started
Prerequisites
Make sure you have Python installed. Then install the required libraries:

Installing the correct modules:

pip install requests beautifulsoup4


🧠 How It Works
Sends a GET request to a news website.

Parses the HTML response using BeautifulSoup.

Extracts headlines from <h2> and <title> tags.

Saves the headlines into news_headlines.txt.

📝 Usage
Run the script:

To run the script: 

python scraper.py
After execution, check news_headlines.txt for the saved headlines.

📂 Output Example (news_headlines.txt)

BBC News - Home
Heatwave hits Europe as temperatures soar
Ukraine pushes forward on the eastern front
...
⚠️ Disclaimer
This script is for educational purposes only. Please ensure that you follow the website's robots.txt and terms of service before scraping.

📃 License
This project is open source and free to use for personal and educational purposes.
