from pyecharts import options as opts
from pyecharts.charts import Bar

# bar = Bar()
#
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家",[5, 20, 36, 10, 75, 90])
# '''
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
# '''
# bar.render("bar.html")

# pyecharts 所有方法均支持链式调用。
# bar = (
#     Bar()
#         .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#         .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#         .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
#     # 或者直接使用字典参数
#     # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
# )
# bar.render("bar.html")

# 渲染成图片文件，这部分内容请参考

### https://user-images.githubusercontent.com/19553554/57307650-8a4d0280-7117-11e9-921f-69b8e9c5e4aa.png