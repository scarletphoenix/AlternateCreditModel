# AlternateCreditModel
The alternative credit risk model focuses on the target group of customers with little or no credit history to evaluate customer credit risk assessment on the basis of other relevant feature points in modern times like utility payments data, social media profile, psychometric test,etc and create an alternate credit score.

We divide the alternate scoring model into two sub-models for scoring:
1. Repayment capacity - This includes calculating the users disposable income after utility and rent payments to check if he is in a position to repay. User-permissible data is employed to detect bad repayment behaviours, existing debts and other useful insights.

2. Lifestyle assessment matrix - This involves creation of a personality matrix of the customer based on a psychometric analysis, social media activity and existing users spending habits. This data helps map a personna of the user indicating the willingness to repay.

Setup:
1. Clone the repository
2. Create virtualenv with python3
3. Run `pip install -r requirements.txt`
4. Run `./server.py`
The local system is now hosting the server apis

There are three demos to see the alternate scores for customer

1. Fetch alternative credit score: `http://127.0.0.1:5000/credit_score/user/{id}`

This api gives the data current values for repayment capacity and lifestyle matrix as well as the total score based on all this criteria

2. Add a new user `http://127.0.0.1:5000/lifestyle/create/user`

This POST request requires some feature scores as parameters and creates a new user with a score based on the decision engine. 

Payload

`{
"psychometric_score" : "9",
"social_media_score" : [
"facebook" : "1"
]
}`

This data creates a new user with a lifestyle matrix

To create the repayment capacity for the user employ the endpoint `http://127.0.0.1:5000/repayment/create/user'

Payload 

`{
"all_sms" : [
<This contains an string array of sms>
  ],
  "monthly_income_score":"9",
  "employment_history_score":"2"
  }`
  
 These two scores created using rule engine are fed into a neural network to generate alternate credit score.
 
 3. Update an existing score
 
This post request will take as input some existing userid and new data to be modified. This demo employs the same endpoints as above for repayment and lifestyle score calculation. Updated values cause and increase/decrease in score as per the metric values given.
 For eg, to check the repayment scroring for user 1 with a different set of SMS, we do as below
 
 Body = `{
 "user_id" : "",
 "all_sms" : [
<This contains a different string array of sms>
  ]
 }`
 
  To update the repayment capacity for the user employ the endpoint `http://127.0.0.1:5000/repayment/create/user` with above body as payload
  
This updates the sms score generated for the customer and gives a new alternate credit score.
Similarly data for lifestyle matrix can be edited providing the required data payload with new changes
