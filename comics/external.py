import requests
import hashlib
import time

class Marvel:
    def __init__(self):
        # TODO Find a better way to store these values
        self.pub_key = 'dab1e729763acfa483ed90eaf40b0530'
        self.private_key = '479258fc2a08d750b9db0990b3eac19015b03878'
        self.url = 'https://gateway.marvel.com:443/v1/public'
        self.url_char_search = '/characters'
        self.url_id = '/characters/'
        self.url_story_id = '/stories/'
        self.auth = '?ts={}&apikey={}&hash={}'

    def getHash(self):
        ts = time.time()
        hsh = ("%s%s%s" % (ts, self.private_key, self.pub_key)).encode('utf-8')
        hash_string = hashlib.md5(hsh).hexdigest()
        return self.auth.format(ts, self.pub_key, hash_string)

    def get_characteres(self, name):
        url = self.url + self.url_char_search
        start = '&nameStartsWith=%s' % name
        response = requests.get(url+self.getHash()+start)
        return response

    def get_id(self, char_id):
        url = self.url + self.url_id + char_id
        response = requests.get(url+self.getHash())
        return response

    def get_story(self, story_id):
        url = self.url + self.url_story_id + story_id
        response = requests.get(url+self.getHash())
        return response

# a = Marvel()
# n = a.getCharacteres('spider')
