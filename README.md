# FSND Linux Server Config, Apache Based Catalog

This is the 6th project in the Udacity FSND program, deploying the catalog project on a Linux Ubuntu server.

-The IP address is 54.69.81.35

-The URL for the hosted catalog app is http://54.69.81.35/

Prerequisite software modules to be installed include:

-pip, sqlalchemy, oauth2client, Flask, postgresql, git

-libapache2-mod-wsgi, requests, psycopg2, virtualenv

In order to setup the Linux Ubuntu server on Amazon Lightsail:

-disabled remote login of the user <code>root</code>.

-disabled password login and key-based <code>SSH</code> authentication is enforced.

-created the user <code>grader</code> with a supplied SSH key generated locally, and gave him <code>sudo</code> access.

-updated the system packages to the most recent versions.

-installed the prequesite software modules mentioned above.

-changed <code>SSH</code> to be hosted on the non-default port <code>2200</code>.

-configured and enabled the ubuntu <code>ufw</code> firewall to only allow for <code>SSH</code>(port 2200), <code>HTTP</code>(port 80), and <code>NTP</code>(port 123).

-disabled the file /etc/apache2/sites-enabled/000-dfault.conf and setup ~/FlaskApp.conf to allow Apache to run the catalog app.

-cloned the catalog app with git into /var/www/, edited project files to handle a postgreSQL database instead of sqlite.

-created flaskapp.wsgi to wrap the catalog app to be ran by apache

-created the psql user catalog, and under it created the database catalog.

-ran the file install_database.py to seed the catalog app's catalog database.

Third party resources

-https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

-http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/

-https://code.google.com/archive/p/modwsgi/wikis/ApplicationIssues.wiki#Access_Rights_Of_Apache_User

-https://serverfault.com/questions/125865/finding-out-what-user-apache-is-running-as

-https://stackoverflow.com/questions/5912701/python-egg-cache-extraction-error-permission-denied-apache-not-seeing-sete
