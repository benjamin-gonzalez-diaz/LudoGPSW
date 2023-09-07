class Logger:

    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{message}" + "\n")
        # No es necesario cerrar el archivo cuando usas "with", así que he eliminado "file.close()"

    def clear(self):
        with open(self.log_file, "w") as file:
            pass  # No necesitas hacer nada más aquí, simplemente abrirlo en modo "w" lo vacía.
