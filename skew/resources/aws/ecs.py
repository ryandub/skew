from skew.resources.aws import AWSResource


class Cluster(AWSResource):
    class Meta(object):
        service = 'ecs'
        type = 'cluster'
        enum_spec = ('list_clusters', 'clusterArns', None)
        id = None
        filter_name = None
        filter_type = None
        detail_spec = None
        name = None
        dimension = None

    @property
    def arn(self):
        return self.data