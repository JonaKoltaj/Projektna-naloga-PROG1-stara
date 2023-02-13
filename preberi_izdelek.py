import re
import requests
import regex_koda
import orodja

# with open('html.txt') as d:
#     spletna_stran = d.read()

# linki = re.findall(regex_koda.rx_link, spletna_stran)

# cookies = {
#     'vtc': 'TKBVYrNxUg4su7UlUVaj6o',
#     'dimensionData': '657',
#     'TBV': '7',
#     'pxcts': '6df7e2a0-a572-11ed-a329-506657466666',
#     '_pxvid': '6df7d566-a572-11ed-a329-506657466666',
#     'ACID': '5dc3d51a-199b-4f57-84f9-c29fe65c3dbf',
#     'hasACID': 'true',
#     'assortmentStoreId': '3081',
#     'hasLocData': '1',
#     '_pxhd': '3354445ddfd23f17e34d52fad0465ba595ebbf0cbebbb12bd8d9e668c5a0469c:6dddb70b-a572-11ed-a3f3-65704a534f4d',
#     'AID': 'wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1675614994117',
#     'TB_Latency_Tracker_100': '1',
#     'TB_Navigation_Preload_01': '1',
#     'TB_SFOU-100': '',
#     '_astc': '76ce20bc765b41736512a09ea6881d96',
#     'bm_mi': '81EDB75574828C692EBF64AB0EA45549~YAAQNBdlX9OUwjGGAQAA2ltkNxJToOYPLNph/42PwTPACNBo2v7TgYucdvy7NFvLT8Cvo1ORRf5P/OcvD5syWnX7CEWCy5+H0u4WojzQ3N96MC+LaBMwOQalrCo4tIYVAaTH9C87gsU2CVhaPGgi6LdfL+Nj2NWDwv46HCNSOeDXQAxBd0K+t5eek8rv1RPrGsefW0Jk0FDyFyDZ0nwVHClBuNV7hhjcJb2fsSDJsqDvgEwDg+VaMQas7lk2+Y4Kfh2FAhmcOzvTpyzwtnTbI0EmKW73DiUHe/IfFSH+mzvenALrobbyiajhyieidsfSQaLsyJoi~1',
#     'ak_bmsc': '1D5C8C232832E72786F5AD5011310478~000000000000000000000000000000~YAAQNBdlX+KUwjGGAQAA419kNxIwzlfQffnMzgNyi2a674KFzYAevgJeF6YBiLWdtlTkb3cUUojNOnYU/A/TmjPYbfcD6ycqT0hNyyZlb9kg6W20IwpJ0reTIZuu1t3PbdQVYj3DPkSCNf1KLlEod627mhEwFj9kxg+LP6Ediyek0AUehCHuNJQ7tvvf2UeljM87IEU5UNbKHgYboPoD/S121B6zqrepIPDiPloY5/yBfXdAhrH19nCoD2eyhx1mGzGSDewV3lBQWav4foH20x042chCuKvCrA6d+6dg14bobfK9GVlARlkr6W5RS72oVXLWdxtC4GwA8WeSyhXe6C5NqrdnaaZwVypj4imSnQjsre/wZquzB0N/r6dhFX8HELGCwO1TiJxd+cUHk5zywkxMWIeLF9gIchcIRCD+LrXeox1ApA==',
#     'wmtboid': '1675967781-5850833164-19917729920-62242906',
#     'auth': 'MTAyOTYyMDE4la5aEAYX91KA7TJnbNAKVbdhPimDBQ5bSv2CfLWDsjEvOTVU3LjOrN%2Ba%2B2wZpD4MaEZJQGRqMP2Us0orXSnSrT2u%2FAZEOIdJBAZtkS3fB6MXOO6mxh9D%2F3jYUav%2FOPRz767wuZloTfhm7Wk2KcjygobRHThsmZk%2BGcqTfIab85Qbu8J%2B5ir9B5VXZJqyyrJlKoHqwugcBf8qf8E8ATK%2BaaUPrWLDS9%2FLfxWLNmMQYG8UMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHQ86swnkDEECrCDC5fd9vKU39c6P%2B8X%2FOXr5uG6Wdq0xpho3AqJRRpE3mYs8IHhbO1Z91KpGkAtzZ0uoy25ggvQIgZr0z5hYEWvdD3RQ9p7mst3JVZWfEaqQaqiKasazt5E5WBBdZBCyKnCQAR7o6eg%3D',
#     'bstc': 'ZH4nR2lZ3oaCAYXgGiQmKo',
#     'mobileweb': '0',
#     'xptc': 'assortmentStoreId%2B3081',
#     'xpth': 'x-o-mart%2BB2C~x-o-mverified%2Bfalse',
#     'xpa': '-7Lfp|0dn-S|10hNA|3AZCz|4ifl2|4sTVz|6N-qW|8J6Zl|Amg8a|Bgys_|D8jju|DSZXu|Dxl8d|GK20V|GUdkG|HpQ44|LHyLT|N0ZXc|QmSf2|SglEw|UUnt1|V9HWe|XUHzs|_oJYa|_vwUM|gY6i6|j8K4O|jx3gX|mwK0m|rwMui|uTxgM|vq9e-|w9B7l|xig4c|z5ZZv',
#     'exp-ck': '0dn-S110hNA14ifl214sTVz1Bgys_1D8jju1DSZXu4Dxl8d2GUdkG1HpQ441LHyLT1N0ZXc2QmSf21UUnt12V9HWe1_oJYa1_vwUM1j8K4O1jx3gX1mwK0m3uTxgM1w9B7l2xig4c1z5ZZv1',
#     'codedefab': 'true',
#     'xptwj': 'rq:d99f8db0f4d9286e8656:X31GWZYjc1/2kqs55pFSs650KIVmXSTy/26DzszS+OcIV7kS6bcClIRE2KhE8jQiEmNzfTLPdZeC48BfiHR751fRxAkYp6D7ZMs2VVAIjhA+sCuYbcfXj/abS+JFPalPl+Q65lEfu6m7ttgAw5/nB89ur/HQzKDVdxPN',
#     'adblocked': 'true',
#     'xpm': '1%2B1675970389%2BTKBVYrNxUg4su7UlUVaj6o~%2B0',
#     'com.wm.reflector': '"reflectorid:0000000000000000000000@lastupd:1675970392000@firstcreate:1675614731483"',
#     'locDataV3': 'eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaXNFeHBsaWNpdCI6ZmFsc2UsImludGVudCI6IlNISVBQSU5HIiwicGlja3VwIjpbeyJidUlkIjoiMCIsIm5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdlcmJlciBSb2FkIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5NTgyOS0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIzMDgxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0NVUkJTSURFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozOC40NzQ0LCJsb25naXR1ZGUiOi0xMjEuMzQzNywicG9zdGFsQ29kZSI6Ijk1ODI5IiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJhY2Nlc3NQb2ludHMiOm51bGwsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMzA4MSIsImRpc3BsYXlOYW1lIjoiU2FjcmFtZW50byBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5NTgyOSIsImFkZHJlc3NMaW5lMSI6Ijg5MTUgR2VyYmVyIFJvYWQiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6Ijk1ODI5LTAwMDAifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjM4LjQ4MjY3NywibG9uZ2l0dWRlIjotMTIxLjM2OTAyNn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImFjY2Vzc1BvaW50cyI6W3siYWNjZXNzVHlwZSI6IkRFTElWRVJZX0FERFJFU1MifV0sImh1Yk5vZGVJZCI6IjMwODEiLCJpc0V4cHJlc3NEZWxpdmVyeU9ubHkiOmZhbHNlLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJERUxJVkVSWV9BRERSRVNTIl19LCJpbnN0b3JlIjpmYWxzZSwicmVmcmVzaEF0IjoxNjc1OTkxOTkxNzA3LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NWRjM2Q1MWEtMTk5Yi00ZjU3LTg0ZjktYzI5ZmU2NWMzZGJmIn0%3D',
#     'locGuestData': 'eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjp0cnVlLCJzdG9yZVNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiMzA4MSIsInRpbWVzdGFtcCI6MTY3NTYxNDY0MDkwNn0sInNoaXBwaW5nQWRkcmVzcyI6eyJpZCI6bnVsbCwidGltZXN0YW1wIjoxNjc1NjE0NjQwOTA2LCJjcmVhdGVUaW1lc3RhbXAiOm51bGwsInR5cGUiOiJwYXJ0aWFsLWxvY2F0aW9uIiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJwb3N0YWxDb2RlIjoiOTU4MjkiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMzA4MSIsInR5cGUiOiJERUxJVkVSWSJ9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjc1NjE0NjQwOTA2LCJiYXNlIjoiOTU4MjkifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NWRjM2Q1MWEtMTk5Yi00ZjU3LTg0ZjktYzI5ZmU2NWMzZGJmIn0%3D',
#     'xptwg': '2267443139:5A124D0CBE83E8:E6D2EE:17A5E6D4:595DC3B0:ADAF925E:',
#     'TS012768cf': '010f2d9f26687a149137927a5e3f0dc0f5f777c4f758cc55ebc697318131546538b7b7bc6c4f3859d0cd29ed24a97f61b0af312234',
#     'TS01a90220': '010f2d9f26687a149137927a5e3f0dc0f5f777c4f758cc55ebc697318131546538b7b7bc6c4f3859d0cd29ed24a97f61b0af312234',
#     'TS2a5e0c5c027': '08f240ec3aab20007f72a6d8ee64f6513460b77b7d6a853a2d30e169993c36ebee01af3d39ca325f08967fe30a113000e3404bef8b906944e92ac8997fd482fc93c56a5ee231ceb818fc5e0bda736e8b66bae6025ed46c84e823e7bcd0fce191',
#     'akavpau_p2': '1675970992~id=c14609637e2360762edc56b6bb72bccc',
#     'bm_sv': 'C00102491BB1429B608158091BEBBEA1~YAAQVRdlX5flCC+GAQAAD7GeNxLj8eIsnog9Sjtu1jfc48nqs2Gh9I34GPqezHBnfp6Tkoek/9lXtEovjcj0UTsbGPEVeLqjoVOGP6gnW1F42yIeKYl3k4p7qEQs0vJFcjFCchDY4YlBqNPhlRwkQm1MnP+SPKZl6z4haxH6V6iWfT1hGPGsFlEy0YMLdTkIcm0ArtTXIb+RkkhlwzY4kwbIUaWrUi0ja7vtbKvqH9CaPsjPj64tFIyI3PY5O7D7a/I=~1',
# }

# headers = {
#     'authority': 'www.walmart.com',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language': 'sl-SI,sl;q=0.9,en-GB;q=0.8,en;q=0.7',
#     'cache-control': 'max-age=0',
#     # 'cookie': 'vtc=TKBVYrNxUg4su7UlUVaj6o; dimensionData=657; TBV=7; pxcts=6df7e2a0-a572-11ed-a329-506657466666; _pxvid=6df7d566-a572-11ed-a329-506657466666; ACID=5dc3d51a-199b-4f57-84f9-c29fe65c3dbf; hasACID=true; assortmentStoreId=3081; hasLocData=1; _pxhd=3354445ddfd23f17e34d52fad0465ba595ebbf0cbebbb12bd8d9e668c5a0469c:6dddb70b-a572-11ed-a3f3-65704a534f4d; AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1675614994117; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; _astc=76ce20bc765b41736512a09ea6881d96; bm_mi=81EDB75574828C692EBF64AB0EA45549~YAAQNBdlX9OUwjGGAQAA2ltkNxJToOYPLNph/42PwTPACNBo2v7TgYucdvy7NFvLT8Cvo1ORRf5P/OcvD5syWnX7CEWCy5+H0u4WojzQ3N96MC+LaBMwOQalrCo4tIYVAaTH9C87gsU2CVhaPGgi6LdfL+Nj2NWDwv46HCNSOeDXQAxBd0K+t5eek8rv1RPrGsefW0Jk0FDyFyDZ0nwVHClBuNV7hhjcJb2fsSDJsqDvgEwDg+VaMQas7lk2+Y4Kfh2FAhmcOzvTpyzwtnTbI0EmKW73DiUHe/IfFSH+mzvenALrobbyiajhyieidsfSQaLsyJoi~1; ak_bmsc=1D5C8C232832E72786F5AD5011310478~000000000000000000000000000000~YAAQNBdlX+KUwjGGAQAA419kNxIwzlfQffnMzgNyi2a674KFzYAevgJeF6YBiLWdtlTkb3cUUojNOnYU/A/TmjPYbfcD6ycqT0hNyyZlb9kg6W20IwpJ0reTIZuu1t3PbdQVYj3DPkSCNf1KLlEod627mhEwFj9kxg+LP6Ediyek0AUehCHuNJQ7tvvf2UeljM87IEU5UNbKHgYboPoD/S121B6zqrepIPDiPloY5/yBfXdAhrH19nCoD2eyhx1mGzGSDewV3lBQWav4foH20x042chCuKvCrA6d+6dg14bobfK9GVlARlkr6W5RS72oVXLWdxtC4GwA8WeSyhXe6C5NqrdnaaZwVypj4imSnQjsre/wZquzB0N/r6dhFX8HELGCwO1TiJxd+cUHk5zywkxMWIeLF9gIchcIRCD+LrXeox1ApA==; wmtboid=1675967781-5850833164-19917729920-62242906; auth=MTAyOTYyMDE4la5aEAYX91KA7TJnbNAKVbdhPimDBQ5bSv2CfLWDsjEvOTVU3LjOrN%2Ba%2B2wZpD4MaEZJQGRqMP2Us0orXSnSrT2u%2FAZEOIdJBAZtkS3fB6MXOO6mxh9D%2F3jYUav%2FOPRz767wuZloTfhm7Wk2KcjygobRHThsmZk%2BGcqTfIab85Qbu8J%2B5ir9B5VXZJqyyrJlKoHqwugcBf8qf8E8ATK%2BaaUPrWLDS9%2FLfxWLNmMQYG8UMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHQ86swnkDEECrCDC5fd9vKU39c6P%2B8X%2FOXr5uG6Wdq0xpho3AqJRRpE3mYs8IHhbO1Z91KpGkAtzZ0uoy25ggvQIgZr0z5hYEWvdD3RQ9p7mst3JVZWfEaqQaqiKasazt5E5WBBdZBCyKnCQAR7o6eg%3D; bstc=ZH4nR2lZ3oaCAYXgGiQmKo; mobileweb=0; xptc=assortmentStoreId%2B3081; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=-7Lfp|0dn-S|10hNA|3AZCz|4ifl2|4sTVz|6N-qW|8J6Zl|Amg8a|Bgys_|D8jju|DSZXu|Dxl8d|GK20V|GUdkG|HpQ44|LHyLT|N0ZXc|QmSf2|SglEw|UUnt1|V9HWe|XUHzs|_oJYa|_vwUM|gY6i6|j8K4O|jx3gX|mwK0m|rwMui|uTxgM|vq9e-|w9B7l|xig4c|z5ZZv; exp-ck=0dn-S110hNA14ifl214sTVz1Bgys_1D8jju1DSZXu4Dxl8d2GUdkG1HpQ441LHyLT1N0ZXc2QmSf21UUnt12V9HWe1_oJYa1_vwUM1j8K4O1jx3gX1mwK0m3uTxgM1w9B7l2xig4c1z5ZZv1; codedefab=true; xptwj=rq:d99f8db0f4d9286e8656:X31GWZYjc1/2kqs55pFSs650KIVmXSTy/26DzszS+OcIV7kS6bcClIRE2KhE8jQiEmNzfTLPdZeC48BfiHR751fRxAkYp6D7ZMs2VVAIjhA+sCuYbcfXj/abS+JFPalPl+Q65lEfu6m7ttgAw5/nB89ur/HQzKDVdxPN; adblocked=true; xpm=1%2B1675970389%2BTKBVYrNxUg4su7UlUVaj6o~%2B0; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1675970392000@firstcreate:1675614731483"; locDataV3=eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaXNFeHBsaWNpdCI6ZmFsc2UsImludGVudCI6IlNISVBQSU5HIiwicGlja3VwIjpbeyJidUlkIjoiMCIsIm5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdlcmJlciBSb2FkIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5NTgyOS0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIzMDgxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0NVUkJTSURFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozOC40NzQ0LCJsb25naXR1ZGUiOi0xMjEuMzQzNywicG9zdGFsQ29kZSI6Ijk1ODI5IiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJhY2Nlc3NQb2ludHMiOm51bGwsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMzA4MSIsImRpc3BsYXlOYW1lIjoiU2FjcmFtZW50byBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5NTgyOSIsImFkZHJlc3NMaW5lMSI6Ijg5MTUgR2VyYmVyIFJvYWQiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6Ijk1ODI5LTAwMDAifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjM4LjQ4MjY3NywibG9uZ2l0dWRlIjotMTIxLjM2OTAyNn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImFjY2Vzc1BvaW50cyI6W3siYWNjZXNzVHlwZSI6IkRFTElWRVJZX0FERFJFU1MifV0sImh1Yk5vZGVJZCI6IjMwODEiLCJpc0V4cHJlc3NEZWxpdmVyeU9ubHkiOmZhbHNlLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJERUxJVkVSWV9BRERSRVNTIl19LCJpbnN0b3JlIjpmYWxzZSwicmVmcmVzaEF0IjoxNjc1OTkxOTkxNzA3LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NWRjM2Q1MWEtMTk5Yi00ZjU3LTg0ZjktYzI5ZmU2NWMzZGJmIn0%3D; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjp0cnVlLCJzdG9yZVNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiMzA4MSIsInRpbWVzdGFtcCI6MTY3NTYxNDY0MDkwNn0sInNoaXBwaW5nQWRkcmVzcyI6eyJpZCI6bnVsbCwidGltZXN0YW1wIjoxNjc1NjE0NjQwOTA2LCJjcmVhdGVUaW1lc3RhbXAiOm51bGwsInR5cGUiOiJwYXJ0aWFsLWxvY2F0aW9uIiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJwb3N0YWxDb2RlIjoiOTU4MjkiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMzA4MSIsInR5cGUiOiJERUxJVkVSWSJ9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjc1NjE0NjQwOTA2LCJiYXNlIjoiOTU4MjkifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NWRjM2Q1MWEtMTk5Yi00ZjU3LTg0ZjktYzI5ZmU2NWMzZGJmIn0%3D; xptwg=2267443139:5A124D0CBE83E8:E6D2EE:17A5E6D4:595DC3B0:ADAF925E:; TS012768cf=010f2d9f26687a149137927a5e3f0dc0f5f777c4f758cc55ebc697318131546538b7b7bc6c4f3859d0cd29ed24a97f61b0af312234; TS01a90220=010f2d9f26687a149137927a5e3f0dc0f5f777c4f758cc55ebc697318131546538b7b7bc6c4f3859d0cd29ed24a97f61b0af312234; TS2a5e0c5c027=08f240ec3aab20007f72a6d8ee64f6513460b77b7d6a853a2d30e169993c36ebee01af3d39ca325f08967fe30a113000e3404bef8b906944e92ac8997fd482fc93c56a5ee231ceb818fc5e0bda736e8b66bae6025ed46c84e823e7bcd0fce191; akavpau_p2=1675970992~id=c14609637e2360762edc56b6bb72bccc; bm_sv=C00102491BB1429B608158091BEBBEA1~YAAQVRdlX5flCC+GAQAAD7GeNxLj8eIsnog9Sjtu1jfc48nqs2Gh9I34GPqezHBnfp6Tkoek/9lXtEovjcj0UTsbGPEVeLqjoVOGP6gnW1F42yIeKYl3k4p7qEQs0vJFcjFCchDY4YlBqNPhlRwkQm1MnP+SPKZl6z4haxH6V6iWfT1hGPGsFlEy0YMLdTkIcm0ArtTXIb+RkkhlwzY4kwbIUaWrUi0ja7vtbKvqH9CaPsjPj64tFIyI3PY5O7D7a/I=~1',
#     'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
# }

# params = {
#     'athbdg': 'L1600',
# }

# from tqdm import tqdm
# vsi_izdelki = []
# for i in tqdm(range(len(linki))):
#     response = requests.get('https://www.walmart.com' + linki[i], params=params, cookies=cookies,headers=headers,)
#     if 'Robot or human' in response.content.decode('utf-8'):
#         input(' Zaznalo te je kot robota, osvezi stran v browserju')
#         response = requests.get('https://www.walmart.com' + linki[i], params=params, cookies=cookies, headers=headers)
#     vsi_izdelki.append(response.content.decode('utf-8'))
    
with open('jagode.txt', encoding='utf-8') as d:
    jagode = d.read()
    
with open('kumarca.txt', encoding='utf-8') as d:
    kumarca = d.read()
    
with open('voda.txt', encoding='utf-8') as d:
    voda = d.read()

# izluscimo glavne podatke iz izdelka in jih damo v slovar
def izlusci_glavne_podatke(izdelek):
    podatki_izdelka = {}
    podatki = re.findall(regex_koda.rx_izdelek, izdelek)
    brand = podatki[0][0]
    podatki_izdelka['Brand'] = brand
    # preverimo ce sta v imenu brand ali kolicina in ju odstranimo
    ime = podatki[0][1]
    stevilka = re.findall(r'\d', ime)
    if brand in ime:
        ime = ime.replace(brand + " ", "")
    if len(stevilka) != 0:
        rx = r',\s\d+.*'
        niz = ' '.join(re.findall(rx, ime))
        ime = ime.replace(niz, "")
    if 'Each' in ime:
        ime = ime.replace(", Each", "")
    podatki_izdelka['Title'] = ime
    podatki_izdelka['Rating'] = float(podatki[0][2])
    podatki_izdelka['Price'] = float(podatki[0][3])
    return podatki_izdelka
    
def izlusci_relativno_ceno(izdelek):
    podatki = re.findall(regex_koda.rx_relativna_cena, izdelek)
    if len(podatki) != 0:
        rel_cena = podatki[0]
    else:
        rel_cena = None
    return rel_cena

# ce je v imenu kolicina jo nastejemo, ce je ni, je to posamicen izdelek
def izlusci_kolicino(izdelek):
    podatki = re.findall(regex_koda.rx_izdelek, izdelek)
    ime = podatki[0][1]
    stevilka = re.findall(r'\d', ime)
    if len(stevilka) != 0:
        rx = r'\d+.*'
        niz = re.findall(rx, ime)[0]
    else:
        niz = 'Unit'
    return niz

# kar mors se nrdit je ustrezn tip podatkov izluscit
def izlusci_hranilno_vrednost(izdelek):
    hr_vred = {}
    podatki = re.findall(regex_koda.rx_hranilna_vrednost, izdelek)
    if len(podatki) != 0:
        hr_vred['Calories'] = int(podatki[0][0])
        for i, vrednost in enumerate(regex_koda.hranilne_vrednosti):
            # locimo na prazne podatke in na neprazne
            if podatki[0][2*i+1] == 'null':
                hr_vred[vrednost] = 0
            if podatki[0][2*i+2] == 'null':
                hr_vred[vrednost + ' DVP'] = 0
            else:
                # najprej naredimo int ali float iz kolicine
                kolicina = podatki[0][2*i+1].replace('"', '')
                rx = r'[A-Za-z]'
                enota = ''.join(re.findall(rx, kolicina))
                niz = kolicina.replace(enota, '')
                if '.' in niz:
                    hr_vred[vrednost] = float(niz)
                else:
                    hr_vred[vrednost] = int(niz)
                # potem naredimo int iz dvp, dvp je vedno procent
                dvp = podatki[0][2*i+2].replace('"', '')
                niz = dvp.replace('%', '')
                hr_vred[vrednost + ' DVP'] = int(niz)
    return hr_vred
        
# tuki preveri da je rel cena podana, ce je, preveri ce je podana teza v naslovu in pol preveri ce se ujema
# def izracunaj_kolicino(izdelek):
#     rel_cena = izloci_relativno_ceno(izdelek)
#     if rel_cena:
#         rx_enota = re.compile(r'/*')
    
print(izlusci_hranilno_vrednost(jagode))
print(izlusci_hranilno_vrednost(kumarca))
print(izlusci_hranilno_vrednost(voda))