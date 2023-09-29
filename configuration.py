from pydantic_settings import BaseSettings
import dotenv


class Settings(BaseSettings):
    browserstack_username: str
    browserstack_accesskey: str
    browserstack_url: str = 'http://hub.browserstack.com/wd/hub'
    app_url: str = 'bs://sample.app'
    project_name: str = 'First Python mobile project'
    build_name: str = 'browserstack-build-1'
    session_name: str = 'BStack IOS and Android tests'
    ios_version: str = '13'
    ios_device: str = 'iPhone 11 Pro'
    android_device: str = 'Samsung Galaxy S22'
    android_version: str = '12.0'


settings = Settings(_env_file=dotenv.find_dotenv(), _env_file_encoding='utf-8')
