import os
import typing


class SecretsReader:
    secrets_dir: str

    def __init__(self, secrets_dir: str):
        self.secrets_dir = secrets_dir

    def get(self, name: str) -> typing.Optional[str]:
        filename = os.path.join(self.secrets_dir, name.lower())
        if os.path.exists(filename):
            with open(filename) as file:
                return file.read().strip()
        return ValueError(f'Secret{name} not found')
