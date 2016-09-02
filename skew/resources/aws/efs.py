from skew.resources.aws import AWSResource


class FileSystem(AWSResource):

    class Meta(object):
        service = 'efs'
        type = 'filesystem'
        enum_spec = ('describe_file_systems', 'FileSystems', None)
        id = 'FileSystemId'
        filter_name = None
        filter_type = None
        detail_spec = None
        name = 'FileSystemId'
        dimension = None