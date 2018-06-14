from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.views import View
import trackerMain.models as md
import sys
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

#mcapi declared in appconfig

def index(request):
    return HttpResponse("Test")

def startNode(request):
    context  = {}
    return render(request,"startNode.html",context)

def middleNode(request):
    context  = {}
    return render(request,"middleNode.html",context)
    
def endNode(request, iID='0'):
    context = {'iID':iID}
    return render(request,"endNode.html",context)
    
def test(request, iID='0', nID='0'):
    try:
        description = md.DistributionNodes.objects.get(nodeID = nID).description
    except:
        description = "None"
    context = {'iID':iID, 'nID':nID, 'description':description}
    return render(request,"testing.html",context)

class address(View):
    #new address
    def post(self, request):
        newAddr = mcapi.getnewaddress()
        r = md.DistributionNodes(address = newAddr, description = request.POST['description'])
        r.save()
        mcapi.grant(newAddr,"connect,send,receive,create,issue")
        return JsonResponse({'success': True, 'nodeID': r.pk, 'address': newAddr})
    
    #list transcations with address
    def get(self, request):
        addr = md.DistributionNodes.objects.get(nodeID = request.POST['nodeID']).address
        data = mcapi.listaddresstransactions(addr, 10, true) #count=10 verbose=true
        return JsonResponse({'success': True, 'data':data})
    
class item(View):
    #new item
    def post(self, request):
        iID = request.POST['itemID']    #itemID must be always String. Uniqueness enforced by MC
        amount = request.POST['amount']
        addr = md.DistributionNodes.objects.get(nodeID = request.POST['nodeID']).address
        transaction = mcapi.issue(addr, iID, amount, 1)
        return JsonResponse({'success': True, 'txid': transaction})
    
    #list items with id    
    def get(self, request):
        if 'itemID' in request.GET and request.GET['itemID'] != "":
            assets = mcapi.listassets(request.GET['itemID']) 
        else:
            assets = mcapi.listassets()
        #print(assets)
        return JsonResponse({'success': True, 'assets': str(assets)})
        
class transfer(View):
    #move item. Leave nodeID2 empty to move to end/burn address
    def post(self, request):
        iID = request.POST['itemID']
        amount = float(request.POST['amount'])
        try:
            addr1 = md.DistributionNodes.objects.get(nodeID = request.POST['nodeID1']).address
            if request.POST['nodeID2'] != "":
                addr2 = md.DistributionNodes.objects.get(nodeID = request.POST['nodeID2']).address
            else:
                addr2 = endAddress
        except:
             return JsonResponse({'success': False, 'Error': 'No ID found'})
        transaction = mcapi.sendassetfrom(addr1, addr2, iID, amount)
        return JsonResponse({'success': True, 'txid': transaction})
            
class data(View):
    def get(self, request):
        addresses = mcapi.getaddresses()
        permissions = mcapi.getpermissions()
        return JsonResponse({'success': True, 'addresses' : addresses, 'permissions' : permissions})