> Part of the web crawler systems.

## 1. 医院医生信息

网站地图url: https://www.haodf.com/sitemap.html

原有网站： http://www.haodf.com/

## 2. 药物相互作用信息
药智网爬取药物相互作用信息

https://db.yaozh.com/interaction

http://www.medix.cn/Main.aspx

## 3. 疾病知识库

http://pmmp.cnki.net/cdd/Disease/dis_detail.aspx?id=41955&SearchType=1 #relationmed


## 4. 指标库

http://jbk.39.net/jiancha/sgnjc/

## 5. 寻医问药网站


## 6. 知乎网

- 遍历知乎所以的用户，获取用户的个人相关信息，关注和被关注用户列表，以及用户的话题关注情况。完成对知乎网关系网络的遍历；

- 使用MySQL数据库进行存储，遍历列表使用redis高速缓存进行存储；

- 分为scrapy和self-framework两个版本，推荐使用self-framework；

- url样例：https://www.zhihu.com/people/excited-vczh/following