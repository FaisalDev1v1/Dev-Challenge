import boto3

def main():
    your_aws_credentials = {
        'aws_access_key_id': 'YOUR_ACCESS_KEY',
        'aws_secret_access_key': 'YOUR_SECRET_ACCESS_KEY',
    }
    bucket_name = 'mytask2'

    try:
        s3 = boto3.client('s3', **your_aws_credentials)
        log_files = s3.list_objects_v2(Bucket=mytask2)['Contents']

        for file in log_files:
            file_key = file['Key']
            try:
                file_obj = s3.get_object(Bucket=mytask2, Key=file_key)
                line_count = sum(1 for line in file_obj['Body'].iter_lines())

                with open('Result.txt', 'a') as f:
                    f.write(f'File: {file_key}, Lines: {line_count}\n')

            except s3.exceptions.NoSuchKey:
                print(f'Error: File not found: {file_key}')
            except Exception as e:
                print(f'Error processing file {file_key}: {e}')

    except boto3.exceptions.ClientError as e:
        print(f'Error connecting to AWS: {e}') 

if __name__ == "__main__":
    main()
