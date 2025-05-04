import boto3

def handler(event, context):
    # Create an SSM (AWS Systems Manager) client
    ssm = boto3.client('ssm')

    try:
        # Attempt to retrieve the parameter from SSM Parameter Store
        response = ssm.get_parameter(Name='/html/dynamic_string', WithDecryption=False)
        value = response['Parameter']['Value']
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': f"<h1>The saved string is {value}</h1>"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': 'Error fetching string'
        }
