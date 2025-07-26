# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/18 08:25
# @Author: Enbryan Xie



from passlib.hash import md5_crypt

hash = md5_crypt.hash('123456', salt='EvaLvDXI')
print(hash)


