    [Route("fitbit")]
    public ActionResult Authorize()
    {

        //make sure you've set these up in Web.Config under <appSettings>:
        string ConsumerKey = ConfigurationManager.AppSettings["FitbitConsumerKey"];
        string ConsumerSecret = ConfigurationManager.AppSettings["FitbitConsumerSecret"];


        Fitbit.Api.Authenticator authenticator = new Fitbit.Api.Authenticator(ConsumerKey,
                                                                                ConsumerSecret,
                                                                                "http://api.fitbit.com/oauth/request_token",
                                                                                "http://api.fitbit.com/oauth/access_token",
                                                                                "http://api.fitbit.com/oauth/authorize");
        RequestToken token = authenticator.GetRequestToken();
        Session.Add("FitbitRequestTokenSecret", token.Secret.ToString()); //store this somehow, like in Session as we'll need it after the Callback() action

        //note: at this point the RequestToken object only has the Token and Secret properties supplied. Verifier happens later.

        string authUrl = authenticator.GenerateAuthUrlFromRequestToken(token, true);
        return Redirect(authUrl);
    }