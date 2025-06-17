from airflow.sdk import dag, task, Context
from typing import Any,Dict
# Example DAG demonstrating the use of XComs to pass data between tasks
# Note: This code assumes that the Airflow SDK is correctly set up and that the
# necessary imports are available in your environment.
# This code is for educational purposes and may need adjustments based on your Airflow setup.
# Import necessary modules from Airflow SDK

@dag

def xcom_dag():

    @task
    def t1() -> Dict[str, Any]:
        val = 42
        my_sentenct = "Hello, Airflow!"
        return dict(val=val, my_sentenct=my_sentenct)

    @task
    def t2(data : Dict[str, Any]):
        # Retrieve the value pushed by t1
        print(data['val'])
        print(data['my_sentence'])
   
    val = t1()
    t2(val)
    
xcom_dag()