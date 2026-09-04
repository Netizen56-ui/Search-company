import json
from datetime import datetime

# 1. Leer el estado actual
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# --- 2. AQUÍ VA TU LÓGICA (Scraping, cálculos, peticiones, etc.) ---
# ...
# -------------------------------------------------------------------

# 3. Actualizar los resultados
data['runs'] += 1
data['last_run'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data['latest_result'] = f"Ejecución exitosa número {data['runs']}"

# 4. Guardar los cambios en el archivo
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
  
