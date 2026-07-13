#!/usr/bin/env python3
"""
Translation utilities: ES→EN translation, Spanish term extraction, local dictionaries.
"""
import re
from collections import Counter


SPANISH_STOPWORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "del", "al", "a", "en", "por", "para", "con", "sin",
    "que", "es", "son", "se", "no", "más", "como", "pero",
    "este", "esta", "estos", "estas", "ese", "esa", "aquel",
    "tiene", "hay", "puede", "hace", "todo", "muy", "ya",
    "o", "e", "si", "cuando", "donde", "quien", "cual",
    "le", "lo", "me", "mi", "tu", "su", "nos",
    "fue", "ser", "era", "está", "están", "había", "han",
    "hay", "sólo", "solo", "cada", "otro", "otra", "otros", "otras",
    "mismo", "misma", "mismos", "mismas", "tal", "tales",
    "aquí", "ahí", "allí", "entonces", "después", "antes",
    "durante", "hasta", "desde", "hacia", "según", "entre",
    "sobre", "bajo", "ante", "tras", "mediante",
    "porque", "pues", "aunque", "embargo",
    "todo", "toda", "todos", "todas", "nada", "algo", "alguien",
    "nadie", "ninguno", "ninguna", "mucho", "poca", "poco",
    "demasiado", "bastante", "apenas", "casi", "siempre",
    "nunca", "antes", "después", "luego", "pronto", "tarde",
    "aquello", "eso", "ello", "les", "ellas", "ellos",
    "mí", "ti", "sí", "os", "vosotros",
}

LOCAL_DICT_ES_EN = {
    "proposición": "proposition", "negación": "negation",
    "enunciado": "statement", "verdad": "truth", "falsedad": "falsehood",
    "booleano": "boolean", "variable": "variable", "operador": "operator",
    "conjunción": "conjunction", "disyunción": "disjunction",
    "condicional": "conditional", "bicondicional": "biconditional",
    "cinética": "kinetics", "reacción": "reaction",
    "concentración": "concentration", "temperatura": "temperature",
    "catalizador": "catalyst", "catalisis": "catalysis",
    "superficie": "surface", "colisión": "collision",
    "velocidad": "velocity", "tasa": "rate",
    "energía": "energy", "activación": "activation",
    "equilibrio": "equilibrium", "irreversible": "irreversible",
    "reversible": "reversible", "espontáneo": "spontaneous",
    "termodinámica": "thermodynamics", "entalpía": "enthalpy",
    "entropía": "entropy", "presión": "pressure", "volumen": "volume",
    "solución": "solution", "soluto": "solute", "solvente": "solvent",
    "saturado": "saturated", "insaturado": "unsaturated",
    "precipitación": "precipitation", "disolución": "dissolution",
    "cristalización": "crystallization", "evaporación": "evaporation",
    "destilación": "distillation", "filtración": "filtration",
    "titración": "titration", "indicador": "indicator",
    "molaridad": "molarity", "dilución": "dilution", "tampón": "buffer",
    "ácido": "acid", "óxido": "oxide",
    "hidróxido": "hydroxide", "carbonato": "carbonate",
    "sulfato": "sulfate", "nitrato": "nitrate", "fosfato": "phosphate",
    "cloruro": "chloride", "electrolito": "electrolyte", "ión": "ion",
    "anión": "anion", "catión": "cation", "oxidación": "oxidation",
    "reducción": "reduction", "electrodo": "electrode",
    "ánodo": "anode", "cátodo": "cathode", "polímero": "polymer",
    "monómero": "monomer", "isómero": "isomer",
    "estereoquímica": "stereochemistry", "alcano": "alkane",
    "alqueno": "alkene", "alquino": "alkyne", "aromático": "aromatic",
    "benceno": "benzene", "fenol": "phenol", "éter": "ether",
    "éster": "ester", "aldehído": "aldehyde", "cetona": "ketone",
    "carboxílico": "carboxylic", "amina": "amine", "amida": "amide",
    "nucleofílico": "nucleophilic", "electrofílico": "electrophilic",
    "sustitución": "substitution", "eliminación": "elimination",
    "polimerización": "polymerization", "hidrólisis": "hydrolysis",
    "combustión": "combustion", "respiración": "respiration",
    "fotosíntesis": "photosynthesis", "metabolismo": "metabolism",
    "enzima": "enzyme", "sustrato": "substrate",
    "covalente": "covalent", "iónico": "ionic", "metálico": "metallic",
    "hidrógeno": "hydrogen", "carbono": "carbon",
    "nitrógeno": "nitrogen", "oxígeno": "oxygen", "azufre": "sulfur",
    "fósforo": "phosphorus", "halógeno": "halogen",
    "periódico": "periodic", "electronegatividad": "electronegativity",
    "ionización": "ionization", "electrón": "electron",
    "orbital": "orbital", "cuántico": "quantum", "onda": "wave",
    "frecuencia": "frequency", "longitud de onda": "wavelength",
    "amplitud": "amplitude", "interferencia": "interference",
    "difracción": "diffraction", "espectroscopía": "spectroscopy",
    "cromatografía": "chromatography", "isótopo": "isotope",
    "radiactivo": "radioactive", "vida media": "half-life",
    "decaimiento": "decay", "fisión": "fission", "fusión": "fusion",
    "neutrón": "neutron", "protón": "proton", "fotón": "photon",
    "quark": "quark", "bosón": "boson",
    "fermión": "fermion", "hadrón": "hadron",
    "simetría": "symmetry", "conservación": "conservation",
    "carga": "charge", "campo": "field", "partícula": "particle",
    "masa": "mass", "peso": "weight", "fuerza": "force",
    "aceleración": "acceleration", "momento": "momentum",
    "fricción": "friction", "tensión": "tension",
    "compresión": "compression", "trabajo": "work",
    "potencia": "power", "eficiencia": "efficiency",
    "mecánico": "mechanical", "térmico": "thermal",
    "eléctrico": "electrical", "químico": "chemical",
    "magnético": "magnetic", "óptico": "optical",
    "resonancia": "resonance", "voltaje": "voltage",
    "corriente": "current", "resistencia": "resistance",
    "impedancia": "impedance", "capacitancia": "capacitance",
    "inductancia": "inductance", "conductividad": "conductivity",
    "densidad": "density", "gravedad": "gravity",
    "flotabilidad": "buoyancy", "estequiometría": "stoichiometry",
    "limitante": "limiting", "rendimiento": "yield",
    "teórico": "theoretical", "empírico": "empirical",
    "molecular": "molecular", "fórmula": "formula",
    "estructural": "structural", "cristal": "crystal",
    "retículo": "lattice", "enlace": "bond",
    "hibridación": "hybridization",
    "grafo": "graph", "vértice": "vertex", "arista": "edge",
    "camino": "path", "ciclo": "cycle", "árbol": "tree",
    "matriz": "matrix", "vector": "vector", "álgebra": "algebra",
    "algoritmo": "algorithm", "complejidad": "complexity",
    "función": "function", "constante": "constant", "ecuación": "equation",
    "teorema": "theorem", "demostración": "proof",
    "conjunto": "set", "elemento": "element",
    "probabilidad": "probability", "estadística": "statistics",
    "distribución": "distribution", "varianza": "variance",
    "desviación": "deviation", "correlación": "correlation",
    "regresión": "regression", "hipótesis": "hypothesis",
    "significancia": "significance", "intervalo": "interval",
    "muestra": "sample", "población": "population",
    "proposición": "proposition", "proposición": "proposition",
    "reacción": "reaction", "colisión": "collision",
    "concentración": "concentration", "velocidad": "velocity",
    "catalizador": "catalyst", "superficie": "surface",
    "temperatura": "temperature", "energía": "energy",
    "partícula": "particle", "enlace": "bond",
    "producto": "product", "reactivo": "reactant",
    "compuesto": "compound", "elemento": "element",
    "átomo": "atom", "molécula": "molecule",
    "mezcla": "mixture", "solución": "solution",
    "sólido": "solid", "líquido": "liquid", "gas": "gas",
    "estado": "state", "fase": "phase",
    "propiedad": "property", "magnitud": "magnitude",
    "medida": "measurement", "unidad": "unit",
    "fórmula": "formula", "ecuación": "equation",
    "resultado": "result", "proceso": "process",
    "método": "method", "técnica": "technique",
    "teoría": "theory", "ley": "law", "principio": "principle",
    "modelo": "model", "hipótesis": "hypothesis",
    "dato": "data", "dato": "data", "información": "information",
    "análisis": "analysis", "síntesis": "synthesis",
    "clasificación": "classification", "categoría": "category",
    "estructura": "structure", "composición": "composition",
    "formación": "formation", "transformación": "transformation",
    "evolución": "evolution", "cambio": "change",
    "diferencia": "difference", "semejanza": "similarity",
    "relación": "relationship", "conexión": "connection",
    "factor": "factor", "causa": "cause", "efecto": "effect",
    "consecuencia": "consequence", "importancia": "importance",
    "aplicación": "application", "utilidad": "usefulness",
    "ejemplo": "example", "caso": "case",
    "situación": "situation", "condición": "condition",
    "nivel": "level", "grado": "degree", "tipo": "type",
    "clase": "class", "forma": "form", "manera": "way",
    "parte": "part", "todo": "whole", "sistema": "system",
    "conjunto": "set", "grupo": "group", "serie": "series",
    "secuencia": "sequence", "orden": "order",
    "regla": "rule", "criterio": "criterion",
    "razón": "reason", "sentido": "sense",
    "concepto": "concept", "idea": "idea",
    "definición": "definition", "descripción": "description",
    "explicación": "explanation", "interpretación": "interpretation",
    "representación": "representation", "observación": "observation",
    "medición": "measurement", "experimento": "experiment",
    "investigación": "research", "estudio": "study",
    "conocimiento": "knowledge", "aprendizaje": "learning",
    "comprensión": "understanding", "análisis": "analysis",
    "crítica": "critique", "evaluación": "evaluation",
    "comparación": "comparison", "contraste": "contrast",
    "relación": "relation", "asociación": "association",
    "dependencia": "dependence", "interacción": "interaction",
    "influencia": "influence", "efecto": "effect",
    "resultado": "outcome", "conclusión": "conclusion",
    "resumen": "summary", "síntesis": "synthesis",
    "integración": "integration", "aplicación": "application",
    "práctica": "practice", "teoría": "theory",
    "prueba": "test", "ensayo": "essay",
    "exposición": "exposition", "narración": "narration",
    "descripción": "description", "argumentación": "argumentation",
    "perspectiva": "perspective", "enfoque": "approach",
    "método": "method", "procedimiento": "procedure",
    "técnica": "technique", "estrategia": "strategy",
    "herramienta": "tool", "recurso": "resource",
    "medio": "medium", "soporte": "support",
    "fuente": "source", "referencia": "reference",
    "bibliografía": "bibliography", "citación": "citation",
    "-original": "original", "primario": "primary",
    "secundario": "secondary", "terciario": "tertiary",
}


def extract_spanish_terms(text, max_terms=25):
    """Extrae términos en español del texto, filtrando stopwords y palabras cortas."""
    words = re.findall(r'\b[a-zA-ZáéíóúñüÁÉÍÓÚÑÜ]{4,}\b', text)
    filtered = [
        w.lower() for w in words
        if w.lower() not in SPANISH_STOPWORDS
    ]
    counter = Counter(filtered)
    return [word for word, _ in counter.most_common(max_terms)]


def translate_to_english(term):
    """Traduce español→inglés. Diccionario local primero, luego API."""
    if term in LOCAL_DICT_ES_EN:
        return LOCAL_DICT_ES_EN[term]
    try:
        from deep_translator import GoogleTranslator
        result = GoogleTranslator(source='es', target='en').translate(term)
        if result and result.lower() != term.lower():
            first = result.split(",")[0].strip()
            return first
    except Exception:
        pass
    return term


def get_context_sentence(text, term):
    """Extrae la oración donde aparece el término."""
    sentences = re.split(r'[.!?\n]+', text)
    for s in sentences:
        if re.search(rf'\b{re.escape(term)}\b', s, re.IGNORECASE):
            clean = s.strip()
            if len(clean) > 10:
                return clean[:200]
    return ""


def get_ipa(term):
    """Obtiene transcripción IPA de un término en inglés."""
    try:
        import eng_to_ipa as ipa_lib
        result = ipa_lib.convert(term)
        if result and result != term:
            return str(result)
    except ImportError:
        pass
    except Exception:
        pass
    return ""
