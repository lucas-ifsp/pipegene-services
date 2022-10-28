from queue import Queue
import requests
import os

Tasks = Queue()

PLATFORM_URL = os.getenv('PLATFORM_URL', "localhost")

#TODO change provider id
PROVIDER_ID = "b34f6ff1-48d5-4848-99a1-027d53d34f01"

def Job():
    if not Tasks.empty():
        task = Tasks.get()
        try:
            execution_id = task.get("execution_id")
            step_id = task.get("step_id")
            filename = task.get("filename")

            url = "http://{}:8080/api/v1/providers/{}/executions/{}/steps/{}".format(PLATFORM_URL, PROVIDER_ID, execution_id, step_id)
            headers = {}
            payload = {
                "status": "SUCCESS",
                "uri": "http://localhost:5016/v1/uploads/{}".format(filename)
            }
            response = requests.request("POST", url, json=payload, headers=headers, timeout=(3.05, 10))
            print(response.status_code)
            print(response.json())
        except Exception as error:
            print(error)
            return None

