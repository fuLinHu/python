


jso = '''
{
    "name" : "政策数据_房地产开发",
    "jobStatus" : "3",
    "knowledgeSource" : ObjectId("5f6c02511345fd2b483347f2"),
    "hand" : false,
    "automatic" : 1,
    "defaultThread" : 0,
    "crawlerConfig" : {
        "seed_urls" : "http://www.fangchan.com/policy/28/",
        "list_url" : "//a[text()*='下一页']",
        "list_rule_type" : "xpath",
        "detail_url" : "//div[@class='related-news']//ul/li/a",
        "detail_rule_type" : "xpath",
        "detail_more_url" : "",
        "detail_more_rule_type" : "regex",
        "basePropertyList" : [
            {
                "labelName" : "标题",
                "labelParam" : "99bc91f7792842129ba10a6ae19a47fe",
                "field_url" : "//h1[1]/text()",
                "field_type" : "xpath"
            },
            {
                "labelName" : "正文",
                "labelParam" : "58e8ce8f6a114a6ab8c642e2602d922e",
                "field_url" : "//div[@class='summary-text']",
                "field_type" : "xpath"
            },
            {
                "labelName" : "城市",
                "labelParam" : "d9455512f4d842b8b7822a4d94b354f2",
                "field_url" : "/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[1]/span",
                "field_type" : "xpath"
            },
            {
                "labelName" : "颁发时间",
                "labelParam" : "ddb674a3922f4e3f9d1dda6ee9b69e9c",
                "field_url" : "/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[2]/span",
                "field_type" : "xpath"
            },
            {
                "labelName" : "发文字号",
                "labelParam" : "eb8166e68d4b458185f712a8d4c4b86b",
                "field_url" : "/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/span",
                "field_type" : "xpath"
            },
            {
                "labelName" : "发文机构",
                "labelParam" : "88d954dc77964520946eeba51dcd63a0",
                "field_url" : "/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[4]/span",
                "field_type" : "xpath"
            },
            {
                "labelName" : "实施日期",
                "labelParam" : "d2e02e2b4ac74b3fab1161ef0a1d7f53",
                "field_url" : "/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[5]/span",
                "field_type" : "xpath"
            },
            {
                "labelName" : "效力级别",
                "labelParam" : "b0f85a677855453c9535e62d1f6efe1a",
                "field_url" : "/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[6]/span",
                "field_type" : "xpath"
            },
            {
                "labelName" : "类别",
                "labelParam" : "00cbd8cd9fb143deafbab5478d491621",
                "field_url" : "/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[7]/span",
                "field_type" : "xpath"
            },
            {
                "labelName" : "关键词",
                "labelParam" : "493aeb9d352045acbd53ee4d53559aa7",
                "field_url" : "/html/body/div[1]/div[3]/div[1]/div[3]",
                "field_type" : "xpath"
            }
        ]
    },
    "isIncrement" : "1",
    "hasCheckData" : "0",
    "taskBatch" : 2,
    "createDate" : ISODate("2020-09-24T05:43:36.213Z")
}
      '''


import json

data2 = json.loads(jso)
print(data2)


f = open("E:\付林虎\付林虎\python\day1\python\io1\source","r",encoding="utf-8")

for i in f:
    data2["name"] = "政策数据_"+i
    print(data2)
