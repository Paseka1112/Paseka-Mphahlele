import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tweepy
import os
from email.message import EmailMessage

X_BEARER_TOKEN = "MY X_BEARER_TOKEN"
Brand_Name = 'Checkers Sixty60'
keywords = "(broken OR worst OR terrible OR hate OR complaint OR support OR fails)"
Search_Query = f"@{Brand_Name} {keywords} -is:retweet"

it_team = "pasekammphahlele@gmail.com"
pr_team = "pasekammphahlele@gmail.com"
smtp_server = "smtp.gmail.com"  
smtp_port = 587
password = "my password went here" 

def send_email(tweet_text, tweet_id, author_id):
    """An email notification is sent when a possible complaint is found"""
    ##When I ran the program I was surprised to find links to other apps like Tik Tok and Youtube
    tweet_url = f"https://x.com{tweet_id}"

    msg = MIMEMultipart()
    msg['Subject'] = f"Potential X Complaint: @{Brand_Name}"
    msg['From'] = it_team
    msg['To'] = pr_team
    
    body = f"""For your attention: Potential customer complaint detected on X
            User ID: {author_id}
            Tweet Content: "{tweet_text}
            Link: {tweet_url}
            """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(it_team, password)
        server.send_message(msg)
        server.quit()
        print("Email alert send successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_complaints():
    client = tweepy.Client(bearer_token = X_BEARER_TOKEN)
    try:
        response = client.search_recent_tweets(query= Search_Query, 
                tweet_fields = ['created_at', 'author_id'], max_results = 20)

        if response.data:
            print(f"Found {len(response.data)} potential complaints.")
            
            for tweet in response.data:
                send_email(str(tweet.text), tweet.id, tweet.author_id)
        else:
            print("No new complaints found.")

    except Exception as e:
        print(f"Error fetching X API: {e}")

if __name__ == "__main__":
    check_complaints()
