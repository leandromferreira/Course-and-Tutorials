import twitter

consumer_key = 'key'
consumer_secret = 'secret'
access_token = 'token'
access_secret = 'secret'



api = twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token,
                access_token_secret=access_secret)


print(api.VerifyCredentials())


follwers = api.GetFollowers()
friends = api.GetFriends()

status_var = '@nickname #Python is amazing! #30daysofpython http://site.com/projects'
post_update = api.PostUpdates(status=status_var)

length_status = twitter.twitter_utils.calc_expected_status_length(status=status_var)

new_messsage = api.PostDirectMessage(screen_name='site', text='Hi there')
print(new_messsage)

#
new_magic_message = api.PostDirectMessage(screen_name='MagicJohnson', text='Hey Magic! Big fan.')
print(new_magic_message)



api.GetUser(user)
api.GetReplies()
api.GetUserTimeline(user)
api.GetHomeTimeline()
api.GetStatus(status_id=787079994451202048)
api.DestroyStatus(status_id)
api.GetFriends(user)
api.GetFollowers()
api.GetFeatured()
api.GetDirectMessages()
api.GetSentDirectMessages()
api.PostDirectMessage(user, text)
api.DestroyDirectMessage(message_id)
api.DestroyFriendship(user)
api.CreateFriendship(user)
api.LookupFriendship(user)
api.VerifyCredentials()

