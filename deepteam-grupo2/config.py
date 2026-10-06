"""Configuración central: qué modelos de Ollama se usan para cada rol."""
from deepeval.models import OllamaModel

OLLAMA_URL = "http://localhost:11434"

# Modelo VÍCTIMA (el chatbot que atacamos). Pequeño y rápido.
TARGET_MODEL = "llama3.2:3b"

# Modelo ATACANTE (genera los ataques) y JUEZ (evalúa si el ataque funcionó).
# Si tu PC tiene poca RAM, cambia a "llama3.2:3b".
ATTACKER_MODEL = "qwen2.5:7b"

simulator = OllamaModel(model=ATTACKER_MODEL, base_url=OLLAMA_URL, temperature=0.7)
evaluator = OllamaModel(model=ATTACKER_MODEL, base_url=OLLAMA_URL, temperature=0)
