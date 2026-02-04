# pacure/labs.py
class PacureAI:
    """
    Librería WCAI para importación: import pacure.ai.labs
    """
    def __init__(self, mode="p100"):
        self.mode = mode
        self.memory = []

    def create_game(self, idea, images=None):
        # Aquí se conectaría con la API del modelo en Kaggle o Local
        print(f"WCAI analizando: {idea} con {len(images) if images else 0} imágenes.")
        
        # Estructura JSON que mencionamos antes
        game_data = {
            "status": "success",
            "files": ["index.html", "game.js", "style.css"],
            "preview_url": "./preview"
        }
        return game_data

    def add_feature(self, new_prompt):
        # Seguir la conversación
        self.memory.append(new_prompt)
        return "Característica añadida al código."
