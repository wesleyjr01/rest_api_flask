# REST Principles
#### What we know so far?
* Going to a site does a **GET** request.
* This normally returns **HTML**, but it can return other
things, like text or errors, for example.
* We can do other things than **GET**, **POST** for example.
---
#### What is a REST API?
* A REST API uses those same concepts that we've looked at, GET, POST and so on, so there's no technical things going on in a REST API. All that **REST is a way of thinking about how a web server responds to your requests**, and how a web server behaves in general.
* It doesn't respond with just data.
* It responds with **resources**, a thing in the server.
    * **Resources**?
    * Similar to object-oriented programming. 
    * Think of the server as having resources, and each is able to interact with the pertinent request:  
    
        |  Request  |     Item resource     |   |
        |----------|:-------------:|------:|
        | **GET** |  /item/chair |  |
        | **POST** |    /item/chair  |  With extra data  |
        | **PUT** | /item/chair |   With extra data  |  
        | **DELETE** | /item/chair |     | 
    * As you can see all of there four requests above have the same endpoint /item/chair, that's because they are alll accessing the same resource. **The chair element of the item resource**. So this could be the item resource, and whenever we interact with an item we know that the endpoint is going to be the same.
    * Now we can start thinking of our interactions with the server as not individual requests, but resources, and now we can do things like GET a resource or POST something to the resource, or create a resource, delete a resource and so on, which simplifies the way of thinking, simplifies the thought process behind these interactions, because now instead of dealing with just individual endpoints, we're dealing with something a bit larger.
    * So once again, it is similar to object-oriented programming. In object-oriented programming objects are just things that hold some data and then some more data in the form of methods, and they have a name, and here it's a similar thing. Here is another example:
        |    |   ItemList resource       |   |
        |----------|:-------------:|------:|
        | **GET** |  /items |  |
    * Above we see another endpoint, **/items** and we can probably see the similarity, **/items** and **/item** probably fairly related, but it's a **different endpoint** and we're no longer retrieving and individual resource, **/items** probably means we're retrieving multiple items, therefore it cannot be the **Item resource**, it must be something like an **ItemList resource** for example.
---
#### Stateless
* Another key feature is that REST is supposed to be stateless.
* This means one request cannot depend on any other requests.
* The server only knows about the current request, and not any previous requests.
* Example 01, imagine we create a chair item:
    * **POST** **/item/chair** creates an item.