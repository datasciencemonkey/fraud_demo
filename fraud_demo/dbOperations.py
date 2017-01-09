__author__ = 'sgangichetty'

import sqlite3


def create_fraud_claim_ticket(database_uri, table_name):
    """RUN ONLY THE FIRST TIME>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    Function is very specific to this project. Don't use outside intended scope.
    Creating a table on SQLite to save the fraud data
    This part of the code establishes connections and creates the needed table
    usage: create_fraud_claim_ticket('transactions.db','my_test_table')
    """
    connection = sqlite3.connect(database_uri)
    cursor = connection.cursor()
    create_table = """CREATE TABLE IF NOT EXISTS {} (order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    gender text,
                    title text,
                    given_name text,
                    middle_initial text,
                    surname text,
                    street_address text,
                    city text,
                    state text,
                    state_full text,
                    zipcode text,
                    country text,
                    country_full text,
                    email_address text,
                    username text,
                    password text,
                    browser_user_agent text,
                    telephone_number text,
                    telephone_number_country_code text,
                    mothers_maiden text,
                    birthday text,
                    age INTEGER,
                    CC_type text,
                    CC_number text,
                    cvv2 text,
                    cc_expiration text,
                    national_id text,
                    color text,
                    occupation text,
                    ref_domain text,
                    guid text,
                    latitude decimal(8,2),
                    longitude decimal(8,2),
                    total_session_length decimal(8,2),
                    pageview_pre_purchase_visits INTEGER,
                    time_on_cart decimal(8,2),
                    product_view_count INTEGER,
                    total_visit_clicks INTEGER,
                    fraud INTEGER,
                    customer_credit_selection text,
                    payment_type text,
                    plan_type text,
                    existing_ecom_customer INTEGER,
                    dtree_node INTEGER,
                    em_event_probability decimal(8,2),
                    em_classification INTEGER,
                    avs_response_code text,
                    customer_id INTEGER
                    )""".format(table_name)
    try:
        cursor.execute('drop table if exists {}'.format(table_name))
        cursor.execute(create_table)
        print('Query Succeeded - table {} was built or it already exists'.format(table_name))
        connection.close()
    except:
        raise BaseException('Check DDL or connection parameters')  # Some Generic exception that pushes traceback


# write_df.to_sql('order_claim_ticket_la', conn, if_exists='append', index=False, chunksize=10000)

def insert_records_to_db(df, database_name):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    query = """insert into order_claim_ticket_v3(
                        gender,
                        title,
                        given_name,
                        middle_initial,
                        surname,
                        street_address,
                        city,
                        state,
                        state_full,
                        zipcode,
                        country,
                        country_full,
                        email_address,
                        username,
                        password,
                        browser_user_agent,
                        telephone_number,
                        telephone_number_country_code,
                        mothers_maiden,
                        birthday,
                        age,
                        CC_type,
                        CC_number,
                        cvv2,
                        cc_expiration,
                        national_id,
                        color,
                        occupation,
                        ref_domain,
                        guid,
                        latitude,
                        longitude,
                        total_session_length,
                        pageview_pre_purchase_visits ,
                        time_on_cart,
                        product_view_count ,
                        total_visit_clicks ,
                        fraud ,
                        customer_credit_selection ,
                        payment_type ,
                        plan_type ,
                        existing_ecom_customer,
                        dtree_node,
                        em_event_probability,
                        em_classification,
                        avs_response_code,
                        customer_id
                        ) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                                            ,?,?,?,?,?,?,?,?,?,?,?
                                            ,?,?,?,?,?)"""
    try:
        cursor.executemany(query, df.to_records(index=False))
        print("Insert query Succeeded")
        connection.commit()
        connection.close()
    except:
        raise BaseException("Insert Query failed")


if __name__ == '__main__':
    create_fraud_claim_ticket('transactions2.db', 'order_claim_ticket_v3')
