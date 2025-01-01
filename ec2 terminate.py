import boto3

ec2 = boto3.client('ec2')

response = ec2.terminate_instances(
    InstanceIds=[
        'i-0d7a984985d0cf230', 'i-0f78b21c734f00724',
    ],
)

print(response)