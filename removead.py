# encoding: UTF-8

import re
import codecs

file1 = open('old.txt')
file2 = codecs.open('new.txt', 'w', 'utf-8')

p0 = re.compile(u'广告①([\w\W\u4e00-\u9fff]+)')
p1 = re.compile(u'开心([\u4e00-\u9fa5])就好([\u4e00-\u9fa5])手打')
p2 = re.compile(u'开([\u4e00-\u9fa5])心([\u4e00-\u9fa5])就([\u4e00-\u9fa5])好([\u4e00-\u9fa5])手([\u4e00-\u9fa5])打')
p3 = re.compile(u'开心就好手打')
p4 = re.compile(u'欢迎您来，欢迎您再来，记住我们([\w\W\u4e00-\u9fff]+)')
p5 = re.compile(u'飞库手打')


def func1(m):
    return m.group(1) + m.group(2)


def func2(m):
    return m.group(1) + m.group(2) + m.group(3) + m.group(4) + m.group(5)


for line in open('old.txt', 'r'):
    line = file1.readline()
    pureLine = p0.sub("", line.decode('utf-8'))
    pureLine = p3.sub("", pureLine)
    pureLine = p1.sub(func1, pureLine)
    pureLine = p2.sub(func2, pureLine)
    pureLine = p4.sub("", pureLine)
    pureLine = p5.sub("", pureLine)
    file2.write(pureLine)

file1.close()
file2.close()

# p0 = re.compile(u'广告①([\w\W\u4e00-\u9fff]+)')
# p1 = re.compile(u'开心([\u4e00-\u9fa5])就好([\u4e00-\u9fa5])手打')
# p2 = re.compile(u'开([\u4e00-\u9fa5])心([\u4e00-\u9fa5])就([\u4e00-\u9fa5])好([\u4e00-\u9fa5])手([\u4e00-\u9fa5])打')
# p3 = re.compile(u'开心就好手打')
#
# content = u'''
# 广告①[SOHU广告]广告②[百度广告]广告③[智源广告]广告④[阿里广告]广告⑤[Google广告]正文第171章【男人的“天堂”】（上）
# “美洲的毒品开心市就好场手打一直很稳定……但是这次，美妙的天气给了我们一个很好的机会……南美的毒品种植园在这次连续的飓风气候中损夫惨重……现在的问题是，今年的产量肯定无法满足市场的需求！我收到的消息是，尽管开地心狱就天好使手已打经竭尽全力调动货源……但是别忘记了，加拿大下面还有一个美国……美国的黑手党和几大家族，他们也要蚕食掉一部分货源。原本就并不充足的货源。地狱天使还要和美国的黑道瓜分，得到的那份额就更少的！”
# “陈阳。这几个月我也没闲着，你在国内的底子，我已经让方胖子给我了。你在国内的那些恩怨，我很了解……我说句难听点的话。这事情，我交给组织内其他的那些老兄弟，我不放心！因为他们大多对这件事情抱有成见！如果我交给新人，我不放心！我们大圈现在内部的新一代的兄弟，都是本地人出生的，对国内已经没有太多的概念。开心就好手打我本人还是倾向于相信国内来的兄弟。这只是算是我的私人感情倾向。你是我暂时定的助手人选……你放心，我不会一下子放权给你……我没那么大胆！但是如果你能让我满意的话，我保证你会在这里得到你想要的一切！我们和本地的传统华人帮会不同，我们是二十年前登录来到北美，靠着热血和手里的枪。硬是打出了一片天地！我们不像那些流传的帮会，讲究资历……在我这里，只要你是自己人，只要你有本事，我就保证你能出位！”他缓缓的吸了口烟，看着我，笑了笑：“前提是，你能话下去！”
# “我们大圈大多数都是偷渡来的，当初为了压制我们的发展，这些本地的帮会就常常以什么宗亲会，同乡会，华商会之类的组织形势。向政府，向警方，抗议偷渡的情况，要求警方大力打压偷渡现象……”八爷笑道：“最他妈让我可笑的是，这些家伙还发表过一些声明，抗议中国政府对于偷渡行为的不作为，他们甚至要求中国政府加大对国内偷渡到北美的行为的打击……其实，这些都是为了压制我们大圈！因为在最开始，他们曾经和我们狠狠的干过。被我们干得很惨，所以他们怕了！这些家伙的作为让我很无奈……同样是中国人，我并不想和他们为敌。他们说偷渡……嘿！你去唐人街随便看着，很多华裔。他们的第一代，开心就好手打绝大多数都是被卖猪仔卖到北美来的！之后的，他们的上几代，有多少也是偷渡的！！真正合法来到加拿大定居的，移民的，很少很少……大部分合法移民来的，谁会出来混黑道啊！现在他们在这扎下根了，不用偷渡了，或者说是对偷渡的依赖不大了，为了打压我们这些新偷渡来的。就发表抗议，甚至帮着北美政府一起抗议国内的政府……关于M国的那个什么狗屁人权议案，里面就有攻击国内政府对于偷渡犯罪的打击力度不够，上面就有很多本地传统华人帮会的签名！！这帮孙子！”
# '''
#
# search0 = p0.search(content)
# search1 = p1.search(content)
# search2 = p2.search(content)
# search3 = p3.search(content)
# if search0:
#     print "match0:" + search0.group()
# elif search1:
#     print "match1:" + search1.group()
# elif search2:
#     print "match2:" + search2.group()
# elif search3:
#     print "match3:" + search3.group()
