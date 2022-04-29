from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    
    # Empty out existing data
    Game.query.delete()
    
    # Add sample games- name, description
    mario_bros = Game(name="Super Mario Bros.", description="A Classic Nintendo Game")
    sudoku = Game(name="Sudoku", description="A Japanese number game")
    hide_and_seek = Game(name="Hide and Seek", description="Don't play this at night")
    
    # Add sample data to the database
    db.session.add_all([mario_bros, sudoku, hide_and_seek])
    db.session.commit()
    


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
