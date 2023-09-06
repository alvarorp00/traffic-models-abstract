from engine import Engine
from config import Config
from run_config import RunConfig

def run_simulation():
    config = Config()  # Cargar configuración
    run_config = RunConfig(config)  # Cargar configuración de ejecución

    engine = Engine(run_config)  # Crear motor de simulación
    engine.run()  # Ejecutar simulación