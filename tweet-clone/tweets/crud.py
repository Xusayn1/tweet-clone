from typing import List, Any
from core.db_settings import execute_query
from psycopg2.extras import DictRow


def get_all_tweets(offset: int = 0, sort_by_likes: bool = False) -> List[DictRow]:
    """
    Fetches 5 tweets at a time with optional sorting by popularity (likes).
    :param offset: Number of tweets to skip for pagination.
    :param sort_by_likes: If True, sorts by like count, otherwise by date.
    :return: List of tweets with author and like count.
    """
    order_by: str = "like_count DESC" if sort_by_likes else "t.created_at DESC"

    query: str = f"""
        SELECT t.id, u.username, t.tweet, t.created_at,
               (SELECT COUNT(*) FROM likes WHERE tweet_id = t.id) as like_count
        FROM tweets t
        JOIN users u ON t.user_id = u.id
        ORDER BY {order_by}
        LIMIT 5 OFFSET %s
    """

    result: Any = execute_query(query=query, params=(offset,), fetch="all")
    return result if isinstance(result, list) else []


def add_new_tweet_ui(user_id: int) -> None:
    """
    Handles user input to create a new tweet. Matches '4. Add Tweet' in main menu.
    """
    content: str = input("\nWhat's on your mind?: ").strip()

    if not content:
        print("❌ Tweet content cannot be empty.")
        return

    query: str = "INSERT INTO tweets (user_id, tweet) VALUES (%s, %s)"
    if execute_query(query=query, params=(user_id, content)):
        print("✅ Tweet posted successfully!")
    else:
        print("❌ Error: Could not save your tweet.")


def show_my_tweets_ui(user_id: int) -> None:
    """
    Displays tweets posted by the current user. Matches '2. My Tweets'.
    """
    query: str = """
        SELECT t.id, t.tweet, t.created_at, 
               (SELECT COUNT(*) FROM likes WHERE tweet_id = t.id) as like_count
        FROM tweets t
        WHERE t.user_id = %s 
        ORDER BY t.created_at DESC
    """
    my_tweets: Any = execute_query(query=query, params=(user_id,), fetch="all")

    if not my_tweets:
        print("\n--- You haven't posted any tweets yet ---")
        return

    print("\n" + "=" * 15 + " YOUR TWEET HISTORY " + "=" * 15)
    for tweet in my_tweets:
        date_str: str = tweet['created_at'].strftime('%Y-%m-%d %H:%M') if tweet['created_at'] else "N/A"

        print(f"ID: {tweet['id']} | ❤️ Likes: {tweet['like_count']}")
        print(f"Content: {tweet['tweet']}")
        print(f"Date: {date_str}")
        print("-" * 45)
    print("=" * 50)


def delete_tweet_ui(user_id: int) -> None:
    """
    Deletes a tweet belonging to the user. Matches '1. Delete my tweet' in sub-menu.
    """
    try:
        tweet_id: int = int(input("Enter Tweet ID to delete: "))

        query: str = "DELETE FROM tweets WHERE id = %s AND user_id = %s"
        result: Any = execute_query(query=query, params=(tweet_id, user_id))

        if result:
            print(f"✅ Tweet #{tweet_id} has been deleted.")
        else:
            print("❌ Access denied or Tweet not found.")
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")