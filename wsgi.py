from app import create_app

app = create_app(os.getenv('APP_SETTINGS'))
