__author__ = 'sgangichetty'

import sqlite3
import csv
import os
import time, datetime

max_customer_id = 57970704  # this is a static max based on existing data on the table
request_cols = ['order_id',
                'gender',
                'title',
                'given_name',
                'middle_initial',
                'surname',
                'street_address',
                'city',
                'state',
                'zipcode',
                'country',
                'country_full',
                'email_address',
                'username',
                #'password',
                'telephone_number',
                'mothers_maiden',
                'birthday',
                'CC_type',
                'cvv2',
                'cc_expiration',
                'national_id',
                'color',
                'occupation',
                'ref_domain',
                'guid',
                'latitude',
                'longitude',
                'total_session_length',
                'pageview_pre_purchase_visits',
                'time_on_cart',
                'product_view_count',
                'total_visit_clicks',
                'customer_credit_selection',
                'payment_type',
                'plan_type',
                'existing_ecom_customer']


def get_random_records(req_cols, db_table_name, database_name):
    """Function gets one record from the db table"""
    query = '''select {}
            from {}
            order by random()
            limit 1;'''.format(','.join(map(str, request_cols)), db_table_name)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    result = cursor.execute(query)
    tup_row = result.fetchone()
    dict_row = dict(zip(req_cols, tup_row))
    connection.close()
    return tup_row, dict_row


def get_time_stamp():
    """a simple time stamp generator """
    return int(time.mktime(datetime.datetime.utcnow().timetuple()))


'''Implement a record write back to the db here and establish call when data is streamed into the app'''

# remove the file if it exists - so its not always appending
try:
    os.remove('fraud_data.csv')
except OSError:
    pass

while True:
    if __name__ == '__main__':
        sel_rec = (
            get_random_records(req_cols=request_cols, db_table_name='order_claim_ticket_v3',
                               database_name='transactions2.db'))
        sel_rec[1]['assigned_customer_id'] = max_customer_id + 1
        sel_rec[1]['opcode'] = 'i'
        stream_tuple = ('i', get_time_stamp()) + sel_rec[0] + (max_customer_id + 1,)
        max_customer_id += 1
        time.sleep(.20)
        print(stream_tuple)  # this will be published into a file or an ESP endpoint
        with open('fraud_data.csv', 'a', newline='') as myfile:
            writer = csv.writer(myfile)
            writer.writerow(stream_tuple)
