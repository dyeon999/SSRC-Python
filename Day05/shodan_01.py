import shodan
import json

SHODAN_API_KEY = "" #### 이거 채워야한다!!



api = shodan.Shodan(SHODAN_API_KEY)

query = 'apache'
results = api.search(query)

try:
    for match in results['matches'][:2]:
        #print(json.dumps(result, indent=4))
        print(f"IP정보: {match['ip_str']}")
        print(f"포트정보: {match['port']}")
        print(f"Org: {match.get('org', 'N/A')}")
        print(f"Location: {match['location']['country_name']}")
        print(f"Hostnames: {', '.join(match['hostnames']) if match['hostnames'] else 'N/A'}")
except shodan.APIError as e:
    print(f"ERROR: {e}")