
import json
import json
dump_data ={
    "animals": {
        "dog": [
            {
                "name": "Rufus",
                "age":15
            },
            {
                "name": "Marty",
                "age": "null"
            }
        ]
    }
}
load_data = json.loads(dump_data)
jobs=load_data['animals']['dog']
result2 = []
for i in data:
# 从根节点开始，匹配name节点
    result2.append(jsonpath.jsonpath(i,'$..name')[0])
print(result2)


def get_comments(url):
    data = []
    doc = get_json(url)
    jobs=doc['hotComments']
    for job in jobs:
        dic = {}
        #从根节点开始，匹配content节点
        dic['content']=jsonpath.jsonpath(job,'$..content')[0] #评论
        dic['time']= stampToTime(jsonpath.jsonpath(job,'$..time')[0]) #时间
        dic['userId']=jsonpath.jsonpath(job['user'],'$..userId')[0]  #用户ID
        dic['nickname']=jsonpath.jsonpath(job['user'],'$..nickname')[0]#用户名
        dic['likedCount']=jsonpath.jsonpath(job,'$..likedCount')[0] #赞数
        data.append(dic)
    return pd.DataFrame(data)

final_result = get_comments('http://music.163.com/api/v1/resource/comments/R_SO_4_483671599?limit=10&offset=0')