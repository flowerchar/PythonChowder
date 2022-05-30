import requests

url = 'http://jwc.nau.edu.cn/Students/NauEventHandle.ashx?class=CourseEelectDeal&meth=AddCourse'
headers = {
    'cookie':'ASP.NET_SessionId=wewkjiguaddafszhibjxztui; _d_id=9fe8f84e309b9806c33d4dea7f0391; .ASPXCOOKIEDEMO=9764D96746D7A2841A3502648415C223B0BEF6D871C5667CC9F60A86EEC90115F1D37C5C2C8AA3837ACCA65CBAA5226A203CF5C0CD67CAF9E364EB89040E3E9CAFA0C306D1C5D0382CEF71476F07E2AD7644CADBBA4545FC91591B853EB5C9ED503B1870BA190CFA0D174873F55E820560F0E02D0FEE17377A7D21671E720062B5BCF9989D5D82FE85D8E6FB3F459FDC8D8ECD1D20AB44F2F8E35A2F211D1A75',
    'host':'jwc.nau.edu.cn',
    'origin':'http://jwc.nau.edu.cn',
    'referer':'http://jwc.nau.edu.cn/Students/ZXCourseElection.aspx?t=F214BD16643A3AED0853984813F585F0&cid=9F02F38AA4DF616B',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}
data = {
    'CourseSelectStyle': "先到先得",
    'banRule': "False",
    'courseID': "10400900",
    'endDate': "D359BC00CBC33401041CBD7A36B5A594902CCB983859DA83",
    'limitNum': "0",
    'startDate': "355616CDD038C829549E27D00D4FCF77921BFB5F64C74CB9",
    'teachingClass': "zx327",
    'term': "202120221",
    'token': "f669fc6c4a30061e3e9ac166a99a68aa"
}
resp = requests.post(url=url, headers=headers, data=data)
print(resp.status_code)
print(resp.text)