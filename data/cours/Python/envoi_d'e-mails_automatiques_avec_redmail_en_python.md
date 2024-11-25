
**Redmail** est une bibliothèque Python qui permet d'envoyer des e-mails de manière simple et rapide en utilisant des services de messagerie tels que **Gmail**. Voici un guide pour utiliser **Redmail** pour envoyer des e-mails automatisés à partir de Python.

## Pré-requis

Avant d'envoyer des e-mails avec **Redmail**, vous devez :
1. Avoir un compte **Gmail** actif.
2. Générer un **mot de passe d'application** pour garantir la sécurité lors de l'utilisation de Redmail. Pour ce faire, rendez-vous sur le lien suivant : [Google App Passwords](https://myaccount.google.com/apppasswords).

Le mot de passe d'application est un mot de passe spécifique que Google génère pour permettre à des applications tierces d'accéder à votre compte sans divulguer vos identifiants personnels.

## Installation de Redmail

Pour installer **Redmail**, utilisez la commande suivante :

```bash
pip install redmail
```

## Exemple de Script pour Envoyer un E-mail

Voici un exemple de script Python utilisant **Redmail** pour envoyer un e-mail via **Gmail** :

```python
from redmail import gmail

# Remplacez par votre adresse Gmail et le mot de passe d'application
gmail.username = "votre_adresse@gmail.com"
gmail.password = "votre_mot_de_passe_d_application"

gmail.send(
    subject="Email de test",
    receivers=["destinataire@example.com"],
    text="Ceci est un email de test envoyé avec Redmail et Gmail."
)
```

### Explication du Code
- **`from redmail import gmail`** : Importation de la classe `gmail` de la bibliothèque **Redmail**.
- **`gmail.username`** : Renseignez votre adresse Gmail.
- **`gmail.password`** : Utilisez le **mot de passe d'application** généré par Google.
- **`gmail.send()`** : Utilisez cette fonction pour envoyer un e-mail. Les paramètres incluent :
  - `subject` : Le sujet de l'email.
  - `receivers` : Une liste d'adresses e-mail des destinataires.
  - `text` : Le corps du message.

## Considérations de Sécurité

- **Ne partagez jamais votre mot de passe d'application** : Il est important de garder le mot de passe d'application privé et sécurisé.
- **Variables d'Environnement** : Il est recommandé d'utiliser des **variables d'environnement** pour stocker votre nom d'utilisateur et votre mot de passe afin de ne pas les inclure directement dans votre script.

Exemple d'utilisation avec des variables d'environnement :

```python
import os
from redmail import gmail

# Récupérer les identifiants à partir des variables d'environnement
gmail.username = os.getenv("GMAIL_USERNAME")
gmail.password = os.getenv("GMAIL_APP_PASSWORD")

gmail.send(
    subject="Email de test sécurisé",
    receivers=["destinataire@example.com"],
    text="Cet email est envoyé en utilisant des variables d'environnement pour plus de sécurité."
)
```

## Lien vers les Mots de Passe d'Application
Pour générer un mot de passe d'application, suivez ce lien : [Google App Passwords](https://myaccount.google.com/apppasswords).

## Conclusion
Avec **Redmail**, l'envoi d'e-mails en Python est à la fois **simple** et **sûr**, tant que vous suivez les bonnes pratiques de sécurité, telles que l'utilisation des mots de passe d'application et des variables d'environnement. Cette méthode est idéale pour automatiser l'envoi de notifications, d'alertes, ou pour tester des fonctionnalités dans des projets personnels.