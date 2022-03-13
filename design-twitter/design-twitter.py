class Twitter:
    from collections import defaultdict
    def __init__(self):
        # (user, posts)
        self.posts = []
        # (follower, followee)
        self.flw = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        n = len(self.posts)
        for i in range(n-1, -1, -1):
            uid, twid = self.posts[i]
            if uid in self.flw[userId] or uid == userId:
                out.append(twid)
            if len(out) == 10:
                break
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.flw[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.flw[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)