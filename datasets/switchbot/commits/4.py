class SwitchBot:
    BASE_URL        = 'https://api.switch-bot.com'
    BASE_PATH       = os.path.dirname(os.path.abspath(__file__))
    TOKEN_FILE      = os.path.join(BASE_PATH, 'token.txt')

    def __init__(self):
        with open(SwitchBot.TOKEN_FILE, 'r') as f:
            self.token = f.read().strip()

    def get_headers(self):
        return { 'Authorization': self.token }

    def get_url(self, *pathes):
        url = SwitchBot.BASE_URL + '/v1.0'
        for path in pathes:
            url += '/' + path
        return url

    def do_get(self, url, data, headers={}):
        req = Request(url, data, headers)
        req.add_header('Authorization', self.token)
        res = urlopen(req)
        return res.read().decode()
