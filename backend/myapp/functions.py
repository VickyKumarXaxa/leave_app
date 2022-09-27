# from myapp import db

# def TableCreator(tablename):
#   class MyTable(db.Model):
#     __tablename__ = tablename
#     id = db.Column(db.Integer(), primary_key=True)
#     leave_id = db.Column(db.Integer(), db.ForeignKey('leave.id'), nullable=False)
#     status = db.Column(db.String(20), nullable=False)
#   return MyTable