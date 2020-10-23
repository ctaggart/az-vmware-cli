# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServiceSpecification(Model):
    """Service specification payload.

    :param log_specifications: Specifications of the Log for Azure Monitoring
    :type log_specifications: list[~vendored_sdks.models.LogSpecification]
    :param metric_specifications: Specifications of the Metrics for Azure
     Monitoring
    :type metric_specifications:
     list[~vendored_sdks.models.MetricSpecification]
    """

    _attribute_map = {
        'log_specifications': {'key': 'logSpecifications', 'type': '[LogSpecification]'},
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[MetricSpecification]'},
    }

    def __init__(self, **kwargs):
        super(ServiceSpecification, self).__init__(**kwargs)
        self.log_specifications = kwargs.get('log_specifications', None)
        self.metric_specifications = kwargs.get('metric_specifications', None)
