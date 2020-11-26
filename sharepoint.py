from shareplum import Site
from shareplum import Office365
import os

class SharepointSite():
    def __init__(self):
        authcookie = Office365(
        os.environ.get('SHAREPOINT_URL'), 
        username=os.environ.get('SHAREPOINT_USER_EMAIL'), 
        password=os.environ.get('SHAREPOINT_PASSWORD')
        ).GetCookies()
        self.access = Site(os.environ.get('SHAREPOINT_SITE_URL'), authcookie=authcookie)
        self.lists = {}
        sharepoint_lists = self.access.GetListCollection()
        for sharepoint_list in sharepoint_lists:
            if sharepoint_list['BaseType'] == 'GenericList':
                self.lists[sharepoint_list['Title']] = List(self.access.List(sharepoint_list['Title']))
    
    def delete_all_lists_rows(self):
        for sharepoint_list in self.lists:
            self.lists[sharepoint_list].delete_list_rows()

class List():
    def __init__(self, sharepoint_list):
        self.list = sharepoint_list
        self.list_items = ListItems(sharepoint_list.GetListItems())

    def delete_list_rows(self):
        rows_ids = self.list_items.get_rows_ids()
        if rows_ids != []:
            self.list.UpdateListItems(rows_ids, kind='Delete')

    def insert_list_rows(self, data):
        if data != []:
            self.list.UpdateListItems(data=data, kind='New')

class ListItems():
    def __init__(self, items):
        self.list_items = items

    def get_rows_ids(self):
        ids = []
        for row in self.list_items:
            ids.append(row['ID'])
        return ids