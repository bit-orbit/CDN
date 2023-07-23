#!/usr/bin/env python3
import sqlite3
import requests
import json

db = sqlite3.connect('x-ui.db')

print('*'*999)



dd = """{
  "api": {
    "services": [
      "HandlerService",
      "LoggerService",
      "StatsService"
    ],
    "tag": "api"
  },
  "dns": null,
  "fakeDns": null,
  "inbounds": [
    {
      "listen": "127.0.0.1",
      "port": 62789,
      "protocol": "dokodemo-door",
      "settings": {
        "address": "127.0.0.1"
      },
      "sniffing": null,
      "streamSettings": null,
      "tag": "api"
    },
    {
      "listen": null,
      "port": 443,
      "protocol": "vless",
      "settings": {
        "clients": [
          {
            "email": "t2jor9lj",
            "flow": "",
            "id": "64e5d0c3-88b5-4aee-8119-e76d2e62649d"
          },
          {
            "email": "modanloo.test",
            "flow": "",
            "id": "ad551441-1c0e-4736-9ebc-9f06c250dcc7"
          },
          {
            "email": "modan.loo.01",
            "flow": "",
            "id": "a3de985e-2451-4e38-c66f-fa8a9834577d"
          },
          {
            "email": "mohamad.karimzade.01",
            "flow": "",
            "id": "4f3db1a2-dab2-4a2e-d1ba-f664361c8aef"
          },
          {
            "email": "modan.loo.05",
            "flow": "",
            "id": "e6f3d650-0459-4811-de69-a0616f90a4cd"
          },
          {
            "email": "modan.loo.06",
            "flow": "",
            "id": "4b4bc365-bf51-4b10-b2ee-2953e445ba1e"
          },
          {
            "email": "modan.loo.07",
            "flow": "",
            "id": "3b9641d9-f4b4-4de7-8457-6da60eac21af"
          },
          {
            "email": "modan.loo.08",
            "flow": "",
            "id": "4c8a3a45-e75d-4aef-ed3d-63d95287a49e"
          },
          {
            "email": "modan.loo.09",
            "flow": "",
            "id": "9c59db6d-d71a-488c-96b7-075112fc92d9"
          },
          {
            "email": "modan.loo.10",
            "flow": "",
            "id": "d662a8b9-a82d-4b11-e891-b0a1f81abd56"
          },
          {
            "email": "modan.loo.11",
            "flow": "",
            "id": "54c09e4c-97c6-4990-9dfc-357238e1fe19"
          },
          {
            "email": "modan.loo.12",
            "flow": "",
            "id": "01348c14-48e3-4619-e270-867a6b736c3a"
          },
          {
            "email": "mb.tina.06",
            "flow": "",
            "id": "4eeedc64-e2a1-44de-9fde-e4164cb0ad6c"
          },
          {
            "email": "f4t67tjw",
            "flow": "",
            "id": "f1db0bb9-d53e-4432-e4aa-981b9a841094"
          },
          {
            "email": "k8e83yk0",
            "flow": "",
            "id": "f990d113-6340-49b1-cdfd-d99ba6bdba0a"
          },
          {
            "email": "zxcuyq8b",
            "flow": "",
            "id": "d6714af3-4f9c-485d-e6e6-13985612492c"
          },
          {
            "email": "sajad.sadra.01",
            "flow": "",
            "id": "b8c44c62-a1f1-448b-bb50-2425d308ff83"
          },
          {
            "email": "theEx",
            "flow": "",
            "id": "2d31b294-5a47-40e7-e62c-13a88ac2be63"
          },
          {
            "email": "arman.bro",
            "flow": "",
            "id": "36000c02-b4b9-4a46-8d89-01529db79c2b"
          },
          {
            "email": "techno_arena_02",
            "flow": "",
            "id": "707296b4-e1b5-4a79-f34a-e3d01ff7fc95"
          },
          {
            "email": "by36xs9k",
            "flow": "",
            "id": "64d34975-df98-4c1e-cc2f-9cad8edc3ea0"
          },
          {
            "email": "fwdmpiar",
            "flow": "",
            "id": "d0603166-5522-4f42-dc6f-c0a1a1096402"
          },
          {
            "email": "bflgc8my",
            "flow": "",
            "id": "4ab2a316-c2a8-4e40-bece-16eff5756255"
          },
          {
            "email": "mbm64gbv",
            "flow": "",
            "id": "ee0b25e2-f935-4db6-b907-522d5936f623"
          },
          {
            "email": "8vif6yfb",
            "flow": "",
            "id": "f7301362-9393-4a20-8dfc-976b3c73dde7"
          },
          {
            "email": "tywwqk37",
            "flow": "",
            "id": "f6eb749b-1ea5-4ab3-e605-92fad3702e54"
          },
          {
            "email": "ivd3br3a",
            "flow": "",
            "id": "f9b032c9-52b9-4a9d-a2b0-08b9656b3b64"
          },
          {
            "email": "3176s3nl",
            "flow": "",
            "id": "aee45a55-01a7-4dd8-fbd9-553c9e1f1752"
          },
          {
            "email": "sd6xu0rs",
            "flow": "",
            "id": "861a90bd-3210-4d3e-aa27-af252c2e688f"
          },
          {
            "email": "ighfof3j",
            "flow": "",
            "id": "7ea9f032-0d8f-404c-fd57-3b0ca475b6b3"
          },
          {
            "email": "5oucrij4",
            "flow": "",
            "id": "66a6ab68-4c5a-4038-e9dc-a5bc1b0dccaa"
          },
          {
            "email": "4t0xf694",
            "flow": "",
            "id": "b433270f-2929-4627-b500-1b7b2caf76ea"
          },
          {
            "email": "f0hqru9x",
            "flow": "",
            "id": "97d32930-e58d-4a57-eda6-26243d192bf4"
          },
          {
            "email": "1o4yfog0",
            "flow": "",
            "id": "2bd8c8e6-2fab-42c3-9e25-b9c386e9e736"
          },
          {
            "email": "jobl2l3j",
            "flow": "",
            "id": "c4759257-25e4-4167-87d0-7be6106e039c"
          },
          {
            "email": "7kebnyd5",
            "flow": "",
            "id": "33d1e130-bc66-405f-89f9-97c9d2292b06"
          },
          {
            "email": "nte4878u",
            "flow": "",
            "id": "8649051f-27dc-42e7-dea9-e512372d455c"
          },
          {
            "email": "6bxx2act",
            "flow": "",
            "id": "410b4cd2-e1d8-4b19-e0e0-c25c5d6d76e6"
          },
          {
            "email": "f8tfakar",
            "flow": "",
            "id": "f2e772b6-a06a-461d-fc0f-4c4b379bf360"
          },
          {
            "email": "wewisajb",
            "flow": "",
            "id": "54b6e1f7-0e90-4c52-e67b-3e0e54315e89"
          },
          {
            "email": "95ol7pud",
            "flow": "",
            "id": "03bef9bc-46de-489e-ecdb-495bbbcccded"
          },
          {
            "email": "0i29qra7",
            "flow": "",
            "id": "2b3dd21b-ad45-495e-da22-2275ef8cdce8"
          },
          {
            "email": "shavidi.03",
            "flow": "",
            "id": "842dc5d5-2c3b-4582-d985-aefb80ee1054"
          },
          {
            "email": "first",
            "flow": "",
            "id": "f2f27398-bbed-4585-940b-8a1488911022"
          },
          {
            "email": "ketab.khane",
            "flow": "",
            "id": "cb7d3225-095a-4093-db52-4910527c4fa2"
          },
          {
            "email": "ghamar",
            "flow": "",
            "id": "c2db83c7-8040-4dc3-86c0-f6aa4e9ff41a"
          },
          {
            "email": "mavil.02",
            "flow": "",
            "id": "c1968fbf-35f0-4d49-8cea-0f234ffd7e07"
          },
          {
            "email": "mr.abd",
            "flow": "",
            "id": "43972f89-9291-4499-c35a-8aba0789d7f9"
          },
          {
            "email": "apg",
            "flow": "",
            "id": "68ced016-090f-4006-a1ea-8f85f1a83019"
          },
          {
            "email": "shayan.kooni",
            "flow": "",
            "id": "f09753e1-674c-4b61-e7fc-d6174013465b"
          },
          {
            "email": "yxaitdgem",
            "flow": "",
            "id": "de560119-a68f-44e9-a52f-b04ce68487b8"
          },
          {
            "email": "nv3h4ndxm",
            "flow": "",
            "id": "ffc1d6b1-6d35-45c1-bbe9-7aed24035880"
          },
          {
            "email": "a0o9ox60m",
            "flow": "",
            "id": "da0501fe-96e4-43a2-fb82-24af625d8d20"
          },
          {
            "email": "gsnvv53km",
            "flow": "",
            "id": "7f40876d-5a55-4471-a749-30e11e7db484"
          },
          {
            "email": "qfxi2dt3m",
            "flow": "",
            "id": "9e18b21c-4cf5-4888-d143-5fce0b8e2dfc"
          },
          {
            "email": "blueRose",
            "flow": "",
            "id": "97aa1758-85b3-418c-b5a6-525993169a2b"
          },
          {
            "email": "mobile.rayka.01",
            "flow": "",
            "id": "93f954b7-9a4d-4a67-c69b-19bdb9212508"
          },
          {
            "email": "mobile.rayka.02",
            "flow": "",
            "id": "33a0df6e-d4ef-4b00-bb0f-cd723fad5f72"
          },
          {
            "email": "mobile.rayka.03",
            "flow": "",
            "id": "7a8150a2-c828-42f3-c3cf-782f505221a4"
          },
          {
            "email": "mobile.rayka.04",
            "flow": "",
            "id": "d095d56f-fac7-44d8-c3d1-d019794ba99a"
          },
          {
            "email": "mehran.alm",
            "flow": "",
            "id": "7b2c6cd6-179c-48b4-a392-dd575a6155db"
          },
          {
            "email": "mohamad.kalantari",
            "flow": "",
            "id": "5ed374be-e806-4b77-c647-71ddb369456d"
          },
          {
            "email": "mobile.rayka.05",
            "flow": "",
            "id": "074ac066-af1c-414c-8eb4-385a93e4d75d"
          },
          {
            "email": "mobile.rayka.06",
            "flow": "",
            "id": "c8dbd2de-62ff-40ab-e4c6-af4b5840ceaf"
          },
          {
            "email": "mobile.rayka.07",
            "flow": "",
            "id": "3af0788f-36b7-4058-d2b4-0505734e84b3"
          },
          {
            "email": "mobile.rayka.08",
            "flow": "",
            "id": "d1e80475-c072-4ae9-fcaf-ca4e1ce9ebef"
          },
          {
            "email": "shavidi.04",
            "flow": "",
            "id": "d2044123-8cf9-4750-ecd3-0d563fed29eb"
          },
          {
            "email": "7v4bojxf",
            "flow": "",
            "id": "cc5c36eb-149d-40a0-f94a-ac16d76f065c"
          },
          {
            "email": "h6h060yr",
            "flow": "",
            "id": "4dea6a1c-685c-4133-b9ae-19df6e75f16f"
          },
          {
            "email": "mi4y1dl0",
            "flow": "",
            "id": "4a4962a3-c8b8-4cdb-b9a5-af74ab864211"
          },
          {
            "email": "marzi.farid",
            "flow": "",
            "id": "6a8c38fd-9aaa-45fe-f30d-cfbafd76dda1"
          },
          {
            "email": "modan.loo.13",
            "flow": "",
            "id": "489b132e-c1bc-4d94-ed02-fa7cf1a6c59d"
          },
          {
            "email": "meyti.self",
            "flow": "",
            "id": "580d2a4e-a5f0-4032-8029-644687685f51"
          },
          {
            "email": "apg.milad",
            "flow": "",
            "id": "a33be500-794b-4f5e-aded-e101d95bd484"
          }
        ],
        "decryption": "none",
        "fallbacks": []
      },
      "sniffing": {
        "destOverride": [
          "http",
          "tls",
          "quic"
        ],
        "enabled": true
      },
      "streamSettings": {
        "network": "ws",
        "security": "tls",
        "tlsSettings": {
          "alpn": [
            "h2",
            "http/1.1"
          ],
          "certificates": [
            {
              "certificateFile": "/root/cert.crt",
              "keyFile": "/root/private.key"
            }
          ],
          "cipherSuites": "",
          "maxVersion": "1.3",
          "minVersion": "1.0",
          "serverName": "",
          "settings": {
            "allowInsecure": false,
            "domains": [
              {
                "domain": "ukmyself5.wiregeek.ir",
                "remark": "direct"
              },
              {
                "domain": "irmyself3.wiregeek.ir",
                "remark": "bridge"
              },
              {
                "domain": "touk5.octocat.ir",
                "remark": "cdn"
              },
              {
                "domain": "irmyselftest.wiregeek.ir",
                "remark": "brg2"
              },
              {
                "domain": "liara.run",
                "remark": "liara"
              }
            ],
            "fingerprint": "",
            "serverName": "ukmyself5.wiregeek.ir"
          }
        },
        "wsSettings": {
          "acceptProxyProtocol": false,
          "headers": {},
          "path": "/"
        }
      },
      "tag": "inbound-443"
    }
  ],
  "log": {
    "access": "./access.log",
    "error": "./error.log",
    "loglevel": "warning"
  },
  "outbounds": [
    {
      "protocol": "freedom",
      "settings": {}
    },
    {
      "protocol": "blackhole",
      "settings": {},
      "tag": "blocked"
    }
  ],
  "policy": {
    "levels": {
      "0": {
        "statsUserDownlink": true,
        "statsUserUplink": true
      }
    },
    "system": {
      "statsInboundDownlink": true,
      "statsInboundUplink": true
    }
  },
  "reverse": null,
  "routing": {
    "domainStrategy": "IPIfNonMatch",
    "rules": [
      {
        "inboundTag": [
          "api"
        ],
        "outboundTag": "api",
        "type": "field"
      },
      {
        "ip": [
          "geoip:private"
        ],
        "outboundTag": "blocked",
        "type": "field"
      },
      {
        "outboundTag": "blocked",
        "protocol": [
          "bittorrent"
        ],
        "type": "field"
      }
    ]
  },
  "stats": {},
  "transport": null
}"""


d = json.loads(dd)
d = d['inbounds'][1]['settings']['clients']

for i in d:
    for j in list(db.execute('select * from client_traffics')):
        if i['email'] == j[3]:
            # print(i['email'], j[3], i['id'])
            i['total'] = j[4]+j[5]
            i['expire'] = j[6]


# print(d)



# for i in enumerate(list(db.execute('select * from client_traffics'))):
#     print("email: ", i[1][3])
#     _email = i[1][3]
#     _total = i[1][4]+i[1][5]
#     _expire = i[1][6]
#     print('***')
#     print(d)
#     print("total: ", i[1][4]+i[1][5])
#     print("expire: ", i[1][6])


for i in d:
    
    _email = i['email']
    _total = i['total']
    _expire = i['expire']
    _id = i['id']
    
    
    print(_email, _total, _expire, _id)
    
    cookies = {
        'lang': 'en-US',
        'session': 'MTY4ODM1MTUzN3xEdi1CQkFFQ180SUFBUkFCRUFBQWRmLUNBQUVHYzNSeWFXNW5EQXdBQ2t4UFIwbE9YMVZUUlZJWWVDMTFhUzlrWVhSaFltRnpaUzl0YjJSbGJDNVZjMlZ5XzRNREFRRUVWWE5sY2dIX2hBQUJCQUVDU1dRQkJBQUJDRlZ6WlhKdVlXMWxBUXdBQVFoUVlYTnpkMjl5WkFFTUFBRUxURzluYVc1VFpXTnlaWFFCREFBQUFCbl9oQllCQWdFSGJHOWhaR2x1WndFSU1USXpPMmhoYUdzQXxmrphSHHmnjBbZUANKE-W6IZPw5N7aoWi47updHHyXwA==',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'lang=en-US; session=MTY4ODM1MTUzN3xEdi1CQkFFQ180SUFBUkFCRUFBQWRmLUNBQUVHYzNSeWFXNW5EQXdBQ2t4UFIwbE9YMVZUUlZJWWVDMTFhUzlrWVhSaFltRnpaUzl0YjJSbGJDNVZjMlZ5XzRNREFRRUVWWE5sY2dIX2hBQUJCQUVDU1dRQkJBQUJDRlZ6WlhKdVlXMWxBUXdBQVFoUVlYTnpkMjl5WkFFTUFBRUxURzluYVc1VFpXTnlaWFFCREFBQUFCbl9oQllCQWdFSGJHOWhaR2x1WndFSU1USXpPMmhoYUdzQXxmrphSHHmnjBbZUANKE-W6IZPw5N7aoWi47updHHyXwA==',
        'Origin': 'https://mosco01.wiregeek.ir:2665',
        'Referer': 'https://mosco01.wiregeek.ir:2665/panel/inbounds',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    response = requests.post('https://mosco01.wiregeek.ir:2665/panel/inbound/list', cookies=cookies, headers=headers)

    d = {
    'clients': [{
    'id': '66781f37-8c79-4803-aa82-aa9ef9487524',
    'flow': '',
    'email': f'{_email}',
    'limitIp': 0,
    'totalGB': _total,
    'expiryTime': _expire,
    'enable': True,
    'tgId': '',
    'subId': 'sfvw9ooex0bvogc8'}]
}

    cookies = {
        'lang': 'en-US',
        'session': 'MTY4ODM1MTUzN3xEdi1CQkFFQ180SUFBUkFCRUFBQWRmLUNBQUVHYzNSeWFXNW5EQXdBQ2t4UFIwbE9YMVZUUlZJWWVDMTFhUzlrWVhSaFltRnpaUzl0YjJSbGJDNVZjMlZ5XzRNREFRRUVWWE5sY2dIX2hBQUJCQUVDU1dRQkJBQUJDRlZ6WlhKdVlXMWxBUXdBQVFoUVlYTnpkMjl5WkFFTUFBRUxURzluYVc1VFpXTnlaWFFCREFBQUFCbl9oQllCQWdFSGJHOWhaR2x1WndFSU1USXpPMmhoYUdzQXxmrphSHHmnjBbZUANKE-W6IZPw5N7aoWi47updHHyXwA==',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'lang=en-US; session=MTY4ODM1MTUzN3xEdi1CQkFFQ180SUFBUkFCRUFBQWRmLUNBQUVHYzNSeWFXNW5EQXdBQ2t4UFIwbE9YMVZUUlZJWWVDMTFhUzlrWVhSaFltRnpaUzl0YjJSbGJDNVZjMlZ5XzRNREFRRUVWWE5sY2dIX2hBQUJCQUVDU1dRQkJBQUJDRlZ6WlhKdVlXMWxBUXdBQVFoUVlYTnpkMjl5WkFFTUFBRUxURzluYVc1VFpXTnlaWFFCREFBQUFCbl9oQllCQWdFSGJHOWhaR2x1WndFSU1USXpPMmhoYUdzQXxmrphSHHmnjBbZUANKE-W6IZPw5N7aoWi47updHHyXwA==',
        'Origin': 'https://mosco01.wiregeek.ir:2665',
        'Referer': 'https://mosco01.wiregeek.ir:2665/panel/inbounds',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    data = {
        'id': '1',
        'settings': json.dumps(d),
    }

    response = requests.post('https://mosco01.wiregeek.ir:2665/panel/inbound/addClient', cookies=cookies, headers=headers, data=data)


    cookies = {
        'lang': 'en-US',
        'session': 'MTY4ODM1MTUzN3xEdi1CQkFFQ180SUFBUkFCRUFBQWRmLUNBQUVHYzNSeWFXNW5EQXdBQ2t4UFIwbE9YMVZUUlZJWWVDMTFhUzlrWVhSaFltRnpaUzl0YjJSbGJDNVZjMlZ5XzRNREFRRUVWWE5sY2dIX2hBQUJCQUVDU1dRQkJBQUJDRlZ6WlhKdVlXMWxBUXdBQVFoUVlYTnpkMjl5WkFFTUFBRUxURzluYVc1VFpXTnlaWFFCREFBQUFCbl9oQllCQWdFSGJHOWhaR2x1WndFSU1USXpPMmhoYUdzQXxmrphSHHmnjBbZUANKE-W6IZPw5N7aoWi47updHHyXwA==',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'lang=en-US; session=MTY4ODM1MTUzN3xEdi1CQkFFQ180SUFBUkFCRUFBQWRmLUNBQUVHYzNSeWFXNW5EQXdBQ2t4UFIwbE9YMVZUUlZJWWVDMTFhUzlrWVhSaFltRnpaUzl0YjJSbGJDNVZjMlZ5XzRNREFRRUVWWE5sY2dIX2hBQUJCQUVDU1dRQkJBQUJDRlZ6WlhKdVlXMWxBUXdBQVFoUVlYTnpkMjl5WkFFTUFBRUxURzluYVc1VFpXTnlaWFFCREFBQUFCbl9oQllCQWdFSGJHOWhaR2x1WndFSU1USXpPMmhoYUdzQXxmrphSHHmnjBbZUANKE-W6IZPw5N7aoWi47updHHyXwA==',
        'Origin': 'https://mosco01.wiregeek.ir:2665',
        'Referer': 'https://mosco01.wiregeek.ir:2665/panel/inbounds',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    response = requests.post('https://mosco01.wiregeek.ir:2665/panel/inbound/list', cookies=cookies, headers=headers)