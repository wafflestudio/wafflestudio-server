import pydantic


class DBConfig(pydantic.BaseSettings):
    username: str = pydantic.Field(..., env="USERNAME")
    password: str = pydantic.Field(..., env="PASSWORD")
    host: str = pydantic.Field(..., env="HOST")
    port: int = pydantic.Field(..., env="PORT")

    class Config:
        case_sensitive = False