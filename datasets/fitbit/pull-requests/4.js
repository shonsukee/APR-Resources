function authorize() {
	var oAuthConfig = UrlFetchApp.addOAuthService("fitbit");
	oAuthConfig.setAccessTokenUrl("https://api.fitbit.com/oauth/access_token");
	oAuthConfig.setRequestTokenUrl("https://api.fitbit.com/oauth/request_token");
	oAuthConfig.setAuthorizationUrl("https://api.fitbit.com/oauth/authorize");
	oAuthConfig.setConsumerKey(getConsumerKey());
	oAuthConfig.setConsumerSecret(getConsumerSecret());

	var options = {
	  "oAuthServiceName" : "fitbit",
	  "oAuthUseToken" : "always"
	};

	// get The profile but don't do anything with it -- just to force
	// authentication
	var result = UrlFetchApp.fetch(
		"https://api.fitbit.com/1/user/-/profile.json", options);
	var o = Utilities.jsonParse(result.getContentText());

	return o.user;
	// options are dateOfBirth, nickname, state, city, fullName, etc. see
	// http://wiki.fitbit.com/display/API/API-Get-User-Info
}
