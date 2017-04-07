import requests

class Socket():
    url = ''
    port = ''
    path = ''
    authorization=''

    def __init__(self, url='', port='', path='', authorization=''):
        self.url = url
        self.port = port
        self.path = path
        self.authorization = authorization

    def emit(self, message):
        # Send a http request to emit a new message
        url = self.url
        if self.port:
            url += ':' + self.port
        url += self.path + '/emit'
        headers = {'X-Authorization-Token': self.authorization}
        print(url)
        print(message)
        r = requests.post(url, data=message, headers=headers);


    
