from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config='development'):
    app = Flask(__name__)
    
    if config == 'development':
        app.config['SECRET_KEY'] = 'dev-key'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bakery.db'
    else:
        app.config['SECRET_KEY'] = 'prod-key'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bakery_prod.db'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    from app.routes import main
    app.register_blueprint(main)
    
    with app.app_context():
        db.create_all()
        init_db()
    
    return app

def init_db():
    from app.models import Product
    if not Product.query.first():
        products = [
            Product(name='Chocolate Cake', price=20.00, description='Rich chocolate cake'),
            Product(name='Apple Pie', price=15.00, description='Classic apple pie'),
            Product(name='Croissant', price=3.50, description='Buttery croissant'),
            Product(name='Bread', price=5.00, description='Fresh bread')
        ]
        for product in products:
            db.session.add(product)
        db.session.commit()