# What is Digital Ocean
* DigitalOcean is a provider of servers, which means we can rent a server from them, for a small amount of money each month.  
What that means, and the way it's *different from Heroku*, is that in DigitalOcean we get acess to the computer itself that is running our software.  
* That means we can do things like change the users, add more programs to run in the server simultaneously, as opposed to just our application, we can change security parameters, we can potentially even deploy our application to many servers and connect them together.
* Essentially we can do anything we want, because when we rent through DigitalOcean, we are going to own the server in which the app is running. However, when we deploy on Heroku, Heroku servers run our app, but we don't get acess to the servers themselves.
* So if you want to deploy your application, and you want you application to Scale, and you want to keep costs down, but you are willing to do a bit more work, DigitalOcean may be the tool for you.
* There is a bit more work involved when deploying with DigitalOcean because we have to set up each of the servers. In Heroku we just press a button and the app gets deployed, here we'll have to install the database and install the application into the server and run it. But it shouldn't take too long, and once you know how to do it, it'll be a fairly quick process.
* Now, the link https://m.do.co/c/d54c088544ed gives 2 months free for your DigitalOcean applications.  
---
# Adding New Droplets in DigitalOcean
* Press New Droplet.
* Selecting Additional options:
    * **Private Network**: allows two of our droplets (so far we only have one) to connect to each other without going to though the internet. For example, it might allow your REST API droplet to connect to a database droplet, we are here doind that in the same droplet, so we dont need this.
    * **IPv6**: by default all the droplets run with IPv4 which is a pretty old version of the IP(Internet Protocol). The IPv6 is the newer version, we wont need that in this section.
    * **User data**: some DigitalOcean specific configuration parameters, we are going to leave that unchecked.
* **Use a password to sign-up.**  
* **Click on Acess Console to log in and see the terminal.**
---
# Installing PostgresSQL in Ubuntu 16.04
* You can connect to your droplet (as a root user) directly from your terminal:
    * ssh root@\<IPv4\>, and then type password. In this case it is ssh root@64.225.20.194
    * sudo apt update
    * sudo apt install postgresql postgresql-contrib
* **When we install PostgresSQL it adds another user to our server**. That user is the one who owns PostgresSQL installation. So we are going to change over to that user, instead of being logged in as the root user, we're gonna swap over and be logged in as the Postgres User:
    * sudo -i -u postgres
    * See that it changed from **root@restapi-course-trial:~#** to **postgres@restapi-course-trial:~$**
    * $ psql <- connects to PostgresSQL database
    * Every user in postgraes, automatically connects to a postgres database, with the same name as the user, with the same name as the user.
    * \conninfo <- You are ,connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
    * \q <- leaves the psql process, it leaves the database and goes back tot he Unix terminal.
    * exit <- logout off the postgres user and go back being the root user.  
---
# Creating a UNIX user in Ubuntu 16.04
* username = wesley, in this case.
* When we log in as the root user, we have acess to do anything so it can potentially mess up your server, making sure that you have to create another one. So we are going to create a new user by following the command ```adduser <username>```. It creates a *new user called username* and a *new group called username* as well. A group is a collection of users and you can set group permissions. For example, you may tell the Ubuntu server that all users in the group Jose have access to a specific folder, for example, it is just a way of setting permissions in Unix.
* Next make sure you put a different password from the root user for security.
* The next thing we have to do is make sure the *username* user can temporarily gain acess to being root so that we can do things like install programmes and things like that. We're gonna do that by running the command ```visudo```. A file will open, and you will type ```wesley  ALL=(ALL:ALL) ALL```
right under ```root  ALL=(ALL:ALL) ALL``` under the **# User privilege specification** line.
* Once that's done, we are going to save the file to the disk running the command ```CTRL+O```, and then we are going to press  **enter** to save it on top of the existing file, and finally we're gonna press ```CTRL+X``` to exit.
* The next thing we have to do is to make sure that the **uername** user can login to the server directly as the Jose user, as the opposed to the root user. So we press ```vi /etc/ssh/sshd_config```, opening another text file. Now you go down the file to the line ```#LoginGraceTime 2m``` and set just below it ```PermitRootLogin yes``` to ```PermitRootLogin no``` (Enter INSERT Mode by pressing "I", then press "ESC" to leave Insert mode). After that, go to the very bottom of the text file, press "ENTER" and write ```AllowUsers <usernmae>```, than the press "ESC" again. What it does is it tells ssh (our connection protocol) to allow the \<username\> user to connect with this server. So we've denied the root user from connecting and now we're allowing the \<username\> user to connect.
* So once you've pressed "ESC" to leave Insert Mode, press ```:wq``` (Write and Quit). And at the very end, we press ```service sshd reload```
---
# Setting up our new user with PostgresSQL permissions
* username = wesley, in this case.
* login by doing ```ssh username@IP``` and then become the root user ```sudo su```, and then we become the postgres user ```sudo -i -u postgres```, which has acess to all things PostgresSQL related.
* Now we're going to create a PostgreSQL user. The PostgreSQL user must have, for now, the same name as the Unix user (wesley in this case). ```createuser wesley -P```, -P allows to create a new password for this user.
* So now we make sure there is a database created for that user, ```createdb username```. Remember a PostgreSQL server can have many databases, we already have **one called postgres**, and now we created **another one called username**. Now we're gonna stop becoming the postgres user and go back to being username, to press ```exit``` to goes back to root, and ```exit``` again and it goes back to username, and now we can type ```psql``` to connect to **username database**.
* Now type ```\conninfo``` and see that **we are connected to the databe username as the user username**.
* Press ```\q``` if you want to leave the terminal.
* By default, when we connect to PostgreSQL we didn't have to provide a password because, by default, PostgreSQL realises that there is a user called *username* in the database and that has acess to the *username* database. So there's a postgres user called Jose, and that has acess to *username* database, and because they are called the same as Unix user, PostgreSQL just accepts that is ok. This is not very safe, so let's make sure that PostgreSQL asks us for our password. Type ```sudo vi /etc/postgresql/10/main/pg_hba.conf```, scroll down the text and go just below the line ```# "local" is for Unix domain socket connections only``` and change from ```local all all peer``` to ```local all all md5``` and then press ```ESC and :wq```. **peer** means we have acess to everything, while **md5** asks for a password. Now whenever we want to log in, we have to put a password. Also, if you don't change it to **md5** SQLAlchemy won't work, because it is unsecure.
---
# Setting up nginx and our REST API 
* Nginx is what's called a reverse proxy. What that means is that Nginx is going to act as a gateway between our application and external users. It's going to accept incoming requests, and then it's going to decide what to do with those requests. We're going to configure Nginx so those requests go stright to our application.
* The first thing to do is to login into your server and ```sudo apt update``` and then ```sudo apt install nginx```, now we must let nginx have acess through the firewall, so the incoming requests dont get blocked ```sudo ufw status```, it sais *Status: inactive*, so we're going to enable firewall ```sudo ufw enable```, and finally we have to give Nginx acess, so we're going to do ```sudo ufw allow 'Nginx HTTP'```, and now if you do ```sudo ufw status``` it will show that Nginx HTTP is allowed.
* Now allow ssh so we dont get locked out of the server! ```sudo ufw allow ssh```
* Now we're going to make sure that Nginx is running, and it should be running, and the way to check that in Ubuntu is with the system controller: ```systemctl status nginx```.
* Now we're going to the Nginx config and we're going to add our rest api to the Nginx config: ```sudo vi /etc/nginx/sites-available/items-rest.conf``` entering a brand new file, press "I" to go into Insert mode, we will write a bunch os stuff:  

```
server{  
    listen 80;  
    real_ip_header X-Forwarded-For;
    set_real_ip_from 127.0.0.1;  
    server_name localhost;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/var/www/html/items-rest/socket.sock;
        uwsgi_modifier1 30;
    }  

    error_page 404 /404.html;  
    location = /404.html {  
        root /usr/share/nginx/html;  
    }  

    error_page 500 502 503 504 /50x.html;   
    location = /50x.html {  
        root /usr/share/nginx/html;  
    }

}
```

* Now we enable the configs by ```sudo ln -s /etc/nginx/sites-available/items-rest.conf /etc/nginx/sites-enabled/```.
* Now ```sudo mkdir /var/www/html/items-rest```. This is where our application is going to live. WE created this directory as the root user, and now we have to give our *username* acess to it too. ```sudo chown -R wesley:wesley /var/www/html/items-rest```(changed owner of this directory to the wesley user and to the wesley group, as opposed to the root user and the root group.)
* Now we go into the directory ```cd /var/www/html/items-rest``` and the next thing we have to do is to **clone our Python App**. So I am going to use the same app as we used in the Heroku section: ```sudo git clone https://github.com/wesleyjr01/first_heroku_flask_restful_app.git .```
* In order to produce logs for our App, we're going to create a directory called log: ```mkdir log```
* Install Python stuff: ```sudo apt install python-pip```, then we're going to install a set of tools that Python needs to be able to compile from source ```sudo apt install python3-dev``` and finally ```sudo apt install libpq-dev```
* Now we must install virtualenv ```pip install virtualenv```.
* Now we are going to install a virtualenvironment in the same folder: ```virtualenv venv --python=python3```
* ```source venv/bin/activate```
* ```pip install -r requirements.txt```

* Observations on **server{}** configs: 
    * Firstly we defined the server, and this **server is going to be able to listen to incoming requests and then dispatch them where appropriate**. So this app, this server is going to **listen on port 80, which is the default HTTP port**. Whenever we acess a website on the internet, we're accessing on port 80, it is the default. So listening on port 80 is going to be interesting because it means that users don't have to do something like ```GET mysite.com:5645```, the colon(:) will be omitted whenever we access our rest api because the default is port 80. So if we're listening on port 80, we don't have to specify the port number.
    * **set_real_ap_from**: Although Nginx is going to forward the ip adress of the requester to our Flask app(real_ip_header X-Forwarded-For;), it's also going to say that the request is really coming from 127.0.0.1, which is local host, because Nginx is receiving the request, and then it's going to send that request to the Flask app, which will be running on local host.
    * **location / {}**: Whenever somebody accesses the root location of the server, it's going to redirect them somewhere, and where it's going to redirect them is to our Flask app.