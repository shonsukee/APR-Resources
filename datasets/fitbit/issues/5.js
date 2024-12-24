function getFitbitService() {
	return OAuth1.createService(identifier)
	// Set the endpoint URLs.
	.setAccessTokenUrl("https://api.fitbit.com/oauth/access_token")
	.setRequestTokenUrl("https://api.fitbit.com/oauth/request_token")
	.setAuthorizationUrl("https://api.fitbit.com/oauth/authorize")

	// Set the consumer key and secret.
	.setConsumerKey(getConsumerKey())
	.setConsumerSecret(getConsumerSecret())

	// Set the project key of the script using this library.
	.setProjectKey(projectKey)


	// Set the name of the callback function in the script referenced
	// above that should be invoked to complete the OAuth flow.
	.setCallbackFunction('authCallback')

	// Set the property store where authorized tokens should be persisted.
	.setPropertyStore(PropertiesService.getUserProperties());
}
