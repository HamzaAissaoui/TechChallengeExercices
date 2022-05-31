# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from app import app, db


# migrate = Migrate(app, db)

# class img(db.Model):
#     __tablename__ = 'images'
#     imgid = db.Column(db.Integer, primary_key=True)
#     imgdata = db.Column(db.LargeBinary)

#     def __init__(self, imgdata):
#         self.imgdata = imgdata

#     def __repr__(self):
#         return '<id {}>'.format(self.imgid)
    
#     def serialize(self):
#         return {
#             'imgid': self.imgid, 
#             'imgdata': self.imgdata
#         }