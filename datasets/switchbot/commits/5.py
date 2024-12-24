BASE_END_POINT = 'https://api.switch-bot.com/v1.0'
devices = requests.get(
    url=BASE_END_POINT + '/devices',
    headers={
        'Authorization': os.environ['SWITCH_BOT_OPEN_TOKEN']
    }
).json()['body']

class LivingCurtains():
    def __init__(self):
        for k, v in enumerate(devices['deviceList']):
            if v['deviceName'] == 'カーテン':
                key = k
                break
        self.__devices_ids = devices['deviceList'][key]['curtainDevicesIds']

    def open(self) -> None:
        for device_id in self.__devices_ids:
            requests.post(
                url=f'{BASE_END_POINT}/devices/{device_id}/commands',
                headers={
                    'Authorization': os.environ['SWITCH_BOT_OPEN_TOKEN'],
                    'Content-Type': 'application/json; charset=utf8',
                },
                data=json.dumps({
                    'command': 'turnOn',
                    'parameter': 'default',
                    'commandType': 'command'
                })
            )

class InfraredRemoteDevice():
    def __init__(self, deviceName:str):
        for k, v in enumerate(devices['infraredRemoteList']):
            if v['deviceName'] == deviceName:
                key = k
                break
        self.__devices_id = devices['infraredRemoteList'][key]['deviceId']

    def turn_off(self) -> None:
        requests.post(
            url=f'{BASE_END_POINT}/devices/{self.__devices_id}/commands',
            headers={
                'Authorization': os.environ['SWITCH_BOT_OPEN_TOKEN'],
                'Content-Type': 'application/json; charset=utf8',
            },
            data=json.dumps({
                'command': 'turnOff',
                'parameter': 'default',
                'commandType': ''
            })
        )
