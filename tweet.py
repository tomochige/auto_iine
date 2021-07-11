import os
import tweepy
#from dotenv import load_dotenv
import datetime
import random
import time
#import smtplib, ssl
#from email.mime.text import MIMEText


def main():
    #load_dotenv(override=True)
    mm = random.randrange(60,1800)
    print(f"待機:{mm}秒***************************")
    time.sleep(mm)

    #GAC = os.environ['GAC']
    #GPW = os.environ['GPW']

    CK = os.environ['CK']
    CS = os.environ['CS']
    AT = os.environ['AT']
    ATS = os.environ['ATS']

    #TOADD = os.environ['TOADD']

    keyword_arr = ['#駆け出しエンジニアと繋がりたい','#Webデザイナーと繋がりたい','#プログラミング初心者','#今日の積み上げ','#プログラミング','#Python']
    keyword_no = random.randrange(0,5)
    search_word = keyword_arr[keyword_no]
    
    auth = tweepy.OAuthHandler(CK,CS)
    auth.set_access_token(AT,ATS)
    api = tweepy.API(auth)

    count = random.randrange(5,15)

    #print(f"search:{search_word}｜count:{count}")

    tweets = api.search(search_word,
                    include_entities=True,
                    tweet_mode="extended",
                    lang="ja",
                    count=count,
                    execlude="retweets",
                    execlud_replies=True
                    )

    for tweet in tweets:
        id = tweet.id  # id取得
        # いいねするツイート内容を改行なしで取得
        text = tweet.full_text.replace('\n', '')
        # いいねをする。(いいねがされているものをもう一度いいねするとエラーが出るので、例外処理)
        
        try:
            wait_time = random.randrange(10,60)
            #print(f"id:{id}｜wait_time:{wait_time}｜text:{text}")
            time.sleep(wait_time)
            api.create_favorite(id)
        except:
            pass
        
    print(f"{search_word} で{count}件いいねしました。最後のいいねツイートは https://twitter.com/tomyamkn3/status/{id}")
    
    '''
    #メール送信
    # メールデータ(MIME)の作成 --- (*3)
    subject = "いいね定期連絡"
    body = f"{search_word} で{count}件いいねしました。最後のいいねツイートは https://twitter.com/tomyamkn3/status/{id}"
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["To"] = TOADD
    msg["From"] = GAC

    # Gmailに接続 --- (*4)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
        context=ssl.create_default_context())
    server.login(GAC, GPW)
    server.send_message(msg) # メールの送信    
    '''

if __name__ == "__main__":
    main()

