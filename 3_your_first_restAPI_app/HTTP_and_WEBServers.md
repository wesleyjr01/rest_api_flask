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
    > GET /login HTTP/1.1  
    > Host: https://twitter.com  

    As you can see, up to the .com is the host name, and anything after that is the path, what we are requesting.
    So, in this case, the host is https://twitter.com, and the path is **/login** which is what comes after.

    2) Similarly for this other page https://git-scm.com/download/mac, it performs the GET request:
    > GET /download/mac HTTP/1.1  
    > Host: https://git-smc.com

    3) Finally, https://www.google.co.uk/:
    > GET / HTTP/1.1
    > Host: https://www.google.co.uk
---
* Differences:
    * 