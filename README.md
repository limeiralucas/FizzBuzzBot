# FizzBuzz Twitter Bot

## How to run:

### Clone the repository and access the project root

```
git clone https://github.com/lucasalveslm/FizzBuzzBot.git && cd FizzBuzzBot
```

### Create .env file on project's root directory and fill with your app and account info

```
FZ_DB_HOST="mysql"

TW_CONSUMER_KEY="twitter_app_key"
TW_CONSUMER_SECRET="twitter_app_secret"

TW_OAUTH_TOKEN="twitter_account_oauth_token"
TW_OAUTH_TOKEN_SECRET="twitter_oauth_secret"

CELERY_RESULT_BACKEND_HOST="redis"
CELERY_RESULT_BACKEND_DB="1"

BROKER_HOST="redis"
BROKER_DB="1"

REDIS_HOST="redis"
REDIS_DB="0"
```

### Run the containers

```
docker-compose up
```

### How to use

#### Just tweet a mention to the profile you used on bot configuration with a number. You can test it right now tweet to @FizzBuzzBot1

```
@FizzBuzzBot1 15
```
