from datetime import datetime
from my_app.app import db, login_manager, app
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=True)
    last_name = db.Column(db.String(40), nullable=True)
    n_name = db.Column(db.String(25), unique=True, nullable=True)
    password = db.Column(db.String(25), nullable=True)
    email = db.Column(db.String(35), unique=True, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    created = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)



    def __repr__(self):
        return "<Users ID: {}, First name: {}, Last name: {}>".format(self.id,
                                                                      self.first_name,
                                                                      self.last_name
                                                                      )

    def __str__(self):
        return "<Users ID: {}, First name: {}, Last name: {}>".format(self.id,
                                                                      self.first_name,
                                                                      self.last_name
                                                                      )

class Album(db.Model):
    __tablename__ = "album"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, *args, **kwargs):
        super(Album, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<Album ID: {}, Title: {}>".format(self.id, self.title)

    def __str__(self):
        return "<Album ID: {}, Title: {}>".format(self.id, self.title)

class Photo(db.Model):
    __tablename__ = "photo"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(80), nullable=True)
    created = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Photo, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<Photo ID: {}, Name: {}>".format(self.id, self.name)

    def __str__(self):
        return "<Photo ID: {}, Name: {}>".format(self.id, self.name)

@login_manager.user_loader
def load_user(users_id):
    return Users.query.get(int(users_id))
