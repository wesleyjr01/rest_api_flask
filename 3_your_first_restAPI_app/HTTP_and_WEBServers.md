# HTTP, WebServers and Requests

* **HTTP** is one of the most popular protocolls, one of the
most popular way of creating interactions and allowing
interactions between two internet connected elements,
such as your computer and another computer.
---
* What is a **WEB server**? This course is all about creating
WEB servers, so that kinda gives you a bit of a hint.
**DEFINITION**: a WEB server is a piece of software designed
to accept incoming web requests.
---
* For example, Google has many web servers. Whenever we go
to http://www.google.com in our browser, we send something
to a web server. And when we send something to the web server,
the web server can then decide to respond back. It may not respond.
---
* What do we send to the web servers? When you go to http://www.google.com, you send the following, exactly what the server sees.  
 
> #### GET / HTTP/1.1  
> #### Host: www.google.com  

*  So when a user such as ourselves acesses the Google home page on one of their servers somewhere receives this piece of information (above), this is what's callled get request.
* The server then sees **GET / HTTP/1.1**, and a hostname
    * So the **GET** is called a **Verb**, it tells the server what we think the server is going to return, so what is expected of the server.
    * The **/** is the **Path**, which is what we want out of the server.
    * And finally, **HTTP/1.1** is the **Protocol** and this is the most popular http protocol.
* So this is all the server sees, and when we create our own web server applicactions, we're going to see something very similar.
* So, what? Is that all? Well acctually, yeah. That's all the server sees, and the server sees that and then there's some code, and the code is what the server runs on and that allows it to make a decision as to what it's going to respond with.
* So, different servers may interpret the get request in many different ways and they'll respond differently. For example:      
    * the server may give you an error, if **/** is not found. 
    * It may give you and error if **HTTP** is not supported. * It may give you an error if the server is unavailable. * Or it may not give error, it may give you HTML code back (which is what it normally does). 
    * It may also give you some text back.
* What else?
    * Going to any page with your browser such as Chrome, or Safari or Firefox will always do the same, it will always going to do a **GET request**.
---
* Examples:
    1) If you go to the twitter page, and attempt to log at https://twitter.com/login, that perform the GET request **GET/login**:
    > #### GET /login HTTP/1.1  
    > #### Host: https://twitter.com  

    As you can see, up to the .com is the host name, and anything after that is the path, what we are requesting.
    So, in this case, the host is https://twitter.com, and the path is **/login** which is what comes after.

    2) Similarly for this other page https://git-scm.com/download/mac, it performs the GET request:
    > #### GET /download/mac HTTP/1.1  
    > #### Host: https://git-smc.com

    3) Finally, https://www.google.co.uk/:
    > #### GET / HTTP/1.1
    > #### Host: https://www.google.co.uk
---
* Differences:
    * The only difference is what the server on the other end responds with.
    * Twiter responds with the Twitter login HTML page.
    * The git-smc responds with the git-smc downloads for mac HTML page.
    * The google reponds with the main google home page.
---
* What Else?
    * Going to a page will always do a **GET** request, so no matter where you go, the server's always gonna see the same thing. That's because the browser, such as Chrome or Safari is configured to do a get request whenever it accesses a page.
    * But there are many other things we can do, such as **POST, DELETE, PUT, OPTIONS, HEAD**, and much more.
    * Each server responds differently to each, but they normally have the same meaning in each server. So, all servers will respond to a **POST** request in similar ways, all servers will respond to a **DELETE** request in similar ways, in the same way that all servers will respond to a **GET** request in similar ways. That's because these things are so widely used that have nearly become a standard now.
    ---
* **HTTP Verbs**:

| **Verb**   |      **Meaning**      |  **Example** |
|----------|:-------------:|------:|
| GET |  Retrieve Something | GET /item/1 |
| POST |    Receive data, and use it   |   POST /item |
| PUT | Make sure something is there |    PUT /item |  
| DELETE | Remove something |    DELETE /item/1 | 

* **POST**: for the server means receive data and use it. Presumably if you do **POST / item** that may create a new item, ex ```{"name" : "Chair", "Price" : 9.99}```. Also when you do a **POST** request normally you have to send some data along the post request, and it may be a piece of json

* **PUT**: it means make sure something is there. Notice how it doesn't create things or do anything, it just makes sure that something is there. So if you do **PUT /item** with some data again ```{"name" : "Chair", "Price" : 7.99}```, that may create a new chair to make sure that the chair exists. Or, if the chair's already there, it may update the chair, change the price.

* **DELETE**: it tends to mean remove something such as **DELETE /item/1**, and presumably it will delete the item with ID number 1.