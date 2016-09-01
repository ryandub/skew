from skew.resources.aws import AWSResource


class LogGroup(AWSResource):

    class Meta(object):
        service = 'logs'
        type = 'log-group'
        enum_spec = ('describe_log_groups', 'logGroups', None)
        id = 'logGroupName'
        filter_name = 'logGroupName'
        filter_type = 'list'
        detail_spec = None
        name = 'logGroupName'
        date = 'creationTime'
        dimension = None

    @property
    def arn(self):
        return self.data.get('arn')
