class FitbitOauthClient(object):
    API_ENDPOINT = "https://api.fitbit.com"
    AUTHORIZE_ENDPOINT = "https://www.fitbit.com"

    request_token_url = "%s/oauth/request_token" % API_ENDPOINT
    access_token_url = "%s/oauth/access_token" % API_ENDPOINT
    authorization_url = "%s/oauth/authorize" % AUTHORIZE_ENDPOINT

    def __init__(self, client_key, client_secret, resource_owner_key=None,
                 resource_owner_secret=None, user_id=None, callback_uri=None,
                 *args, **kwargs):
        """
        Create a FitbitOauthClient object. Specify the first 5 parameters if
        you have them to access user data. Specify just the first 2 parameters
        to access anonymous data and start the set up for user authorization.
        Set callback_uri to a URL and when the user has granted us access at
        the fitbit site, fitbit will redirect them to the URL you passed.  This
        is how we get back the magic verifier string from fitbit if we're a web
        app. If we don't pass it, then fitbit will just display the verifier
        string for the user to copy and we'll have to ask them to paste it for
        us and read it that way.
        """

        self.session = requests.Session()
        self.client_key = client_key
        self.client_secret = client_secret
        self.resource_owner_key = resource_owner_key
        self.resource_owner_secret = resource_owner_secret
        if user_id:
            self.user_id = user_id
        params = {'client_secret': client_secret}
        if callback_uri:
            params['callback_uri'] = callback_uri
        if self.resource_owner_key and self.resource_owner_secret:
            params['resource_owner_key'] = self.resource_owner_key
            params['resource_owner_secret'] = self.resource_owner_secret
        self.oauth = OAuth1Session(client_key, **params)

    def _request(self, method, url, **kwargs):
        """
        A simple wrapper around requests.
        """
        return self.session.request(method, url, **kwargs)

    def make_request(self, url, data={}, method=None, **kwargs):
        """
        Builds and makes the OAuth Request, catches errors
        https://wiki.fitbit.com/display/API/API+Response+Format+And+Errors
        """
        if not method:
            method = 'POST' if data else 'GET'
        auth = OAuth1(
            self.client_key, self.client_secret, self.resource_owner_key,
            self.resource_owner_secret, signature_type='auth_header')
        response = self._request(method, url, data=data, auth=auth, **kwargs)

        if response.status_code == 401:
            raise HTTPUnauthorized(response)
        elif response.status_code == 403:
            raise HTTPForbidden(response)
        elif response.status_code == 404:
            raise HTTPNotFound(response)
        elif response.status_code == 409:
            raise HTTPConflict(response)
        elif response.status_code == 429:
            exc = HTTPTooManyRequests(response)
            exc.retry_after_secs = int(response.headers['Retry-After'])
            raise exc

        elif response.status_code >= 500:
            raise HTTPServerError(response)
        elif response.status_code >= 400:
            raise HTTPBadRequest(response)
        return response
