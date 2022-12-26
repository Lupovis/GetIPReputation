# Get IP Reputation

Lupovis Prowl is an API you can use to obtain IP reputation as well as techniques tactics and proceedures, indicators of attacks and indicators of compromise associated with an IP address.  

Lupovis deploys decoys across the internet and collects and analyse requests made by malicious nodes. 


## BASH with CURL 

```
curl 'https://84h9dq7p3c.execute-api.eu-west-1.amazonaws.com/live/GetIPReputation?ip=<IP Address>' -H "x-api-key: <API Key>"
```

### Powershell 
```
curl 'https://84h9dq7p3c.execute-api.eu-west-1.amazonaws.com/live/GetIPReputation?ip=<IP Address>' -H "x-api-key: <API Key>"
```

## Integration with Azure Sentinel 

In this blog post we provide an example an how to integrate Prowl with Azure Sentinel to reduce the noise and improve SOAR. 

[Here](https://www.lupovis.io/automate-ip-addresses-enrichment-in-azure-sentinel/) 
