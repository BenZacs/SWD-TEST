import json
import requests

host = 'http://localhost:8000/api'

header = {"Content-Type": "application/json"}


def test_create_student_score():
    data = {"first_name": "",
            "last_name": "",
            "subject_title": "",
            "score": 0
            }

    response = requests.post(url=f'{host}/student_score/', headers=header, data=json.dumps(data))
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")


def test_get_student_score(student_id):
    response = requests.get(url=f"{host}/student_score/{student_id}/", headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")


def test_personnel_details():
    response = requests.get(url=f"{host}/personnel_details/Dorm Palace School", headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4, ensure_ascii=False)}\n")


def test_school_hierarchy():
    response = requests.get(url=f"{host}/school_hierarchy/", headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4, ensure_ascii=False)}\n")


def test_school_structure():
    response = requests.get(url=f"{host}/school_structure/", headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4, ensure_ascii=False)}\n")


if __name__ == '__main__':
    pass

    test_create_student_score()
    test_get_student_score(1)
    test_personnel_details()
    test_school_hierarchy()
    test_school_structure()


