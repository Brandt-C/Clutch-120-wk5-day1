from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

from .forms import CreatePostForm, UpdatePostForm
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
            return redirect(url_for('ig.feed'))
    return render_template('create_post.html', form=form)

@ig.route('/feed', methods=['GET'])
@login_required
def feed():
    # posts = Post.query.all()
    # posts = Post.query.order_by(Post.date_created.desc()).all()
    posts = Post.query.order_by(Post.date_created).all()[::-1]
    print(posts)

    return render_template('feed.html', posts=posts)

@ig.route('/post/<int:post_id>')
@login_required
def ind_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return render_template('post.html', p = post)
    else:
        print('That post doesn\'t exist!')
    return redirect(url_for('ig.feed'))


@ig.route('/post/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get(post_id)
    if post.user_id != current_user.id:
        flash('This is not your post to modify!', 'danger')
        return redirect(url_for('ig.feed'))
    form = UpdatePostForm()
    if request.method == 'POST':
        if form.validate():
            title = form.title.data
            body = form.body.data
            img_url = form.img_url.data
            print(title, body, img_url)

            post.title = title
            post.body = body
            post.img_url = img_url
            post.save_changes()
            flash('post updated', 'secondary')
            return redirect(url_for('ig.ind_post', post_id=post.id))

    return render_template('update_post.html', form=form, post=post)


@ig.route('/post/delete/<int:post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post.user_id == current_user.id:
        post.delete_post()
        flash('post is gone forever!', 'warning')
    else:
        flash("Can't delete what's not yours!", 'danger')
    return redirect(url_for('ig.feed'))


