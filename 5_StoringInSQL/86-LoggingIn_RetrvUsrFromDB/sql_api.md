We are going to start using SQLite with our API, and we're going to sign users in. So we're going to be able to log in using
SQLite. Now, what that's going to mean, is that we are going to store users in SQLite and when the user calls the auth endpoint,
we are going to retrieve their username and password from the database, we're going to compare that username and password to the
username and password they're sending in the request, and then we're going to see if they match, and if they do, we're going to send back a jwt token.