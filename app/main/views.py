from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from ..models import User, Pitch, Comment
from flask_login import login_required, current_user
from .. import db, photos
from .forms import PitchForm, CommentForm, UpdateProfile
import markdown2