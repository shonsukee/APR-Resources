AFOAuth1Client *oAuthClient = [[AFOAuth1Client alloc] initWithBaseURL:[NSURL URLWithString:@"http://api.fitbit.com/"] key:@"key-removed" secret:@"secret-removed"];

[oAuthClient authorizeUsingOAuthWithRequestTokenPath:@"/oauth/request_token" userAuthorizationPath:@"http://www.fitbit.com/oauth/authorize?display=touch" callbackURL:[NSURL URLWithString:@"bitrockr://fitbit/success"] accessTokenPath:@"/oauth/access_token" accessMethod:@"POST" scope:nil success:^(AFOAuth1Token *accessToken, id responseObject) {
    NSLog(@"AUTH COMPLETE :: %@", accessToken);
} failure:^(NSError *error) {
    NSLog(@"AUTH FAILED");
}];