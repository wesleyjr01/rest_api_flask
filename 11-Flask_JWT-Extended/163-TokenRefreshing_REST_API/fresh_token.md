# Ever seen something like this?
 * You are logged in, and you are browsing along, and then you try to make some action in the website, and then you are asked to loggin again, like when you try to delete a github repository. Why do they do that? The answer is they do it because they realise that I am logged in, but I haven't given them my username for a few days, so although it's unlikely someone stole my computer, it is possible.
 * So when I'm doing something quite critical, they wanna make sure that it really is me and it's not that unlikely scenario where somebody else have stolen my device. So in these cases, they want what's called a fresh token.
 * **The token generated when a user log in is a Fresh token**, and when it expires, in most cases, the application refreshed it generetaing a Refreshed Token. But, if the user tries to do some criticcal action, it is required a Fresh token, so he has to log in again.