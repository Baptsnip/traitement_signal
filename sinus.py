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

# Génération de la sinusoïde
signal = np.sin(2 * np.pi * frequence * temps)

# Ajouter un bip de 1000 Hz à la fin du signal
bip_duree = 0.5  # Durée du bip en secondes
bip_frequence = 1000  # Fréquence du bip en Hz

# Création du signal du bip
bip_temps = np.linspace(0, bip_duree, int(frequence_echantillonnage * bip_duree), endpoint=False)
bip_signal = np.sin(2 * np.pi * bip_temps)

# Ajouter le bip à la fin du signal
signal = np.concatenate((signal, bip_signal))

# Affichage de la sinusoïde avec le bip
plt.plot(np.linspace(0, duree + bip_duree, len(signal)), signal)
plt.title("Sinusoïde de 440 Hz ")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 0.01)  # Zoom sur les premières millisecondes pour mieux voir la forme d'onde
plt.grid()
plt.show()

# Lecture du signal
sd.play(signal, frequence_echantillonnage)
sd.wait()
