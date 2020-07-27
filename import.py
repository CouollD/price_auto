import peewee

# データベースの指定
db = peewee.SqliteDatabase("data.db")

# ユーザモデルを定義
class User(peewee.Model):
    userId = peewee.TextField()
    userCompany = peewee.TextField()
    userDiscountRate = peewee.IntegerField()

    class Meta:
        database =db

# ユーザーテーブル作成
User.create_table()

# tsvファイルを一行づつ読み込んで、タブで分割し、それぞれをデータベースに登録
for line in open("user.tsv", "r"):
    (userId, userCompany, userDiscountRate) =tuple(line[:-1].split("\t"))
    if userDiscountRate.isdigit():
        # 一行目のコメント対応
        User.create(user =userId,userCompany = userCompany,userDiscountRate = int(userDiscountRate))
        