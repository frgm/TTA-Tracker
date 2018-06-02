from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpcUser = 'multichainrpc'
rpcPassword = 'At5XJMFjjfCZhwfhEctA3XoY5aMKN1ZwivajyYWT163R'
rpcHost = 'localhost'
rpcPort = '9258 '
chainname = 'test'
mcapi = AuthServiceProxy('http://%s:%s@%s:%s'%(rpcUser,rpcPassword,rpcHost,rpcPort))
#r = mcapi.getinfo()
#print(r)
addr = "17CPfL8mtTeAg3hFdJKaEEvZfFi5xYiQnGqN46"
#mcapi.grant(addr,"connect,send,receive")
transaction = mcapi.issue(addr, "itemName", 100, 1)
print(transaction)