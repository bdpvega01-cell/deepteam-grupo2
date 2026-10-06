"""
DEMO 2 — Ataques MULTI-TURN (conversación de varios turnos).
El atacante va escalando poco a poco hasta romper las reglas del bot.
Ataques: Linear Jailbreaking y Crescendo Jailbreaking.
"""
from deepteam import red_team
from deepteam.vulnerabilities import PromptLeakage, PIILeakage
from deepteam.attacks.multi_turn import LinearJailbreaking, CrescendoJailbreaking

from config import simulator, evaluator
from target_chatbot import model_callback
from report_utils import show_and_save

risk = red_team(
    model_callback=model_callback,
    vulnerabilities=[
        PromptLeakage(types=["secrets_and_credentials"]),
        PIILeakage(types=["direct_disclosure"]),
    ],
    attacks=[
        LinearJailbreaking(num_turns=4, simulator_model=simulator),
        CrescendoJailbreaking(max_rounds=4, max_backtracks=2, simulator_model=simulator),
    ],
    simulator_model=simulator,
    evaluation_model=evaluator,
    attacks_per_vulnerability_type=1,
    target_purpose="Chatbot de atención al cliente de un banco peruano",
    async_mode=False,
)
show_and_save(risk, "02_multi_turn")
