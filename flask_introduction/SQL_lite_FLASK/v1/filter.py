from app import db, Message, app

with app.app_context():
    db.create_all()  # sukurs mūsų lentelę DB

    message_antanas = Message.query.filter_by(name='Antanas')
    print(message_antanas.all())

    # [Antanas - antanas@mail.lt]