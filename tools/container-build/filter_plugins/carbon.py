#
# INTEL CONFIDENTIAL
# Copyright (c) 2018 Intel Corporation
#
# The source code contained or described herein and all documents related to
# the source code ("Material") are owned by Intel Corporation or its suppliers
# or licensors. Title to the Material remains with Intel Corporation or its
# suppliers and licensors. The Material contains trade secrets and proprietary
# and confidential information of Intel or its suppliers and licensors. The
# Material is protected by worldwide copyright and trade secret laws and treaty
# provisions. No part of the Material may be used, copied, reproduced, modified,
# published, uploaded, posted, transmitted, distributed, or disclosed in any way
# without Intel's prior express written permission.
#
# No license under any patent, copyright, trade secret or other intellectual
# property right is granted to or conferred upon you by disclosure or delivery
# of the Materials, either expressly, by implication, inducement, estoppel or
# otherwise. Any license under such intellectual property rights must be express
# and approved by Intel in writing.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


def organize_images(images):
    image_names = list(images.keys())
    image_reqs = {}
    for image in image_names:
        if 'required' not in images[image]:
            image_reqs[image] = []
        else:
            image_reqs[image] = [value for key,value in images[image]['required'].items()]
    layers = []

    while len(image_names) > 0:
        layer = []
        for image in image_names:
            if len(image_reqs[image]) == 0:
                layer.append(image)
        if len(layer) == 0:
            raise Exception("Loop error: {}".format(image_names))
        layers.append(layer)
        for image in layer:
            image_names.remove(image)
            for obs_image in image_names:
                if image in image_reqs[obs_image]:
                    image_reqs[obs_image].remove(image)
    return layers


class FilterModule(object):
    """ Carbon tests core jinja2 filters """

    def filters(self):
        return {
          'organize_images': organize_images
        }
