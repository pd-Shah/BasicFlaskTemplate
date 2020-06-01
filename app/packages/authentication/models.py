from app.init import db

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(length=64), unique=True, )
    users = db.relationship("User", back_populates="role", lazy="dynamic")

    def __repr__(self):
        return "<Role {0}>".format(self.name)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(length=256, ), unique=True, )
    family = db.Column(db.String(length=256, ), )
    username = db.Column(db.String(length=256, ), )
    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
    )
    role = db.relationship("Role", back_populates="users",)
    email = db.Column(db.String(length=256), unique=True)

    def __repr__(self):
        return "<User {0}>".format(self.name)
