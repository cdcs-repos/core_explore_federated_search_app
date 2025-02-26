""" Federated user views
"""
from core_main_app.utils.rendering import render
from django.core.urlresolvers import reverse
from core_explore_common_app.utils.protocols.oauth2 import send_get_request
from urlparse import urljoin
import core_federated_search_app.components.instance.api as instance_api
import json


def data_detail(request):
    """ Display data's detail for a remote data.

    Args:
        request:

    Returns:

    """
    # get parameters
    data_id = request.GET['id']
    instance_name = request.GET['instance_name']

    try:
        # get instance information
        instance = instance_api.get_by_name(instance_name)
    except:
        # TODO: catch good exception, redirect to error page
        pass

    # FIXME: reverse args
    # Get detail view base url (to be completed with data id)
    url = urljoin(instance.endpoint, reverse("core_main_app_rest_data_get_by_id_with_template_info"))
    url = "{0}?id={1}".format(url, str(data_id))

    # execute request
    response = send_get_request(url, instance.access_token)

    record = json.loads(response.text)

    # data to context
    data = {'title': record['title'],
            'xml_content': record['xml_content'],
            'template': {'hash': record['template']['hash'], 'display_name': record['template']['_display_name']}}

    context = {
        'data': data
    }

    assets = {
        "js": [
            {
                "path": 'core_main_app/common/js/XMLTree.js',
                "is_raw": False
            },
            {
                "path": 'core_main_app/user/js/data/detail.js',
                "is_raw": False
            },
        ],
        "css": ["core_main_app/common/css/XMLTree.css"],
    }

    return render(request, 'core_explore_federated_search_app/user/data_detail.html', context=context, assets=assets)
