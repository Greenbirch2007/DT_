
from app import db
from flask import abort

class Video(db.Model):

    __tablename__ ='video'
    id = db.Column(db.Integer, primary_key=True)
    vid = db.Column(db.String(50))
    coverUrl = db.Column(db.Text)
    desc = db.Column(db.Text)
    synopsis = db.Column(db.Text)
    title = db.Column(db.String(100))
    updateTime = db.Column(db.Integer)
    theme = db.Column(db.String(10))
    isDelete = db.Column(db.Boolean,default=False)

    def to_json(self):
        # 完成数据模型到JSON格式化的序列化字段转换
        json_blog ={
            "id":self.vid,
            "coverUrl":self.coverUrl,
            "desc":self.desc,
            'synopsis':self.synopsis,
            "title":self.title,
            "updateTime":self.updateTime

        }

        return json_blog

def getHomepageData():
    result = {}
    banners = Video.query.filter_by(theme="banner")
    result["banner"] = [banner.to_json() for banner in banners]
    #  获取homepage
    first = Video.query.filter_by(theme='hot').all()
    second = Video.query.filter_by(theme="dramatic").all()
    third = Video.query.filter_by(theme="idol").all()
    if len(first) and len(second) and len(third):
        homepage = [
            {'hot broastcast':[item.to_json for item in first]},
            {'dramatic threater':[item.to_json for item in second]},
            {'ido threatre':[item.to_json for item in third]}
        ]
        result['homepage'] =homepage
        return result
    else:
        abort(404)