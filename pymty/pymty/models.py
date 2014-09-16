from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)

class Image(ndb.Model):
    name = ndb.StringProperty()
    mime = ndb.StringProperty()
    content = ndb.BlobProperty()

class Company(BaseModel):
    updated = ndb.DateTimeProperty(auto_now=True)
    name = ndb.StringProperty()
    intro = ndb.TextProperty()
    image = ndb.KeyProperty(kind=Image)
    active = ndb.BooleanProperty(default=True)

class Job(ndb.Model):
    updated = ndb.DateTimeProperty(auto_now=True)
    title = ndb.StringProperty(required=True)
    description = ndb.TextProperty(required=True)
    company = ndb.KeyProperty(required=True, kind=Company)
    tags = ndb.StringProperty(repeated=True)
    level = ndb.StringProperty()
