from src.backend.groq_chat import req_groq_langchain
from src.config.constants import Roles
from src.backend.func.twitter import make_tweet

def main():
    tweet = req_groq_langchain(Roles.TASK_SOCIAL_MEDIA_POSTER, "I am starting a facebook clone called netbox, create a tweet on an interesting topic and make it big")
    make_tweet(tweet["text"])
    
if __name__ == "__main__":
    main()
