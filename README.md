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
SharepointSite() has access to all lists of type 'GenericList' of your site

it can clean all the list with:
```python
sharepoint_site.delete_all_lists_rows()
```
Or access a specific list By:
```python
sharepoint_site.lists['ListName']
```
and do:
```python
sharepoint_site.lists['ListName'].insert_list_rows(data) 
```
where data is a list of dictionarys, like:

[

{"Column 1":"value 1", "Column 2":"Value 1"},

{"Column 1":"value 2", "Column 2":"Value 2"}

]


