app.get("/authorize", function (req, res) {
	client.getRequestToken().then(function (results) {
		var token = results[0],
			secret = results[1];
		requestTokenSecrets[token] = secret;
		res.redirect("http://www.fitbit.com/oauth/authorize?oauth_token=" + token);
	}, function (error) {
		res.send(error);
	});
});