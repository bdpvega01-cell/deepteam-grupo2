"""
DEMO 3 — Escaneo con el framework OWASP Top 10 for LLMs (2025).
LLM_01 Prompt Injection | LLM_02 Sensitive Info Disclosure | LLM_07 System Prompt Leakage
(Puedes agregar más categorías, pero con Ollama local tarda más.)
"""
from deepteam import red_team
from deepteam.frameworks import OWASPTop10

from config import simulator, evaluator
from target_chatbot import model_callback
from report_utils import show_and_save

risk = red_team(
    model_callback=model_callback,
    framework=OWASPTop10(categories=["LLM_01", "LLM_02", "LLM_07"]),
    simulator_model=simulator,
    evaluation_model=evaluator,
    attacks_per_vulnerability_type=1,
    target_purpose="Chatbot de atención al cliente de un banco peruano",
    async_mode=False,
)
show_and_save(risk, "03_owasp")
