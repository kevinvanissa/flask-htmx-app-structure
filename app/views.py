from flask import Blueprint, render_template, request, flash, redirect, url_for, session, g
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from app.forms import LoginForm, SignupForm, ContactForm
from app.models import User
from app.extensions import db


main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
error_bp = Blueprint('error', __name__, url_prefix='/error')

# ================ STARTUP FUNCTIONS ===================
def load_user(id):
    return db.session.get(User, int(id))
    #return User.query.get(int(id))

def before_request_func():
    g.user = current_user


# ================= ERROR HANDLERS =====================
@error_bp.app_errorhandler(404)
def handle_404(error):
    return render_template('errors/404.html'), 404


@error_bp.app_errorhandler(401)
def handle_401(error):
    return render_template('errors/401.html'), 401


@error_bp.app_errorhandler(500)
def handle_500(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500


@error_bp.app_errorhandler(413)
def handle_413(error):
    db.session.rollback()
    return render_template('errors/413.html'), 413


# ================= AUTH VIEWS =======================

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('There is already a user with this email!', category='danger')
            return redirect(url_for('auth.signup'))
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(
                form.password.data))
        db.session.add(user)
        db.session.commit()
        flash(
            'Thanks for registering. You can now log in',
            category='info')
        return redirect(url_for('auth.login'))
    return render_template(
        'auth/signup.html',
        form=form,
        )


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            flash(
                'The username or password you entered is incorrect!',
                category='danger')
            return redirect(url_for('auth.login'))

        if user.password is None or user.password == "":
            flash(
                'The username or password you entered is incorrect!',
                category='danger')
            return redirect(url_for('auth.login'))
        
       
        if user and check_password_hash(
                user.password,
                form.password.data):
            print("logging in user...")
            login_user(user)
            flash('You have successfully logged in', category='success')
            return redirect(request.args.get('next') or url_for('main.dashboard'))
        else:
            flash('The username or password you entered is incorrect!', category='danger')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html',
                           form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out!', category='success')
    return redirect(url_for('auth.login'))

# ============== Info Pages ======================

@main_bp.route('/about')
def about():
    return render_template('pages/about.html')


@main_bp.route('/contact')
def contact():
    form = ContactForm()
    return render_template('pages/contact.html', form=form)


# ============== Main Applications ==================

@main_bp.route('/')
def index():
    return render_template('pages/index.html') 

@main_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('pages/dashboard.html') 

@main_bp.route('/test_modal', methods=['GET'])
@login_required
def test_modal():
    return render_template('modals/modal_test.html') 


@main_bp.route('/get_data_test', methods=['GET'])
@login_required
def get_data_test():
    tasks = [
            {'task': 'Configure Application Tests', 'status': 'Pending'},
            {'task': 'Create Flask Tutorial', 'status': 'Pending'},
            {'task': 'Learn Golang', 'status': 'Completed'},
            {'task': 'Learn Rust', 'status': 'In Progress'}
           ]

    return render_template('partials/_data_test.html', tasks=tasks) 




