# How the Domain Name System works?
Explaination can be seen in the following link:  
https://books.tecladocode.com/rest-apis-with-flask-and-python/domains-and-https/what-is-a-domain#what-ip-address-do-they-represent
* TLD(Top Level Domain).
* Going back to CloudFlare, what we've set up in the last video, xxxxxx.ns.cloudflare.com and yyyyyyy.ns.cloudflare.com are the Authoritative name servers. So, those are the servers that know the IP adress of your domain wesleybortolozo.com, and in the DNS settings in CloudFlare, we have defined the IP adress, so whenever we go to one of those two name servers, they will know "Ok this A record exists, wesleybortolozo.com is the IP adress \<IPv4\>", and they will give the browser this IP Adress.