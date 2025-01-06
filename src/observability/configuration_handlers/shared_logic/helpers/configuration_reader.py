class ConfigurationReader:
    @staticmethod
    def read_configfile(configfile_path: str) -> str:
        with open(configfile_path) as file:
            return file.read()
