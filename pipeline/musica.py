"""Música de fondo original, generada por código: sin licencias de terceros ni reclamos de Content ID.

Arma una cama suave de acordes (pad) con un pulso leve de bajo, con una progresión elegida
a partir de una semilla, y la mezcla debajo de la voz bajando el volumen cuando hay narración.
"""
import numpy as np

# Progresiones en semitonos sobre la tónica (acordes de 4 notas). Todas en modo mayor/menor suave.
PROGRESIONES = [
    [(0, 4, 7, 11), (9, 12, 16, 19), (5, 9, 12, 16), (7, 11, 14, 17)],   # Imaj7 vi IV V
    [(0, 3, 7, 10), (8, 12, 15, 19), (3, 7, 10, 14), (10, 14, 17, 21)],  # im7 VI III VII
    [(0, 4, 7, 14), (5, 9, 12, 16), (9, 12, 16, 19), (7, 11, 14, 19)],   # I IV vi V
]


def _nota(freq, dur, sr):
    t = np.arange(int(dur * sr)) / sr
    # pad: fundamental + octava suave, con un leve vibrato para que no suene plano
    vib = 1 + 0.002 * np.sin(2 * np.pi * 4.5 * t)
    onda = np.sin(2 * np.pi * freq * vib * t) + 0.35 * np.sin(2 * np.pi * 2 * freq * t) + 0.12 * np.sin(2 * np.pi * 3 * freq * t)
    ataque, salida = int(0.6 * sr), int(0.8 * sr)
    env = np.ones_like(t)
    env[:ataque] = np.linspace(0, 1, ataque)
    env[-salida:] = np.linspace(1, 0, salida)
    return onda * env


def generar(duracion, sr=24000, semilla=0):
    rng = np.random.default_rng(semilla)
    prog = PROGRESIONES[semilla % len(PROGRESIONES)]
    tonica = 110 * 2 ** (rng.integers(0, 7) / 12)  # La2 a Mi3
    compas = 2.4 if semilla % 2 else 2.0           # segundos por acorde
    n = int(np.ceil(duracion / compas)) + 1
    largo = int((n * compas + 1) * sr)
    pista = np.zeros(largo)
    for i in range(n):
        acorde = prog[i % len(prog)]
        ini = int(i * compas * sr)
        for st in acorde:
            nota = _nota(tonica * 2 ** (st / 12), compas + 0.8, sr)
            pista[ini:ini + len(nota)] += nota[: largo - ini] / len(acorde)
        # pulso de bajo en cada tiempo
        for k in range(2):
            b_ini = ini + int(k * compas / 2 * sr)
            t = np.arange(int(0.35 * sr)) / sr
            bajo = np.sin(2 * np.pi * tonica / 2 * 2 ** (acorde[0] / 12) * t) * np.exp(-t * 9)
            pista[b_ini:b_ini + len(bajo)] += 0.5 * bajo[: largo - b_ini]
    pista = pista[: int(duracion * sr)]
    # fundidos de entrada y salida
    f = int(1.0 * sr)
    pista[:f] *= np.linspace(0, 1, f)
    pista[-f:] *= np.linspace(1, 0, f)
    return pista / (np.max(np.abs(pista)) + 1e-9)


def mezclar(voz, sr, semilla=0, nivel=0.12, nivel_con_voz=0.045):
    """Devuelve voz + música, bajando la música cuando suena la voz (ducking)."""
    voz = voz.astype(np.float64)
    musica = generar(len(voz) / sr, sr, semilla)[: len(voz)]
    if len(musica) < len(voz):  # el redondeo de int(duracion * sr) puede dejarla 1 muestra corta
        musica = np.pad(musica, (0, len(voz) - len(musica)))
    # envolvente de la voz en ventanas de 50 ms, suavizada
    v = int(0.05 * sr)
    energia = np.sqrt(np.convolve(voz ** 2, np.ones(v) / v, mode="same"))
    habla = (energia > 0.02).astype(float)
    s = int(0.25 * sr)
    habla = np.convolve(habla, np.ones(s) / s, mode="same")
    ganancia = nivel - (nivel - nivel_con_voz) * np.clip(habla, 0, 1)
    salida = voz + musica * ganancia
    return (salida / max(1.0, np.max(np.abs(salida)) / 0.98)).astype(np.float32)
