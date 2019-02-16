const config = {
  encoding: "gbk",
  max_number: 20, // 每个时间节点最多显示的条目数。
  showMessage: true, // 控制是否显示顶部附加信息文字。

  // !!!请确保打开此项时，使用的是标准日期格式！!!(即：YYYY-MM-DD HH:MM)
  // 如果关闭，排序顺序为csv表格的时间字段自上而下的出现顺序。
  // 如果你的日期格式为标准的日期格式，则可以无视数据排序，达到自动按照日期顺序排序的效果。
  auto_sort: false, // 时间自动排序。开启auto_sort可以实现时间的自动补间。
  timeFormat: "%Y-%m-%d",
  reverse: false, // 倒序，使得最短的条位于最上方

  // 类型根据什么字段区分？如果是name，则关闭类型显示
  divide_by: "type",

  // 颜色根据什么字段区分？
  divide_color_by: "type",
  // 字段的值与其对应的颜色值
  color: {
    '魔法师': "#17C",
  },

  changeable_color: false, // 颜色绑定增长率

  // 附加信息内容。
  itemLabel: "左侧文字",
  typeLabel: "右侧文字",
  item_x: 250, // 榜首项目信息的水平位置 。
  text_y: -50, // 上方文字水平高度。
  text_x: 1200, // 右侧文字横坐标
  offset: 250, // 偏移量


  display_barInfo: 0, // 长度小于display_barInfo的bar将不显示barInfo。
  interval_time: 0.5, // 时间点间隔时间。
  // 注意！使用计时器和使用类型目前不能兼容，即不能同时开启！
  use_counter: true, // 使用计数器，计数器会出现在右上角，记录着当前榜首的持续时间。
  step: 1, // 每个时间节点对于计数器的步长。比如时间节点日期的间隔可能为1周（七天），那么step的值就应该为7。
  format: ".0f", // 格式化数值，这里控制着数值的显示位数。主要靠修改中间的数字完成，如果为1则为保留一位小数。

  labelx: -55, // label x轴位置
  show_x_tick: true, // 是否显示x轴轴线
  left_margin: 250, // 图表左右上下间距。
  right_margin: 150, // 注意，left_margin不包括左侧的label，修改数值较小会导致左侧label不显示
  top_margin: 180,
  bottom_margin: 0,

  dateLabel_switch: true, // 是否开启时间标签。
  dateLabel_x: null, // 时间标签坐标。建议x：1000 y：-50开始尝试，默认位置为x:null,y:null
  dateLabel_y: null,

  allow_up: false, // 允许大于平均值的条消失时上浮。
  enter_from_0: false, // 设置动画效果，如果为true，则新进入的条目从0开始。
  big_value: true, // 如果所有数字都很大，导致拉不开差距则开启此项使得坐标原点变换为（最小值）*2-（最大值）
  use_semilogarithmic_coordinate: false, // 如果要使用半对数坐标，则开启此项
  long: false, // barinfo太长？也许可以试试这个
  wait: 2, // 延迟多少个时间节点开始
  update_rate: 1, // 单独控制交换动画速度倍率

  // animation:'linear', // 开启匀速动画效果
  showLabel: true,
  use_img: true,
  // 图片路径，本地图片或者网上图片。
  imgs: {
    '张三': 'http://i1.hdslb.com/bfs/face/983034448f81f45f05956d0455a86fe0639d6a36.jpg',
    '李四': 'http://i1.hdslb.com/bfs/face/983034448f81f45f05956d0455a86fe0639d6a36.jpg',
    '王二麻子': 'http://i1.hdslb.com/bfs/face/983034448f81f45f05956d0455a86fe0639d6a36.jpg',
  },
  background_color: "#FFF", // 全局背景颜色
  rounded_rectangle: true // 矩形柱是否为圆角矩形
};