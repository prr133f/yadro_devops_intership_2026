import requests


def make_request():
    resp = requests.get("http://178.154.213.101/random/100,200,300,400,500")
    if resp.status_code in (100, 200, 300):
        print(f"Status code: {resp.status_code}\t Body: {resp.text}")
    else:
        raise Exception(f"Special status code: {resp.status_code}")


if __name__ == "__main__":
    for _ in range(5):
        try:
            make_request()
        except Exception as e:
            print(e)
