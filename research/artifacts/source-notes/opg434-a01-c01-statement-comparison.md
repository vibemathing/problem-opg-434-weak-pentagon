# OPG434 c01 — 精确陈述比较

verdict: `candidate_only`
读取日期：2026-09-06。只保存书目信息、短摘要和数学定义比较；
不保存完整网页、论文、检索噪声或聊天。

## 已检查的仓库来源

基线 `aa9fc64c4e7b9c9d841f2a53c480169038b18bdf`：
`problem-library/records/canonical-problems.jsonl` 明确是任意五色边赋值；
`research/records/failed-routes.jsonl` 为空；
`research/records/attempts.jsonl` 和 `research/records/obligation-graphs.jsonl`
绑定本次 Attempt/Route/Graph/target。知识源 registry 的数学软件来源
没有提供本轮可执行的图论 verifier；来源命中不视为数学验收。

## S1：原始问题页

Robert Šámal, “Weak pentagon problem”, Open Problem Garden，
页面标注 2007-07-13：
https://www.openproblemgarden.org/op/weak_pentagon_problem

定位：首个 Conjecture；随后 reformulations 和 Proposition。
比较：其五色删除条件与合同一致。本文仅把该条件拆为奇圈击中条件，
不宣称解决图类上的存在性。页面也列出 Clebsch 同态和 cut-continuous
表述，不能把这些名称当成对给定颜色类逐项相等的证明。
页面解释 cut 时应采用精确定义 \(\delta(U)\)：U 与补集之间的全部边。
任意生成二分子图的边集只一定包含于某个 cut，不一定自身是 cut。

## S2：固定版本的一手论文

Matt DeVos and Robert Šámal, “High-girth cubic graphs are homomorphic to
the Clebsch graph”, arXiv:math/0602580v2，2009-10-23：
https://arxiv.org/html/math/0602580v2

定位：Abstract；Propositions 1.1/3.2；Theorem 1.3；
Conjectures 1.4/1.6；Section 3。
Abstract 明示边着色可 “possibly improperly”。
Theorem 1.3 的图类是最大度至多 3、girth 至少 17，不能覆盖合同全部
无三角形三正则图。Conjecture 1.4 使用 Clebsch 同态表述。
Proposition 3.2 使用精确的 cut complements：
\(S=E\setminus\delta(U)\)。
本轮等价引理允许一般奇圈边横截集，故从本文到该命题需要正规化，
不能直接假定每个原颜色类就是 cut complement。

## S3：edge transversal 术语

Petr Kolman, Bernard Lidický, Jean-Sébastien Sereni,
“On Minimum Fair Odd Cycle Transversal”，KAM report s956：
https://kam.mff.cuni.cz/kamserie/clanky/2010/s956.pdf

定位：印刷页 2 的 OCT 定义（已检查该页渲染）。
该文明确 \(F\subseteq E\) 且 \((V,E\setminus F)\) 二分；与本文的边版本
相同。它优化单个横截集的局部度，不证明五个不交横截集的存在性。
检索中也出现删顶点的 OCT 文献，未将其混入本目标。

## S4：另一个 Pentagon 问题

Jaroslav Nešetřil 的 “Pentagon problem”，Open Problem Garden，
页面标注 2007-03-24：
https://www.openproblemgarden.org/?q=node/167

与 S2 Conjecture 1.6 交叉核对：它要求充分大 girth 的三正则图同态到 C5。
它不是“无三角形”假设，也不是 proper 五边着色。
C5 同态在同一给定图上可推出弱五边形条件；这里不把两个不同图类上的
全称猜想写成未经证明的等价关系。

## 检索与限度

查询包括 weak pentagon、odd cycle transversals partition、
pentagon conjecture Clebsch triangle free cubic。
没有进行完整现状或新颖性审计；论文日期固定不代表后续无进展。
本候选的基本等价证明是显式有限图推导，引用用于归属和术语核对，
并不替代 verifier receipt。
