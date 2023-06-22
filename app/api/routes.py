from flask import Blueprint, request, json

from ..models import Post


api = Blueprint('api', __name__, url_prefix='/api')

@api.get('/posts') 
def get_posts():
    posts = Post.query.all()
    post_list = [p.to_dict() for p in posts]
    return {
        'status' : 'ok',
        'posts' : post_list 
    }

@api.get('/post/<int:post_id>')
def get_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return {
            'post': post.to_dict(),
            'status': 'ok'
        }
    else:
        return {
            'status' : 'NOT ok',
            'message' : 'there is no post for that id'
        }
    
@api.post('/createpost')
def create_post_api():
    data = request.json  #this is coming from the POST request body
    title = data['title']
    body = data['body']
    img_url = data['img_url']
    user_id = data['user_id']

    new = Post(title, body, img_url, user_id)
    new.save_post()
    return {
        'status': 'ok',
        'message' : 'New post has been created!'
    }
