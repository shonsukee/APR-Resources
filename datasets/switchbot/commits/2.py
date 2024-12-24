def main() -> None:
    url = f"https://api.switch-bot.com/v1.0/devices/{DEVID}/status"
    headers = {'Authorization': APIKEY}
    influx_client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN,
                                   org=INFLUX_ORG)
    write_api = influx_client.write_api(write_options=SYNCHRONOUS)
    time_range = (NIGHT_BEGIN, NIGHT_END)
    logger.info(f"Startup: {UA_STRING}")
    while True:
        (deg_f, rel_hum) = read_sensor(url, headers)
        watts = asyncio.run(read_consumption(PLUG_IP))
        record = [
            {
                "measurement": INFLUX_MEASUREMENT,
                "fields": {
                    "degF": deg_f,
                    "rH": rel_hum,
                    "power": watts
                }
            }
        ]
        write_api.write(bucket=INFLUX_BUCKET, record=record)
        now = strftime("%H:%M", localtime())
        if check_time_range(now, time_range):
            # We are in night schedule
            if deg_f < NIGHT_LOW:
                asyncio.run(plug_on(PLUG_IP))
                logger.info(f"Night: Change state to ON, temp: {deg_f}")
            elif deg_f > NIGHT_HIGH:
                asyncio.run(plug_off(PLUG_IP))
                logger.info(f"Night: Change state to OFF, temp: {deg_f}")
            else:
                # no state change required
                pass
        else:
            # we are in day schedule
            if deg_f < DAY_LOW:
                asyncio.run(plug_on(PLUG_IP))
                logger.info(f"Day: Change state to ON, temp: {deg_f}")
            elif deg_f > DAY_HIGH:
                asyncio.run(plug_off(PLUG_IP))
                logger.info(f"Day: Change state to OFF, temp: {deg_f}")
            else:
                # no state change required
                pass
        sleep(SLEEP_TIME)
