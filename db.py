from deta import Deta


def check(conn_str):
    db = Deta().Base('python-flask')
    # db.put({"message": "It works!"}, "test")
    return db.get("test")

