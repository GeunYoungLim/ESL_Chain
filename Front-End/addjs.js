var web3 = new Web3(new Web3.providers.HttpProvider("http://*"));
//49.236.137.164:8545
var manager = web3.eth.contract(JSON.parse(ESLProductManagerAbi)).at("0x90dd5500ed3882a936d11da3094d6f67812b1d48");

var accounts = web3.eth.accounts[0];
var result = web3.personal.unlockAccount(web3.eth.accounts[0], "1234", 0);

var updateEvent = manager.updateProductEvent({}, {fromBlock:0, toBlock: 'lastest'})
updateEvent.watch(function(error, result){
    if (error) {
        //에러 처리.
        return;
    }
    product = result.args;
    //상품 아이디
    itemId = product["id"]["c"][0];
    //상품 이름.
    itemName = product["itemName"];
    //상품 가격.
    itemPrice = product["itemPrice"];
    //상품 URL.
    itemURL = product["itemURL"];
    alert(product + '가 추가되었습니다.');


});

var newProductEvent = manager.newProductEvent({}, {fromBlock:0, toBlock: 'lastest'})
newProductEvent.watch(function(error, result){
    if (error) {
        //에러처리
    }
    product = result.args;
    //상품 아이디
    itemId = product["id"]["c"][0];
    //상품 이름.
    itemName = product["itemName"];
    //상품 가격.
    itemPrice = product["itemPrice"];
    //상품 URL.
    itemURL = product["itemURL"];


    alert(product + '업데이트 되었습니다.');
});

var count = manager.getProductCount.call()["c"][0];

for (i = 0; i< count; i++){

    product = manager.getProductById(i);
    //상품 아이디
    itemId = product["id"]["c"][0];
    //상품 이름.
    itemName = product["itemName"];
    //상품 가격.
    itemPrice = product["itemPrice"];
    //상품 URL.
    itemURL = product["itemURL"];

    //추가 하기.
}
