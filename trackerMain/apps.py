from django.apps import AppConfig
from subprocess import call


class TrackermainConfig(AppConfig):
    name = 'trackerMain'
    def ready(self):
        rpcUser = 'multichainrpc'
        rpcPassword = 'At5XJMFjjfCZhwfhEctA3XoY5aMKN1ZwivajyYWT163R'
        rpcHost = 'localhost'
        rpcPort = '9258 '
        chainname = 'test'
        mchostdir='%APPDATA%\MultiChain-Host'
        
        call('multichain-util -datadir=%s create TTA-Tracker'%(mchostdir)) #Error if it exists
        call('multichaind TTA-Tracker -daemon -datadir=%s -rpcuser=%s -rpcpassword=%s'%(mchostdir,rpcUser,rpcPassword))
        
        global mcapi = AuthServiceProxy('http://%s:%s@%s:%s'%(rpcUser,rpcPassword,rpcHost,rpcPort))
        endAddress = 'end' #Burn address. Change to actual address
        return
