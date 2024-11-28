# Gestionnaire de Clés SSH et GPG 🔐

![Application Screenshot](screenshot.webp)

**Une application moderne et intuitive pour simplifier la gestion de vos clés SSH et GPG.**

---

## 🎯 **Fonctionnalités principales**

- **Lister les clés existantes**  
  📄 Affiche toutes les clés SSH présentes dans votre dossier `~/.ssh`.

- **Supprimer toutes les clés**  
  🗑️ Supprime toutes vos clés SSH ainsi que le fichier `config`.

- **Supprimer une clé spécifique**  
  🚮 Supprime une clé spécifique sélectionnée par l'utilisateur.

- **Générer une clé SSH**  
  🔑 Crée une nouvelle clé SSH avec les types supportés : `ed25519` et `RSA`.

- **Générer une clé GPG pour GitHub**  
  🔏 Générez une clé GPG pour signer vos commits sur GitHub.

- **Voir/Éditer le fichier `config`**  
  🛠️ Affiche ou modifie facilement le fichier `config` présent dans le dossier `~/.ssh`.

- **Quitter**  
  ❌ Ferme l'application rapidement et proprement.

---

## ✨ **Pourquoi utiliser cette application ?**

Cette application est un véritable gain de temps pour toute personne travaillant avec des clés SSH ou GPG, qu'il s'agisse de développeurs, administrateurs système, ou novices dans ces technologies. 

Avec une interface moderne et conviviale, elle vous permet de :
- **Créer, gérer et supprimer des clés facilement** sans passer par des lignes de commande complexes.
- **Améliorer votre productivité** grâce à des outils rapides et simples d'utilisation.
- **Configurer vos clés GitHub et autres services** en quelques clics seulement.

---

## 📥 **Installation**

1. **Cloner le dépôt**  
   Téléchargez le projet en exécutant :  
   `git clone https://github.com/votre-utilisateur/ssh-key-manager.git`  

   Accédez au dossier :  
   `cd ssh-key-manager`

2. **Configurer l'environnement virtuel**  
   Créez un environnement Python virtuel et activez-le :  
   `python -m venv venv`  
   `.\venv\Scripts\activate`

3. **Installer les dépendances**  
   Exécutez :  
   `pip install -r requirements.txt`

4. **Générer l'exécutable**  
   Utilisez le script fourni pour compiler l'application :  
   `.\build.bat`

5. **Lancer l'application**  
   Une fois la compilation terminée, l'exécutable sera disponible dans le dossier `dist` :  
   `dist\ssh_key_manager.exe`

---

## 🛠 **Dossiers et fichiers inclus**

- **`README.md`** : Documentation détaillée du projet.  
- **`ssh_key_manager.py`** : Fichier principal contenant le code de l'application.  
- **`requirements.txt`** : Liste des dépendances nécessaires pour exécuter ou compiler l'application.  
- **`build.bat`** : Script pour installer les dépendances et générer l'exécutable.  
- **Dossier `icons`** : Contient les icônes utilisées pour enrichir l'interface utilisateur.  
- **Dossier `dist`** : Contient l'exécutable après compilation.  

---

## 🚧 **Problèmes connus**

### 1. **Fichier `config` ne s'ouvre pas dans Visual Studio Code**  
   Le fichier `~/.ssh/config` ne s'ouvre pas dans VS Code, même après avoir ajouté son exécutable au PATH sous Windows.

   **Solution temporaire :**  
   Vérifiez si l'exécutable de VS Code est bien accessible depuis le terminal :
   `code --version`  

   Si cela ne fonctionne pas, ouvrez manuellement le fichier ou remplacez l'éditeur par un autre dans le code de l'application.

---

### 2. **Les icônes ne s'affichent pas correctement**  
   Bien que les fichiers d'icônes soient présents dans le dossier `icons`, elles n'apparaissent pas sur les boutons de l'application.

   **Solution temporaire :**  
   Vérifiez que les chemins vers les icônes sont corrects dans le fichier Python (`ssh_key_manager.py`) et assurez-vous que les fichiers sont au bon format (PNG, ICO).

---

## 🤝 **Comment contribuer ?**

Si vous souhaitez aider, voici quelques axes d'amélioration possibles :  
- Résoudre les problèmes liés à l'ouverture du fichier `config` dans VS Code.  
- Corriger l'affichage des icônes sur les boutons de l'application.  
- Ajouter de nouvelles fonctionnalités, comme la gestion avancée des clés GPG.  
- Tester l'application sur différents systèmes et signaler des bugs.

Pour contribuer, faites un fork du projet, effectuez vos modifications, puis soumettez une Pull Request !  

---

## 📄 **Cahier des charges** 

- **Objectif principal :** Simplifier la gestion des clés SSH et GPG grâce à une application visuelle et intuitive.  
- **Contraintes :**  
  - Compatibilité avec Windows 10 et 11.  
  - Interface utilisateur moderne avec un thème sombre et des animations fluides.  
  - Outils intégrés pour générer et gérer les clés sans utiliser la ligne de commande.  

---

Merci d'utiliser le **Gestionnaire de Clés SSH et GPG** ! N'hésitez pas à partager vos retours pour l'améliorer davantage 🚀.
