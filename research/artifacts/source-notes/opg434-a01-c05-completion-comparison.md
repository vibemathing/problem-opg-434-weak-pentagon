# c05 — 补全构造的来源与陈述比较

verdict: candidate_only；检索日期：2026-09-06。

## 复用检索
查询包含 regular supergraph odd girth、two copies maximum degree triangle free、
cubic completion homomorphism Clebsch。

University of Regina, Math Central, “A bipartite graph”：
https://mathcentral.uregina.ca/QQ/database/QQ.09.12/h/student1.html
搜索结果给出署名 Claude 的答复：复制两份图并连接相应缺度顶点，
用于把二分图扩充为同一最大度的正则二分图。
直接打开该页返回 Cache miss，所以本次只记录搜索摘录命中，
不声称完整页面核验。关系为 weaker：该摘录针对二分图，
未给出本稿的一般奇围长等式或固定五色赋值延拓。
本文提供自包含证明，不以该答复作为缺失步骤的替代。

## 普通围长与奇围长
DeVos–Šámal, “High-girth cubic graphs are homomorphic to the Clebsch graph”：
https://arxiv.org/abs/math/0602580
https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.20580
2011年期刊摘要明确使用最大度3及 girth 至少17；不是 odd girth 至少17。
本轮搜索可读取摘要，Wiley 直接打开返回403。早先 c02 已记录 arXiv v2
文本定位及截图失败；本轮没有重新声称对全文或其计算部分做了验证。

c05 对 C17 的补全含4圈而保留奇围长17，精确阻止把普通围长定理
经过此补全误用到仅有奇围长条件的图上。不是对文献定理的反例。

## 状态边界
本稿只比较定义域和显式变换，不执行补全程序，不搜索不存在的 witness，
也不把搜索命中视为 Result 或新颖性审计。
