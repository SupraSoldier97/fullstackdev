
                          Log Analysis

  What is it?
  -----------

  This project is intended for my Full Stack Web Developer's Course on Udacity.
  It is a log analysis tool written in python3, used as script that executes commands in the PostgreSQL library. This script polls an 
  actual PSQL server named 'news'. The data it queries is as follows: 

  1. Three most popular articles of all time according to the logs on the database ranked in order by views.
  2. Most popular article author of all time ranked by view and listed by author name.
  3. Log table showing which days had HTTP status error codes (404) greater than 1%

  The Latest Version
  ------------------
  Release 1.0


  Installation
  ------------

  1. Find the zipped folder with the files named 'log_analysis.py', 'newsdata.sql' and 'createviews.sql' with Finder (Mac) or 
     SearchBar (Windows).
     Unzip the file contents onto your Desktop.

  2. With the new files you extracted, cd into the working directory where they reside.
     Then, run "psql -d news -f newsdata.sql" in the terminal/command prompt window to load the 
     site data in to your local database.

  3. In the same directory, run "psql -d news -f createviews.sql" to create a view that was custom made
     for this project.


  4. a) For Windows Users:
        Run the python3 script by dragging it into your Command Prompt window.

     b) For Mac/Unix Users:
        Run 'python3 log_analysis.py' to run the script.


  NOTE: If the file does not work you may need to modify the file permissons or work as a
        super user. To modify the permissions you can run in the terminal:
        'chmod u+X log_analysis.py' then re-run the command to open the file as stated above.

   5. After running the python file, it will query and analyze the data on the news database and return the
      outputs listed above.

 
  Licensing
  ---------

  Open Source Software


  Contacts
  --------

     o If you would like to help modify this code or find a bug feel free to email
     me at suprasoldier97@gmail.com
