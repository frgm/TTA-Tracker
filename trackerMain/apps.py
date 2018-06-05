from django.apps import AppConfig
from subprocess import call


class TrackermainConfig(AppConfig):
    name = 'trackerMain'
    def ready(self):
        call('multichain-util -datadir="%APPDATA%\MultiChain-Host" create TTA-Tracker') #Error if it exists
        call('multichaind TTA-Tracker -daemon -datadir="%APPDATA%\MultiChain-Host"')
        
        rpcUser = 'multichainrpc'
        rpcPassword = 'At5XJMFjjfCZhwfhEctA3XoY5aMKN1ZwivajyYWT163R'
        rpcHost = 'localhost'
        rpcPort = '9258 '
        chainname = 'test'
        global mcapi = AuthServiceProxy('http://%s:%s@%s:%s'%(rpcUser,rpcPassword,rpcHost,rpcPort))
        endAddress = 'end' #Burn address. Change to actual address
        mcapi.grant(addr,"connect,send,receive,create,issue,mine")
        return
