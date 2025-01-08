from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages',methods=['GET','POST'])
def messages():
    if request.method == "GET":
        messages = [message.to_dict() for message in Message.query.all()]
        return make_response(
            messages,
            200
        )
    elif request.method == "POST":
        data = request.get_json()
        new_message = Message(
            body=data['body'],
            username=data['username']
        )
        db.session.add(new_message)
        db.session.commit()
        message_dict = new_message.to_dict()
        return make_response(
            message_dict,
            200
        )

@app.route('/messages/<int:id>',methods=['GET','PATCH','DELETE'])
def messages_by_id(id):
    message = Message.query.filter_by(id=id).first()
    if request.method == "GET":
        response_body = message.to_dict()
        status_code = 200
    elif request.method == "PATCH":
        data = request.get_json()
        for field in data:
            setattr(message, field, data[field])
        db.session.add(message)
        db.session.commit()
        response_body = message.to_dict()
        status_code = 200
    elif request.method == "DELETE":
        db.session.delete(message)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "Message deleted."
        }
        status_code = 200

    return make_response(
        response_body,
        status_code
    )

if __name__ == '__main__':
    app.run(port=4000)
