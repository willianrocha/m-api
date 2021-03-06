import requests
import hashlib
import time

class Marvel:
    def __init__(self):
        # TODO Find a better way to store these values
        self.pub_key = 'dab1e729763acfa483ed90eaf40b0530'
        self.private_key = '479258fc2a08d750b9db0990b3eac19015b03878'
        self.url = 'https://gateway.marvel.com:443/v1/public'
        self.auth = '?ts={}&apikey={}&hash={}'

    def get_hash(self):
        ts = time.time()
        hsh = ("%s%s%s" % (ts, self.private_key, self.pub_key)).encode('utf-8')
        hash_string = hashlib.md5(hsh).hexdigest()
        return self.auth.format(ts, self.pub_key, hash_string)

    def get(self, url):
        try:
            response = requests.get(url,timeout=10).json()
        except requests.exceptions.Timeout:
            # TODO Logging
            response = {}
        return response

    def get_characteres(self, name):
        url = self.url + '/characters'
        start = '&nameStartsWith=%s' % name
        response = self.get(url+self.get_hash()+start)
        try:
            list_char = response['data']
        except KeyError:
            #NOTE Should i raise some error here? for debuggin
            list_char = None
        return list_char

    def get_id(self, char_id):
        url = self.url + ('/characters/%s' % char_id)
        response = self.get(url+self.get_hash())
        try:
            char = response['data']['results'][0]
            attr_text = response['attributionText']
        except KeyError:
            char = None
            attr_text = None
        return char, attr_text

    def get_id_comics(self, char_id):
        url = self.url + ('/characters/%s/comics' % char_id)
        response = self.get(url+self.get_hash())
        try:
            char_comics = response['data']['results']
        except KeyError:
            char_comics = None
        return char_comics

    def get_comics(self, comic_id):
        url = self.url + ('/comics/%s' % comic_id)
        response = self.get(url+self.get_hash())
        try:
            comic = response['data']['results'][0]
            attribution_text = response['attributionText']
        except KeyError:
            comic = None
            attribution_text = None
        return comic, attribution_text

    def get_comics_characters(self, comic_id):
        url = self.url + ('/comics/%s/characters' % comic_id)
        response = self.get(url+self.get_hash())
        try:
            comic_char = response['data']['results']
        except KeyError:
            comic_char = None
        return comic_char

# a = Marvel()
# n = a.getCharacteres('spider')
