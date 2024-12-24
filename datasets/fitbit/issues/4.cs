    public AuthenticationTests()
    {
        authenticator = new Fitbit.Api.Authenticator(Configuration.ConsumerKey,
                                        Configuration.ConsumerSecret,
                                        "http://api.fitbit.com/oauth/request_token",
                                        "http://api.fitbit.com/oauth/access_token",
                                        "http://api.fitbit.com/oauth/authorize");

    }
