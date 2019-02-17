# be-coding-challenge

### Expectations

- We do not expect you to completely finish the challenge. We ask that candidates spend 4 hours or more working through the challenge. With that we understand that everyones schedule and availability is different so we ask that you provide a reasonable estimate of your time commitment so we can take it into account when evaluating your submission.
- We expect you to leverage creative license where it makes sense. If you'd like to change the project structure, pull in libraries, or make assumptions about the requirements we openly encourage you to do so. All that we ask is that you are prepared to talk about your choices in future interviews.

### Challenge

For this challenge you will be implementing a family tree API.

The API should be capable of keeping track of people and the connections between them.

While you have full control to model the entities as you see fit you should keep the following guidelines in mind.

Details about a person and their relationships should be editable. At a minimum you should use the following traits to describe a person:

- First name
- Last name
- Phone number
- Email address (unique)
- Address
- Birth date

When thinking about relations between people the API should be able to provide the following information

- For a given person list all of their siblings
- For a given person list all of their parents
- For a given person list all their children
- For a given person list all of their grandparents
- For a given person list all of their cousins

### Getting started

##### Running the service in a virtual environment

If you are using python 3.7 you will need to run
```bash
pipenv run pip install pip==18.0
```

To install dependencies you will need to run
```bash
pipenv install
```

Once dependencies are installed you can run the service with
```bash
pipenv run python manage.py
```
or
```bash
pipenv shell
python server.py
```

---

## Notes

http://flask.pocoo.org/docs/1.0/patterns/appfactories/
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure

https://github.com/miguelgrinberg/microblog

### Creating Database

http://www.databaseanswers.org/data_models/genealogy/index.htm

### Todo

- [x] testing config
- [x] migrations
- [x] marshmallow
- [ ] data model
- [ ] CRUD endpoints for all tables
- [ ] pull out relationships

### Scratch Pad

```python
parent = Person(first_name="Aly", last_name="Sivji", email="alysivji@gmail.com")
child = Person(first_name="Aly Jr", last_name="Sivji", email="jrsivji@@gmail.com")
parent.children.append(child)
db.session.add(parent)
db.session.add(child)
db.session.commit()

husband = Person(first_name="Aly", last_name="Sivji", email="sivpack@gmail.com")
wife = Person(first_name="Alya", last_name="Sivji", email="sivpack-spouse@gmail.com")
second_wife = Person(first_name="Alia", last_name="Shivji", email="sivpack-spouse2@gmail.com")
# husband._spouse1.append(wife)
db.session.add(husband)
db.session.add(wife)
db.session.commit()

_spouse1 = db.relationship(
    "Person",
    secondary="spouse",
    primaryjoin="Person.id==spouse.c.spouse1_id",
    secondaryjoin="Person.id==spouse.c.spouse2_id",
    backref=db.backref('_spouse2', lazy='joined'),
    lazy="joined",
)

@hybrid_property
def spouse(self):
    return list(self._spouse1).extend(list(self._spouse2))

@spouse.setter
def spouse(self, other):
    self._spouse1.append(other)


r = Relationship(p, p1)
r = Relationship()
p.relations.add(p1)
p
p.relations
p1.relations
p.relations.append(p1)
p
p.relations
db.session.add(p)
db.session.add(p1)
db.session.commit()
hist
```
