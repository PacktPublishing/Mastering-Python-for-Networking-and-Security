# -*- encoding: utf-8 -*-
import msfrpc
client = msfrpc.Msfrpc({'uri':'/msfrpc', 'port':'5553', 'host':'127.0.0.1', 'ssl': True})
auth = client.login('msf','password')
if auth:
    print str(client.call('core.version'))+'\n'
    print str(client.call('core.thread_list', []))+'\n'
    print str(client.call('job.list', []))+'\n'
    print str(client.call('module.exploits', []))+'\n'
    print str(client.call('module.auxiliary', []))+'\n'
    print str(client.call('module.post', []))+'\n'
    print str(client.call('module.payloads', []))+'\n'
    print str(client.call('module.encoders', []))+'\n'
    print str(client.call('module.nops', []))+'\n'