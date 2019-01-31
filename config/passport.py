from authomatic.providers import oauth2

SOCIAL_LOGIN = {
    'default': 'google',

    'google': {
        'class_': oauth2.Google,

        'consumer_key': '923896266353-tse696iqi8qgkajjq5ue858316m03ht6.apps.googleusercontent.com',
        'consumer_secret': 'W-kGDtJqCX_K3IaXRpH9KW4B',

        'scope': oauth2.Google.user_info_scope,
        'url': 'https://www.googleapis.com/userinfo/v2/me',
    },
}
