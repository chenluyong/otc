## API protocol
The API is based on HTTP protocol [JSON RPC](http://json-rpc.org/), whose request method must be POST. Its URL is：/jsonrpc and the Content-Type is：application/json

**Request**
* method: method，String
* params: parameters，Array
* id: Request id, Integer
* example:

```
{
    "jsonrpc":"2.0",
    "method":"balance.update",
    "params":[1,"usdt","deposit",1,"0.0005",{}],
    "id":1
}
```

**Response**
* result: Json object，null for failure
* error: Json object，null for success，non-null for failure
1. code: error code
2. message: error message
* id: Request id, Integer
* example:

```
{
    "result": "success",
    "id": 1,
    "jsonrpc": "2.0"
}
```


General error code:
* 1: invalid argument
* 2: internal error
* 3: service unavailable
* 4: method not found
* 5: service timeout



## Asset API
**资产查询**
* method: `balance.query`
* params: unfixed parameters, first parameter is user ID, followed by list of asset names. Return to user's overall asset if the list is blank.
1. user_id: 用户编号 user ID，Integer
* 示例: `{"jsonrpc":"2.0","method":"balance.query","params":[1],"id":1570871171}`
* result: {"asset": {"available": "amount", "freeze": "amount"}}
* example:

```
"params": [1, "BTC"]
"result": {"BTC": {"available": "1.10000000","freeze": "9.90000000"}}
```



**修改资产**
* method: `balance.update`
* params:
1. user_id: user ID，Integer
2. asset: asset name，String
3. business: business type，String
4. business_id: business ID，Integer, but it will only succeed once with multiple operations of the same user_id, asset, business or business_id
5. change: balance change，String, negative numbers for deduction
6. detail: Json object，attached information
* result: "success"
* error code:
10. repeat update
11. balance not enough
* 示例: `{"jsonrpc":"2.0","method":"balance.update","params": [1, "BTC", "deposit", 1, "1.2345",{}],"id":1570871171}`
* example:

```
"params": [1, "BTC", "deposit", 100, "1.2345"]
"result": "success"
```


