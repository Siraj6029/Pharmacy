def add_dummy_data_for_distributor(db):
    db.session.execute("INSERT into distributor (name, address, contact) \
    VALUES ('UDL', 'peshawar', '1234'), ('siraj', 'peshawar', '5678')")

def add_dummy_data_for_customer(db):
    db.session.execute("INSERT into customer (name, address) VALUES ('siraj', '12345')")