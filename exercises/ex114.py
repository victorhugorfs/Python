import requests

def check_site(url='https://www.pudim.com.br/', timeout=5):
    try:
        answer = requests.get(url, timeout=timeout, allow_redirects=True)
        status = answer.status_code
        final_url = answer.url

        if 200 <= status < 400:
            return True, status, final_url
        else:
            return False, status, final_url
        
    except requests.Timeout:
        return False, 'timeout', url
    except requests.ConnectionError:
        return False, 'connection_error', url
    except requests.RequestException as e:
        return False, f'request_error: {e.__class__.__name__}', url


def main():
    url = 'https://www.pudim.com.br/'
    ok, info, final_url = check_site(url, timeout=5)

    if ok:
        print(f'OK ✅ Site accessible (status {info}). URL final: {final_url}')
    else:
        print(f'FAILURE ❌ Site inaccessible ({info}).')


if __name__ == '__main__':
    main()