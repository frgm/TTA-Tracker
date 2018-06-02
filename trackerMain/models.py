from django.db import models

#one wallet, multiple addresses
#node is a physical point in the chain of production
#different from node in the blockchain(only one blockchain node)
class DistributionNodes(models.Model):
    nodeID = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.address
