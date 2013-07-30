#!/usr/bin/env python

from ncclient import manager
from ncclient.xml_ import *

import time

def connect(host, port, user, password):
    conn = manager.connect(host=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
            hostkey_verify=False)

    print 'opening private configuration'
    lock = conn.open_configuration()

    # build configuration element
    config = new_ele('system')
    sub_ele(config, 'host-name').text = 'bar'

    send_config = conn.load_configuration(config=config)
    print send_config.tostring

    check_config = conn.validate()
    print check_config.tostring

    compare_config = conn.compare_configuration()
    print compare_config.tostring

    print 'commit confirmed 300'
    commit_config = conn.commit(confirmed=True, timeout='300')
    print commit_config.tostring

    print 'sleeping for 5 sec...'
    time.sleep(5)

    print 'closing configuration'
    close_config = conn.close_configuration()
    print close_config.tostring

if __name__ == '__main__':
    connect('router', 22, 'netconf', 'Juniper!')
