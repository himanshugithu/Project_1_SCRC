import requests

def fetch_data_from_urls(urls):
    def onem2m_get_request(resource_url):
        headers = {"X-M2M-Origin": "iiith_guest:iiith_guest", "Content-Type": "application/json"}
        latest_data = []
        data= []

        try:
            response = requests.get(resource_url, headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        except requests.exceptions.HTTPError as err:
            print(f"GET request failed with status code: {err.response.status_code}")
            print(err.response.text)
            return None
        except Exception as e:
            print("An error occurred:", e)
            return None

        if response.status_code == 200:
            #print("GET request successful!")
            response_data = response.json()
            response_data = response_data.get('m2m:cin', {}).get('con', '').split(',')  # Assuming the response is JSON dataint
            if urls[0]:
                if 'AE-SR' in resource_url:#temp,humi,co2
                    specific_data = response_data[1:4]  # Example: Get the first element from the list
                    latest_data.append(specific_data)
                    #print(specific_data)
                elif 'AE-WM/WM-WD/WM-WD-KH95-00' in resource_url:#tds
                    specific_data = response_data[4]  # Example: Get value corresponding to a key
                    latest_data.append(specific_data)
                    #print(specific_data)
                elif 'AE-SL' in resource_url:#solar
                    specific_data = response_data[1]  # Example: Get value corresponding to a key
                    latest_data.append(specific_data)
                    #print(specific_data) 
                elif 'AE-WM/WM-WF/WM-WF-KB04-70' in resource_url:#total water flow
                    specific_data = response_data[2]  # Example: Get value corresponding to a key
                    latest_data.append(specific_data)
                    #print(specific_data)  
                elif 'AE-AQ/AQ-SN00-00' in resource_url:#air quility
                    specific_data = response_data[8]  # Example: Get value corresponding to a key
                    latest_data.append(specific_data)
                    #print(specific_data)
                elif 'AE-WN/WN-L001-03' in resource_url:#signal strenth
                    specific_data = response_data[2]  # Example: Get value corresponding to a key
                    latest_data.append(specific_data)
                    #print("....",specific_data)   
            if urls[1]:
                if'AE-SL/SL-VN03-00' in resource_url:
                    specific_data = response_data[1]  # Example: Get the first element from the list
                    data.append(specific_data)
                    #print(specific_data)
                elif 'AE-SL/SL-VN02-00' in resource_url:
                    specific_data = response_data[1]  # Example: Get value corresponding to a key
                    data.append(specific_data)
                    #print(specific_data) 
                elif 'AE-SL/SL-VN02-01' in resource_url:
                    specific_data = response_data[1]  # Example: Get value corresponding to a key
                    data.append(specific_data)
                    #print(specific_data)  
                elif 'AE-SL/SL-NI03-00' in resource_url:
                    specific_data = response_data[1]  # Example: Get value corresponding to a key
                    data.append(specific_data)
                    #print(specific_data)
                elif 'AE-SL/SL-NI03-01' in resource_url:
                    specific_data = response_data[0]  # Example: Get value corresponding to a key
                    data.append(specific_data)
                    #print(specific_data)             
        else:
            print(f"Unexpected status code: {response.status_code}")

        return latest_data

    all_latest_data = []
    all_data =[]
    for url in urls[0]:
        latest_data = onem2m_get_request(url)
        if latest_data:
            all_latest_data.append(latest_data)

    for url in urls[1]:
        data = onem2m_get_request(url)
        if data:
            all_data.append(data)     

    return all_latest_data,all_data

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
    
    data1,data2 = fetch_data_from_urls([url1,url2])
    # print(data1)
    # for data in data1:
    #     print(data ,type(data))
    # print(data1)
    # print(data2)
#[[,temp,humidity],]