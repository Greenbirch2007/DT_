
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, UniqueConstraint, ForeignKeyConstraint, \
    Index


egine = create_engine('mysql+pymysql://root@127.0.0.1:3306/DT?charset=utf8', max_overflow=5)

# 创建一个Base类，后面床架你的每个包都需要继承这个类
Base = declarative_base()


# 创建单表：业务线
class Business(Base):
    __tablename__ ='business'
    id = Column(Integer,primary_key=True,autoincrement=True)
    bname = Column(String(32),nullable=False,index=True)

# 多对一：多个服务可以属于一个业务线，多个业务线不能包含同一个服务


class Service(Base):
    __tablename__= 'service'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sname = Column(String(32), nullable=False, index=True)
    ip = Column(String(15), nullable=False)
    port = Column(Integer, nullable=False)

    business_id =Column(Integer,ForeignKey('business.id'))

    __table_args__ =(
        UniqueConstraint(ip,port,name='uix_ip_port'),
        Index('ix_id_same',id,sname)
    )


# 一对一：一种角色只能管理一条业务先，一条业务线只能被一种角色管理

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rname = Column(String(32), nullable=False, index=True)
    priv = Column(String(64), nullable=False)

    business_id = Column(Integer, ForeignKey('business.id'), unique=True)


# 多对多:多个用户可以是同一个role,多个role可以包含同一个用户
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(32), nullable=False, index=True)


class Users2Role(Base):
    __tablename__ = 'users2role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey('users.id'))
    rid = Column(Integer, ForeignKey('role.id'))

    __table_args__ = (
        UniqueConstraint(uid, rid, name='uix_uid_rid'),
    )
# 创建所有表
def init_db():
    Base.metadata.create_all(egine)


# 删除数据库所有表
def drop_db():
    Base.metadata.drop_all(egine)

if __name__ == '__main__':
    init_db()

