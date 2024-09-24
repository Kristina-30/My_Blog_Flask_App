from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class CreatePostForm(FlaskForm):
    title = StringField("Titlu", validators=[DataRequired()])
    subtitle = StringField("Subtitlu", validators=[DataRequired()])
    author = StringField("Nume", validators=[DataRequired()])
    img_url = StringField("URL Imagine", validators=[DataRequired(), URL()])
    body = CKEditorField("Conținutul blogului", validators=[DataRequired()])
    submit = SubmitField("Postează")


class RegisterForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    name = StringField(label="Nume", validators=[DataRequired()])
    password = PasswordField(label="Parola", validators=[DataRequired()])
    submit = SubmitField("Înregistrează-te")


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Parola", validators=[DataRequired()])
    submit = SubmitField("Log in")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comentează", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
