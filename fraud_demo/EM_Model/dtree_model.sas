*------------------------------------------------------------*;
* EM SCORE CODE;
*------------------------------------------------------------*;
*------------------------------------------------------------*;
* EM SCORE CODE;
*------------------------------------------------------------*;
*------------------------------------------------------------*;
* TOOL: Input Data Source;
* TYPE: SAMPLE;
* NODE: Ids5;
*------------------------------------------------------------*;
*------------------------------------------------------------*;
* TOOL: Partition Class;
* TYPE: SAMPLE;
* NODE: Part3;
*------------------------------------------------------------*;
*------------------------------------------------------------*;
* TOOL: Extension Class;
* TYPE: MODEL;
* NODE: Tree3;
*------------------------------------------------------------*;
****************************************************************;
******             DECISION TREE SCORING CODE             ******;
****************************************************************;

******         LENGTHS OF NEW CHARACTER VARIABLES         ******;
LENGTH I_fraud  $    1;
LENGTH _WARN_  $    4;

******              LABELS FOR NEW VARIABLES              ******;
label _NODE_ = 'Node' ;
label _LEAF_ = 'Leaf' ;
label P_fraud0 = 'Predicted: fraud=0' ;
label P_fraud1 = 'Predicted: fraud=1' ;
label Q_fraud0 = 'Unadjusted P: fraud=0' ;
label Q_fraud1 = 'Unadjusted P: fraud=1' ;
label V_fraud0 = 'Validated: fraud=0' ;
label V_fraud1 = 'Validated: fraud=1' ;
label I_fraud = 'Into: fraud' ;
label U_fraud = 'Unnormalized Into: fraud' ;
label _WARN_ = 'Warnings' ;


******      TEMPORARY VARIABLES FOR FORMATTED VALUES      ******;
LENGTH _ARBFMT_1 $      1; DROP _ARBFMT_1;
_ARBFMT_1 = ' '; /* Initialize to avoid warning. */
LENGTH _ARBFMT_12 $     12; DROP _ARBFMT_12;
_ARBFMT_12 = ' '; /* Initialize to avoid warning. */


******             ASSIGN OBSERVATION TO NODE             ******;
IF  NOT MISSING(time_on_cart ) AND
  time_on_cart  <       5.596007671555 THEN DO;
  _ARBFMT_12 = PUT( plan_type , $CHAR12.);
   %DMNORMIP( _ARBFMT_12);
  IF _ARBFMT_12 IN ('SMALL - 3GB' ,'MEDIUM - 6GB' ) THEN DO;
    _NODE_  =                    4;
    _LEAF_  =                    1;
    P_fraud0  =                    1;
    P_fraud1  =                    0;
    Q_fraud0  =                    1;
    Q_fraud1  =                    0;
    V_fraud0  =                    1;
    V_fraud1  =                    0;
    I_fraud  = '0' ;
    U_fraud  =                    0;
    END;
  ELSE DO;
    _NODE_  =                    5;
    _LEAF_  =                    2;
    P_fraud0  =     0.09459459459459;
    P_fraud1  =      0.9054054054054;
    Q_fraud0  =     0.09459459459459;
    Q_fraud1  =      0.9054054054054;
    V_fraud0  =     0.03225806451612;
    V_fraud1  =     0.96774193548387;
    I_fraud  = '1' ;
    U_fraud  =                    1;
    END;
  END;
ELSE DO;
  _ARBFMT_12 = PUT( plan_type , $CHAR12.);
   %DMNORMIP( _ARBFMT_12);
  IF _ARBFMT_12 IN ('MEDIUM' ) THEN DO;
    _NODE_  =                    6;
    _LEAF_  =                    3;
    P_fraud0  =                    0;
    P_fraud1  =                    1;
    Q_fraud0  =                    0;
    Q_fraud1  =                    1;
    V_fraud0  =                    0;
    V_fraud1  =                    1;
    I_fraud  = '1' ;
    U_fraud  =                    1;
    END;
  ELSE DO;
    IF  NOT MISSING(pageview_pre_purchase_visits ) AND
      pageview_pre_purchase_visits  <                 66.5 THEN DO;
      IF  NOT MISSING(total_session_length ) AND
               21.8247237795 <= total_session_length  THEN DO;
        _NODE_  =                   11;
        _LEAF_  =                    5;
        P_fraud0  =                    1;
        P_fraud1  =                    0;
        Q_fraud0  =                    1;
        Q_fraud1  =                    0;
        V_fraud0  =                  0.8;
        V_fraud1  =                  0.2;
        I_fraud  = '0' ;
        U_fraud  =                    0;
        END;
      ELSE DO;
        _NODE_  =                   10;
        _LEAF_  =                    4;
        P_fraud0  =                    0;
        P_fraud1  =                    1;
        Q_fraud0  =                    0;
        Q_fraud1  =                    1;
        V_fraud0  =                    0;
        V_fraud1  =                    1;
        I_fraud  = '1' ;
        U_fraud  =                    1;
        END;
      END;
    ELSE DO;
      _NODE_  =                    9;
      _LEAF_  =                    6;
      P_fraud0  =     0.99967087846829;
      P_fraud1  =      0.0003291215317;
      Q_fraud0  =     0.99967087846829;
      Q_fraud1  =      0.0003291215317;
      V_fraud0  =      0.9996661213315;
      V_fraud1  =     0.00033387866849;
      I_fraud  = '0' ;
      U_fraud  =                    0;
      END;
    END;
  END;

****************************************************************;
******          END OF DECISION TREE SCORING CODE         ******;
****************************************************************;

drop _LEAF_;
*------------------------------------------------------------*;
* TOOL: Score Node;
* TYPE: ASSESS;
* NODE: Score4;
*------------------------------------------------------------*;
*------------------------------------------------------------*;
* Score4: Creating Fixed Names;
*------------------------------------------------------------*;
LABEL EM_SEGMENT = 'Node';
EM_SEGMENT = _NODE_;
LABEL EM_EVENTPROBABILITY = 'Probability for level 1 of fraud';
EM_EVENTPROBABILITY = P_fraud1;
LABEL EM_PROBABILITY = 'Probability of Classification';
EM_PROBABILITY =
max(
P_fraud1
,
P_fraud0
);
LENGTH EM_CLASSIFICATION $%dmnorlen;
LABEL EM_CLASSIFICATION = "Prediction for fraud";
EM_CLASSIFICATION = I_fraud;
*------------------------------------------------------------*;
* TOOL: Input Data Source;
* TYPE: SAMPLE;
* NODE: Ids5;
*------------------------------------------------------------*;
*------------------------------------------------------------*;
* TOOL: Partition Class;
* TYPE: SAMPLE;
* NODE: Part3;
*------------------------------------------------------------*;
*------------------------------------------------------------*;
* TOOL: Extension Class;
* TYPE: MODEL;
* NODE: Tree3;
*------------------------------------------------------------*;
****************************************************************;
******             DECISION TREE SCORING CODE             ******;
****************************************************************;

******         LENGTHS OF NEW CHARACTER VARIABLES         ******;
LENGTH I_fraud  $    1;
LENGTH _WARN_  $    4;

******              LABELS FOR NEW VARIABLES              ******;
label _NODE_ = 'Node' ;
label _LEAF_ = 'Leaf' ;
label P_fraud0 = 'Predicted: fraud=0' ;
label P_fraud1 = 'Predicted: fraud=1' ;
label Q_fraud0 = 'Unadjusted P: fraud=0' ;
label Q_fraud1 = 'Unadjusted P: fraud=1' ;
label V_fraud0 = 'Validated: fraud=0' ;
label V_fraud1 = 'Validated: fraud=1' ;
label I_fraud = 'Into: fraud' ;
label U_fraud = 'Unnormalized Into: fraud' ;
label _WARN_ = 'Warnings' ;


******      TEMPORARY VARIABLES FOR FORMATTED VALUES      ******;
LENGTH _ARBFMT_1 $      1; DROP _ARBFMT_1;
_ARBFMT_1 = ' '; /* Initialize to avoid warning. */
LENGTH _ARBFMT_12 $     12; DROP _ARBFMT_12;
_ARBFMT_12 = ' '; /* Initialize to avoid warning. */


******             ASSIGN OBSERVATION TO NODE             ******;
IF  NOT MISSING(time_on_cart ) AND
  time_on_cart  <       5.596007671555 THEN DO;
  _ARBFMT_12 = PUT( plan_type , $CHAR12.);
   %DMNORMIP( _ARBFMT_12);
  IF _ARBFMT_12 IN ('SMALL - 3GB' ,'MEDIUM - 6GB' ) THEN DO;
    _NODE_  =                    4;
    _LEAF_  =                    1;
    P_fraud0  =                    1;
    P_fraud1  =                    0;
    Q_fraud0  =                    1;
    Q_fraud1  =                    0;
    V_fraud0  =                    1;
    V_fraud1  =                    0;
    I_fraud  = '0' ;
    U_fraud  =                    0;
    END;
  ELSE DO;
    _NODE_  =                    5;
    _LEAF_  =                    2;
    P_fraud0  =     0.09459459459459;
    P_fraud1  =      0.9054054054054;
    Q_fraud0  =     0.09459459459459;
    Q_fraud1  =      0.9054054054054;
    V_fraud0  =     0.03225806451612;
    V_fraud1  =     0.96774193548387;
    I_fraud  = '1' ;
    U_fraud  =                    1;
    END;
  END;
ELSE DO;
  _ARBFMT_12 = PUT( plan_type , $CHAR12.);
   %DMNORMIP( _ARBFMT_12);
  IF _ARBFMT_12 IN ('MEDIUM' ) THEN DO;
    _NODE_  =                    6;
    _LEAF_  =                    3;
    P_fraud0  =                    0;
    P_fraud1  =                    1;
    Q_fraud0  =                    0;
    Q_fraud1  =                    1;
    V_fraud0  =                    0;
    V_fraud1  =                    1;
    I_fraud  = '1' ;
    U_fraud  =                    1;
    END;
  ELSE DO;
    IF  NOT MISSING(pageview_pre_purchase_visits ) AND
      pageview_pre_purchase_visits  <                 66.5 THEN DO;
      IF  NOT MISSING(total_session_length ) AND
               21.8247237795 <= total_session_length  THEN DO;
        _NODE_  =                   11;
        _LEAF_  =                    5;
        P_fraud0  =                    1;
        P_fraud1  =                    0;
        Q_fraud0  =                    1;
        Q_fraud1  =                    0;
        V_fraud0  =                  0.8;
        V_fraud1  =                  0.2;
        I_fraud  = '0' ;
        U_fraud  =                    0;
        END;
      ELSE DO;
        _NODE_  =                   10;
        _LEAF_  =                    4;
        P_fraud0  =                    0;
        P_fraud1  =                    1;
        Q_fraud0  =                    0;
        Q_fraud1  =                    1;
        V_fraud0  =                    0;
        V_fraud1  =                    1;
        I_fraud  = '1' ;
        U_fraud  =                    1;
        END;
      END;
    ELSE DO;
      _NODE_  =                    9;
      _LEAF_  =                    6;
      P_fraud0  =     0.99967087846829;
      P_fraud1  =      0.0003291215317;
      Q_fraud0  =     0.99967087846829;
      Q_fraud1  =      0.0003291215317;
      V_fraud0  =      0.9996661213315;
      V_fraud1  =     0.00033387866849;
      I_fraud  = '0' ;
      U_fraud  =                    0;
      END;
    END;
  END;

****************************************************************;
******          END OF DECISION TREE SCORING CODE         ******;
****************************************************************;

drop _LEAF_;
*------------------------------------------------------------*;
* TOOL: Score Node;
* TYPE: ASSESS;
* NODE: Score4;
*------------------------------------------------------------*;
*------------------------------------------------------------*;
* Score4: Creating Fixed Names;
*------------------------------------------------------------*;
LABEL EM_SEGMENT = 'Node';
EM_SEGMENT = _NODE_;
LABEL EM_EVENTPROBABILITY = 'Probability for level 1 of fraud';
EM_EVENTPROBABILITY = P_fraud1;
LABEL EM_PROBABILITY = 'Probability of Classification';
EM_PROBABILITY =
max(
P_fraud1
,
P_fraud0
);
LENGTH EM_CLASSIFICATION $%dmnorlen;
LABEL EM_CLASSIFICATION = "Prediction for fraud";
EM_CLASSIFICATION = I_fraud;
