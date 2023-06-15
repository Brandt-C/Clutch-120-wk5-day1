from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from .forms import CreatePostForm
from ..models import Post

ig = Blueprint('ig', __name__, template_folder='ig_templates' )


@ig.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm()
    if request.method == 'POST':
        if form.validate():
            title = form.title.data
            body = form.body.data
            img_url = form.img_url.data

            new = Post(title, body, img_url, current_user.id)
            new.save_post()
            return redirect(url_for('land'))
    return render_template('create_post.html', form=form)

@ig.route('/feed', methods=['GET'])
@login_required
def feed():
    # posts = Post.query.all()
    posts = Post.query.order_by(Post.date_created.desc()).all()
    print(posts)

    return render_template('feed.html', posts=posts)
