import wave
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Paramètres de la sinusoïde
frequence_echantillonnage = 44100  # Hz
duree = 3  # secondes
frequence = 440  # Hz

# Création de l'axe temporel
temps = np.linspace(0, duree, int(frequence_echantillonnage * duree), endpoint=False)

# Génération de la première sinusoïde
signal1 = np.sin(2 * np.pi * frequence * temps)

# Ajouter un bip de 1000 Hz à la fin du signal
bip_duree = 0.5  # Durée du bip en secondes
bip_frequence = 1000  # Fréquence du bip en Hz

# Création du signal du bip
bip_temps = np.linspace(0, bip_duree, int(frequence_echantillonnage * bip_duree), endpoint=False)
bip_signal = np.sin(2 * np.pi * bip_frequence * bip_temps)

# Ajouter le bip à la fin du signal
signal1 = np.concatenate((signal1, bip_signal))

# Créer une deuxième sinusoïde décalée dans le temps (par exemple, de 0.5 secondes)
decalage_temps = 0.5  # Décalage en secondes
temps2 = np.linspace(decalage_temps, duree + bip_duree + decalage_temps, len(signal1))

# Génération de la deuxième sinusoïde avec une amplitude de 0.5
signal2 = 0.5 * np.sin(2 * np.pi * frequence * temps2)

# Ajouter un bip à la fin du signal2
bip_signal2 = 0.5 * np.sin(2 * np.pi * bip_frequence * bip_temps)
signal2 = np.concatenate((signal2, bip_signal2))

# Combinaison des deux signaux
signal_combine = signal1 + signal2

# Affichage de la sinusoïde avec le bip et la deuxième sinusoïde
plt.plot(np.linspace(0, duree + bip_duree, len(signal_combine)), signal_combine)
plt.title("Sinusoïde de 440 Hz + 2ème sinusoïde décalée")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 0.01)  # Zoom sur les premières millisecondes pour mieux voir la forme d'onde
plt.grid()
plt.show()

# Lecture du signal combiné
