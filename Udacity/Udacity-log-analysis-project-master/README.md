# Log Analysis
The log anaylsis in Udacity's full stack web development nanodegree program.
## Project Overview
The project required me to create SQL queries that would fetch results from a large database of a news website.The objective of this project is to expand on SQL database skills.

## Requirements
[VirtualBox](https://www.virtualbox.org/) - An open source virtualiztion product.\
[Git](https://git-scm.com/) - An open source version control system
[Python 3](https://www.python.org/download/releases/3.0/) - The code uses ver 3.6.4\
[Vagrant](https://www.vagrantup.com/) - A virtual environment builder and manager\

##  How to access the project?

Follow the steps below to access the code of this project:

 1. Download all the requirements above
 2. Clone this repository.
 3. Download [this newspaper database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) database.
 4. Navigate to the Udacity folder in your terminal and then navigate to the vagrant folder
 5. Open Git Bash and launch the virtual machine with`vagrant up`
 6. Once Vagrant installs necessary files use `vagrant ssh` to continue.
 7. Unpack the  database folder contents and move them to the current folder
 8.  To load the database type `psql -d news -f newsdata.sql`
 9. To run the database type `psql -d news`
 10. Use command `python project3.py` to run the python program that fetches query results.

