class SwitchBotApiClientImpl @Inject() (
  okHttpClient: OkHttpClient,
  switchBotConfiguration: SwitchBotConfiguration,
  cacheClient: CacheClient[SwitchBotDevicesDataModel],
  clock: Clock
)(implicit
  executionContext: ExecutionContext
) extends SwitchBotApiClient {
  import SwitchBotApiClientImpl.*

  private val logger = LoggerFactory.getLogger(this.getClass)

  private def requestWithAuthorization(path: String): Request =
    new Request.Builder()
      .url(switchBotConfiguration.switchBotEndpoint.resolve(path).toURL)
      .addHeader(
        "Authorization",
        switchBotConfiguration.oauthToken
      )
      .build()

  private val getAllDevicesRequest: Request =
    requestWithAuthorization("/v1.0/devices")

  private def getMeterInfoRequest(deviceId: String): Request =
    requestWithAuthorization(s"/v1.0/devices/$deviceId/status")

  def getMeterInfo: Future[Seq[SwitchBotMeterInfo]] =
    for {
      allDevices <- getAllDevices
      meterIds = allDevices.collect { case (SwitchBotDeviceType.MeterPlus, deviceId) =>
        deviceId
      }
      meterJsonStrings <- Future.sequence(
        meterIds.toSeq.map(id =>
          Future(
            blocking(
              okHttpClient
                .newCall(getMeterInfoRequest(id))
                .execute()
                .body()
                .string()
            )
          )
        )
      )
      result <- Future.sequence(
        meterJsonStrings.map(meterJsonString =>
          Json
            .fromJson[SwitchBotMeterInfo](
              Json.parse(meterJsonString)
            )
            .fold(
              error =>
                Future.failed(
                  new IllegalArgumentException(
                    s"""JSON parse error!
                       |  error: ${error.mkString(",")}
                       |  response: $meterJsonString
                       |""".stripMargin
                  )
                ),
              Future.successful
            )
        )
      )
    } yield result
}