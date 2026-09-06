# c02 — 割补集、同态及来源访问记录

verdict: candidate_only；访问日期：2026-09-06。

## 原始来源和定位

DeVos–Šámal, arXiv:math/0602580v2 (2009-10-23)：
https://arxiv.org/abs/math/0602580
https://arxiv.org/pdf/math/0602580

摘要页列出版本历史；PDF 首行标识 v2。PDF 印刷页2定义完整割及割补集；
页11的 Proposition 3.2 给出四个不交割补集、五个割补集分拆、
PQ4 同态、到 C5 的 cut-continuous edge map 的存在性等价；
页11的 Observation 3.1 识别二进制模型。页12续证。

本次 PDF 文本读取成功，页11/12截图请求返回 Cache miss，故不声称完成
该 PDF 的视觉复核。仅使用可解析的定义与文字公式，不使用图示数据。
c01 保存的 arxiv.org/html/math/0602580v2 地址在本次重读返回 Cache miss；
上述摘要/PDF定位是可重读的替代入口，并不改变 c01 数学推导。

Robert Šámal 的原始问题页：
https://www.openproblemgarden.org/op/weak_pentagon_problem
首个 Conjecture 与后面的 Proposition 是原赋值条件与存在性同态重述，
不是断言每个给定合法赋值已经 cut-continuous。

## 精确差异

合同颜色类：删去后为二分图的一般奇圈边横截集。
论文 Proposition 3.2 的起点：完整割的补集。
c02 第3节给出“横截集包含割补集”；第4节给出保持可行性但可改变颜色
的正规化。因此存在性等价不意味着对原颜色类逐项相等。

c02 第2节是显式14顶点三正则见证，说明原色1在某7-圈出现两次，
所以对应剩余5条圈边不可能是割的限制。其用途是排除错误强化，
不是声称合同图类中存在不可着色图。

c02 的四位局部证书具体写出距离条件和逆向着色，避免只引用
“Clebsch graph”名称而隐去图模型或依赖。
本次未执行论文中的 C 程序；也未重验其高围长定理。
