#!usr/bin/python3
import requests

def fetch_todo_progress(employee_id):
    #api endpoint
    url = f'https://jsonplaceholder.typicode.com/todos/{employee_id}'

    try:

        response = requests.get(url)
        todos = response.json()

        if not todos:
            print("No TODO data found for this employee.")
            return

        #extract relevant information
        employee_name = todos[0]['userId']
        total_tasks = len(todos)
        done_tasks = sum(1 for todo in todos if todo['completed'])

        #display progress
        print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}')
        for todo in todos:
            if todo['completed']:
                print(f'\t{todo["title"]}')
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')
