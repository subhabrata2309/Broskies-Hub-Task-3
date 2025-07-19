#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


url = "https://www.bbc.com/news"
response = requests.get(url)
html_content = response.text


soup = BeautifulSoup(html_content, "html.parser")

h2_headlines = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
title_tag = soup.title.get_text(strip=True) if soup.title else "No Title"


all_headlines = [title_tag] + h2_headlines


with open("news_headlines.txt", "w", encoding="utf-8") as file:
    for headline in all_headlines:
        file.write(headline + "\n")

print("Headlines saved to news_headlines.txt")


# In[ ]:


'''Interview Questions

1. What is a Get Request?
Ans:  A GET request is an HTTP method used to request data from 
a specified resource, such as a web page.

2. How do you install external packages in Python?
Ans: Use the command pip install package_name in the terminal 
or command prompt.

3. What is a User-Agent in HTTP?
Ans: A User-Agent is a string in an HTTP header that 
identifies the browser or tool making the request.

4. What is soup.find_all()?
Ans:  It is a BeautifulSoup method that returns a list of all HTML 
elements that match the specified tag or filters.



5. What are the risk of web scrapping?
Ans:  Risks include legal issues, getting IP banned, violating 
website terms, and breaking code if the site's structure changes.



6. what's the difference between id and class in HTML?
Ans: id is unique to one element; class can be shared by multiple 
elements.



7. What is an HTML tag?
Ans: An HTML tag is a code element (like <h1>, <p>, <div>) used to 
define content and structure on a webpage.



8. What does .text return in BeautifulSoup?
Ans: It returns all the text content within an HTML tag, without 
any HTML markup.



9. What is a try-except block?
Ans: It's used in Python to handle errors gracefully by running 
code in try and catching exceptions in except.

10. What are HTTP status codes?
Ans: They are 3-digit codes returned by a server to indicate the
result of an HTTP request (e.g., 200 OK, 404 Not Found).




'''

