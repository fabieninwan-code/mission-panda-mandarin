[app]
title = Mission Panda Mandarin
package.name = missionpandamandarin
package.domain = org.cm2mandarin

source.dir = .
source.include_exts = py,kv,json,png,jpg,atlas,wav,mp3

version = 0.1

# numpy est requis par l'analyse de ton (core/audio_analyse.py, core/tons.py)
# plyer permet l'enregistrement micro multiplateforme
requirements = python3,kivy,numpy,plyer

# Autorisation nécessaire pour enregistrer la voix de l'élève
android.permissions = RECORD_AUDIO

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/assets/icone.png

android.api = 34
android.minapi = 24
android.ndk = 26.1.10909125
android.archs = arm64-v8a,armeabi-v7a

android.gradle_dependencies = 

android.add_src = 

[buildozer]
log_level = 2
warn_on_root = 1
