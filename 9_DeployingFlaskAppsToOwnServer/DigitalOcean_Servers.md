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