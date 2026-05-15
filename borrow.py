BORROW_AUDIT_RULE = "auto_record"


def borrow_book(username, book_id):
    record = {
        "username": username,
        "book_id": book_id,
        "status": "borrowed"
    }
    return record


def describe_borrow_rule():
    return "当前借阅审核规则：" + BORROW_AUDIT_RULE
