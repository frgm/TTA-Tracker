function newItem(){
    $.ajax({
        method: 'POST',
        url : 'api/item',
        data: {'itemID': $('#txtItemID').val(), 'amount': 100, 'nodeID': $('#txtNodeID').val()}
    }).done(function(response){
        if(response.success){
            lblOut.val("Transaction ID: " + response.txid);
            genQR($('#txtItemID').val());
        } else {
            lblOut.val('err')
        }
    });
}

function genQR(string){
    $('#divQR').empty();
    $('#divQR').qrcode(string);
}

function newAddress(){
    $.ajax({
        method: 'POST',
        url : 'api/address',
        data: {'description': 'Test Address'}
    }).done(function(response){
        if(response.success){
            lblOut.val("Node ID , address: " + response.nodeID + " , " + response.address);
        } else {
            lblOut.val('err');
        }
    });
}

function listItems(){
    $.ajax({
        method: 'GET',
        url : 'api/item',
        data: {}   
    }).done(function(response){
        if(response.success){
            lblOut.val(response.assets);
        } else {
            lblOut.val('err')
        }
    });
}

function listTransactions(){
    $.ajax({
        method: 'GET',
        url : 'api/address',
        data: {'nodeID': $('#txtNodeID').val()}   
    }).done(function(response){
        if(response.success){
            lblOut.val(response.data);
        } else {
            lblOut.val('err')
        }
    });
}


function sendItem(){
    $.ajax({
        method: 'POST',
        url : 'api/transfer',
        data: {'itemID': $('#txtItemID').val(), 'amount': 2, 'nodeID1': $('#txtNodeID').val(), 'nodeID2': $('#txtNodeID2').val()}
    }).done(function(response){
        if(response.success){
            lblOut.val("txid: " + response.txid);
        } else {
            lblOut.val('err');
        }
    });
}