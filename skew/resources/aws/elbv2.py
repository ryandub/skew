
from skew.resources.aws import AWSResource


class LoadBalancer(AWSResource):

    class Meta(object):
        service = 'elbv2'
        type = 'loadbalancer'
        enum_spec = ('describe_load_balancers',
                     'LoadBalancers', None)
        id = None
        filter_name = None
        filter_type = None
        detail_spec = None
        name = None
        dimension = None

    @property
    @property
    def arn(self):
        return self.data.get('LoadBalancerArn')