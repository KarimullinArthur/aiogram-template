from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token:str = Field("BOT_TOKEN")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
