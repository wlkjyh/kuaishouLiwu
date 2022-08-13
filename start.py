from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import hashlib,requests
import time
import pyttsx3,datetime

starttime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print("准备启动浏览器")
print("[{}] 启动浏览器".format(starttime))
driver = webdriver.Chrome()
# driver = webdriver.Edge()
url = "https://live.kuaishou.com/u/KPL704668133"
driver.get(url)
time.sleep(2)
# print("网页启动成功，需要刷新一次浏览器")
print("[{}] 重新加载一次网页".format(starttime))
driver.refresh()
time.sleep(1)
# print("启动成功，开始获取弹幕")
loginclickd = False

liwuarr = {}
liwuarr["http://p1-live.a.yximgs.com/uhead/AB/2019/01/03/15/BMjAxOTAxMDMxNTU4NTdfMF9nOV9sdg==.jpg"] = "啤酒"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2020/08/21/17/BMjAyMDA4MjExNzQ5NTdfMF9nMzI3X2x2.jpg"] = "恋爱宇宙"
liwuarr["http://p4-live.a.yximgs.com/uhead/AB/2019/01/11/15/BMjAxOTAxMTExNTAyMzdfMF9nMTE0X2x2.jpg"] = "玫瑰"
liwuarr["http://p1-live.a.yximgs.com/uhead/AB/2019/08/22/15/BMjAxOTA4MjIxNTM4NDdfMF9nMl9sdg==.jpg"] = "棒棒糖"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2020/07/25/11/BMjAyMDA3MjUxMTI2NTFfMF9nMjY5X2x2.jpg"] = "游乐园"
liwuarr["http://p1-live.a.yximgs.com/uhead/AB/2022/07/06/14/BMjAyMjA3MDYxNDQyMjZfMF9nMzA2X2x2.jpg"] = "浪漫邮轮"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2022/07/06/12/BMjAyMjA3MDYxMjAyMDFfMF9nMjg5X2x2.jpg"] = "玫瑰花园"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2022/07/06/14/BMjAyMjA3MDYxNDA2MTdfMF9nMjg3X2x2.jpg"] = "真爱大炮"
liwuarr["http://p4-live.a.yximgs.com/uhead/AB/2020/06/15/11/BMjAyMDA2MTUxMTE2MzlfMF9nMjk4X2x2.jpg"] = "奥里给"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2020/01/15/15/BMjAyMDAxMTUxNTU5MTdfMF9nMTRfbHY=.jpg"] = "钻戒"
liwuarr["http://p4-live.a.yximgs.com/uhead/AB/2022/07/06/12/BMjAyMjA3MDYxMjAzNTlfMF9nMTZfbHY=.jpg"] = "皇冠"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2022/07/06/14/BMjAyMjA3MDYxNDA1MDlfMF9nMzExX2x2.jpg"] = "私人飞机"
liwuarr["http://p4-live.a.yximgs.com/uhead/AB/2019/10/22/10/BMjAxOTEwMjIxMDA2NDRfMF9nMjIyX2x2.jpg"] = "凤冠"
liwuarr["http://p1-live.a.yximgs.com/uhead/AB/2021/03/25/17/BMjAyMTAzMjUxNzM3NTlfMF9nMjIzX2x2.jpg"] = "火箭"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2020/02/11/14/BMjAyMDAyMTExNDA0MjJfMF9nMjI1X2x2.jpg"] = "穿云箭"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2020/02/11/14/BMjAyMDAyMTExNDA0MjJfMF9nMjI1X2x2.jpg"] = "烟花"
liwuarr["http://p1-live.a.yximgs.com/uhead/AB/2022/07/06/12/BMjAyMjA3MDYxMjAwNDZfMF9nMjE5X2x2.jpg"] = "告白气球"
liwuarr["http://p2-live.a.yximgs.com/uhead/AB/2020/09/05/16/BMjAyMDA5MDUxNjExMDBfMF9nMjk3X2x2.jpg"] = "超跑车队"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2019/11/19/10/BMjAxOTExMTkxMDE2NDRfMF9nMjQyX2x2.jpg"] = "金龙"
liwuarr["http://p2-live.a.yximgs.com/uhead/AB/2019/11/19/10/BMjAxOTExMTkxMDE3MDRfMF9nMjQzX2x2.jpg"] = "豪车幻影"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2019/11/12/10/BMjAxOTExMTIxMDIxMzNfMF9nMjQ0X2x2.jpg"] = "超级6"
liwuarr["http://p1-live.a.yximgs.com/uhead/AB/2019/11/19/10/BMjAxOTExMTkxMDE1MjRfMF9nMjQ1X2x2.jpg"] = "水晶"
liwuarr["http://p4-live.a.yximgs.com/uhead/AB/2020/03/05/15/BMjAyMDAzMDUxNTA4NDNfMF9nMjY3X2x2.jpg"] = "吻你"
liwuarr["http://p4-live.a.yximgs.com/uhead/AB/2020/07/25/11/BMjAyMDA3MjUxMTI3MjNfMF9nMjY4X2x2.jpg"] = "浪漫城堡"
liwuarr["http://p4-live.a.yximgs.com/uhead/AB/2019/11/19/10/BMjAxOTExMTkxMDE2MDVfMF9nMjQ2X2x2.jpg"] = "金莲"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2019/11/19/10/BMjAxOTExMTkxMDE1NDdfMF9nMjQ3X2x2.jpg"] = "福袋"
liwuarr["http://p4-live.a.yximgs.com/uhead/AB/2021/01/13/19/BMjAyMTAxMTMxOTAwNTBfMF9nMTAwMDVfbHY=.jpg"] = "入场券"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2019/04/11/11/BMjAxOTA0MTExMTU4NDVfMF9nMTY0X2x2.jpg"] = "猫粮"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2022/06/21/11/BMjAyMjA2MjExMTQ4MTNfMF9nMTA4NDdfbHY=.jpg"] = "吱吱鼠"
liwuarr["http://p2-live.a.yximgs.com/uhead/AB/2021/11/18/17/BMjAyMTExMTgxNzMwNDhfMF9nMTA0NzBfbHY=.jpg"] = "YYDS"
liwuarr["http://p1-live.a.yximgs.com/uhead/AB/2021/05/25/14/BMjAyMTA1MjUxNDIxNDdfMF9nMjY2X2x2.jpg"] = "幸运魔盒"
liwuarr["http://p1-live.a.yximgs.com/uhead/AB/2022/06/21/10/BMjAyMjA2MjExMDQ3MTFfMF9nMTA4MjNfbHY=.jpg"] = "草履虫"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2021/09/24/14/BMjAyMTA5MjQxNDE4MDhfMF9nMTAzODFfbHY=.jpg"] = "小白菜"
liwuarr["http://p5-live.a.yximgs.com/uhead/AB/2022/07/06/11/BMjAyMjA3MDYxMTU5NDNfMF9nMTk3X2x2.jpg"] = "棒棒糖"
liwuarr["http://p4-live.a.yximgs.com/uhead/AB/2021/09/29/11/BMjAyMTA5MjkxMTQ1NTNfMF9nMTAzNzFfbHY=.jpg"] = "人气票"
liwuarr_md5 = {}

print("[{}] 开始加载礼物MD5".format(starttime))

for key in liwuarr:
    value = liwuarr[key]
    # 获取md5
    r = requests.get(key)
    md5 = hashlib.md5(r.content).hexdigest()
    liwuarr_md5[md5] = value
    # print("md5:", md5, "礼物名称:", value)
    
    print("[{}][{}] {}".format(starttime,value,md5))


print("[{}] 加载礼物MD5完成".format(starttime))

last = ""
driver.refresh()
time.sleep(1)
driver.refresh()
time.sleep(3)

onload = False
now = False
while True:
    # Y-m-d H:M:S
    datetimes = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chat_list = driver.find_elements_by_class_name("chat")
    chat = chat_list[0]
    chat = chat.text
    # print(chat)
    if "登录发弹幕" in chat:
        if loginclickd == False:
            print("[{}] 登录快手后继续".format(datetimes))
            driver.find_element_by_class_name("comment-login-tips").click()
            loginclickd = True

        else:
            print("[{}] 登录快手后继续".format(datetimes))

        time.sleep(3)
    else:
        if onload == False:
            onload = True
            driver.refresh()
            time.sleep(3)

        body = driver.find_element_by_tag_name("body")
        body = body.text
        if "在线观众" not in body:
            print("[{}] 页面出现问题，开始重新刷新页面".format(datetimes))
            driver.refresh()
            time.sleep(6)
            print("[{}] 刷新完成".format(datetimes))



        chat_history_container = driver.find_element_by_class_name("chat-history-container")
        chat_info = chat_history_container.find_elements_by_class_name("chat-info")
        chat_info_bak = chat_info
        chat_info = chat_info[-1]
        chat_infos = chat_info.get_attribute("innerHTML")
        username = chat_info.find_element_by_class_name("username").text
        username = username[:-1]
        comment = chat_info.find_element_by_class_name("comment").text
        # 去掉所有的空格
        comment = comment.replace(" ", "")

        if "送" == comment:
            try:
                gift_img = chat_info.find_element_by_class_name("gift-img")
                gift_img = gift_img.get_attribute("src")
                if last != chat_info_bak:
                    last = chat_info_bak
                    r = requests.get(gift_img)
                    gift_img_md5 = hashlib.md5(r.content).hexdigest()
                    if gift_img_md5 in liwuarr_md5:
                        gift_name = liwuarr_md5[gift_img_md5]
                        # print("{}送了一个{}".format(username, gift_name))
                        print("[{}][{}] 送了一个：{}".format(datetimes, username, gift_name))

                        chat_info.find_element_by_class_name("username").click()
                        # pyttsx3.speak("感谢大哥{}送来的{}".format(username, gift_name))
                        time.sleep(0.2)
                        # print("Init OK!!!")

                        user_detail_name = driver.find_elements_by_class_name("user-detail-name")[0]
                        user_detail_name = user_detail_name.get_attribute("href")
                        userid = user_detail_name.split("/")[-1]
                        # print(userid)
                        req = "http://127.0.0.1:8900/shua.do?userid={}&gift={}&username={}".format(userid, gift_name,username)
                        requests.get(req)

                        if len(last) > 1024 * 1024:
                            print("[{}] 页面缓存太大，刷新页面".format(datetimes))
                            driver.refresh()
                            time.sleep(6)
                            print("[{}] 刷新完成".format(datetimes))

                                                 

                    else:
                        # print("{}送了一个未知礼物{}".format(username, gift_img_md5))
                        print("[{}][{}] 送了一个未知礼物：{}".format(datetimes, username, gift_img_md5))
                        # 记录到文件
                        with open("gift.txt", "a") as f:
                            f.write("MD5：{}  地址：{}".format(gift_img_md5, gift_img))
                            f.write("\n")
                            # 保存
                            f.close()


            except:
                # print("程序发送错误")
                print("[{}] 程序发生错误".format(datetimes))
        elif "点亮了" in comment:
            if last != chat_info_bak:
                last = chat_info_bak
                # print("{}点亮了爱心".format(username))
                print("[{}][{}] 点亮了爱心".format(datetimes, username))
            # pyttsx3.speak("感谢我大哥{}点亮了爱心".format(username))
