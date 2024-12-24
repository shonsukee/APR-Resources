request_token = client.request_token
current_user.update(:token => request_token.token, :secret => request_token.secret)
redirect "http://www.fitbit.com/oauth/authorize?oauth_token=#{current_user.token.to_s}"
