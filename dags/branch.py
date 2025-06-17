from airflow.sdk import dag, task

@dag
def branch_dag():
    
    @task
    def a():
        return 1

    @task.branch
    def b(val: int):
        if val == 1:
            return "equal_1"
        return "different_from_1"
        return 'task_a'
    @task
    def equal_1(val: int):
        print(f"Value is equal to {val}")
    @task
    def different_from_1(val: int):
        print(f"Value is different from 1: {val}")

    val = a()
    b(val) >> [equal_1(val),different_from_1(val)]

branch_dag()