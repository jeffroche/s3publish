import boto3
import botocore
import logging
import mimetypes
import os


logger = logging.getLogger(__file__)


class Publisher(object):

    def __init__(self, bucket, src_folder, credentials=None):
        self.src_folder = src_folder
        self.bucket_name = bucket
        self.credentials = credentials

    def connect(self):
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(self.bucket_name)
        try:
            self.s3.meta.client.head_bucket(Bucket=self.bucket_name)
        except botocore.exceptions.ClientError as e:
            error_code = int(e.response['Error']['Code'])
            if error_code == '404':
                raise PublishException(("Bucket does not exist. "
                                        "You must create it first"))

    def publish(self, dry_run=False, make_public=True):
        self.connect()
        files = self.list_local(self.src_folder)
        for f in files:
            self.write_file(f, make_public, dry_run=dry_run)

    def write_file(self, filename, make_public, dry_run=False):
        full_path = os.path.join(self.src_folder, filename)
        key = filename
        print "Writing {}".format(full_path)
        mime, _ = mimetypes.guess_type(filename)
        if mime is None:
            mime = 'text/plain'
        kwargs = {'ContentType': mime}
        if make_public:
            kwargs['ACL'] = 'public-read'
        if not dry_run:
            self.bucket.upload_file(full_path, key, ExtraArgs=kwargs)

    def list_local(self, root_folder):
        """Generate a list of the local files to upload

        The returned list is of the file's relative path to the root
        folder
        """
        all_files = []
        for path, _, files in os.walk(root_folder):
            for f in files:
                full_path = os.path.join(path, f)
                rel_path = os.path.relpath(full_path, root_folder)
                print "File", f
                print "Full path", full_path
                print "Rel path ", rel_path
                all_files.append(rel_path)
                log_msg = "File: {}".format(rel_path)
                print log_msg
                logger.debug(log_msg)
        return all_files

    def list_remote(self):
        return self.bucket.objects.all()


class PublishException(Exception):
    pass
