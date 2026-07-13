# .english — Sistema de Aprendizaje de Inglés en Terminal

Sistema completo de aprendizaje de inglés con repetición espaciada (SRS), pronunciación IPA, audio automático y conversación. Todo funciona desde la terminal sin necesidad de Anki ni interfaces gráficas.

## Características

- **Motor SRS con FSRS** — Algoritmo de repetición espaciada (mismo que Anki 23.10+)
- **Audio automático** — Genera pronunciación con gTTS y se reproduce con afplay
- **IPA con guía en español** — Desglose fonético para hispanohablantes
- **Generación desde Obsidian** — Extrae vocabulario de notas .md automáticamente
- **Conversación con audio** — Practica hablando con respuestas de audio
- **100% terminal** — Sin dependencia de Anki ni GUI

## Requisitos

### Sistema
- **macOS** (usa `afplay` para reproducción de audio)
- **Python 3.12+**

### Dependencias de Python

```bash
pip install fsrs gtts eng_to_ipa deep_translator
```

| Paquete | Propósito |
|---------|-----------|
| `fsrs` | Motor de repetición espaciada FSRS |
| `gtts` | Text-to-Speech (Google) |
| `eng_to_ipa` | Transcripción IPA del inglés |
| `deep_translator` | Traducción EN↔ES |

### Sistema (ya incluido en macOS)
- `afplay` — Reproducción de audio
- `ffmpeg` — Procesamiento de audio (gTTS lo usa internamente)

## Instalación

```bash
# Clonar o copiar la carpeta
cp -r .english ~/.english

# Instalar dependencias
pip install fsrs gtts eng_to_ipa deep_translator
```

## Uso Rápido

```bash
# Menú principal
python3 ~/.english/scripts/english_session.py

# Repasar vocabulario
python3 ~/.english/scripts/english_session.py review

# Ver progreso
python3 ~/.english/scripts/english_session.py stats

# Generar cards desde notas Obsidian
python3 ~/.english/scripts/english_session.py generate

# Conversación con audio
python3 ~/.english/scripts/english_session.py conversation
```

## Estructura

```
.english/
├── README.md                 # Este archivo
├── SKILL.md                  # Skill manifest para opencode
├── scripts/
│   ├── english_session.py    # Punto de entrada principal
│   ├── srs_engine.py         # Motor FSRS con SQLite
│   ├── review.py             # Repaso con audio + IPA
│   ├── conversation.py       # Conversación con audio
│   ├── generate_cards.py     # Generar cards desde Obsidian
│   └── utils/
│       ├── __init__.py       # Exporta todas las utilidades
│       ├── audio.py          # gTTS + afplay
│       ├── ipa.py            # Fonética IPA
│       └── translate.py      # Traducción + diccionario
├── data/
│   ├── cards.db              # Base de datos SRS (se crea automáticamente)
│   ├── progress.json         # Progreso de procesamiento
│   ├── audio/                # Audio temporal de vocabulario
│   └── conversation_audio/   # Audio temporal de conversación
```

## Flujo de Repaso

1. Aparece la card con término + IPA
2. **El audio suena automáticamente** (gTTS → afplay)
3. Se muestra desglose fonético en español
4. Tú respondes, calificas 1-4
5. FSRS reprograma la siguiente revisión
6. **El audio se auto-elimina después de sonar**

### Calificaciones

| Rating | Significado | Efecto FSRS |
|--------|-------------|-------------|
| 1 | Otra vez | Repetir pronto |
| 2 | Difícil | Intervalo corto |
| 3 | Bien | Intervalo normal |
| 4 | Fácil | Intervalo largo |

### Comandos durante repaso

- `Enter` — Mostrar respuesta
- `1-4` — Calificar
- `s` — Suspender card
- `q` — Salir

## Generación de Cards

El sistema extrae automáticamente vocabulario de notas Obsidian:

```bash
# Generar desde una nota específica
python3 scripts/generate_cards.py ~/Documents/GitHub/Nous/obsidian/02_quimica/01_cinetica_quimica.md

# Generar desde todas las notas pendientes
python3 scripts/generate_cards.py
```

### Proceso de extracción

1. Lee el archivo .md
2. Limpia LaTeX, código, callouts
3. Extrae palabras de 6+ caracteres
4. Filtra stopwords y palabras en español
5. Traduce con diccionario local + deep_translator
6. Genera IPA con eng_to_ipa
7. Crea cards EN→ES y ES→EN

### Diccionario local

Incluye 100+ términos científicos pre-traducidos (química, física, matemáticas, computación). Ver `utils/translate.py` para la lista completa.

## Conversación

```bash
python3 scripts/english_session.py conversation
```

- Escribe en inglés o español
- El sistema responde con audio automáticamente
- Modos: automático, solo inglés, solo español

## Datos

### Ubicación

```
~/.english/data/
├── cards.db          # SQLite — todas las cards y revisiones
├── progress.json     # Qué notas ya se procesaron
├── audio/            # MP3s temporales (se auto-limpian)
└── conversation_audio/  # Audio de conversación
```

### Backup

```bash
# Copiar todos los datos
cp -r ~/.english/data ~/backup_english_data
```

## Solución de Problemas

### No suena el audio
- Verificar que `afplay` funciona: `afplay /System/Library/Sounds/Glass.aiff`
- Verificar que gTTS genera audio: `python3 -c "from gtts import gTTS; gTTS('test', lang='en').save('/tmp/test.mp3')"`

### Error de traducción
- El sistema usa diccionario local primero, luego deep_translator
- Si falla, devuelve el término en inglés sin traducir

### No encuentra notas
- Verificar que `VAULT_DIR` en `generate_cards.py` apunta a tu vault Obsidian
- Las notas deben terminar en `.md`

### Base de datos corrupta
```bash
rm ~/.english/data/cards.db
python3 scripts/srs_engine.py  # Se recrea automáticamente
```

## Licencia

MIT
