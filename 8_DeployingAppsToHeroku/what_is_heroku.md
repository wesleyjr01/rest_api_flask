# What is Heroku?
* A web service that runs your code and allows others to acess it.
* It can run your Flask applications.
* It makes them available for others to interact with.
* This is called "hosting".
* Heroku works with **Dynos**. A Dyno is a Virtual Machine. So when you run your application, your application doesn't have control of the computer in which it is running, it only has control of the virtual system, that has been created specifically for that dyno. That mean that are a couple of limitations in terms of what we can do.
* We can tell Heroku to run our Python app, and also we will have to tell it to run something called **uWSGI**. **uWSGI** is a way of serving your Flask Application. Although the Flask application has a serving layer, that's how we acess it using postman or our web server, it's not the best, and also it is limited in what it can interact with. By running **uWSGI**, which is another Python library, on top, we're going to make our Flask app a lot more flexible.
* Heroku also enables **SSL (Secure Sockets Layer)** for you
* SSL allows communication between the client (you) and the server (Heroku) to be encrypted. Very useful when sending sensitive information, such as passwords.
### Conclusion
* Heroku is a distributed hosting service, each Dyno is seppareted from the others.
* Each server is called a "Dyno", and it runs you application.
* The Free tier gives you 1 dyno, but limited running hours.
* Good security profile due to SSL.