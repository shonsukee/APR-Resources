def main() -> None:
    # True Min Run time should be the specified interval less the
    # regular sleep time
    real_min_run_time = MIN_RUN_TIME - SLEEP_TIME
    url = f"https://api.switch-bot.com/v1.0/devices/{DEVID}/status"
    headers = {'Authorization': APIKEY}
    influx_client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN,
                                   org=INFLUX_ORG)
    write_api = influx_client.write_api(write_options=SYNCHRONOUS)
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
        if rel_hum >= HIGH:
            asyncio.run(plug_on(PLUG_IP))
            logger.info(f"Change state to ON, rH: {rel_hum}")
            # sleep for specified min run time, less standard sleep time,
            # we will still perform that sleep later anyhow.
            sleep(real_min_run_time)
        elif rel_hum < LOW:
            asyncio.run(plug_off(PLUG_IP))
            logger.info(f"Change state to OFF, rH: {rel_hum}")
        else:
            pass
        sleep(SLEEP_TIME)
