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

from skew.resources.aws import AWSResource

LOG = logging.getLogger(__name__)


class Key(AWSResource):

    class Meta(object):
        service = 'kms'
        type = 'key'
        enum_spec = ('list_keys', 'Keys', None)
        detail_spec = None
        id = 'KeyId'
        filter_name = None
        filter_type = None
        name = 'KeyId'
        dimension = None

    @property
    def arn(self):
        return self.data['KeyArn']


class Alias(AWSResource):

    class Meta(object):
        service = 'kms'
        type = 'alias'
        enum_spec = ('list_aliases', 'Aliases', None)
        detail_spec = None
        id = 'AliasName'
        filter_name = None
        filter_type = None
        name = 'AliasName'
        dimension = None

    @property
    def arn(self):
        return self.data['AliasArn']
