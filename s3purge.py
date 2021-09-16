
import argparse
import boto3
import datetime


def purge(bucket, days, prefix):
    before = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days)
    s3 = boto3.resource("s3")
    objects = s3.Bucket(bucket).objects.all()
    files = [x for x in objects if x.key.startswith(prefix) and x.last_modified < before]
    count = len(files)

    if count > 0:
        print("Deleting {:,.0f} file{:s}".format(count, "" if count == 1 else "s"))
        for file in files:
            file.delete()


def get_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    return [x['Name'] for x in response['Buckets']]


def days_type(x):
    x = int(x)
    if x < 1:
        raise argparse.ArgumentTypeError('cannot be less than 1')
    return x


def bucket_type(x):
    x = str(x)
    if x not in get_buckets():
        raise argparse.ArgumentTypeError('must be a valid bucket name')
    return x


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="s3purge", description="Purge old files from an aws.s3 bucket.")
    parser.add_argument("--days", default=14, help="Delete files older than DAYS old (Default: 14, must be > 0)",
                        type=days_type)
    parser.add_argument("--prefix", default="", help="Only include files starting with PREFIX (Default: '')")
    parser.add_argument("bucket", help="Delete files from this bucket only", type=bucket_type)

    args = parser.parse_args()

    purge(args.bucket, args.days, args.prefix)
