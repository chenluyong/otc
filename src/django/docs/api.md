# JSON RESTful HTTP API



## 区块链

### 交易
#### `GET /address/:address/tx`
* 描述：以太坊交易记录
* 请求：/address/0x38405b5cbeb2a1ab038b4f802304eacb20ea6938/tx
* 返回：
```json
{
    "code" : 0,
    "version" : "1.0.0",
    "data":[
    ]
}
```

#### `GET /address/:address/utxo`
* 描述：比特币未花费交易utxo
* 请求：/address/3D6AHJ3RRyfUvpJfN7sczZLZYwCcVYd5vD/utxo
* 返回：
```json
{
    "code": 0,
    "message": "success",
    "data": [
        {
            "txid": "a0bdb867a6803f2ddef105471949eb41613c1c43f4325a4ab6d4b486955fe725",
            "vout": 0,
            "status": {
                "confirmed": false,
                "block_height": null,
                "block_hash": null,
                "block_time": null
            },
            "value": 1119619
        }
    ]
}
```

#### `GET /address/:address/token/tx`
#### `GET /address/:address/token/:token/tx`
* 描述：以太坊代币交易记录
* 请求： GET /address/0x38405b5cbeb2a1ab038b4f802304eacb20ea6938/token/usdt/tx
* 返回：
```json
{
    "code" : 0,
    "version" : "1.0.0",
    "data":[
    
    ]
}
```

#### `GET /tx/:txid`
* 描述：以太坊交易详情
* 请求：GET /tx/0xedbd09c77879172b5ac1c6e73bafe6dbd2fee1079ddb22acae002d9607f57cb9
* 返回：
```json
{
    "code":0,
    "msg":"success",
    "version":"1.0.0",
    "data":{
        "txid":"0xedbd09c77879172b5ac1c6e73bafe6dbd2fee1079ddb22acae002d9607f57cb9",
        "from":"0xc6e3cbc2afc2d1a12153e76c5ae538b1fd6ff5f9",
        "to":"0xdac17f958d2ee523a2206206994597c13d831ec7",
        "value":158290000,
        "fee":11025,
        "fee_detail":{
            "gas_limit":136800,
            "gas_price":41390000000,
            "gas_used":56221
        },
        "status":{
            "confirmed":true,
            "block_hash":"0x8c7e911d23efae541f9298ed90cdd3188259b53a20a90e8280b8bd47a4d27a66",
            "block_height":633719,
            "block_time":1591625096
        },
        "is_token":true,
        "token_detail":{
            "symbol":"usdt",
            "to":"0xcb7cb6af2ddf17cb095a7783a5c326c8df423a79",
            "value":158290000
        }
    }
}
```
### 地址

#### `GET /address/:address`
* 描述：地址信息
* 请求：GET /address/0x38405b5cbeb2a1ab038b4f802304eacb20ea6938
* 返回：
```json
{
    "code" : 0,
    "version" : "1.0.0",
    "data":{
        "address" : "0x38405b5cbeb2a1ab038b4f802304eacb20ea6938",
        "balance" : 186000,
        "spent_count" : 0
    }
}
```

#### `GET /address/:address/token/:token`
* 描述：账户地址代币余额
* 请求：GET /address/0x38405b5cbeb2a1ab038b4f802304eacb20ea6938/token/usdt
* 返回：
```json
```


#### `GET /address/:address/spent_count`
* 描述：以太坊获取当前账户地址转出笔数
* 请求：GET /address/0x38405b5cbeb2a1ab038b4f802304eacb20ea6938/spent_count
* 返回：
```json
{
    "code" : 0,
    "version" : "1.0.0",
    "data":{
        "address" : "0x38405b5cbeb2a1ab038b4f802304eacb20ea6938",
        "balance" : 186000,
        "spent_count" : 0
    }
}
```


##### `POST /broadcast/eth`
* 描述：广播交易
* 请求：GET /address/0x38405b5cbeb2a1ab038b4f802304eacb20ea6938
* 返回：
```json
{
    "code" : 0,
    "version" : "1.0.0",
    "data":{
        "txid" : "0xedbd09c77879172b5ac1c6e73bafe6dbd2fee1079ddb22acae002d9607f57cb9"
    }
}
```

## 市场
##### `GET /ticker/`
* 描述：交易结构
* 请求：GET /address/0x38405b5cbeb2a1ab038b4f802304eacb20ea6938
* 返回：
```json
{
    "code" : 0,
    "version" : "1.0.0",
    "data":{
        "txid" : "0xedbd09c77879172b5ac1c6e73bafe6dbd2fee1079ddb22acae002d9607f57cb9"
    }
}
```

## 安全

### 来源IP的国家
