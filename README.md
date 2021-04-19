This is a python implementation of the Meltwater Challenge.
The purpose of this repo is to have a site that will accept a text file from the user and a string of words.
Then the program should redact all the words in the string throughout the text file.

To install this application navigate to the root application directory and run the command `pip install requirements.txt`.
Then to run the application from the same root directiory run the command `python app.py`.

Running the `app.py` file in an idea will accomplish the same result and allow for debugging.

To add new endpoint wire the correct pathing as a route in the `app.py` file and then add an html view file to the
directory `templates`.