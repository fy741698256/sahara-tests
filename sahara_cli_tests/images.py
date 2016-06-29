#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from sahara_cli_tests import base


class SaharaImageCLITest(base.ClientTestBase):

    def openstack_image_list(self):
        self.assertTableStruct(self.listing_result('image list'), [
            'Name',
            'Id',
            'Username',
            'Tags'
        ])

    def openstack_image_register(self, name_to_register):
        images_list = self.openstack('image list')
        images = self.parser.listing(images_list)
        images_name = [p['Name'] for p in images]
        flag = None
        for image_name in images_name:
            if image_name == name_to_register:
                flag = ''.join([' --username fedora ', image_name])
        if flag is None:
            raise self.skipException('No available image for testing')
        self.assertTableStruct(
            self.listing_result(''.join(['image register', flag])), [
                'Field',
                'Value'
            ])
        return name_to_register

    def openstack_image_show(self, image_name):
        self.assertTableStruct(
            self.listing_result(''.join(['image show ', image_name])), [
                'Field',
                'Value'
            ])

    def openstack_image_tags_add(self, image_name):
        flag = ''.join([image_name, ' --tags test'])
        self.assertTableStruct(
            self.listing_result(''.join(['image tags add ', flag])), [
                'Field',
                'Value'
            ])

    def openstack_image_tags_remove(self, image_name):
        flag = ''.join([image_name, ' --tags test'])
        self.assertTableStruct(
            self.listing_result(''.join(['image tags remove ', flag])), [
                'Field',
                'Value'
            ])

    def openstack_image_unregister(self, image_name):
        self.assertTableStruct(
            self.listing_result(''.join(['image unregister ', image_name])), [
                'Field',
                'Value'
            ])
