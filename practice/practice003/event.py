# coding: utf-8
"""twitterAPIを使用してワード検索し結果をCSV保存

    下記記事のコードを元にさせて頂き作成

    「停電」に関するツイートをpythonで収集して、WordCloudで可視化してみた
    https://qiita.com/pocket_kyoto/items/0f43c9fdce87bddd31cf

"""

import json
import time
import calendar
import csv
from requests_oauthlib import OAuth1Session


# twitterAPIのキーを記載したテキストファイル(.gitignoreに設定するよう注意)
#
#    以下の形式で記載
#
#    consumer_key:hogehoge
#    consumer_secret:fugafuga
#    access_token:piyopiyo
#    access_secret:foobar
#
FILEPASS_API_KEYS = "./key.txt"

# APIリクエストの繰り返し回数。ツイート取得可能数に100ツイート/リクエストの制限があるため、指定回数ループする。
API_REPEATS = 10


def main(word: str) -> bool:
    """
    Args:
        word(string): 検索ワード

    Returns:
        bool: 1件以上の検索結果を格納したCSVファイルを作成できたらTrue, それ以外はFalse

    """
    flag = False
    KEYS = loadAPIKey(FILEPASS_API_KEYS)
    if (not word) or (not KEYS):
        return flag

    twitter = OAuth1Session(KEYS['consumer_key'], KEYS['consumer_secret'],
                            KEYS['access_token'], KEYS['access_secret'])
    tweets = getTwitterData(twitter, word, repeat=API_REPEATS)
    flag = makeCSVFromTweets(tweets)

    return flag


def loadAPIKey(filepass):
    """
    Args:
        filepass(string): APIキーを記載したファイルのパス

    Returns:
        dict or bool: 必要なAPIキーを全て読み込めた場合、辞書型で"APIキーの項目名:APIキーの値"。それ以外はFalse。

    """
    APIkeys = {}
    requiredKeys = [
        "consumer_key", "consumer_secret", "access_token", "access_secret"
    ]

    try:
        f = open(filepass)
    except OSError:
        return False

    try:
        l_strip = [s.strip() for s in f.readlines()]
        f.close()
        APIkeys.update([i.split(":") for i in l_strip])
    except Exception:
        return False

    for requiredKey in requiredKeys:
        if requiredKey not in APIkeys:
            return False

    return APIkeys


def getTwitterData(twitter, key_word, repeat=10):
    """
    Args:
        twitter(obj): OAuth認証済みのセッション
        key_word(string): 検索ワード
        repeat(int): APIリクエストの繰り返し回数。1回あたり最大100ツイートしか検索できないため、繰り返しリクエストする。

    Returns:
        array of dict: 辞書型に変換したツイート情報を、各ツイートを要素とする配列で返却。

    """
    # TwitterAPIのエンドポイントと取得用のパラメータ
    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {'q': key_word, 'count': '100', 'result_type': 'recent'}

    tweets = []

    mid = -1

    for i in range(repeat):
        params['max_id'] = mid  # midよりも古いIDのツイートのみを取得する
        res = twitter.get(url, params=params)
        if res.status_code == 200:  # 正常通信出来た場合

            sub_tweets = json.loads(res.text)['statuses']  # レスポンスからツイート情報を取得

            user_ids = []
            for tweet in sub_tweets:
                user_ids.append(int(tweet['id']))
                tweets.append(tweet)

            # ループで取得したmidよりも古いツイートを取るための工夫
            if len(user_ids) > 0:
                min_user_id = min(user_ids)
                mid = min_user_id - 1
            else:
                mid = -1
            print(mid)  # 時系列で見た時に最も古いツイートID

        else:  # 正常通信出来なかった場合
            print("Failed: %d" % res.status_code)

    print("ツイート取得数：%s" % len(tweets))
    return tweets


def YmdHMS(created_at):
    time_utc = time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
    unix_time = calendar.timegm(time_utc)
    time_local = time.localtime(unix_time)
    return time.strftime("%Y/%m/%d %H:%M:%S", time_local)


def makeCSVFromTweets(tweets):
    """
    Args:
        tweets(array of dict): 辞書型のツイート情報を要素とする配列

    Returns:
        bool: 1件以上のツイート情報を格納したCSVファイルを作成できたらTrue, それ以外はFalse

    """
    CATEGORY = [
        'created_at', 'screen_name', 'name', 'id_str', 'text', 'id_str',
        'in_reply_to_user_id_str', 'is_quote_status', 'lang'
    ]

    if len(tweets) == 0:
        return False

    try:
        with open("result.csv", "w", encoding="utf_8") as f:
            writer = csv.writer(f)
            writer.writerow(CATEGORY)
            for tweet in tweets:
                row = [
                    tweet['created_at'], tweet['user']['screen_name'],
                    tweet['user']['name'], tweet['user']['id_str'],
                    tweet['text'], tweet['id_str'],
                    tweet['in_reply_to_user_id_str'], tweet['is_quote_status'],
                    tweet['lang']
                ]
                for value in row:
                    if type(value) == "str":
                        value = value.encode("utf_8", 'backslashreplace')
                writer.writerow(row)
    except csv.Error:
        return False

    return True
