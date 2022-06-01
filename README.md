# ProjectSecu
Ce script est un bot twitter crée avec des API grâce à la plate-forme developer.twitter.com fait en python.

Afin de créer un bot twitter qui nous permet de retweeter, liker et s'abonner à des tweets d'un certain hashtag "#cybersecurity", nous avons proceder comme suit:
1.Creation d'un compte twitter nommé: @UltimateBotGtr
2.Creation d'une App project grâce à https://developer.twitter.com/
3.Activer OAuth 1.0a
4.Modifier les permissions de l'app en "Read and Write"
5.On génére les API keys et les Tokens access et on les mets dans le script credentials.py
6.Création du script twitterbot_retweet.py, ce script permet de: 
  - Vérifier l'état de la connexion au compte.
  - Afficher ses propres tweets avec l'ID du tweet.
  - Afficher les tweets qui sont dans mon fil d'actualité "Home".
  - Afficher les abonnés du compte avec le nom du user.
  - Retweet, like, et follow tous les tweets avec le #cybersecurity.
Remarque : Nous avons choisi le mot cybersecurity mais il est tout à fait possible de changer ce mot, ou d'en ajouter plusieurs en modifiant la ligne contentant QUERY dans le fichier config.py par exemple comme suit : QUERY= ('#cybersecurity OR #hackers OR #kalilinux') le programme exécutera cela selon donc plusieurs hashtags.
