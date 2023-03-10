# Get IP Reputation

Lupovis Prowl is an API you can use to obtain IP reputation as well as techniques tactics and procedures, indicators of attacks and indicators of compromise associated with an IP address.  

Lupovis deploys decoys across the internet and collects and analyse requests made by malicious nodes. 


## BASH with CURL 

```
curl 'https://api.prowl.lupovis.io/GetIPReputation?ip=<IP Address>' -H "x-api-key: <API Key>"
```

### Powershell 
```
Invoke-WebRequest -Headers $("x-api-key = <API Key>" | ConvertFrom-StringData) 'https://api.prowl.lupovis.io/GetIPReputation?ip=<IP Address>'
```

## Integration with Azure Sentinel 

In this blog post we provide an example an how to integrate Prowl with Azure Sentinel to reduce the noise and improve SOAR. 

[Here](https://www.lupovis.io/automate-ip-addresses-enrichment-in-azure-sentinel/) 
