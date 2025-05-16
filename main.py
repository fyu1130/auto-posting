import tweepy
import schedule
import time
import json
from datetime import datetime

# 設定ファイル読み込み
def load_accounts():
    with open("accounts.json", "r") as f:
        return json.load(f)

# 投稿処理
def post_tweet(account):
    try:
        auth = tweepy.OAuth1UserHandler(
            account["api_key"],
            account["api_secret"],
            account["access_token"],
            account["access_token_secret"]
        )
        api = tweepy.API(auth)
        api.update_status(account["message"])
        print(f"{datetime.now()} - {account['id']} 投稿成功")
    except Exception as e:
        print(f"{datetime.now()} - 投稿失敗：{account['id']} → {e}")

# スケジュール登録
def setup_schedule():
    accounts = load_accounts()
    for account in accounts:
        schedule.every().day.at(account["post_time"]).do(post_tweet, account)

if __name__ == "__main__":
    setup_schedule()
    print("スケジューラ起動中...")
    while True:
        schedule.run_pending()
        time.sleep(1)
