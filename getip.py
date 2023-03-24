import click
from requests import get


def get_help_texts():
    data = {
        "-i": "Set IP-adress for check. If param is empty - will check your current public IP-adress"
    }
    return data


def get_current_ip():
    request = 'https://api.ipify.org?format=json'
    response = get(request).json()
    return response['ip']


def get_ip_data(ip):
    request = f'http://ipwho.is/{ip}'
    response = get(request).json()
    return response


@click.command()
@click.option('-i', default=get_current_ip(), help=get_help_texts()['-i'])
def main(i):
    ip_data = get_ip_data(i)

    for key, value in ip_data.items():
        pattern = f"{key.ljust(20, '.').title().replace('_', ' ')}:"

        if key == 'ip':
            print(key.ljust(20, '.').upper().replace('_', ' ') + ':', value)
            continue

        elif key == 'flag':
            print(pattern, value['img'])
            continue

        print(pattern, value)


if __name__ == "__main__":
    main()
