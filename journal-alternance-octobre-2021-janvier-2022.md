---
title: Journal d'activité
subtitle: octobre 2021 janvier 2022
toc-title: <%= t('.toc_title') %>
lang: fr
---

# Projets
- Correction du tentacule Picklog de l'outil de test appelé le Kraken
- Correction de l'activité VerifyCheckSignature du tentacule C21Whitebox du kraken
- Correction de bugs graphiques sur l'interface web Parcel Tracker 5 qui permet de suivre les colis dans le système d'information

## Colis 21
Colis 21 est un système d'information. Il s'agit d'un ensemble de programmes qui communiquent entre eux pour assurer une représentation informatique des réels colis en circulation afin de les tracer, les suivre et d'effectuer des actions en cas d'anomalies détectés.

## Le kraken
Le kraken est un programme qui sert à tester Colis 21 en simulant des colis dans le système d'information 

## Parcel Tracker 5
Parcel Tracker 5 est la 5e version de l'outil Parcel Tracker. Parcel Tracker est une interface web qui permet de suivre l'évolution des colis. Celle-ci est faite en React et se base sur une web service en .Net.

# Périodes

## Correction de l'activité VerifyCheckSignature du tentacule C21Whitebox du Kraken

### Objectifs et missions poursuivies
- Comprendre le fonctionnement du tentacule.
- Comprendre l'API de Colis21
- Comprendre le fonctionnement du moteur
- Corriger l'activité du tentacule

### Actions concrètes (1 à 3 actions par objectif, 5 à 6 lignes par action)
- Reproduction du bug sur l'environnement test-v sur lequel travaille les testeurs puis en local en configurant mon environnement de façon adéquate. Avant même de me lancer dans la correction du bug j'essaie tout d'abord reproduire le bug dans l'environnement de test appelé test-v sur lequel le bug a tout d'abord été détecté. Pour cela j'ai besoin de me connecter en vpn au réseau de l'entreprise afin d'avoir accès aux différents environnements sur lesquels sont le kraken est déployé.

- Une fois le bug reproduit sur l'environnement de test j'essaie de le reproduire en local en configurant mon environnement local avec une nouvelle branche git basée sur la même branche utilisée pour l'environnement test-v et je mets à jour ma base de données mongodb par rapport à la base de données utilisée sur test-v.

- Il me faut ensuite analyser quelles sont les tentacules nécessaires à lancer pour pouvoir lancer mon cas de tests sans avoir. L'idéal est de lancer uniquement les tentacules nécessaires au cas de test choisi et pas les autres car cela aurait pour effet de ralentir mon poste en local.

### Difficultés rencontrées et solutions trouvées (environ 1 page)

#### Analyse

##### Difficulté
Afin de pouvoir me lancer dans la correction du bug j'avais tout d'abord besoin de bien comprendre le fonctionnement de l'application en elle-même. Comme plusieurs services faisant partie du système d'information partagent le même code source en commun, celui-ci est très fourni et il peut être assez difficile d'investiguer quels sont les zones pertinentes dans la résolution du problème. Pour cela j'ai effectué des recherches dans le block note en ligne que partage l'équipe sur One Note pour rechercher des informations concernant le projet sous un aspect technique mais aussi fonctionnel.

##### Solution
Longues périodes d'analyse du code source et du block note contenant des informations sur la partie fonctionnelle et technique du projet

#### Compatiblité de versions

##### Difficulté
Pour bien configurer mon environnement de développement en local afin de corriger le bug, je dois passer par plusieurs étapes. Tout d'abord je dois aller sur le site Azure Devops qui regroupe notre code source et nos tâches à effectuer selon la méthodologie agile. Dessus je dois trouver le bug à résoudre et lui ajouter une nouvelle tâche de réalisation que je dois créer. Il faut ensuite que je crée une nouvelle branche git partant d'une branche git stable du projet qui est d'habiture master. Il faut ensuite lier cette branche à ma tâche de réalisation et récupérer ma branche en local. Une fois cela fait ce n'est pas encore suffisant pour pouvoir lancer le projet en local. En effet le Kraken est un projet qui dépend de middlewares pour fonctionner. Ces middlewares sont RabbitMQ, MongoDB et Logstash. Pour cela il faut les lancer également et grâce à une technologie de conteneurisation appelé Docker cela est rendu possible facilement depuis un fichier texte. Cependant la base de données que j'avais en local n'était pas compatible avec la branche git utilisée. Il m'a donc fallu faire une importation de la base de données depuis l'environnement de test pour m'en servir. Cela est possible grâce à une commande assez longue difficile à retenir.

##### Solution
Comme je devais régulièrement taper la commande permettant l'importation de base de données à des versions différentes selon les branches git utilisées, j'ai réalisé un script Bash permettant de charger des alias permettant de faire cela automatiquemement avec des commandes faciles à retenir.

#### Échec de comparaison

##### Difficulté
Le bug que je devais résoudre était sur un tentacule du kraken. En réalite le Kraken n'est pas un seul programme mais un ensemble de programmes utilisant le framework .Net en C#. Ces programmes sont appelés des tentacules et sont controlées par un programme appelé le Brain. Celui-ci est responsable de démarrer, interagir et stopper les tentacules du kraken. Chaque tentacule est fournie avec une liste d'activités. Ces activités correspondent à une simulation des étapes de la vie d'un colis et les tentacules sont en quelque sorte des catégories d'activités. Il est ensuite possible pour un testeur de combiner ces activités en définissant ce que l'on appelle un cas de test afin de représenter un scénario de la vie d'un colis et de s'assurer que le système d'information se comporte comme il devrait. Le cas de test peut ensuite être exécuté pour lancer la simulation du scénario de la vie du colis.
Erreur dans la comparaison de signatures sous format svg à 1 pixel près

##### Solution
Sollicitation du Tech Lead pour m'orienter dans la recherche de la cause du problème

### Compétences acquises (hard et soft skills) (environ 1 page)

#### Hard skills
Montée en compétences sur RabbitMQ et sur MongoDB

#### Soft skills
En passant par ces différentes étapes j'ai pu me rendre compte 

## Travail sur Parcel Tracker 5

### Objectifs et missions poursuivies
- Comprendre l'organisation du code source du projet React
-> Lecture du code de l'application React et expérimentation sur de nouvelles branches git pour étudier le fonctionnement des composants

- Comprendre la hiérarchie des composants React dans l'application
-> Installation du plugin React-Dev-Tools sur firefox pour afficher la hiérarchie des composants dans la console de firefox

- Trouver leur définition dans le code source
-> Recherche des occurrences des noms de composants en utilisant grep

### Action concrètes (1 à 3 actions par objectif, 5 à 6 lignes par action)

#### Action 1
Déploiement de l'outil Parcel Tracker en local pour reproduire le bug en question

#### Action 2
Déploiement de l'outil 

#### Action 3 

### Difficultés rencontrées et solutions trouvées (environ 1 page)
- Compréhension d'un système très large et complexe pas toujours très bien documenté.

### Compétences acquises (hard et soft skills) (environ 1 page)
- Montée en compétences sur React

# Glossaire
- Git: Logiciel de gestion de version d'un code source. Git permet de tracer l'évolution d'un code source grâce à un historique qui comprend une liste de commits.
- Commit: Un commit est une modification incrémentale du code source que le développeur peut nommer et appliquer à l'historique.
- Branche: Version divergente d'un code source qui comprend une nouvelle historique de commit dont les premiers sont en communs. Un projet git comprend habituellement une branche principale stable appelée "master" et chaque nouvelle fonctionnalité est développée sur une nouvelle branche git basée sur master afin d'être fusionner plus tard.
- Pull Request: Demande de fusion d'une branche git vers une autre (habituellement vers master). Une Pull Request a pour but d'être examiné par les développeurs expérimentés de de l'équipe habituellement le Responsable Technique et les Techs Lead. Si celle-ci est validée par ces membres alors les nouveaux commits ajoutés sur cette branche sont appliqués aussi sur master. On appelle cela la fusion. Remarque la fusion dans un sens et dans l'autre peuvent ne pas produire le même résultat.
- Système d'information: Un système d'information est un ensemble de services utilisant des technologies adaptées pour interagir entre eux afin de collecter, traiter et stocker des données.
- Environnement (Informatique): Un environnement est un contexte sur une machine qui permet de déployer une copie du système d'information afin de le développer et tester ses services.
- Terminal : Application de bureau permettant d'utiliser les programmes d'une machine en tapant une commande sous forme textuelle
- Bash : Langage permettant d'exécuter des commandes pour exécuter des programmes
- React: Framework front-end permettant de rendre des applications web plus dynamiques
- Framework: Ensemble de règles et de librairies qui définissent l'organisation d'un code source pour un type d'application prédéfinit.
- Composant: Terme propre à React qui correspond à une abstraction permettant de simplifier l'organisation du code source
