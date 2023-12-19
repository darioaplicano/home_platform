import subprocess

def start_flask_app():
    # Construye la imagen y levanta los contenedores
    subprocess.run(["docker-compose", "up", "--build"])

def stop_flask_app():
    # Detiene la ejecución de los contenedores
    subprocess.run(["docker-compose", "down"])

if __name__ == "__main__":
    start_flask_app()
