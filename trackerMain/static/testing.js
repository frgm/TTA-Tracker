function testNewItem(){
    $.ajax({
        method: 'POST',
        url : 'api/item',
        data: {'itemID': $('#txtItemID').val(), 'amount': 100, 'nodeID': $('#txtNodeID').val()}
    }).done(function(response){
        if(response.success){
            alert("Transaction ID: " + response.txid);
        } else {
            alert('err')
        }
    });
}

function testNewAddress(){
    $.ajax({
        method: 'POST',
        url : 'api/address',
        data: {'description': 'Test Address'}
    }).done(function(response){
        if(response.success){
            alert("Node ID , address: " + response.nodeID + " , " + response.address);
        } else {
            alert('err');
        }
    });
}

function testItems(){
    $.ajax({
        method: 'GET',
        url : 'api/item',
        data: {}   
    }).done(function(response){
        if(response.success){
            console.log(response.assets);
        } else {
            alert('err')
        }
    });
}



function testTransfer(){
    $.ajax({
        method: 'POST',
        url : 'api/transfer',
        data: {'itemID': $('#txtItemID').val(), 'amount': 2, 'nodeID1': $('#txtNodeID').val(), 'nodeID2': $('#txtNodeID2').val()}
    }).done(function(response){
        if(response.success){
            alert("txid: " + response.txid);
        } else {
            alert('err');
        }
    });
}

//1
//17CPfL8mtTeAg3hFdJKaEEvZfFi5xYiQnGqN46
//5
//1Y6ih1GiK3CFGsjwiYh6jjh6daZopWn3BJsjVc