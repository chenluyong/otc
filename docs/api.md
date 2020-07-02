# JSON RESTful HTTP API



## 区块链

### 交易

#### `GET /address/:address/token/tx`
#### `GET /address/:address/token/:token/tx`
#### `GET /address/:address/tx`
* 描述：交易记录、代币交易记录
* 请求：/address/0x38405b5cbeb2a1ab038b4f802304eacb20ea6938/tx
* ETH 返回：
```json
{
    "code" : 0,
    "version" : "1.0.0",
    "data":[
        {
            "txid":"0xedbd09c77879172b5ac1c6e73bafe6dbd2fee1079ddb22acae002d9607f57cb9",
            "from":"0xc6e3cbc2afc2d1a12153e76c5ae538b1fd6ff5f9",
            "to":"0xdac17f958d2ee523a2206206994597c13d831ec7",
            "value":158290000,
            "fee":11025,
            "fee_detail":{
                "gas_limit":136800,
                "gas_price":41390000000,
                "gas_used":null
            },
            "status":{
                "confirmed":false,
                "block_hash":null,
                "block_height":null,
                "block_time":null
            },
            "is_token":true,
            "token_detail":{
                "symbol":"usdt",
                "to":"0xcb7cb6af2ddf17cb095a7783a5c326c8df423a79",
                "value":158290000
            }
        },
        {
            "txid":"0xedbd09c77879172b5ac1c6e73bafe6dbd2fee1079ddb22acae002d9607f57cb9",
            "from":"0xc6e3cbc2afc2d1a12153e76c5ae538b1fd6ff5f9",
            "to":"0xdac17f958d2ee523a2206206994597c13d831ec7",
            "value":158290000,
            "fee":734580000021000,
            "fee_detail":{
                "gas_limit":21000,
                "gas_price":34980000001,
                "gas_used":21000
            },
            "status":{
                "confirmed":true,
                "block_hash":"0x8c7e911d23efae541f9298ed90cdd3188259b53a20a90e8280b8bd47a4d27a66",
                "block_height":633719,
                "block_time":1591625096
            },
            "is_token":false
        }
    ]
}
```
* BTC 返回：
```json
{
    "code" : 0,
    "version" : "1.0.0",
    "data":[
        {
            "txid":"6296106a5d1c4b38371b97369d1c39bde50512caf06cf282ea8983c49b5805d3",
            "from":"1M1Ceh4PhgD9UuxWFCj5Wvr31RkTRSERqk",
            "from_detail" : [
                {
                    "txid":"da739e1d5c213bbf0c24c38a08386e8c63e604141b92ec18f282f36a956fcbb0",
                    "vout":0,
                    "prevout":{
                        "scriptpubkey":"76a914db6c3d8f8924e791e4fa6cd408a922745c8de89e88ac",
                        "scriptpubkey_asm":"OP_DUP OP_HASH160 OP_PUSHBYTES_20 db6c3d8f8924e791e4fa6cd408a922745c8de89e OP_EQUALVERIFY OP_CHECKSIG",
                        "scriptpubkey_address":"1M1Ceh4PhgD9UuxWFCj5Wvr31RkTRSERqk",
                        "scriptpubkey_type":"p2pkh",
                        "value":1238924
                    },
                    "scriptsig":"4830450221008530814e4eb99f213d424f8f5f5b506bb570766a6ec297e98e7169dc6ae03b2c022016e92fc95936d3e57981b6a4d0eeb9d666b89219a599e9dbd2fe73e2a054afad0121029d1a3a4be771ab2528a862508cef427a2bb198d96099d8f12307646f31f0a750",
                    "scriptsig_asm":"OP_PUSHBYTES_72 30450221008530814e4eb99f213d424f8f5f5b506bb570766a6ec297e98e7169dc6ae03b2c022016e92fc95936d3e57981b6a4d0eeb9d666b89219a599e9dbd2fe73e2a054afad01 OP_PUSHBYTES_33 029d1a3a4be771ab2528a862508cef427a2bb198d96099d8f12307646f31f0a750",
                    "witness":null,
                    "is_coinbase":false,
                    "sequence":4294967295
                }
            ],
            "to":"multi-address",
            "to_detail" : [
                {
                    "scriptpubkey":"0014df6f8b4663160bdd433e6dbfbe691a1bdc4413df",
                    "scriptpubkey_asm":"OP_0 OP_PUSHBYTES_20 df6f8b4663160bdd433e6dbfbe691a1bdc4413df",
                    "scriptpubkey_address":"bc1qmahck3nrzc9a6se7dklmu6g6r0wygy7l07z9v4",
                    "scriptpubkey_type":"v0_p2wpkh",
                    "value":438755
                },
                {
                    "scriptpubkey":"76a914d336d96454748f633f5f04312dc74634a1600b2088ac",
                    "scriptpubkey_asm":"OP_DUP OP_HASH160 OP_PUSHBYTES_20 d336d96454748f633f5f04312dc74634a1600b20 OP_EQUALVERIFY OP_CHECKSIG",
                    "scriptpubkey_address":"1LFoHTwm1S3n1YqiVoYFAx2nju2RrPeRDi",
                    "scriptpubkey_type":"p2pkh",
                    "value":779831
                }
            ],
            "value":158290000,
            "fee":20338,
            "fee_detail":{
                "gas_price":91.2,
                "gas_used":223
            },
            "status":{
                "confirmed":false,
                "block_hash":null,
                "block_height":null,
                "block_time":null
            },
            "is_token":false
        },
        {
            "txid":"22fcc4feea6909f3f524d1462111e8178212a4a7695499e0e7247126a6340909",
            "from":"multi-address",
            "from_detail" : [
                {
                    "txid":"8cc37940d818264334b18cdae6ef325659a4c5d96af69a2fbd50a9aae52d2d66",
                    "vout":0,
                    "prevout":{
                        "scriptpubkey":"76a914e44380474ec3169405d7f6eade6ca6d7de2e2a4388ac",
                        "scriptpubkey_asm":"OP_DUP OP_HASH160 OP_PUSHBYTES_20 e44380474ec3169405d7f6eade6ca6d7de2e2a43 OP_EQUALVERIFY OP_CHECKSIG",
                        "scriptpubkey_address":"1Mowvo7uf7UtUBJrepqaYJ4GWsfcYgVHdk",
                        "scriptpubkey_type":"p2pkh",
                        "value":5500
                    },
                    "scriptsig":"47304402200869e97f76ad6ea62c4bad1a4ac6a4d4c44edd7cd2e9e22fac7516101987b9ef02207ee639cfff6ef088da4760de04608a4788a657925ad8ea6a4039af49de5e970901210263d953be1ff8cde5c666b4275af857af4f1bd1e54f7417afbc0f3b85594548f6",
                    "scriptsig_asm":"OP_PUSHBYTES_71 304402200869e97f76ad6ea62c4bad1a4ac6a4d4c44edd7cd2e9e22fac7516101987b9ef02207ee639cfff6ef088da4760de04608a4788a657925ad8ea6a4039af49de5e970901 OP_PUSHBYTES_33 0263d953be1ff8cde5c666b4275af857af4f1bd1e54f7417afbc0f3b85594548f6",
                    "witness":null,
                    "is_coinbase":false,
                    "sequence":4294967295
                },
                {
                    "txid":"a8ae568714a388a55f555b8e1bfefbc2829bcb513db88e0acbb7ded152999429",
                    "vout":0,
                    "prevout":{
                        "scriptpubkey":"76a914c3d8eb28d92f1ff47df596173221fdecbda0d02188ac",
                        "scriptpubkey_asm":"OP_DUP OP_HASH160 OP_PUSHBYTES_20 c3d8eb28d92f1ff47df596173221fdecbda0d021 OP_EQUALVERIFY OP_CHECKSIG",
                        "scriptpubkey_address":"1JrYdB9UYVCE1pMUTfK8sK2WfrtkWmn5V8",
                        "scriptpubkey_type":"p2pkh",
                        "value":8753750
                    },
                    "scriptsig":"4730440220633e842fa28a3c9eef71d72803fe26b0b5f2e254856a6eb584cad09e59bf71ac02205b5b11a2747337f92b55ffc4b2d5b7c5a2f407a75ebd8c5247fd1ec1a2d88e0c0121028da08dac6fa785ceb990f6e8bb3ade181212dd019ecd96038b49437acf1e85cd",
                    "scriptsig_asm":"OP_PUSHBYTES_71 30440220633e842fa28a3c9eef71d72803fe26b0b5f2e254856a6eb584cad09e59bf71ac02205b5b11a2747337f92b55ffc4b2d5b7c5a2f407a75ebd8c5247fd1ec1a2d88e0c01 OP_PUSHBYTES_33 028da08dac6fa785ceb990f6e8bb3ade181212dd019ecd96038b49437acf1e85cd",
                    "witness":null,
                    "is_coinbase":false,
                    "sequence":4294967294
                }
            ],
            "to":"multi-address",
            "to_detail" : [
                {
                    "scriptpubkey":"76a914c3d8eb28d92f1ff47df596173221fdecbda0d02188ac",
                    "scriptpubkey_asm":"OP_DUP OP_HASH160 OP_PUSHBYTES_20 c3d8eb28d92f1ff47df596173221fdecbda0d021 OP_EQUALVERIFY OP_CHECKSIG",
                    "scriptpubkey_address":"1JrYdB9UYVCE1pMUTfK8sK2WfrtkWmn5V8",
                    "scriptpubkey_type":"p2pkh",
                    "value":8703900
                },
                {
                    "scriptpubkey":"6a146f6d6e69000000000000001f000000055ae82600",
                    "scriptpubkey_asm":"OP_RETURN OP_PUSHBYTES_20 6f6d6e69000000000000001f000000055ae82600",
                    "scriptpubkey_address":null,
                    "scriptpubkey_type":"op_return",
                    "value":0
                }
            ],
            "value":158290000,
            "fee":55350,
            "fee_detail":{
                "gas_price":150,
                "gas_used":369
            },
            "status":{
                "confirmed":false,
                "block_hash":null,
                "block_height":null,
                "block_time":null
            },
            "is_token":true,
            "token_detail":{
                "symbol":"usdt",
                "to":"1JrYdB9UYVCE1pMUTfK8sK2WfrtkWmn5V8",
                "value":23000000000
            }
        }
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
* 描述：获取当前账户地址转出笔数
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
        
    }
}
```

## 安全

### 来源IP的国家
