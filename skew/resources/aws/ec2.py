# Copyright (c) 2014 Scopely, Inc.
# Copyright (c) 2015 Mitch Garnaat
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import logging

from botocore.exceptions import ClientError

import skew.awsclient
from skew.resources.aws import AWSResource

LOG = logging.getLogger(__name__)


class Instance(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'instance'
        enum_spec = ('describe_instances', 'Reservations[].Instances[]', None)
        detail_spec = None
        id = 'InstanceId'
        filter_name = 'InstanceIds'
        filter_type = 'list'
        name = 'PublicDnsName'
        date = 'LaunchTime'
        dimension = 'InstanceId'

    @property
    def parent(self):
        return self.data['ImageId']


class SecurityGroup(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'security-group'
        enum_spec = ('describe_security_groups', 'SecurityGroups', None)
        detail_spec = None
        id = 'GroupId'
        filter_name = 'GroupId'
        filter_type = 'list'
        name = 'GroupId'
        date = None
        dimension = None


class KeyPair(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'key-pair'
        enum_spec = ('describe_key_pairs', 'KeyPairs', None)
        detail_spec = None
        id = 'KeyName'
        filter_name = 'KeyNames'
        name = 'KeyName'
        date = None
        dimension = None


class Address(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'address'
        enum_spec = ('describe_addresses', 'Addresses', None)
        detail_spec = None
        id = 'PublicIp'
        filter_name = 'PublicIps'
        filter_type = 'list'
        name = 'PublicIp'
        date = None
        dimension = None


class Volume(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'volume'
        enum_spec = ('describe_volumes', 'Volumes', None)
        detail_spec = None
        id = 'VolumeId'
        filter_name = 'VolumeIds'
        filter_type = 'list'
        name = 'VolumeId'
        date = 'createTime'
        dimension = 'VolumeId'

    @property
    def parent(self):
        if len(self.data['Attachments']):
            return self.data['Attachments'][0]['InstanceId']
        else:
            return None


class Snapshot(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'snapshot'
        enum_spec = (
            'describe_snapshots', 'Snapshots', {'OwnerIds': ['self']})
        detail_spec = None
        id = 'SnapshotId'
        filter_name = 'SnapshotIds'
        filter_type = 'list'
        name = 'SnapshotId'
        date = 'StartTime'
        dimension = None

    @property
    def parent(self):
        if self.data['VolumeId']:
            return self.data['VolumeId']
        else:
            return None


class Image(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'image'
        enum_spec = (
            'describe_images', 'Images', {'Owners': ['self']})
        detail_spec = None
        id = 'ImageId'
        filter_name = 'ImageIds'
        filter_type = 'list'
        name = 'ImageId'
        date = 'StartTime'
        dimension = None

    @property
    def parent(self):
        if self.data['VolumeId']:
            return self.data['VolumeId']
        else:
            return None


class Vpc(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'vpc'
        enum_spec = ('describe_vpcs', 'Vpcs', None)
        detail_spec = None
        id = 'VpcId'
        filter_name = 'VpcIds'
        filter_type = 'list'
        name = 'VpcId'
        date = None
        dimension = None


class Subnet(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'subnet'
        enum_spec = ('describe_subnets', 'Subnets', None)
        detail_spec = None
        id = 'SubnetId'
        filter_name = 'SubnetIds'
        filter_type = 'list'
        name = 'SubnetId'
        date = None
        dimension = None


class CustomerGateway(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'customer-gateway'
        enum_spec = ('describe_customer_gateways', 'CustomerGateway', None)
        detail_spec = None
        id = 'CustomerGatewayId'
        filter_name = 'CustomerGatewayIds'
        filter_type = 'list'
        name = 'CustomerGatewayId'
        date = None
        dimension = None


class InternetGateway(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'internet-gateway'
        enum_spec = ('describe_internet_gateways', 'InternetGateway', None)
        detail_spec = None
        id = 'InternetGatewayId'
        filter_name = 'InternetGatewayIds'
        filter_type = 'list'
        name = 'InternetGatewayId'
        date = None
        dimension = None


class RouteTable(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'route-table'
        enum_spec = ('describe_route_tables', 'RouteTables', None)
        detail_spec = None
        id = 'RouteTableId'
        filter_name = 'RouteTableIds'
        filter_type = 'list'
        name = 'RouteTableId'
        date = None
        dimension = None


class NetworkAcl(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'network-acl'
        enum_spec = ('describe_network_acls', 'NetworkAcls', None)
        detail_spec = None
        id = 'NetworkAclId'
        filter_name = 'NetworkAclIds'
        filter_type = 'list'
        name = 'NetworkAclId'
        date = None
        dimension = None


class VpcPeeringConnection(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'vpc-peering-connection'
        enum_spec = ('describe_vpc_peering_connections',
                     'VpcPeeringConnection', None)
        detail_spec = None
        id = 'VpcPeeringConnectionId'
        filter_name = 'VpcPeeringConnectionIds'
        filter_type = 'list'
        name = 'VpcPeeringConnectionId'
        date = None
        dimension = None


class NetworkInterface(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'network-interface'
        enum_spec = ('describe_network_interfaces', 'NetworkInterfaceIds',
                     None)
        detail_spec = None
        id = 'NetworkInterfaceId'
        filter_name = 'NetworkInterfaceIds'
        filter_type = 'list'
        name = 'NetworkInterfaceId'
        date = None
        dimension = None


class NatGateway(AWSResource):

    class Meta(object):
        service = 'ec2'
        type = 'nat-gateway'
        enum_spec = ('describe_nat_gateways', 'NatGateways',
                     None)
        detail_spec = None
        id = 'NatGatewayId'
        filter_name = 'NetworkInterfaceIds'
        filter_type = 'list'
        name = 'NetworkInterfaceId'
        date = None
        dimension = None

    @classmethod
    def enumerate(cls, arn, region, account, resource_id=None, **kwargs):
        client = skew.awsclient.get_awsclient(
            cls.Meta.service, region, account, **kwargs)
        kwargs = {}
        do_client_side_filtering = False
        if resource_id and resource_id != '*':
            # If we are looking for a specific resource and the
            # API provides a way to filter on a specific resource
            # id then let's insert the right parameter to do the filtering.
            # If the API does not support that, we will have to filter
            # after we get all of the results.
            filter_name = cls.Meta.filter_name
            if filter_name:
                if cls.Meta.filter_type == 'list':
                    kwargs[filter_name] = [resource_id]
                else:
                    kwargs[filter_name] = resource_id
            else:
                do_client_side_filtering = True
        enum_op, path, extra_args = cls.Meta.enum_spec
        if extra_args:
            kwargs.update(extra_args)
        LOG.debug('enum_op=%s' % enum_op)
        try:
            data = client.call(enum_op, query=path, **kwargs)
        except ClientError as e:
            data = {}
            # if the error is because the resource was not found, be quiet
            if 'This request has been administratively disabled.' in e.message:
                pass
            elif 'NotFound' not in e.response['Error']['Code']:
                raise
        LOG.debug(data)
        resources = []
        if data:
            for d in data:
                if do_client_side_filtering:
                    # If the API does not support filtering, the resource
                    # class should provide a filter method that will
                    # return True if the returned data matches the
                    # resource ID we are looking for.
                    if not cls.filter(arn, resource_id, d):
                        continue
                resources.append(cls(client, d, arn.query))
        return resources