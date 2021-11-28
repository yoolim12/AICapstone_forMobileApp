from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Members(db.Model):
    """ table name : user_list
        table info 
    - id : user id 
    - name : user name
    - password : user password
    """
    
    __tablename__ = 'user_list'
    
    id = db.Column(db.String(45), primary_key=True, nullable=False)
    password = db.Column(db.String(45), nullable=True)
    name = db.Column(db.String(45), nullable=True)

    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name
