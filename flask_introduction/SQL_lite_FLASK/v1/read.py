from app import db, Message, app

with app.app_context():
    db.create_all()  # sukurs mūsų lentelę DB
    all_messages = Message.query.all()
    print(all_messages)

    message_1 = db.session.get(Message,1)
    print(message_1)