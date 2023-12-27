# views.py
from django.http import JsonResponse
from influxdb_client import InfluxDBClient

from django.http import JsonResponse
import json  # Import the json module

client = InfluxDBClient(
    url="https://us-east-1-1.aws.cloud2.influxdata.com",
    token="DAZJtotPKvqEW-NST4uJ7mP5Sc8Td6rCdnWLD5VgNMxA_UVCS33Hkt4RCJmr2fywmo-XbSFD7I4OA3ItBEHB3Q==",
    org="8d7538f2d9a3eff8",
    Bucket="chart"
)
    
def get_data(request):
    bucket = "chart"    
    query_api = client.query_api()

    # Corrected the query syntax
    query = 'from(bucket:"{}") |> range(start: -10m)'.format(bucket)
    result = query_api.query(query)

    # Convert the InfluxDB query result to JSON
    json_result = json.loads(result.to_json())

    # Return JsonResponse with the JSON result
    return JsonResponse(json_result, safe=False)
