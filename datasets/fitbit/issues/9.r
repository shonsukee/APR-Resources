key <- '<edited>'
secret <- '<edited>'
tokenURL <- 'http://api.fitbit.com/oauth/request_token'
accessTokenURL <- 'http://api.fitbit.com/oauth/access_token'
authorizeURL <- 'https://www.fitbit.com/oauth/authorize'

fbr <- oauth_app('fitbitR',key,secret)
fitbit <- oauth_endpoint(tokenURL,authorizeURL,accessTokenURL)

token <- oauth1.0_token(fitbit,fbr)
sig <- sign_oauth1.0(fbr,
    token=token$oauth_token,
    token_secret=token$oauth_token_secret
)

dta <- GET("http://api.fitbit.com/1/user/-/activities/steps/date/2012-08-01/1m.json",sig)
# this will fail unless using curlPercentEncode