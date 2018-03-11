
        Module  - Installing Odoo from Source Code
        ==========================================

        1.1 What is Odoo?
        -----------------

          Odoo is an all-in-one management software that offers a range of business applications that form a complete suite of enterprise management applications targeting companies of all sizes.
          Versions: 7,8,9,10,11.
                    Version 11 runs on Python 3 and above
          Community and Enterprise versions.
          - Odoo Enterprise contains a set of new apps on top of the community Edition
            Not open-sourced and the code is only available to official Odoo partners and Odoo Company.
            Extra Apps like: account_dashboard, account_check_print, web_mobile, project_forecast etc.
        1.2 Requirements
        ----------------

          -> Linux Operating System/Windows (Linux preferred)
          -> Python 2.7
              How to check python version:
                  In your CLI type 'python', it should be something like 
                  'Python 2.7.12 (default, Dec  4 2017, 14:50:18)'
          -> Installing pip
            1. *sudo apt-get install python-pip*
            2. *sudo pip install virtualenv*
            3. *sudo pip install virtualenvwrapper*
          -> Installing Virtual ENV: Using virtualenvwrapper
              1. Run *mkvirtualenv odoo*
              2. To Enter Virtual env: *workon odoo*
              3. To exit: *deactivate*
          -> Postgresql
             Steps to install:
              1. In CLI: *sudo apt-get install postgresql / postgresql-9.6*
              2. *sudo –u postgres psql postgres*
              3. *\password postgres(Enter new password)*
              4. *\q*  - To Exit
              5. *sudo service postgresql restart*
              6. CREATE ROLE odoo LOGIN PASSWORD 'admin';
              7. ALTER ROLE odoo SUPERUSER CREATEROLE CREATEDB;
          -> Pgadmin
              Install it via Software Manager, or 
              Via CLI: *sudo apt-get install pgadmin3*

          
        1.2.1: Download Odoo Source Code
        ---------------------------------
          -> Repository: git@github.com:odoo/odoo.git 10.0
          -> Alternative: Odoo OCB: git@github.com:OCA/OCB.git
          -> *git clone <url> --depth 1*: - Clone Odoo with the latest commit only.
          -> *git clone <url> --depth 1 -b 10.0 --single-branch*

        1.2.2: Python Libraries
        -----------------------
          The python libraries usually required to run a specific version of Odoo is located in ../Odoo10/requirements.txt
          How it install these requirements:
            1. Make sure pip is install: *pip --version*
            2. pip install -r requirements.txt
            3. apt-get install -y npm
            4. sudo ln -s /usr/bin/nodejs /usr/bin/node
            5. sudo npm install -g less

        1.2.3: Installing Wkhtmltopdf
        -----------------------------

          What is it for? - Open source too that Renders HTML to PDF
          sudo apt-get install wkhtmltopdf
        1.3 Setting up Odoo.
        --------------------

            - Navigate to where your Odoo source from git is: E.g cd /home/your_username/odoo10/debian
            - Edit the Odoo Configuration file as follows:
                [options]
                ; This is the password that allows database operations:
                admin_passwd = admin
                db_host = 127.0.0.1
                db_port = 5432
                db_user = odoo10
                db_password = admin
                addons_path = /home/your_username/odoo10/addons

        1.4 Create an executable file with the following config parameters:
        -------------------------------------------------------------------
          -> *touch odoo10.sh*
          -> *chmod +x odoo10.sh*
          -> /usr/bin/python /home/your_username/odoo10/odoo-bin  --config=/home/your_username/odoo10/debian/odoo.conf 
          pause
          or run odoo directly with the following:
          *python odoo-bin -d o10 -c debian/odoo.conf*