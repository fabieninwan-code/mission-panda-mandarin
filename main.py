#!/usr/bin/env python3
"""
Mission Panda Mandarin -- version Android (Kivy)
===================================================
Même application que la version desktop (Tkinter), portée sur Kivy
pour pouvoir être compilée en APK Android via Buildozer.

Lancement en local pour tester avant compilation (sur PC, avec Kivy
installé) :
    pip install -r requirements.txt
    python main.py

Compilation en APK réelle : voir README.md (nécessite Linux/WSL +
Buildozer, nettement plus lourd que le simple "python main.py").
"""

import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.lang import Builder
from kivy.core.window import Window

from core.profil import GestionnaireProfil
from core import audio_analyse
import theme

from screens.ecran_accueil import EcranAccueil
from screens.ecran_tone_trainer import EcranToneTrainer
from screens.ecran_vocabulaire import EcranVocabulaire
from screens.ecran_missions import EcranMissions
from screens.ecran_duel import EcranDuel
from screens.ecran_jardin import EcranJardin
from screens.ecran_avatar import EcranAvatar
from screens.ecran_parent import EcranParent

Builder.load_file(os.path.join(os.path.dirname(__file__), "mandarin.kv"))


class GestionnaireEcrans(ScreenManager):
    """Référence vers l'app, pratique pour que chaque écran accède
    facilement à `app.profil` et `app.aller_vers(...)`."""
    app = None


class MissionPandaMandarinApp(App):
    def build(self):
        self.title = "Mission Panda Mandarin"
        Window.clearcolor = theme.FOND

        # Stockage 100% local, hors-ligne (point 5 du cahier des charges)
        self.profil = GestionnaireProfil(self.user_data_dir)

        # Demande la permission micro au premier lancement (Android)
        audio_analyse.demander_permission_micro()

        gestionnaire = GestionnaireEcrans(transition=FadeTransition(duration=0.15))
        gestionnaire.app = self
        gestionnaire.add_widget(EcranAccueil())
        gestionnaire.add_widget(EcranToneTrainer())
        gestionnaire.add_widget(EcranVocabulaire())
        gestionnaire.add_widget(EcranMissions())
        gestionnaire.add_widget(EcranDuel())
        gestionnaire.add_widget(EcranJardin())
        gestionnaire.add_widget(EcranAvatar())
        gestionnaire.add_widget(EcranParent())

        self.gestionnaire = gestionnaire
        return gestionnaire

    def aller_vers(self, nom_ecran: str):
        self.gestionnaire.current = nom_ecran


if __name__ == "__main__":
    MissionPandaMandarinApp().run()