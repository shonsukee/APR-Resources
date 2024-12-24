public class FitbitOAuthController {
    @RequestMapping(value = "/token")
    public String getToken(HttpServletRequest request) throws IOException, ServletException,
            OAuthMessageSignerException, OAuthNotAuthorizedException,
            OAuthExpectationFailedException, OAuthCommunicationException {

        String oauthCallback = ControllerSupport.getLocationBase(request, env) + "fitbit/upgradeToken";
        if (request.getParameter("guestId") != null)
            oauthCallback += "?guestId=" + request.getParameter("guestId");

        String consumerKey = env.get("fitbitConsumerKey");
        String consumerSecret = env.get("fitbitConsumerSecret");

        OAuthConsumer consumer = new DefaultOAuthConsumer(consumerKey,
                consumerSecret);

        OAuthProvider provider = new DefaultOAuthProvider(
                "https://api.fitbit.com/oauth/request_token",
                "https://api.fitbit.com/oauth/access_token",
                "https://api.fitbit.com/oauth/authorize");

        request.getSession().setAttribute(FITBIT_OAUTH_CONSUMER, consumer);
        request.getSession().setAttribute(FITBIT_OAUTH_PROVIDER, provider);

        if (request.getParameter("apiKeyId")!=null)
            request.getSession().setAttribute(FITBIT_RENEWTOKEN_APIKEYID,
                                              request.getParameter("apiKeyId"));

        String approvalPageUrl = provider.retrieveRequestToken(consumer,
                oauthCallback);

        return "redirect:" + approvalPageUrl;
    }
}