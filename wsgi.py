from app import db, create_app

app = create_app('app.config.ProductionConfig')


@app.before_first_request
def create_database():
    db.create_all()
