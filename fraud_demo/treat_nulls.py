def treat_nulls(datetime,
                order_id,
                customer_id,
                rules_outsort_score,
                scikit_ml_model_score,
                sas_ml_model_score,
                sas_ml_model_probability
                ):
    """Output: datetime, order_id, customer_id,
rules_outsort_score,
scikit_ml_model_score,
sas_ml_model_score,
sas_ml_model_probability, weighted_alert_score""";
    weighted_alert_score = (float(replaceNull(sas_ml_model_score)) + float(
        replaceNull(scikit_ml_model_score))) * 100 + (float(replaceNull(
        rules_outsort_score)) / 100)
    return (datetime,
            order_id,
            customer_id,
            rules_outsort_score,
            scikit_ml_model_score,
            sas_ml_model_score,
            sas_ml_model_probability, weighted_alert_score)


def replaceNull(x):
    if x is None:
        return 0
    else:
        return x
