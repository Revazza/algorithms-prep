import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.user_tweets = {}
        self.user_followings = {}
        self.time = 0

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        if user_id not in self.user_tweets:
            self.user_tweets[user_id] = []
        self.user_tweets[user_id].append((-self.time, tweet_id))
        self.time += 1

    def getNewsFeed(self, user_id: int) -> List[int]:
        followings = self.user_followings.get(user_id, set())

        all_tweets = list(self.user_tweets.get(user_id, []))

        for following in followings:
            tweet = self.user_tweets.get(following, [])
            all_tweets.extend(tweet)

        heapq.heapify(all_tweets)

        return [tweet_id for _, tweet_id in heapq.nsmallest(10, all_tweets)]

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id == followee_id:
            return
        if follower_id not in self.user_followings:
            self.user_followings[follower_id] = set()
        self.user_followings[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if follower_id == followee_id:
            return
        if follower_id in self.user_followings:
            self.user_followings[follower_id].discard(followee_id)