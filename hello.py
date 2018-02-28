import os

print("Hello World!")
aws_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret = os.environ['AWS_SECRET_ACCESS_KEY']
print("AWS KEY ID: |{}{}|".format(aws_id[:len(aws_id)//2], aws_id[len(aws_id)//2:]))
print("AWS SECRET KEY: |{} {}|".format(aws_secret[:len(aws_secret)//2], aws_secret[len(aws_secret)//2:]))