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

from util.k8s.kubectl import start_port_forwarding
from util.app_names import DLS4EAppNames
from util.logger import initialize_logger
from util.exceptions import K8sProxyCloseError, K8sProxyOpenError

logger = initialize_logger(__name__)


class K8sProxy():

    def __init__(self, app_name: DLS4EAppNames):
        self.app_name = app_name

    def __enter__(self):
        logger.debug("k8s_proxy - entering")
        try:
            self.process, self.tunnel_port, self.container_port = start_port_forwarding(self.app_name)
        except Exception as exe:
            error_message = "k8s_proxy - enter - error"
            logger.exception(error_message)
            raise K8sProxyOpenError(error_message) from exe

        return self

    def __exit__(self, *args):
        logger.debug("k8s_proxy - exiting")
        try:
            self.process.kill()
        except Exception as exe:
            error_message = "k8s_proxy - exit - error"
            logger.exception(error_message)
            raise K8sProxyCloseError(error_message) from exe