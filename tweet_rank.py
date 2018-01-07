"""
On Twitter, millions of tweets are posted on a daily basis. Help Twitter write a simple ranking algorithm to find the best of all tweets. It works as follows: A good tweet receives many "likes" from people on Twitter, either from people you follow, or people you do not follow. A tweet is more relevant to you if people you follow also liked the tweet. If enough people you follow have liked that tweet, we recommend that tweet to you. Your task is to complete the function getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold), which returns a list of tweet IDs in sorted order that should be recommended for a certain user. It takes 4 parameters: - followGraph_edges stores follow relationships as an array of tuple of integers. For example, followGraph_edges = Array{(A, B) , (A, C), (B, C)} represents 3 follow relationships: A follows B A follows C B follows C - likeGraph_edges stores like relationships, also in an array of tuple of integers. For example, likeGraph_edges = Array{(A, T1), (B, T2), (A, T2)} means: A liked tweet T1 B liked tweet T2 A liked tweet T2 - targetUser is the user ID for which we generate recommended tweets - minLikeThreshold is the minimum number of likes a tweet must receive from people you follow to be recommended For example, if minLikeThreshold = 4, only tweets that received at least 4 likes from people you follow should be recommended NOTE: If you cannot find a single tweet that meets our requirement, simply return an empty list. You may also use any functions provided by the standard library.
"""
#SORTING ALGORITHM THAT RETURNS POSTS THAT TARGETUSER MIGHT BE INTERESTED IN

# Complete the function below.
# followGraph_edges is a list of tuples (userId, userId)
# likeGraph_edges is also a list of tuples (userId, tweetId)

def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
    currently_following = list() #userIDs of users that are followed by targetUser
    recommended = list() #list of tuples (number of likes, postID)

    for follow_relation in followGraph_edges:
        if follow_relation[0] == targetUser:
            currently_following.append(follow_relation[1]) #appends followed userIDs to currently_following

    for like_relation in likeGraph_edges:
        if like_relation[0] in currently_following:
            if like_relation[1] in [post[1] for post in recommended]:
                for post in recommended:
                    if post[1] == like_relation[1]:
                        opened_post = list(post) #format of opened_post: [number of likes, postID]
                        recommended.remove(post)
                        recommended.append((post[0]+1,post[1])) #modifies tuple containing # of likes and postID by incrementing # of likes
                        break
            else:
                recommended.append((1,like_relation[1])) #creates a new tuple if the post has at least one like.

    recommended.sort() #sorting in increasing order of likes occurs here
    filtered_recommend  = [i[1] for i in recommended if i[0] >= minLikeThreshold] #list comprehension to create new list with only postIDs that fulfill the minLikeThreshold
    return filtered_recommend
