from typing import Any
from core.db_settings import execute_query


def add_like_ui(user_id: int) -> None:
    """
    Handles adding a like to a tweet. Includes duplicate check.
    """
    try:
        tweet_id: int = int(input("Enter Tweet ID to like: "))

        check_query: str = "SELECT id FROM likes WHERE user_id = %s AND tweet_id = %s"
        if execute_query(query=check_query, params=(user_id, tweet_id), fetch="one"):
            print("You have already liked this tweet.")
            return

        query: str = "INSERT INTO likes (user_id, tweet_id) VALUES (%s, %s)"
        if execute_query(query=query, params=(user_id, tweet_id)):
            print("❤️ Successfully liked!")
    except ValueError:
        print("❌ Invalid ID format. Please enter a number.")
    except Exception as e:
        print(f"❌ Error adding like: {e}")


def remove_like_ui(user_id: int) -> None:
    """
    Handles removing a like (Unlike).
    """
    try:
        tweet_id: int = int(input("Enter Tweet ID to unlike: "))

        check_query: str = "SELECT id FROM likes WHERE user_id = %s AND tweet_id = %s"
        if not execute_query(query=check_query, params=(user_id, tweet_id), fetch="one"):
            print("You haven't liked this tweet yet.")
            return

        query: str = "DELETE FROM likes WHERE user_id = %s AND tweet_id = %s"
        if execute_query(query=query, params=(user_id, tweet_id)):
            print("Like removed.")
    except ValueError:
        print("❌ Invalid ID format.")


def show_liked_tweets_ui(user_id: int) -> None:
    """
    Displays all tweets that the current user has liked.
    Matches '3. Liked Tweets' in the main menu.
    """
    query: str = """
        SELECT t.id, t.tweet, t.created_at, u.username 
        FROM tweets t
        JOIN likes l ON t.id = l.tweet_id
        JOIN users u ON t.user_id = u.id
        WHERE l.user_id = %s
        ORDER BY l.created_at DESC
    """
    liked_tweets: Any = execute_query(query=query, params=(user_id,), fetch="all")

    if not liked_tweets:
        print("\n--- You haven't liked any tweets yet ---")
        return

    print("\n" + "❤️  YOUR LIKED TWEETS " + "=" * 30)
    for tweet in liked_tweets:
        date_str: str = tweet['created_at'].strftime('%Y-%m-%d %H:%M') if tweet['created_at'] else "N/A"

        print(f"ID: {tweet['id']} | Author: @{tweet['username']}")
        print(f"Content: {tweet['tweet']}")
        print(f"Posted on: {date_str}")
        print("-" * 45)
    print("=" * 50)


def get_tweet_likes_count(tweet_id: int) -> int:
    """
    Returns the total number of likes for a specific tweet.
    """
    query: str = "SELECT COUNT(*) as count FROM likes WHERE tweet_id = %s"
    result: Any = execute_query(query=query, params=(tweet_id,), fetch="one")
    return result['count'] if result else 0