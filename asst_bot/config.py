from dataclasses import dataclass
from environs import Env


@dataclass
class AsstBot:
    token: str
    prefix: str


@dataclass
class Config:
    asst_bot: AsstBot


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(asst_bot=AsstBot(token=env.str("TOKEN"), prefix=env.str("PREFIX")))
