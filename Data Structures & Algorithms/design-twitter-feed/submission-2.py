class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)   # userId -> [[count, tweetId]]
        self.followMap = defaultdict(set)   # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])  # store tweet with timestamp
        self.count -= 1                                      # newer tweet gets smaller count

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []   # stores newest tweet from each followed user

        self.followMap[userId].add(userId)   # user also sees their own tweets

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1   # start from newest tweet
                count, tweetId = self.tweetMap[followeeId][index]

                # count, tweetId, user, index of next older tweet
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)  # get newest tweet
            res.append(tweetId)                                         # add to feed

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]       # get next older tweet
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)   # add followee

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)   # remove followee