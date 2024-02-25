import streamlit as st
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import time

page = st.sidebar.radio('下雨的小屋', ['Hello here!', '兴趣推荐', '修图神器', '百宝箱', '开心闯关', '网站漫步','想给今天打个分', '留个言吧'])

def page_1():
    for i in range(3):
        st.snow()
    st.title("欢迎走进")
    st.header(":blue[----下雨的小屋]")

def page_2():
    '''兴趣推荐'''
    tabl,tab2,tab3,tab4 = st.tabs(["运动","书籍","日常", "自然"])
    with tabl:
        with open('blue enough - shade.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.image('微信图片_20240219203635.jpg')
        a = st.text_input("你想给我推荐的运动是……")
        st.download_button(label="下载1", data = mymp3, file_name="blue enough - shade.mp3")
    with tab2:
        with open('Relaxing Music - Muisca Para Calmar.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.image('微信图片_20240219203629.jpg')
        b = st.text_input("你想给我推荐的书籍是……")
        st.download_button(label="下载2", data = mymp3, file_name="Relaxing Music - Muisca Para Calmar.mp3")
    with tab3:
        with open('Cosmic Twinkle - Catch Me.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.image('微信图片_20240219203617.jpg')
        c = st.text_input("你想给我推荐的日常是……")
        st.download_button(label="下载3", data = mymp3, file_name="Cosmic Twinkle - Catch Me.mp3")
    with tab4:
        with open('Vuxa - 暮春.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.image('微信图片_20240225123516.jpg')
        st.image('微信图片_20240225124541.jpg')
        st.image('微信图片_20240225124546.jpg')
        st.image('微信图片_20240225124600.jpg')
        st.image('微信图片_20240225124552.jpg')
        st.image('微信图片_20240225124534.jpg')
        st.download_button(label="下载4", data = mymp3, file_name="Vuxa - 暮春.mp3")
    
def page_3():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=["png", "jpeg", "jpg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)

        tab1,tab2,tab3 = st.tabs(["原图","滤镜","改色"])
        with tab1:
            st.image(img)
        with tab2:
            a = st.toggle('模糊滤镜')
            b = st.toggle('轮廓滤镜')
            c = st.toggle('边缘增强滤镜')
            d = st.toggle('浮雕滤镜')
            e = st.toggle('锐化滤镜')
            f = st.toggle('平滑滤镜')
            
            if a:
                st.image(img.filter(ImageFilter.BLUR))
            if b:
                st.image(img.filter(ImageFilter.CONTOUR))
            if c:    
                st.image(img.filter(ImageFilter.EDGE_ENHANCE))
            if d:    
                st.image(img.filter(ImageFilter.EMBOSS))
            if e:    
                st.image(img.filter(ImageFilter.SHARPEN))
            if f:    
                st.image(img.filter(ImageFilter.SMOOTH))
        with tab3:
            st.write('改色1')
            st.image(img_change(img,0,2,1))
            st.write('改色2')
            st.image(img_change(img,1,2,0))
            st.write('改色3')
            st.image(img_change(img,1,0,2))
        
def page_4():
    '''我的百宝箱'''
    tab1,tab2,tab3 = st.tabs(["智慧词典","中小学生诗词查询库","优秀作文选"])
    with tab1:
        st.write('智慧词典')
        with open('words_space.txt', 'r', encoding='utf-8') as f:
            words_list = f.read().split('\n')
        for i in range(len(words_list)):
            words_list[i] = words_list[i].split('#')
        words_dict = {}
        for i in words_list:
            words_dict[i[1]] = [int(i[0]), i[2]]
        with open('check_out_times.txt', 'r', encoding='utf-8') as f:
            times_list = f.read().split('\n')
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])
        word = st.text_input('请输入要查询的单词')
        if word in words_dict:
            st.write(words_dict[word])
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            with open('check_out_times.txt', 'w', encoding='utf-8') as f:
                message = ''
                for k, v in times_dict.items():
                    message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                f.write(message)
            st.write('查询次数：', times_dict[n])
        
    with tab2:
        with open('gushi_c.txt', 'r', encoding='utf-8') as f:
            gushi_list = f.read().split('\n\n')
        for i in range(len(gushi_list)):
            gushi_list[i] = gushi_list[i].split(' ')
        gushi_dict = {}
        sm = []
        sj = []
        for i in gushi_list:
            spl_g = i[1].split('。')
            gushi_dict[i[0]] = spl_g
            sm.append(i[0])
            sj.append(i[1].split("。"))
        g = st.text_input('请输入要查询的古诗(注：请输入完整的一句古诗，并去掉句末的‘。？！’,'
                          '例如：官船来往乱如麻，全仗你抬声价)')
        n = 0
        for i in sj:
            n += 1
            if g in i:
                g_index = sj.index(i) 
                n = g_index
        if n <= 172:
            st.write(sm[g_index])        
            
    with tab3:
        tab1,tab2,tab3,tab4,tab5 = st.tabs(["成长","亲情","自然","哲理","传承"])
        with tab1:
            with open('成长.txt', 'r', encoding='utf-8') as f:
                c = f.read()
                st.write(c)
        with tab2:
            with open('亲情.txt', 'r', encoding='utf-8') as f:
                q = f.read()
                st.write(q)
        with tab3:
            with open('自然.txt', 'r', encoding='utf-8') as f:
                z = f.read()
                st.write(z)
        with tab4:
            with open('哲理.txt', 'r', encoding='utf-8') as f:
                z_ = f.read()
                st.write(z_)
        with tab5:
            with open('传承.txt', 'r', encoding='utf-8') as f:
                c_ = f.read()
                st.write(c_)

    
def page_5():
    '''开心闯关'''
    a = 0
    b = 0
    one = st.radio(
    '把某种或某几种具体物质形态作为世界本原，这类学说属于',
    ['选项1', '选项2', '选项3', '选项4'],
    captions=['朴素唯物主义', '机械唯物主义', 
              '形而上学唯物主义', '庸俗唯物主义'])
    st.write("_____________________________________")
    if one == '选项1':
        a += 10
        b += 1
    elif one == '选项2':
        b += 1
    elif one == '选项3':
        b += 1
    elif one == '选项4':
        b += 1
    
    two = st.radio(
    '马克思主义哲学认为世界在本质上是',
    ['选项1', '选项2', '选项3', '选项4'],
    captions=['各种物质实体的总和', '多样性的物质统一', 
              '物质和精神的统一', '主体和客体的统一'])
    st.write("_____________________________________")
    if two == '选项1':
        b += 1
    elif two == '选项2':
        a += 10
        b += 1
    elif two == '选项3':
        b += 1
    elif two == '选项4':
        b += 1
    
    three = st.radio(
    '随着科学发展观的贯彻落实，许多地方政府开始在经济发展中引入绿色 GDP 概念，改变一味追求 GDP 数量的做法，在追求 GDP 数量的同时提升 GDP 的质量。最大限度的减少资源消耗和环境污染。地方政府对 GDP 的认识转变体现了',
    ['选项1', '选项2', '选项3', '选项4'],
    captions=['矛盾的对立统一', '.辩证的否定观', 
              '量变导致质变', '矛盾的普遍性'])
    st.write("_____________________________________")
    if three == '选项1':
        b += 1
    elif three == '选项2':
        a += 10
        b += 1
    elif three == '选项3':
        b += 1
    elif three == '选项4':
        b += 1
    
    four = st.radio(
    '党的十九届六中全会通过了《中共中央关于党的百年奋斗_____ 和_____ 的决议》',
    ['选项1', '选项2', '选项3', '选项4'],
    captions=['重大改革；发展经验', '重大规划；指导经验', 
              '重大成就；历史经验', '领导成就；远景规划'])
    st.write("_____________________________________")
    if four == '选项1':
        b += 1
    elif four == '选项2':
        b += 1
    elif four == '选项3':
        a += 10
        b += 1
    elif four == '选项4':
        b += 1
    
    five = st.radio(
    '（  ）年，在杭州皮市巷3号，建立了浙江最早的团组织——杭州社会主义青年团',
    ['选项1', '选项2', '选项3', '选项4'],
    captions=['1921', '1922', '1923', '1924'])
    st.write("_____________________________________")
    if five == '选项1':
        b += 1
    elif five == '选项2':
        a += 10
        b += 1
    elif five == '选项3':
        b += 1
    elif five == '选项4':
        b += 1
    
    six = st.radio(
    '___是马克思主义的本质属性，党的理论是来自人民、为了人民、造福人民的理论，人民的创造性实践是理论创新的不竭源泉',
    ['选项1', '选项2', '选项3', '选项4'],
    captions=['人民性', '实践性', '革命性', '现实性'])
    st.write("_____________________________________")
    if six == '选项1':
        a += 10
        b += 1
    elif six == '选项2':
        b += 1
    elif six == '选项3':
        b += 1
    elif six == '选项4':
        b += 1
    
    seven = st.radio(
    '一带一路的全称是_____',
    ['选项1', '选项2', '选项3', '选项4'],
    captions=['“海上丝绸之路经济带”和“21 世纪丝绸之路”', 
              '“海上丝绸之路经济带”和“21 世纪丝绸之路”', 
              '“海上丝绸之路经济带”和“21 世纪丝绸之路经济带”', 
              '“丝绸之路经济带”和“21 世纪海上丝绸之路”'])
    st.write("_____________________________________")
    if seven == '选项1':
        b += 1
    elif seven == '选项2':
        b += 1
    elif seven == '选项3':
        b += 1
    elif seven == '选项4':
        a += 10
        b += 1
    
    eight = st.radio(
    '天津某村庄，在生产经营中既把主要力量放到工业上，又正确地处理了工业和农业的关系，以工业收入补贴农业，实现了改土治碱，促进了农业机械化。农业机械化的发展，又把劳力从农业解放出来,转入工业,促进了工业的发展。这一事例,从唯物辩证法看来是(）',
    ['选项1', '选项2', '选项3', '选项4'],
    captions=['主要矛盾的解决带动次要矛盾的解决，次要矛盾的解决又有利于主要矛盾的解决', 
              '主要矛盾和次要矛盾相互联系、相互斗争', 
              '矛盾发展不平衡，各种矛盾所处的地位不一样', 
              '主要矛盾和次要矛盾在一定条件下可以相五转化'])
    st.write("_____________________________________")
    if eight == '选项1':
        a += 10
        b += 1
    elif eight == '选项2':
        b += 1
    elif eight == '选项3':
        b += 1
    elif eight == '选项4':
        b += 1
    
    nine = st.radio(
    '对待马克思主义，以下哪种态度是不正确的？',
    ['选项1', '选项2', '选项3', '选项4'],
    captions=['.科学的态度 ', '教条的态度 ', '实事求是的态度 ', '马克思主义的态度'])
    st.write("_____________________________________")
    if nine == '选项1':
        b += 1
    elif nine == '选项2':
        a += 10
        b += 1
    elif nine == '选项3':
        b += 1
    elif nine == '选项4':
        b += 1
    
    ten = st.radio(
    '中国共产主义青年团团歌的作词者是（   ）',
    ['选项1', '选项2', '选项3', '选项4'],
    captions=['聂耳', '雷雨声', '田汉', '胡宏伟'])
    st.write("_____________________________________")
    if ten == '选项1':
        b += 1
    elif ten == '选项2':
        b += 1
    elif ten == '选项3':
        b += 1
    elif ten == '选项4':
        a += 10
        b += 1

    if b >= 10:
        if a < 60:
            st.write("阿欧！争取下次及格哦！")
        if a >= 60 and a < 80:
            st.write("恭喜你获得",a,'分',"不错！继续加油哦！")
        if a >= 80 and a <= 100:
            st.write("恭喜你获得",a,'分',"你真棒！你已超过99%的玩家")

def page_6():
    st.write("快找找你想去的网站吧")

    st.link_button('淘宝', 'https://www.taobao.com/')
    st.link_button('抖音', 'https://www.douyin.com/')
    st.link_button('京东', 'https://www.jd.com/')
    st.link_button('必应', 'https://cn.bing.com/')
    st.link_button('酷狗', 'https://www.kugou.com/')
    st.link_button('微博', 'https://weibo.com/')
    st.link_button('1688', 'https://www.1688.com/')
    st.link_button('bilibili', 'https://www.bilibili.com/')
    st.link_button('爱奇艺', 'https://www.iqiyi.com/')
    st.link_button('网易云', 'https://music.163.com/')
    st.link_button('环球网', 'https://www.huanqiu.com/')
    st.link_button('唯品会', 'https://www.vip.com/')
    st.link_button('穷游网', 'https://www.qyer.com/')
    st.link_button('芒果TV', 'https://www.mgtv.com/')
    st.link_button('人民网', 'http://www.people.com.cn/')
    st.link_button('腾讯视频', 'https://v.qq.com/')
    st.link_button('百度贴吧', 'https://tieba.baidu.com/')
    st.link_button('环球军事', 'https://mil.huanqiu.com/')
    st.link_button('中国日报', 'https://www.chinadaily.com.cn/')
    st.link_button('番茄小说', 'https://fanqienovel.com/')
    st.link_button('百度首页', 'https://www.baidu.com/')
    
def page_7():
    '''想给今天打个分'''
    n = 0
    st.write("今日状态")
    st.checkbox("emo")
    st.checkbox("发呆")
    st.checkbox("勿扰")
    st.checkbox("闭关")
    st.checkbox("摸鱼")
    st.checkbox("吸奶茶")
    st.checkbox("微笑")
    st.checkbox("宅")
    st.checkbox("surprised")
    st.checkbox("晴天")
    fen = st.text_input('满分100，我想给今天的我打分……')
    k = ":red[记得先打分才能收获我的祝福哦]"
    st.write(k)
    if st.button('小祝福'):
        if int(fen) < 60 and int(fen) >= 0:
            st.write("不要气馁哦！继续加油，相信自己，希望你开心每一天")
        if int(fen) >= 60 and int(fen) < 90:
            st.write("不错呦！继续努力吧，希望你每天都元气满满")
        if int(fen) >= 90 and int(fen) <=100:
            st.write("太棒啦！明天一定要继续保持，我每天都会给你送上我的祝福哦！")
            
    
def page_8():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        message_list = f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split('#')
    for i in message_list:
        if i[1] == '阿短':
            with st.chat_message('☔'):
                st.write(i[1], ':', i[2])
        elif i[1] == '编程猫':
            with st.chat_message('✨'):
                st.write(i[1], ":", i[2])
        elif i[1] == 'sym':
            with st.chat_message('☕'):
                st.write(i[1], ":", i[2])
    name = st.selectbox('我是……',['阿短', '编程猫', 'sym'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1), name, new_message])
        with open('leave_massages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in message_list:
                message += i[0] + '#' + i[1] +'#' + i[2] + '\n'
            message = message[:-1] 
            f.write(message)
        for i in range(3):
            st.balloons()
    
def img_change(img, rc, gc, bc):
    '''图片处理'''
    # 改色
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)  
    return img

if page == 'Hello here!':
    page_1()
elif page == '兴趣推荐':
    page_2()
elif page == '修图神器':
    page_3()
elif page == '百宝箱':
    page_4()
elif page == '开心闯关':
    page_5() 
elif page == '网站漫步':
    page_6() 
elif page == '想给今天打个分':
    page_7()  
elif page == '留个言吧':
    page_8() 