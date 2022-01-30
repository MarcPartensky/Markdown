# Journal d'activité 2021-2022

## Projets

- Correction du tentacule Picklog de l'outil de test appelé le Kraken
- Correction de l'activité VerifyCheckSignature du tentacule C21Whitebox du kraken
- Correction de bugs graphiques sur l'interface web Parcel Tracker 5 qui permet de suivre les colis dans le système d'information

Période 1 (durée pertinente à déﬁnir par l’apprenti selon la mission)

## Périodes

### Travail sur le Kraken

#### Objectifs et missions poursuivies
- Comprendre le fonctionnement du tentacule.
- Comprendre l'API de Colis21
- Comprendre le fonctionnement du moteur
- Corriger l'activité du tentacule

#### Action concrètes (1 à 3 actions par objectif, 5 à 6 lignes par action)
- Reproduction du bug sur l'environnement test-v sur lequel travaille les testeurs puis en local en configurant mon environnement de façon adéquate.
- Action 2
- Action 3

#### Difficultés rencontrées et solutions trouvées (environ 1 page)
- Compréhension d'un système très large et complexe pas toujours très bien documenté
-> Longues périodes d'analyse du code source et du block note contenant des informations sur la partie fonctionnelle et technique du projet
- Erreur dans la comparaison de signatures sous format svg à 1 pixel près
-> Sollicitation du Tech Lead pour m'orienter dans la recherche de la cause du problème
- Compatibilité des branches git de développement avec les versions de la base de données dans mongodb
-> Mise en place d'un script facilitant la mise à jour des bases de données en local grâces à des fonctions bash

#### Compétences acquises (hard et soft skills) (environ 1 page)
- Montée en compétences sur RabbitMQ et sur MongoDB

### Travail sur Parcel Tracker 5

#### Objectifs et missions poursuivies
- Comprendre l'organisation du code source du projet React
-> Lecture du code de l'application React et expérimentation sur de nouvelles branches git pour étudier le fonctionnement des composants
- Comprendre la hiérarchie des composants React dans l'application
-> Installation du plugin React-Dev-Tools sur firefox pour afficher la hiérarchie des composants dans la console de firefox
- Trouver leur définition dans le code source
-> Recherche des occurrences des noms de composants en utilisant grep

#### Action concrètes (1 à 3 actions par objectif, 5 à 6 lignes par action)
- Déploiement de l'outil Parcel Tracker en local pour reproduire le bug en question
- 
- Action 3

#### Difficultés rencontrées et solutions trouvées (environ 1 page)
- Compréhension d'un système très large et complexe pas toujours très bien documenté.

#### Compétences acquises (hard et soft skills) (environ 1 page)
- Montée en compétences sur React

## Glossaire
- Terminal : Application de bureau permettant d'utiliser les programmes d'une machine en tapant une commande sous forme textuelle
- Bash : Langage permettant d'exécuter des commandes pour exécuter des programmes
- React: Framework front-end permettant de rendre des applications web plus dynamiques
- Framework: Ensemble de règles et de librairies qui définissent l'organisation d'un code source pour un type d'application prédéfinit.
- Composant: Terme propre à React qui correspond à une abstraction permettant de simplifier l'organisation du code source
