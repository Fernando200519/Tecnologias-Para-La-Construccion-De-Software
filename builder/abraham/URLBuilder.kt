class URLBuilder : URLInterface {
    private val hostname: String? = null
    private val protocol: String = null
    private val port: String? = null
    private val path: MutableList<String> = mutableListOf<String>()
    private val queryParams: MutableMap<String, String> = mutableMapOf(String, String)

    override fun setProtocol(protocol: String) {
        this.protocol = protocol
    }

    override fun setHostname(hostname: String) {
        this.hostname = hostname
    }

    override fun setPort(port: String) {
        this.port = port
    }

    override fun addPath(path: String) {
        this.path.add(path)
    }

    override fun addQueryParam(key: String, value: String) {
        this.queryParams[key] = value
    }
    override fun build(): String {
        var url = kotlin.text.StringBuilder()

        this.protocol?.let { url.append("$protocol://") }
        this.hostname?.let { url.append(hostname) }
        this.port?.let { url.append(":$port") }

        if (this.path.isNotEmpty()) {
            this.path.forEach { path ->
                url.append("/$path")
            }
        }

        return TODO()
    }

    fun enconde(value: String): String {  

}