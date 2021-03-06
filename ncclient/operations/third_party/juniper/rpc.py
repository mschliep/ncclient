from ncclient.xml_ import *

from ncclient.operations.rpc import RPC
from ncclient.operations.rpc import RPCReply
from ncclient.operations.rpc import RPCError

class GetConfiguration(RPC):
    def request(self, format='xml', filter=None):
        node = new_ele('get-configuration', {'format':format})
        if filter is not None:
            node.append(filter)
        return self._request(node)

class LoadConfiguration(RPC):
    def request(self, format='xml', rollback=None, action='merge',
            target='candidate', config=None):
        if rollback is not None:
            node = new_ele('load-configuration', {'rollback': str(rollback)})
        elif config is not None:
            if type(config) == list:
                config = '\n'.join(config)
            if action == 'set':
                format = 'text'
            node = new_ele('load-configuration', {'action':action, 'format':format})
            if format == 'xml':
                config_node = sub_ele(node, 'configuration')
                config_node.append(config)
            if format == 'text' and not action == 'set':
                config_node = sub_ele(node, 'configuration-text').text = config
            if action == 'set' and format == 'text':
                config_node = sub_ele(node, 'configuration-set').text = config
        return self._request(node)

class CompareConfiguration(RPC):
    def request(self, rollback=0):
        node = new_ele('get-configuration', {'compare':'rollback', 'rollback':str(rollback)})
        return self._request(node)

class ExecuteRpc(RPC):
    def request(self, rpc):
        if isinstance(rpc, str):
            rpc = to_ele(rpc)
        return self._request(rpc)

class Command(RPC):
    def request(self, command=None, format='xml'):
        node = new_ele('command', {'format':format})
        return self._request(node)

class Reboot(RPC):
    def request(self):
        node = new_ele('request-reboot')
        return self._request(node)

class Halt(RPC):
    def request(self):
        node = new_ele('request-halt')
        return self._request(node)

class OpenConfiguration(RPC):
    def request(self):
        node = new_ele('open-configuration')
        private = sub_ele(node, 'private')
        return self._request(node)

class CloseConfiguration(RPC):
    def request(self):
        node = new_ele('close-configuration')
        return self._request(node)

class CommitConfiguration(RPC):
    def request(self, log=None, check=False, confirmed=False, confirm_timeout=None):
        node = new_ele('commit-configuration')
        if check:
            sub_ele(node, 'check')
        elif confirmed:
            sub_ele(node, 'confirmed')
            if confirm_timeout is not None:
                sub_ele(node, 'confirm-timeout').text = str(confirm_timeout)
        if log is not None and len(log) > 0:
            sub_ele(node, 'log').text = log
        return self._request(node)
