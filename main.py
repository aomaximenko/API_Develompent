from flask import Flask, jsonify, request

from model.post import Post

import json

posts = []

app = Flask(__name__)


class CustomEncoder(json.JSONEncoder):
    def default(self, Post):
        return Post.__dict__


@app.route('/post', methods=['POST'])
def create_post():
    if not posts:
        new_post_id = 1
    else:
        new_post_id = posts[-1].id + 1
    post_json = request.get_json()
    post = Post(post_json['body'], post_json['author'], new_post_id)
    posts.append(post)
    return jsonify({"status": "success"})


@app.route('/post', methods=['GET'])
def read_posts():
    return json.dumps({'posts': posts}, cls=CustomEncoder)


@app.route('/post/<post_id>', methods=['GET'])
def read_post(post_id):
    for i in posts:
        if i.id == int(post_id):
            return i.body
    return "Post not found"


@app.route('/post/<post_id>', methods=['PUT'])
def update_post(post_id):
    update_json = request.get_json()
    for i in posts:
        if i.id == int(post_id):
            i.body = update_json['body']
            return jsonify({"status": "success"})
    return "Post not found"

@app.route('/post/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    for i in posts:
        if i.id == int(post_id):
            posts.remove(i)
            return jsonify({"status": "success"})
    return "Post not found"


if __name__ == '__main__':
    app.run()
