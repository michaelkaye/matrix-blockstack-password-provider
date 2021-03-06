from matrix_blockstack_password_provider import BlockstackPasswordProvider
from twisted.internet import reactor
import requests

class _BlockstackConfig(object):
    pass

blockstack_config = _BlockstackConfig()
blockstack_config.enabled = False
blockstack_config.blockstack_node = "https://core.blockstack.org"

class AccountHandler(object):
    def check_user_exists(self, name):
        return False
    
    def register(self, localpart):
        return localpart, "abc"

class Store(object):
    def set_profile_displayname(self, user, name):
        pass
    def set_profile_avatar_url(self, user, url):
        pass
        
class ProfileHandler(object):
    store = Store()

class HS(object):
    def get_profile_handler(self):
        return ProfileHandler()

ah = AccountHandler()
ah.hs = HS()

requests.post("http://auth.openintents.org/c/asdf")
pwdProvider = BlockstackPasswordProvider(blockstack_config, ah)
result = []
print pwdProvider.check_password("@friedger.id:localhost", "asdf|https://chat.openintents.org")
