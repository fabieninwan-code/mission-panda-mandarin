# 🐼 Mission Panda Mandarin — Version Android (Kivy)

Même application que la version desktop, réécrite avec **Kivy**, le
framework Python standard pour produire des apps mobiles (Android/iOS)
en gardant tout le code en Python.

## ⚠️ À savoir avant de commencer

Il y a **deux étapes bien distinctes** :

1. **Tester l'app sur votre ordinateur** (rapide, 2 commandes) — utile
   pour vérifier que tout fonctionne avant de se lancer dans la
   compilation mobile.
2. **Compiler un vrai fichier `.apk`** installable sur téléphone
   (beaucoup plus long : ça télécharge le SDK/NDK Android, plusieurs
   Go, et ne fonctionne que sous Linux ou WSL — pas nativement sous
   Windows/Mac).

Je ne peux pas fabriquer le `.apk` moi-même dans cet environnement (pas
d'accès réseau ni de système Linux avec Buildozer ici) : le code est
prêt, mais la compilation doit se faire de votre côté, en suivant les
instructions ci-dessous.

---

## Étape 1 — Tester sur votre PC (avant de compiler pour Android)

```bash
pip install -r requirements.txt
python main.py
```

Une fenêtre s'ouvre avec l'interface tactile (même sur PC, avec la
souris). Comme il n'y a pas de vrai enregistrement micro par ce biais
sur desktop, l'app utilise le **mode démo** (voix simulées) pour que
vous puissiez naviguer dans tous les écrans et vérifier que tout
s'affiche correctement.

## Étape 2 — Compiler l'APK Android (avec Buildozer)

Buildozer ne fonctionne que sous **Linux** (nativement) ou via
**WSL** sous Windows (Sous-système Windows pour Linux).

### Sous Windows : installer WSL d'abord
```bash
wsl --install
```
Redémarrez, puis ouvrez le terminal "Ubuntu" installé.

### Puis, dans votre terminal Linux/WSL :
```bash
sudo apt update
sudo apt install -y python3-pip git zip unzip openjdk-17-jdk autoconf libtool pkg-config
pip3 install buildozer cython

cd mandarin_app_android
buildozer android debug
```

La première compilation **télécharge automatiquement** le SDK et le
NDK Android (plusieurs Go) et peut prendre **30 minutes à 1 heure**.
Les suivantes sont beaucoup plus rapides.

Le fichier `.apk` apparaît dans `bin/missionpandamandarin-0.1-debug.apk`.

### Installer l'APK sur le téléphone
- Transférez le fichier `.apk` sur le téléphone (câble USB, e-mail,
  Drive...) puis ouvrez-le pour l'installer (il faudra autoriser
  "Sources inconnues" dans les paramètres Android).
- Ou, téléphone branché en USB avec le débogage activé :
  ```bash
  buildozer android deploy run
  ```

### Alternative sans installer Linux
Si vous ne voulez pas passer par WSL, il existe des services en ligne
gratuits qui exécutent Buildozer pour vous à partir d'un dépôt GitHub
(par ex. GitHub Actions avec une action Buildozer). Cherchez
"buildozer github actions kivy" — c'est plus long à configurer la
première fois, mais ne nécessite pas d'installer Linux localement.

---

## Différences techniques avec la version desktop

| Aspect | Desktop (Tkinter) | Android (Kivy) |
|---|---|---|
| Interface | Tkinter | Kivy (fichiers `.kv`) |
| Micro | `sounddevice` (accès direct continu) | `plyer` (enregistre vers un fichier `.wav`, relu ensuite — API native Android) |
| Courbe de ton | `matplotlib` | Dessin natif Kivy (`Line`/`Ellipse`) — bien plus léger sur mobile |
| Stockage profil | Fichier JSON dans le dossier du projet | Fichier JSON dans `App.user_data_dir` (seul emplacement garanti accessible sans permission spéciale) |
| Analyse du ton (autocorrélation) | **Identique** | **Identique** (`core/audio_analyse.py`) |
| Données (vocabulaire, missions) | **Identiques** (`data/*.json`) | **Identiques** |

## Limites de cette V1 (mêmes que la version desktop)

- Reconnaissance de ton par autocorrélation simple (suffisant pour un
  prototype pédagogique, à améliorer avec un modèle de pitch-tracking
  plus robuste pour une mise en production).
- Pas de vraie reconnaissance de phrase complète pour le module
  Mission Survie (évaluation approximative ton par ton).
- Pas encore de fichiers audio de voix d'enfants natifs (à ajouter
  dans `assets/` — partie "contenu", indépendante du code).
- Le mode démo (voix simulées) prend le relais automatiquement si le
  micro/la permission n'est pas disponible.

## Structure du projet

```
mandarin_app_android/
├── main.py                  # point d'entrée Kivy
├── mandarin.kv               # styles de base + écran d'accueil
├── theme.py                  # couleurs / charte graphique
├── buildozer.spec            # config de compilation Android
├── requirements.txt
├── core/
│   ├── tons.py                # courbes de référence des 4 tons (identique desktop)
│   ├── audio_analyse.py       # enregistrement (plyer) + analyse du pitch
│   └── profil.py              # progression élève (stockage user_data_dir)
├── widgets/
│   └── courbe_ton.py          # widget Kivy dessinant la courbe de ton
├── screens/                  # un .py + un .kv par écran
│   ├── ecran_accueil.py
│   ├── ecran_tone_trainer.py / .kv
│   ├── ecran_vocabulaire.py / .kv
│   ├── ecran_missions.py / .kv
│   ├── ecran_duel.py / .kv
│   ├── ecran_jardin.py / .kv
│   ├── ecran_avatar.py / .kv
│   └── ecran_parent.py / .kv
├── data/
│   ├── vocabulaire.json
│   └── missions.json
└── assets/                   # icône de l'app, sons (à ajouter)
```