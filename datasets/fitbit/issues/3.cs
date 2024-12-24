public OAuthController()
{
     _authenticator = new Authenticator(
     ConfigurationManager.AppSettings["FitbitConsumerKey"],
     ConfigurationManager.AppSettings["FitbitConsumerSecret"],
     "http://api.fitbit.com/oauth/request_token",
     "http://api.fitbit.com/oauth/access_token",
     "http://api.fitbit.com/oauth/authorize");
}
