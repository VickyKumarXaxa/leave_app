
from lib2to3.pgen2.token import GREATEREQUAL
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from myapp.models import User

class AddUserForm(FlaskForm):

    def validate_username(self,user_to_check):
        user = User.query.filter_by(username=user_to_check.data).first()
        if user:
            raise ValidationError('Username already exists: Please try a different username')

    def validate_email(self,email_to_check):
        email_address = User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists: Please try a different email address')

    username = StringField(label='User Name', validators=[Length(min=2, max=30),DataRequired()])
    email = StringField(label='Email Address', validators=[Email(),DataRequired()])
    name = StringField(label='Name',validators=[DataRequired()])
    faculty_staff = SelectField(label='Faculty/Staff', validators=[DataRequired()],choices=['Faculty','Staff'],validate_choice=True)
    department = StringField(label='Department/Section',validators=[DataRequired()])
    designation = StringField(label='Designation/Post heald',validators=[DataRequired()])
    role = SelectField(label='Role', validators=[DataRequired()], choices=['Applicant', 'HOD', 'Administration', 'Authority'])
    submit = SubmitField(label='Add User')

class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

class ChangePasswordForm(FlaskForm):
    password1 = PasswordField(label='Password', validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Change Password')


class LeaveCategoryForm(FlaskForm):
    leave_category = SelectField(label='Type of Leave Required',validators=[DataRequired()],choices=['Casual','Non Casual'],validate_choice=True)
    submit = SubmitField(label='Select')

class CasualLeaveForm(FlaskForm):
    nature_of_leave = SelectField(label='Nature of Leave Required',validators=[DataRequired()],choices=['CL','RH','SCL','ON DUTY'],validate_choice=True)
    start_date = DateField(label='Start Date',format='%Y-%m-%d',validators=[DataRequired()])
    end_date = DateField(label='End Date',format='%Y-%m-%d',validators=[DataRequired()])
    num_of_days = IntegerField(label='Number of days',validators=[DataRequired()])
    purpose_ = StringField(label='Purpose of Leave',validators=[DataRequired()])
    alternative_arrangements = StringField(label='Alternative Arrangements (if any)')
    address_during_leave = StringField(label='Address during the leave/on duty',validators=[DataRequired()])
    phone = StringField(label='Phone No',validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class NonCasualLeaveForm(FlaskForm):
    nature_of_leave = SelectField(label='Nature of Leave Required',validators=[DataRequired()],choices=['Earned Leave', 'Half Pay Leave', 'Extra Ordinary Leave', 'Commuted Leave', 'Vacation', 'Maternity Leave', 'Paternity Leave', 'Child Care Leave'],validate_choice=True)
    start_date = DateField(label='Start Date',format="%Y-%m-%d",validators=[DataRequired()])
    end_date = DateField(label='End Date',format='%Y-%m-%d',validators=[DataRequired()])
    num_of_days = IntegerField(label='Number of days',validators=[DataRequired()])
    purpose_ = StringField(label='Purpose of Leave',validators=[DataRequired()])
    alternative_arrangements = StringField(label='Alternative Arrangements (if any)')
    address_during_leave = StringField(label='Address during the leave/on duty',validators=[DataRequired()])
    phone = StringField(label='Phone No',validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class SelectSortForm1(FlaskForm):
    sort_by = SelectField(label='Sort by',choices=['Latest first','Oldest first', 'Increasing start date', 'Decreasing start date', 'Increasing end date', 'Decreasing end date', 'Increasing duration', 'Decreasing duration'])
    select_by = SelectField(label='Select', choices=['All', 'Casual leaves only', 'Non Casual leaves only', 'Pending', 'Sanctioned', 'Not Sanctioned'])
    submit = SubmitField(label='Filter')


class SelectSortForm2(FlaskForm):
    sort_by = SelectField(label='Sort by',choices=['Latest first','Oldest first', 'Increasing start date', 'Decreasing start date', 'Increasing end date', 'Decreasing end date', 'Increasing duration', 'Decreasing duration'])
    select_by = SelectField(label='Select', choices=['All', 'Approved', 'Rejected'])
    submit = SubmitField(label='Filter')


class RejectRemarks(FlaskForm):
    remarks = StringField(label='Remarks', validators=[DataRequired()])
    submit = SubmitField(label='Confirm')


class LeaveCancellationForm(FlaskForm):
    from_date = DateField(label='Cancel From',format="%Y-%m-%d",validators=[DataRequired()])
    remarks = StringField(label = 'Reason for cancelling Leave', validators = [DataRequired()])
    submit = SubmitField(label = 'Cancel Leave')


class MailForm(FlaskForm):
    submit = SubmitField(label= 'Send Mail')


class RequestResetForm(FlaskForm):
    email =  StringField('Email', validators=[Email(), DataRequired()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email_to_check):
        email_address = User.query.filter_by(email_address=email_to_check.data).first()
        if email_address is None:
            raise ValidationError('There is no account with this email: Please try a different email address')

class ResetPasswordForm(FlaskForm):
    password1 = PasswordField(label='Password', validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Reset Password')


class DeleteUserForm(FlaskForm):
    submit = SubmitField('Delete Account')

# class CreateTableForm(FlaskForm):
#     table_name = StringField(label='Name of the Table',validators=[DataRequired()])
#     submit = SubmitField(label='Create Table')