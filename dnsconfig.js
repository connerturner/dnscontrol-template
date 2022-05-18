// Declare a new Cloudflare DNS Provider and pass it the key from cred.json
var cloudflare_provider = NewDnsProvider("test-domain-on-cloudflare", "CLOUDFLAREAPI");

// Declare empty registrar to disallow registrar operations
var REG_NONE = NewRegistrar("none", "NONE");

D("example.com", REG_NONE, DnsProvider(cloudflare_provider),
    // Root A record example
	A('@', '203.0.113.254', CF_PROXY_ON),
    // A record without cloudflare proxy routing (grey cloud)
	A('noproxy', '203.0.113.253', CF_PROXY_OFF),
    // MX Record example
	MX('@', 20, 'mx2.example.com.'),
	MX('@', 10, 'mx.example.com.'),
    // SPF Record: Only designate example.com and softfail anything else
    SPF_BUILDER({
        label:"@",
        parts: [
            "v=spf1",
            "include:example.com",
            "~all"
        ]
    })
)
