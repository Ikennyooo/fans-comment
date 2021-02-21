import requests
from flask import Flask, render_template
import time
from pyecharts import options as opts
from pyecharts.charts import Bar

app = Flask(__name__)


@app.route("/")
def index():
    shi = []
    shu = []
    shi_warma = []
    shu_warma = []
    for i in range (0,10):
        uid = "699438"
        name = "枯水"
        url = "https://api.bilibili.com/x/relation/stat?vmid=" + uid + "&jsonp=jsonp"
        resp = requests.get(url)   # 通过url爬取到我们想要的json数据
        info = eval(resp.text)
        fensi = info["data"]["follower"]
        shi.append(str(time.strftime("%M:%S")))
        shu.append(fensi)
        time.sleep(1)
    for i in range (0,10):
        uid = "53456"
        name = "沃玛"
        url = "https://api.bilibili.com/x/relation/stat?vmid=" + uid + "&jsonp=jsonp"
        resp_warma = requests.get(url)   # 通过url爬取到我们想要的json数据
        info_warma = eval(resp_warma.text)
        fensi_warma = info_warma["data"]["follower"]
        shi_warma.append(str(time.strftime("%M:%S")))
        shu_warma.append(fensi_warma)
        time.sleep(1)
    bar = (
        Bar()
            .add_xaxis([shi[0], shi[1], shi[2], shi[3], shi[4], shi[5], shi[6], shi[7], shi[8], shi[9]])
            .add_yaxis("枯水", [shu[0], shu[1], shu[2], shu[3], shu[4], shu[5], shu[6], shu[7], shu[8], shu[9]])
            .add_yaxis("Warma", [shu_warma[0], shu_warma[1], shu_warma[2], shu_warma[3], shu_warma[4], shu_warma[5], shu_warma[6], shu_warma[7], shu_warma[8], shu_warma[9]])

            .set_global_opts(title_opts=opts.TitleOpts(title="Bilibili干杯！", subtitle="粉丝数"))
    )
    return render_template("枯水沃玛粉丝可视化.html", shi=shi, shu=shu, bar_options=bar.dump_options())

if __name__ == '__main__':
    app.run()