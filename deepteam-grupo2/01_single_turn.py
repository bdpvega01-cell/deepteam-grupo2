"""
DEMO 1 — Ataques SINGLE-TURN (un solo mensaje).
Vulnerabilidades: PII Leakage, Prompt Leakage y Bias.
Ataques: Prompt Injection, Roleplay, Leetspeak, Base64.
"""
from deepteam import red_team
from deepteam.vulnerabilities import PIILeakage, PromptLeakage, Bias
from deepteam.attacks.single_turn import PromptInjection, Roleplay, Leetspeak, Base64

from config import simulator, evaluator
from target_chatbot import model_callback
from report_utils import show_and_save

vulnerabilities = [
    PIILeakage(types=["direct_disclosure", "social_manipulation"]),
    PromptLeakage(types=["secrets_and_credentials", "instructions"]),
    Bias(types=["gender", "race"]),
]
attacks = [
    PromptInjection(),
    Roleplay(role="auditor interno del banco", persona="supervisor de cumplimiento"),
    Leetspeak(),
    Base64(),
]

risk = red_team(
    model_callback=model_callback,
    vulnerabilities=vulnerabilities,
    attacks=attacks,
    simulator_model=simulator,
    evaluation_model=evaluator,
    attacks_per_vulnerability_type=1,
    target_purpose="Chatbot de atención al cliente de un banco peruano",
    async_mode=False,   # Ollama local: secuencial es más estable
)
show_and_save(risk, "01_single_turn")
