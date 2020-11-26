# sharepoint-lists-access-class
A python class to access sharepoint lists in a easy way
The easy way I find to word with tables from sharepoint is using the lists and the shareplum lib (https://shareplum.readthedocs.io/en/latest/tutorial.html), so this is a class
that access that lists via shareplum (using Office 365).

# usability
- first add the module to your project path

- then you need to install shareplum
$ pip install shareplum

- then set the environment variables (to login using using Office 365):
$ set SHAREPOINT_URL="https://mysharepoint.sharepoint.com"
$ set SHAREPOINT_USER_EMAIL="your-user-email@email.com"
$ set SHAREPOINT_PASSWORD="your sharepoint pass word"
$ set SHAREPOINT_SITE_URL="https://mysharepoint.sharepoint.com/sites/MySite"

- now you can use the class:
to this you need to instantiate an object to represent you site:
```python
sharepoint_site = SharepointSite()
```
