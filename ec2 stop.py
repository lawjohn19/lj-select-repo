import boto3

ec2 = boto3.client('ec2')

response = ec2.stop_instances(
    InstanceIds=[
        'i-0d7a984985d0cf230',
    ],
)

print(response)

