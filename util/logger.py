class Logger:

    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{message}" + "\n")

    def clear(self):
        with open(self.log_file, "w") as file:
            pass