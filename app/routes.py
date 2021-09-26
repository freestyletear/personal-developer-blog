from app import app, requests, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, abort
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, CommentForm
from app.models import User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required
