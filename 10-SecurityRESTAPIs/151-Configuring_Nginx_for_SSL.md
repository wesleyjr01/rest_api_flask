# Configuring nginx for SSL
* The first thing is to go to you server, ```ssh wesley@IPv4```. No we're gonna look at the contests of ```/var/www```, it returned the **html** folder, and that contains our API. But we're gonna make a directory inside ```mkdir /var/www/ssl```, now we're going to create two files in it, one is going to contain the key, the other is going to contain the certificate:  
```
sudo touch /var/www/ssl/wesleybortolozo.com.pem
sudo touch /var/www/ssl/wesleybortolozo.com.key
```
* Now ```sudo vi /var/www/ssl/wesleybortolozo.com.pem``` and paste the content of our Certificate here. Select everything, including the ---BEGIN CERTIFICATE--- and ---END CERTIFICATE--- and paste it there. Now you will do the same with the key, ```sudo vi /var/www/ssl/wesleybortolozo.com.key``` and paste the key content there, including the ---BEGIN--- ---END---.
* Now go back to the CloudFlare page and press OK on the "Origin Certificate Installation" box. Now we're done with this section, do notice that the SSL setting may take 24 hour to be active.
* Now lets go back to the terminal and serve the HTTPS traffic using Nginx, ```sudo vi /etc/nginx/sites-enabled/items-rest.conf```. Before, we setted up our **server{}** and **setted up to listen on port 80, port 80 is for HTTP trafic**. We're gonna listen for a different port which is for HTTPS traffic. So we're going to make a bunch of changes, and the server block will look like this:

```
server{
listen 443 default_server;
server_name wesleybortolozo.com;
ssl on;
ssl_certificate /var/www/ssl/wesleybortolozo.com.pem;
ssl_certificate_key /var/www/ssl/wesleybortolozo.com.key;
real_ip_header X-Forwarded-For;
set_real_ip_from 127.0.0.1;

location / {
    ...
```
* So now if we save and quit this and restart Nginx, everything's working. However, we've got a server listening on 443, and nothing listening on 80, which means we've got HTTPS to work but HTTP is not working now, and we don't wanna give our HTTP users an error. So now, after the entire **sever{}** block we have, we will create another **server{}** block to create a server that listens on port 80 aswell, but we're gonna tell it that whenevr a request comes onto port 80(HTTP request), to send it over to the HTTPS equivalent:
```
server{
listen 80;
server_name wesleybortolozo.com;
rewrite ^/(.*) https://wesleybortolozo.com/$1 permanent;
}
```
* Now save and quit. Now make sure to do ```sudo ufw allow https```. Now ```sudo systemctl reload nginx``` and ```sudo systemctl restart nginx```.
* Finally go to Postman to test the HTTPS requests, make sure to change your URL to use https.
* Thats it! You've got SSL, which means that the connection between your computer and CloudFlare is encrypted using your private key. So you have added security to your server.