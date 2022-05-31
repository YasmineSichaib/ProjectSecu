# ProjectSecu
Ce script est un bot twitter crée avec des API grâce à la plate-forme developer.twitter.com fait en python.

Afin de créer un bot twitter qui nous permet de retweeter, liker et s'abonner à des tweets d'un certain hashtag "#cybersecurity", nous avons proceder comme suit:
1.Creation d'un compte twitter nommé: @UltimateBotGtr
2.Creation d'une App project grâce à https://developer.twitter.com/
3.Activer OAuth 2.0
4.Modifier les permissions de l'app en "Read and Write"
5.On génére les API keys et les Tokens access et on les mets dans le script credentials.py
6.Création du script twitterbot_retweet.py, ce script permet de: 
  - Vérifier l'état de la connexion au compte.
  - Afficher ses propres tweets.
  - Afficher les abonnés du compte avec le nom du user.
  - Retweet, like, et follow tous les tweets avec le #cybersecurity
