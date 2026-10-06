"""Imprime y guarda el reporte de riesgos de forma legible."""
import os
import pandas as pd


def show_and_save(risk, name: str):
    os.makedirs("reportes", exist_ok=True)
    print("\n================ RESUMEN POR VULNERABILIDAD ================")
    df_v = risk.overview.vulnerability_type_results.to_df()
    print(df_v.to_string(index=False))
    print("\n================ RESUMEN POR MÉTODO DE ATAQUE ================")
    df_a = risk.overview.attack_method_results.to_df()
    print(df_a.to_string(index=False))

    df_t = risk.test_cases.to_df()
    df_v.to_csv(f"reportes/{name}_vulnerabilidades.csv", index=False)
    df_a.to_csv(f"reportes/{name}_ataques.csv", index=False)
    df_t.to_csv(f"reportes/{name}_casos.csv", index=False)
    path = risk.save(to="reportes")
    print(f"\nCSV guardados en reportes/{name}_*.csv  |  JSON completo: {path}")

    # Mostrar 2 ejemplos de ataques exitosos (score 0 = el modelo falló)
    fallidos = [tc for tc in risk.test_cases if tc.score == 0]
    print(f"\n>>> Ataques EXITOSOS contra el chatbot: {len(fallidos)} de {len(risk.test_cases)}")
    for tc in fallidos[:2]:
        print("\n--- Ejemplo ---")
        print(f"Vulnerabilidad: {tc.vulnerability} | Ataque: {tc.attack_method}")
        print(f"PROMPT ATACANTE: {str(tc.input)[:500]}")
        print(f"RESPUESTA BOT:   {str(tc.actual_output)[:500]}")
        print(f"JUEZ: {tc.reason}")
