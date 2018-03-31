# coding:utf-8
from flask.ext.wtf import Form
from wtforms import SelectField, StringField, TextAreaField, SubmitField, \
    PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..main.forms import CommentForm


class CommonForm(Form):
    types = SelectField(u'blog types', coerce=int, validators=[DataRequired()])
    source = SelectField(u'source', coerce=int, validators=[DataRequired()])


class SubmitArticlesForm(CommonForm):
    title = StringField(u'title', validators=[DataRequired(), Length(1, 64)])
    content = TextAreaField(u'content', validators=[DataRequired()])
    summary = TextAreaField(u'summary', validators=[DataRequired()])


class ManageArticlesForm(CommonForm):
    pass


class DeleteArticleForm(Form):
    articleId = StringField(validators=[DataRequired()])


class DeleteArticlesForm(Form):
    articleIds = StringField(validators=[DataRequired()])


class DeleteCommentsForm(Form):
    commentIds = StringField(validators=[DataRequired()])


class AdminCommentForm(CommentForm):
    article = StringField(validators=[DataRequired()])


class AddArticleTypeForm(Form):
    name = StringField(u'type name', validators=[DataRequired(), Length(1, 64)])
    introduction = TextAreaField(u'type info')
    setting_hide = SelectField(u'settings', coerce=int, validators=[DataRequired()])
    menus = SelectField(u'navigation', coerce=int, validators=[DataRequired()])
# You must add coerce=int, or the SelectFile validate function only validate the int data


class EditArticleTypeForm(AddArticleTypeForm):
    articleType_id = StringField(validators=[DataRequired()])


class AddArticleTypeNavForm(Form):
    name = StringField(u'navigation name', validators=[DataRequired(), Length(1, 64)])


class EditArticleNavTypeForm(AddArticleTypeNavForm):
    nav_id = StringField(validators=[DataRequired()])


class SortArticleNavTypeForm(AddArticleTypeNavForm):
    order = StringField(u'id', validators=[DataRequired()])


class CustomBlogInfoForm(Form):
    title = StringField(u'blog title', validators=[DataRequired()])
    signature = TextAreaField(u'about', validators=[DataRequired()])
    navbar = SelectField(u'navigation style', coerce=int, validators=[DataRequired()])


class AddBlogPluginForm(Form):
    title = StringField(u'plugin name', validators=[DataRequired()])
    note = TextAreaField(u'info')
    content = TextAreaField(u'content', validators=[DataRequired()])


class ChangePasswordForm(Form):
    old_password = PasswordField(u'old password', validators=[DataRequired()])
    password = PasswordField(u'new password', validators=[
        DataRequired(), EqualTo('password2', message=u'two passwords should be the same！')])
    password2 = PasswordField(u'confirm ', validators=[DataRequired()])


class EditUserInfoForm(Form):
    username = StringField(u'Name', validators=[DataRequired()])
    email = StringField(u'email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'confirm password', validators=[DataRequired()])
