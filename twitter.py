
"""
IPv4 was the first publicly used Internet Protocol. It used 4-byte addresses and permitted 232 distinct values. The typical format for an IPv4 address is A.B.C.D where A, B, C, and D are integers in the inclusive range between 0 and 255. IPv6, with 128 bits, was developed to permit the expansion of the address space. These addresses are represented by eight colon-separated sixteen-bit groups, where each sixteen-bit group is written using 1 to 4 hexadecimal digits. Leading zeroes in a section are often omitted from an address, meaning that the groups 0 is identical to 0000 and group 5 is identical to 0005. Some examples of valid IPv6 addresses are 2001:0db8:0000:0000:0000:ff00:0042:8329 and 3:0db8:0:01:F:ff0:0042:8329. Given n strings of text that may or may not be valid Internet Protocol (IP) addresses, we want to determine whether each string of text is: An IPv4 address. An IPv6 address. Neither an IPv6 address nor an IPv4 address. Complete the checkIP function in the editor below. It has one parameter: an array of strings, ip, where each element i denotes a string of text to be checked. It must return an array of strings where each element i contains the answer for ipi; each answer must be whichever of the following case-sensitive terms is appropriate: IPv4 if the string is a valid IPv4 address. IPv6 if the string is a valid IPv6 address. Neither if the string is not a valid IPv4 or IPv6 address. Input Format Locked stub code in the editor reads the following input from stdin and passes it to the function: The first line contains an integer, n, denoting the number of elements in ip. Each line i of the n subsequent lines (where 0 ≤ i < n) contains a string describing ipi. Constraints 1 ≤ n ≤ 50 1 ≤ ipi ≤ 500 It is guaranteed that any string containing a valid IPv4 or IPv6 address has no leading or trailing whitespace. Output Format The function must return an array of strings where each element i contains the string IPv4, IPv6, or Neither, denoting that ipi was an IPv4 address, an IPv6 address, or Neither (i.e., not an address at all). This is printed to stdout by locked stub code in the editor. Sample Input 0 2 This line has junk text. 121.18.19.20 Sample Output 0 Neither IPv4 Explanation 0 We must check the following n = 2 strings: ip0 = "This line has junk text." is not a valid IPv4 or IPv6 address, so we return Neither in index 0 of our return array. ip1 = "121.18.19.20" is a valid IPv4 address, so we return IPv4 in index 1 of our return array. Sample Input 1 1 2001:0db8:0000:0000:0000:ff00:0042:8329 Sample Output 1 IPv6 Explanation 1 We only have n = 1 value to check. Because ip0 = "2001:0db8:0000:0000:0000:ff00:0042:8329" is a valid IPv6 address, we return IPv6 in index 0 of our return array.
"""

#IP VERIFIER, DETERMINES IF IT IS REAL IPV4 or IPV6

def  checkIP(ip):
    lst = list() #list containing verification results
    correct_parts = False
    all_are_numbers=False
    for index in ip:
        IPv4_parts = index.split(".") #splits the "IP" into a list of parts based on the IPv4 prototcol.
        IPv6_parts = index.split(":") #splits the "IP" into a list of parts based on the IPv6 protocol.
        if len(index) > 1 and len(IPv4_parts) == 4 or len(IPv6_parts) == 8: #check to see if the IPs have the correct lengths
            if len(IPv4_parts) == 4: #further filtering into specific IPv4 verification
                for i in IPv4_parts:
                    for num in i:
                        if num in "0123456789":
                            all_are_numbers=True
                        else:
                            all_are_numbers=False
                            break
                    if all_are_numbers and 0 <= int(i) <= 255:
                        correct_parts=True
                    else:
                        correct_parts=False
                        break
                if correct_parts:
                    lst.append('IPv4')
                else:
                    lst.append('Neither')

            elif len(IPv6_parts) == 8: #further filtering into specific IPv6 verification
                for i in IPv6_parts:
                    if 1 <= len(i) <= 4:
                        for char in i:
                            if char in "0123456789abcdefABCDEF": #assuming IPs are case-sensitive
                                correct_parts=True
                            else:
                                correct_parts=False
                                break
                if correct_parts:
                    lst.append('IPv6')
                else:
                    lst.append('Neither')
        else:
            lst.append('Neither')
    return lst





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
