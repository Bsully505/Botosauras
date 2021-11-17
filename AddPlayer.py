import requests 
 
class AddPlayer:
    url = 'https://slackevent.herokuapp.com/'
    def __init__(self,is_DM,User):
        res =requests.post(self.url+'PostChar', json= {"type":is_DM,"User":User})
        return res.status_code
        
            