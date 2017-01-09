def execute_fraud_rules(order_id,
                        gender,
                        title,
                        given_name,
                        middle_initial,
                        surname,
                        street_address,
                        city,
                        state,
                        zipcode,
                        country,
                        country_full,
                        email_address,
                        username,
                        telephone_number,
                        mothers_maiden,
                        birthday,
                        CC_type,
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
                        pageview_pre_purchase_visits,
                        time_on_cart,
                        product_view_count,
                        total_visit_clicks,
                        customer_credit_selection,
                        payment_type,
                        plan_type,
                        existing_ecom_customer):
    """Output: order_id,
                gender,
                title,
                given_name,
                middle_initial,
                surname,
                street_address,
                city,
                state,
                zipcode,
                country,
                country_full,
                email_address,
                username,
                telephone_number,
                mothers_maiden,
                birthday,
                CC_type,
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
                pageview_pre_purchase_visits,
                time_on_cart,
                product_view_count,
                total_visit_clicks,
                customer_credit_selection,
                payment_type,
                plan_type,
                existing_ecom_customer,
                total_fraud_score,
                total_merit_score,
                outsort_score""";

    total_fraud_score = float(exec_red_light_rules(plan_type,
                                                   payment_type,
                                                   time_on_cart,
                                                   total_visit_clicks))

    total_merit_score = float(exec_green_light_rules(plan_type,
                                                     payment_type,
                                                     CC_type))
    outsort_score = float(calc_outsort_score(total_fraud_score, total_merit_score))

    return (order_id,
            gender,
            title,
            given_name,
            middle_initial,
            surname,
            street_address,
            city,
            state,
            zipcode,
            country,
            country_full,
            email_address,
            username,
            telephone_number,
            mothers_maiden,
            birthday,
            CC_type,
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
            pageview_pre_purchase_visits,
            time_on_cart,
            product_view_count,
            total_visit_clicks,
            customer_credit_selection,
            payment_type,
            plan_type,
            existing_ecom_customer,
            total_fraud_score,
            total_merit_score,
            outsort_score)


# outsort score computation
def calc_outsort_score(total_fraud_score, total_merit_score):
    outsort_score = total_fraud_score - total_merit_score
    if outsort_score <= 0:
        outsort_score = 0
    return outsort_score


# red_light rule resolution

def exec_red_light_rules(plan_type, payment_type, time_on_cart, total_visit_clicks):
    total_fraud_score = 0
    if plan_type == 'Unlimited' and payment_type in ('24 Month Contract', 'Full Price') and time_on_cart < 10:
        total_fraud_score += 100
    if total_visit_clicks < 20:
        total_fraud_score += 100
    return total_fraud_score


# green light rule resolution
def exec_green_light_rules(plan_type, payment_type, CC_type):
    total_merit_score = 0
    if plan_type.lower() == 'unlimited' and CC_type.lower() == 'mastercard':
        if payment_type.lower() == '18 month lease':
            total_merit_score += 100
    return total_merit_score