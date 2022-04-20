# Econ Application
To clone, create an empty directory and cd into it, then use the command "git clone" + the HTTPS URL that appears when you hit the "Code" button in the project repository

#### To push your changes to the repo, use the command "git add files", where files are the files you want to add, if you want to add all your files, do "git add ."

Then, do "git commit -m '<Message>'", where <Message> is the commit message, like a description of what you are adding

Then do "git push origin main", you should see your changes in the repo after you do this


#### To pull the changes from the repository to your local computer, use the command "git pull", this should pull changes from the repository to your computer 

Once you've pulled, you may need to go through certain files and resolve conflicts in code, and accept either the repository's version, or your version. 



#### To test:
For browser bots, make sure you have "requests" and "ws4py" installed locally, then after running "otree devserver" in another terminal, use
the command "otree browser_bots my_project NUM_BOTS" where NUM_BOTS is how many bots you need. You can tweak conditions in the tests.py in the Consent folder.

#### For command line bots, use the command "otree test my_project NUM_BOTS --export=test_cases", where NUM_BOTS is how many bots you need. 
You can look in the test_cases folder afterwards to see the results of the test. 
