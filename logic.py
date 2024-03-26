import tweepy, config

class Logic:
    def __init__(self):
        self.init_api()
        self.get_user_settings()
        self.should_post = True

    def init_api(self):
        self.client = tweepy.Client(
            consumer_key=config.API_KEY, consumer_secret=config.API_KEY_SECRET,
            access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET
        )

    def get_user_settings(self):
        with open(config.DATABASE_PATH, mode='r') as data:
            datalines = data.readlines()

        self.settings = {
            'ADD_TO_CLIPBOARD_AFTER_POSTING':bool(datalines[1].split('=')[1])
            }
        
    def change_setting(self, setting):
        self.settings[setting.split('=')[0]] = setting.split('=')[1]

        datalines = [key+'='+value+'\n' for key, value in self.settings.items()]; datalines.insert(0, 'User Settings\n')

        with open(config.DATABASE_PATH, mode='w') as data:
            data.writelines(datalines)

    def post(self, text):
        try:
            response = self.client.create_tweet(text=text); print(f"https://x.com/user/status/{response.data['id']}")
            print(response.data)
            return response
        except:
            return False
    