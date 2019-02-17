from . import BaseModel
from ..extensions import db


class Person(BaseModel):
    """Represents an individual person"""

    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    birthdate = db.Column(db.DateTime, nullable=True)

    address = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(255), nullable=True)

    # did not use backref as I like auto-complete
    parents = db.relationship(
        "Person",
        secondary="progeny",
        primaryjoin="Person.id==progeny.c.parent_id",
        secondaryjoin="Person.id==progeny.c.child_id",
        lazy="joined",
    )
    children = db.relationship(
        "Person",
        secondary="progeny",
        primaryjoin="Person.id==progeny.c.child_id",
        secondaryjoin="Person.id==progeny.c.parent_id",
        lazy="joined",
    )

    spouse = db.relationship(
        "Person",
        secondary="spouse",
        primaryjoin="Person.id==spouse.c.person_id",
        secondaryjoin="Person.id==spouse.c.spouse_person_id",
        lazy="joined",
    )
