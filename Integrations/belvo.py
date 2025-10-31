from requests.auth import HTTPBasicAuth
from Integrations.base_request import get, post

class BelvoAPI:
    def __init__(self):
        self.base_url = os.environ.get("BELVO_URL")
        self.user = os.environ.get("BELVO_USER")
        self.password = os.environ.get("BELVO_PASS")
        self.auth = HTTPBasicAuth(self.user, self.password)

    def get_institutions(self):
        url = f"{self.base_url}/api/institutions/"
        return get(url, auth=self.auth)

    def get_accounts(self, user, institution):
        url = f"{self.base_url}/api/accounts/"
        link_id = self.get_link(user, institution)
        if not link_id:
            return {'error': 'No link found for user/institution'}

        params = {"link": link_id}
        return get(url, auth=self.auth, params=params)

    def register_link(self, username, password, institution):
        url = f"{self.base_url}/api/links/"
        params = {"institution": institution, "username": username, "password": password}
        return post(url, auth=self.auth, json=params)

    def get_link(self, user, institution):
        pass # From DB

    def get_transactions(self, user, institution, after_date=None, before_date=None): #date format =>'YYYY-MM-DD'
        link_id = self.get_link(user, institution)
        if not link_id:
            return {'error': 'No link found for user/institution'}

        url = f'{self.base_url}/api/transactions/'
        params = {'link': link_id}
        
        if after_date and before_date:
            params.update({'value_date__range': f'{after_date},{before_date}'})
        else:
            if after_date:
                params.update({'value_date__gte': after_date})
            if before_date:
                params.update({'value_date__lte': before_date})
        
        return get(url, auth=self.auth, params=params)
    
        

    

