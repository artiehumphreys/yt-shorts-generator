from unittest.mock import patch, MagicMock
import pytest
from ytshortsgenerator.clients.reddit_client import RedditClient


@pytest.fixture(autouse=True)
def setup_env(monkeypatch):
    monkeypatch.setenv("REDDIT_CLIENT_ID", "id")
    monkeypatch.setenv("REDDIT_CLIENT_SECRET", "secret")
    monkeypatch.setenv("REDDIT_USER_AGENT", "agent")


def test_init_missing(monkeypatch):
    monkeypatch.delenv("REDDIT_CLIENT_ID", raising=False)
    with pytest.raises(ValueError):
        RedditClient()


@patch("ytshortsgenerator.clients.reddit_client.praw.Reddit")
def test_fetch_top_story(mock_reddit):
    fake = MagicMock()
    fake.is_self = True
    fake.over_18 = False
    fake.title = "Test"
    fake.selftext = "Body"
    mock_reddit.return_value.subreddit.return_value.hot.return_value = [fake]

    client = RedditClient()
    story = client.fetch_top_story(limit=1)
    assert story == {"title": "Test", "body": "Body"}
