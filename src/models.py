from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done = db.Column(db.Boolean(), nullable=False)
    label = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.label

    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "done": self.done,
            # do not serialize the password, its a security breach
        }