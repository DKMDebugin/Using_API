# Using_API

# Data Visualization in Python
Use pygal to create Bar chart from the data provided

# How Data is Gotten
Use GitHub & Hacker News API. When an API call is successful the
status code is 200. We used this to create a test for one of the 
modules

# Files
- bar_description.py is used to test the waters

- hn_submission.py uses the Hacker News Api to get data on top stories & comments.
Then store the resulting data in a json file. 

- submission_visualization visualizes the data in bar chart from the json file.
Then renders it to an svg file (hn_submission.svg) in the project dir which you can view using your browser.

- The function most_starred_project() in programming_lang.py uses GitHub API to get data on the top projects
on a list of languages & visualizes the data. The visualization for each language is rendered to an svg
file which takes the name "<language name>_repos.svg".

- test_programming-lang.py creates a test based on the get_status_code() function in programming_lang.py

# NB
You need to run the python modules to create the svg & json files.
