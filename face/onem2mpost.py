import requests
import json
DEV_CREDENTIALS = {
    'username':"Tue_20_12_22",
    'password':"Tue_20_12_22"
    }

def create_cin(uri_cnt, value, cin_labels="", data_format="json", credentials = DEV_CREDENTIALS):
    """
        Method description:
        Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
        under the specified CSE
        Parameters:
        uri_cse : [str] URI of parent CSE
        ae_name : [str] name of the AE
        fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': f'{credentials["username"]}:{credentials["password"]}',
        'Content-type': f'application/{data_format};ty=4'
        }
    body = {
        "m2m:cin": {
            "con": "{}".format(value),
            "lbl": cin_labels,
            "cnf": "text"
        }
    }
    try:
        response = requests.post(uri_cnt, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_cnt, data=json.dumps(body), headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
_url = f"http://dev-onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-L001-03/Data"
if __name__ =="__main__":
    data= "something"
    create_cin(_url ,data)