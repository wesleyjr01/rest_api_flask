### Definition
* A **Model** is our internal representation of an entity,
whereas a **Resource** is the external representation of an entity.
* Our API clients, like a website or a mobile app, think they're interacting
with resources, that's what they see. And when our API responds, it responds with
resources, that's what the client sees.
* However, when we **deal internally in our code with a User**, for example, in our
security.py file, we are using *find_by_username* for example, we are not using
the resource, we are using the model, because that's what gives us the power and
that's what has the code that allows our program to do what it has to do.
* The **model essentially is a helper**, that allows our program or that gives us more flexibility in our program without polluting the **Resource**, which is what the clients interact with.
* So, **models and resources are reasonably separate**, but they can be linked in the case of UserRegister and our User Model.