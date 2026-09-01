"""theme.py -- charte graphique commune, réutilisée par tous les .kv"""

COULEURS_TONS = {
    1: (0.906, 0.298, 0.235, 1),  # rouge
    2: (0.180, 0.800, 0.443, 1),  # vert
    3: (0.204, 0.596, 0.859, 1),  # bleu
    4: (0.902, 0.494, 0.133, 1),  # orange
}

NOMS_TONS = {
    1: "1er ton (plat)",
    2: "2e ton (montant)",
    3: "3e ton (creux)",
    4: "4e ton (qui tombe)",
}

CONSIGNES_TONS = {
    1: "Reste sur une seule note, bien haute, sans bouger.",
    2: "Pars du milieu et monte, comme une question : 'Quoi ?!'",
    3: "Descends d'abord, puis remonte, comme une vague.",
    4: "Pars du haut et tombe fort et vite, comme un ordre !",
}

FOND = (0.059, 0.106, 0.169, 1)
FOND_CARTE = (0.086, 0.149, 0.239, 1)
ACCENT = (0.961, 0.773, 0.094, 1)
TEXTE = (0.957, 0.965, 0.984, 1)
TEXTE_SECONDAIRE = (0.616, 0.690, 0.788, 1)
VERT_SUCCES = (0.180, 0.800, 0.443, 1)
ROUGE_ERREUR = (0.906, 0.298, 0.235, 1)