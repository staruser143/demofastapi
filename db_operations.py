# db_operations.py
from sqlalchemy import text
from models import Session, customers, User, Address

def insert_records(records):
    """
    Inserts the given records into the database.

    Args:
        records (list): A list of records to be inserted.

    Returns:
        None

    Raises:
        Exception: If there is an error inserting the records.

    """
    session = Session()
    try:
        session.add_all(records)
        session.commit()
        print("Records inserted successfully")
    except Exception as e:
        print(f"Error inserting records: {e}")
        session.rollback()
    finally:
        session.close()

def fetch_records():
    session = Session()
    try:
        records = session.query(customers).all()
        for record in records:
            print(f"id: {record.id}, name: {record.name}, age: {record.age}")
        return records
    except Exception as e:
        print(f"Error fetching records: {e}")
        return []
    finally:
        session.close()

def fetch_users_with_addresses():
    session = Session()
    try:
        results = session.query(User, Address).join(Address, User.id == Address.user_id).all()
        for user, address in results:
            print(f"User: {user.name}, Age: {user.age}, Address: {address.address}")
        return results
    except Exception as e:
        print(f"Error fetching joined records: {e}")
        return []
    finally:
        session.close()

def execute_raw_sql(sql_query, params=None):
    session = Session()
    try:
        result = session.execute(text(sql_query), params).fetchall()
        for row in result:
            print(row)
        return result
    except Exception as e:
        print(f"Error executing raw SQL: {e}")
        return []
    finally:
        session.close()


def fetch_users_with_pagination(offset, limit):
    session = Session()
    try:
        results = session.query(User).offset(offset).limit(limit).all()
        for user in results:
            print(f"User: {user.name}, Age: {user.age}")
        return results
    except Exception as e:
        print(f"Error fetching paginated records: {e}")
        return []
    finally:
        session.close()
