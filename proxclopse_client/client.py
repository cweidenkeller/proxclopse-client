from proxclopse_client.common.constants import BASE_URI
from proxclopse_client.routes.get import get_call
from proxclopse_client.routes.create import create_call
from proxclopse_client.routes.delete import delete_call
from proxclopse_client.routes.modify import modify_call
from proxclopse_client.routes.failover import failover_call
from proxclopse_client.routes.set_acl import set_acl_call
from proxclopse_client.routes.list import list_call


class Client(object):

    """
    Setup a Client object pass in the host of the server you are connecting
    to and the port.
    """
    def __init__(self, host='127.0.0.1', port=80):
        self.host = host
        self.port = port
        self.url = 'http://' + host + ':' + port + BASE_URI

    """
    Create a new proxclopse instance.
    This will return an instance object.
    """
    def create(self):
        return create_call(self.url + 'create')

    """
    Delete a proxclopse instance.
    Provide an instance_id to delete it.
    """
    def delete(self, instance_id):
        return delete_call(self.url + instance_id)

    """
    Modify an existing proxclopse instance.
    Provide an instance_id to modify it.
    """
    def modify(self, instance_id):
        return modify_call(self.url + instance_id)

    """
    Get a proxclopse instance.
    Provide an instance_id to get it.
    This will return an instance object.
    """
    def get(self, instance_id):
        return get_call(self.url + instance_id)

    """
    Failover a proxclopse instance.
    Provide an instance_id to fail over.
    """
    def failover(self, instance_id):
        return failover_call(self.url + instance_id)

    """
    Set new ACLs on a proxclopse instance.
    Procide an instance id to modify the ACLs
    """
    def set_acl(self, instance_id):
        return set_acl_call(self.url + instance_id)

    """
    List all proxclopse instances.
    This will return to you a list of instance_ids
    """
    def list(self):
        return list_call(self.url + 'list')
