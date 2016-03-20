S3P: Easily Publish Static HTML to S3
=====================================

S3P is a library for publishing a local folder containing a build of a static website, to S3.


Installation
------------

The recommended installation method is pip::

    pip install s3p


Quickstart
----------

Create a bucket on S3 through the AWS console, if you don't have one already and `configure it for website hosting <https://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html>`_.

Publish your build folder to the S3 bucket:

.. code:: python

    import s3p
    publisher = s3p.Publisher('mybucket', 'path/to/folder')
    publisher.publish()


Acknowledgements
----------------

Most of S3P was built off of ``spenczar``'s lektor-s3 `library <https://github.com/spenczar/lektor-s3>`_.