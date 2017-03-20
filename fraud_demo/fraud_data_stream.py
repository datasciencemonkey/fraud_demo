__author__ = 'sgangichetty'

import sqlite3
import csv
import os
import time, datetime
from pickle import load
from numpy import array

file_name = 'finalized_model.sav'
loaded_model = load(open(file_name, 'rb'))

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
                # 'password',
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


# score the ML Model
def score_model(total_session_length,
                pageview_pre_purchase_visits,
                time_on_cart,
                product_view_count,
                total_visit_clicks):
    X = array([total_session_length,
               pageview_pre_purchase_visits,
               time_on_cart,
               product_view_count,
               total_visit_clicks])
    score = loaded_model.predict(X.reshape(1, -1))
    return score[0]


while True:
    if __name__ == '__main__':
        sel_rec = (
            get_random_records(req_cols=request_cols, db_table_name='order_claim_ticket_v3',
                               database_name='transactions2.db'))
        sel_rec[1]['assigned_customer_id'] = max_customer_id + 1
        sel_rec[1]['opcode'] = 'i'
        sel_rec[1]['os_model_score'] = score_model(sel_rec[1]['total_session_length'],
                                                   sel_rec[1]['pageview_pre_purchase_visits'],
                                                   sel_rec[1]['time_on_cart'],
                                                   sel_rec[1]['product_view_count'],
                                                   sel_rec[1]['total_visit_clicks'])
        os_model_score = sel_rec[1]['os_model_score']
        stream_tuple = ('i','n', get_time_stamp()) + sel_rec[0] + (max_customer_id + 1,) + (os_model_score,)
        max_customer_id += 1
        time.sleep(.20)
        print(stream_tuple)  # this will be published into a file or an ESP endpoint
        with open('fraud_data.csv', 'a', newline='') as myfile:
            writer = csv.writer(myfile)
            writer.writerow(stream_tuple)
