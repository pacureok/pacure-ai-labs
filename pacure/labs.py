import json
import subprocess

class WCAI:
    def __init__(self):
        self.history = []
        self.engine_version = "1.0.0-p100"

    def generate_from_image(self, image_path, prompt):
        # 1. Llamada al motor C++ para pre-procesar
        # subprocess.run(["./bin/processor", image_path])
        
        # 2. Lógica del prompt para Three.js (Simplificado)
        game_code = {
            "metadata": {"title": "WCAI Generated Game", "engine": "Three.js"},
            "logic": f"// Prompt: {prompt}\nconst gravity = -9.8;\nconst player = new Player();",
            "html": "<html><body><canvas id='game'></canvas></body></html>"
        }
        
        self.history.append({"input": prompt, "output": game_code})
        return json.dumps(game_code, indent=4)

    def export(self):
        # Lógica para crear el index.html, script.js y style.css
        print("Exportando archivos de Pacure AI/Labs...")

# Instancia para exportar
# import pacure.ai.labs as wcai
