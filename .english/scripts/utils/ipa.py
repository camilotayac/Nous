#!/usr/bin/env python3
"""
IPA pronunciation utilities: breakdown IPA into Spanish-readable explanations.
"""

IPA_TO_SPANISH = {
    "iː": ("i", "como 'i' en 'siguiente'"),
    "ɪ": ("i", "como 'i' en 'sin' (corta)"),
    "eɪ": ("ei", "como 'ei' en 'rei'"),
    "ɛ": ("e", "como 'e' en 'mes'"),
    "æ": ("a", "como 'a' en 'gato' (abierta)"),
    "ɑː": ("a", "como 'a' en 'papa' (larga)"),
    "ɒ": ("o", "como 'o' en 'tono' (abierta)"),
    "ɔː": ("o", "como 'o' en 'sol' (larga)"),
    "oʊ": ("ou", "como 'ou' en 'coup'"),
    "ʊ": ("u", "como 'u' en 'tubo' (corta)"),
    "uː": ("u", "como 'u' en 'luna' (larga)"),
    "ʌ": ("a", "como 'a' en 'casa' (neutral)"),
    "ə": ("a", "a neutra, como 'a' rápida en 'carne'"),
    "ɜːr": ("er", "como 'er' en 'tierra'"),
    "aɪ": ("ai", "como 'ai' en 'baile'"),
    "aʊ": ("au", "como 'au' en 'auto'"),
    "ɔɪ": ("oi", "como 'oi' en 'oído'"),
    "ɪə": ("ia", "como 'ia' en 'ciao'"),
    "ɛə": ("ea", "como 'ea' en 'beat'"),
    "p": ("p", "como 'p' en 'pan'"),
    "b": ("b", "como 'b' en 'bar'"),
    "t": ("t", "como 't' en 'tono'"),
    "d": ("d", "como 'd' en 'dos'"),
    "k": ("k", "como 'c' en 'casa'"),
    "ɡ": ("g", "como 'g' en 'gas'"),
    "f": ("f", "como 'f' en 'fiesta'"),
    "v": ("v", "como 'v' en 'vida' (vibrante)"),
    "θ": ("z", "como 'z' inglesa (entre s y z)"),
    "ð": ("d", "como 'd' suave entre vocales"),
    "s": ("s", "como 's' en 'sol'"),
    "z": ("s", "como 's' vibrante en 'jazz'"),
    "ʃ": ("sh", "como 'sh' en 'show'"),
    "ʒ": ("sh", "como 'sh' suave en 'medida'"),
    "h": ("j", "como 'j' en 'jardín' (aspirada)"),
    "m": ("m", "como 'm' en 'mesa'"),
    "n": ("n", "como 'n' en 'no'"),
    "ŋ": ("ng", "como 'ng' en 'song' (nasal)"),
    "l": ("l", "como 'l' en 'luna'"),
    "ɹ": ("r", "como 'r' inglesa (sin vibrar)"),
    "r": ("r", "como 'r' inglesa"),
    "w": ("u", "como 'u' en 'fuego' (semivocal)"),
    "j": ("y", "como 'y' en 'yes'"),
    "tʃ": ("ch", "como 'ch' en 'chocolate'"),
    "dʒ": ("dj", "como 'y' en 'yate' (sonora, entre d y y)"),
    "ʔ": ("'", "parada glotal, como pausa en 'uh-oh'"),
    "ˈ": ("", "acento principal (la sílaba siguiente es fuerte)"),
    "ˌ": ("", "acento secundario (menos fuerte)"),
    ".": ("", "separador de sílabas"),
}


def explain_ipa(ipa_string):
    """Break down IPA into (spanish_sound, description) pairs."""
    if not ipa_string:
        return []

    result = []
    i = 0
    ipa = ipa_string.strip("/")

    while i < len(ipa):
        found = False
        for length in [3, 2, 1]:
            chunk = ipa[i:i+length]
            if chunk in IPA_TO_SPANISH:
                spanish, desc = IPA_TO_SPANISH[chunk]
                if spanish:
                    result.append((spanish, desc))
                i += length
                found = True
                break
        if not found:
            if ipa[i] not in " ":
                result.append((ipa[i], f"sonido '{ipa[i]}'"))
            i += 1

    return result


def format_pronunciation_guide(ipa):
    """Format a readable pronunciation guide from IPA."""
    parts = explain_ipa(ipa)
    if not parts:
        return "  No IPA disponible"

    lines = []
    for spanish_sound, description in parts:
        lines.append(f"    {spanish_sound:>4}  {description}")

    return "\n".join(lines)
