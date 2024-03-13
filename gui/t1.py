import requests

def onem2m_get_request(resource_url):
    headers = {"X-M2M-Origin": "iiith_guest:iiith_guest", "Content-Type": "application/json"}
    try:
        response = requests.get(resource_url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        if response.status_code == 200:
            response_data = response.json().get('m2m:cin', {}).get('con', '').split(',')
            return response_data
        else:
            print(f"Unexpected status code: {response.status_code}")
    except requests.exceptions.HTTPError as err:
        print(f"GET request failed with status code: {err.response.status_code}")
        print(err.response.text)
    except Exception as e:
        print("An error occurred:", e)

def fetch_data_from_urls(urls):
    all_latest_data = []
    for url_list in urls:
        latest_data = [onem2m_get_request(url) for url in url_list]
        all_latest_data.append(latest_data)
    return all_latest_data

if __name__ == "__main__":
    url1 = [
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SR/SR-AQ/SR-AQ-KH95-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WM/WM-WD/WM-WD-KH95-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-VN02-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WM/WM-WF/WM-WF-KB04-70/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-AQ/AQ-SN00-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WN/WN-L001-03/Data/la",
    ]
    url2 = [
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-VN03-00/Data/la",  
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-VN02-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-VN02-01/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-NI03-00/Data/la",
        "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SL/SL-NI03-01/Data/la"
    ]
    
    data1, data2 = fetch_data_from_urls([url1, url2])
    print(data1)
    print(data2)
