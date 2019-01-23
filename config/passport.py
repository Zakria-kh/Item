from authomatic.providers import oauth2

SOCIAL_LOGIN = {
    'default': 'google',

    'google': {
        'class_': oauth2.Google,

        'consumer_key': '923896266353-pi3m0bmf0ina2eeke3ftvo0oj8fmf27i.apps.googleusercontent.com',
        'consumer_secret': '6duG-Mm70NdMJp7YU5XwkMQv',

        'scope': oauth2.Google.user_info_scope,
        'url': 'https://www.googleapis.com/userinfo/v2/me',
    },
}
