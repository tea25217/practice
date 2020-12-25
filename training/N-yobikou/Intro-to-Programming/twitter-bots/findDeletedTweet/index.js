'use strict';
const Twitter = require('twitter-lite');
const cron = require('cron').CronJob;
const moment = require('moment-timezone');
const TWITTER_USER_ID = process.env.TWITTER_USER_ID;  // @hogehogeではなく、数字で採番されてるユーザーID

const twitter = new Twitter({
  consumer_key: process.env.TWITTER_API_CONSUMER_KEY,
  consumer_secret: process.env.TWITTER_API_CONSUMER_SECRET,
  access_token_key: process.env.TWITTER_API_ACCESS_TOKEN_KEY,
  access_token_secret: process.env.TWITTER_API_ACCESS_TOKEN_SECRET
});

function sendDirectMessage(message) {
  twitter.post('direct_messages/events/new', {
    event: {
      type: 'message_create',
      message_create: {
        target: {
          recipient_id: TWITTER_USER_ID
        },
        message_data: {
          text: message
        }
      }
    }
  }).then((response) => {
    console.log(response);
  }).catch((err) => {
    console.error(err);
  });
}

const savedTweetsMap = new Map();

function getHomeTimeLine() {
  console.log('cron came!');
  twitter.get('statuses/home_timeline', { count: 200 })
    .then((tweets) => {
      tweets = dateFormats(tweets);

      // 初回起動時は取得するだけで終了
      if (savedTweetsMap.size === 0) {
        tweets.forEach(function(homeTimeLineTweet, key) {
          savedTweetsMap.set(homeTimeLineTweet.id, homeTimeLineTweet); // マップに追加
        });

        return;
      }

      const oldestTime = tweets[tweets.length - 1].created_at;
      savedTweetsMap.forEach(function(savedTweet, key) {
        let isFound = false;
        for (let i = 0; i < tweets.length; i++) {
          if (savedTweet.created_at < oldestTime) {
            // 調査ができなくなったツイート
            savedTweetsMap.delete(key); // 削除
            isFound = true;
            break;
          }
          if (savedTweet.id_str === tweets[i].id_str) {
            // ちゃんと見つかった（削除されていないツイート）
            isFound = true;
            break;
          }
        }
        if (!isFound) {
          const message = `削除されたツイートが見つかりました！\n` +
            `ユーザー名：${savedTweet.user.name}\n` +
            `時刻：${savedTweet.created_at}\n` +
            savedTweet.text;
          sendDirectMessage(message);
          savedTweetsMap.delete(key); // 削除
        }
      });


      // 新しいツイートを追加
      for (let j = 0; j < tweets.length; j++) {
        if (!savedTweetsMap.has(tweets[j].id)) {
          savedTweetsMap.set(tweets[j].id, tweets[j]);
        }
      }

    })
    .catch((err) => {
      console.error(err);
    })

}

// 日付処理
function dateFormats(tweets) {
  tweets.forEach(function(tweet, key) {

    const times = tweet.created_at.split(' ');
    const date = new Date(times[1] + ' ' + times[2] + ', ' + times[5] + ' ' + times[3]);
    tweet.created_at = moment(date).tz('Asia/Tokyo').format('YYYY-MM-DD HH:mm:ss');
  });

  return tweets;

}

const cronJob = new cron({
  cronTime: '00 */2 * * * *', // ２分ごとに実行
  start: true, // newした後即時実行するかどうか
  onTick: function() {
    getHomeTimeLine();
  }
});
getHomeTimeLine();