import subprocess

def start_backend(cmd: str):
  subprocess.call(cmd, shell=True)

if __name__ == "__main__":
  # start backend server
  backend_port = "8080"
  backend_app_dir = "backend.main"
  backend_server_command = f"uvicorn {backend_app_dir}:app --port {backend_port}"
  start_backend(backend_server_command)
