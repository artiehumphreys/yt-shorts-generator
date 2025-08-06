import praw
from ytshortsgenerator.config import settings


class RedditClient:
    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        user_agent: str | None = None,
    ):
        self.client_id = client_id or settings.reddit_client_id
        self.client_secret = client_secret or settings.reddit_client_secret
        self.user_agent = user_agent or settings.reddit_user_agent
        if not all([self.client_id, self.client_secret, self.user_agent]):
            raise ValueError("Missing Reddit API credentials")
        self.reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
        )

    def fetch_top_story(self, subreddit: str = "AmItheAsshole", limit: int = 20):
        pass
