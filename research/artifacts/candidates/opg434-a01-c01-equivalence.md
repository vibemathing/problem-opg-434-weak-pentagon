# 五个奇圈边横截集的等价重述 — Candidate c01

- candidate_id: `candidate:opg434-a01-c01-equivalence`
- problem_id: `problem:opg-434-weak-pentagon`
- attempt_id: `attempt:web-20260906-opg434-a01`
- route_id: `route:odd-cycle-transversal-equivalence-v1`
- graph_id: `graph:opg434-initial-v1`
- obligation_id: `obligation:opg434-five-transversals-equivalence`
- obligation statement SHA-256: `6a6d7d3eca9ac315d45b701fdb8d157af65896a0c83ac046d2466184f4268a99`
- primary_owner: `math-derivation`; verdict: `candidate_only`
- 本文是可复核的纸面推导，不是 verifier receipt。未运行数学程序或形式化内核。

## 1. 冻结对象与量词

合同对象为有限简单无三角形三正则图。颜色赋值是任意函数
\(c:E(G)\to[5]=\{1,2,3,4,5\}\)，不要求 proper，也不要求满射。
原题量词为 \(\forall G\,\exists c\,\forall i\in[5]\)。

本引理先固定任意有限简单图 \(G=(V,E)\) 及任意这样的 c，证明
\[
 \forall i\in[5]\quad
 (V,E\setminus F_i)\text{ 为二分图}
 \ \Longleftrightarrow\
 \forall\text{ 奇圈 }C\subseteq G,\ E(C)\cap F_i\ne\varnothing,
 \qquad F_i=c^{-1}(i).
\]
这里“圈”是无重复顶点的简单圈，“删除”只删除边，始终保留 V；
不是删顶点，也不是取图补图。边横截集是与每个奇圈的边集相交的集合。
允许公理/背景：finite-graph-basic、finite-combinatorics。

“分拆”在此指有标号的两两不交五元组，其并为 E，允许空项。
普通集合论中要求每块非空的 partition，应表述为删去空项后的分拆，
不能偷换成恰有五个非空块。

## 2. 原子推导

### claim:opg434-c01-bipartite-criterion
有限图 H 为二分图，当且仅当 H 没有奇圈。

二分图的任一圈交替经过两个部，故长度为偶数。反向，在 H 的每个
连通分量选一棵有根生成树，按树上到根的距离奇偶给顶点二着色。
若一条边连接同色顶点，树中两端间的唯一路径长为偶数；该边不是树边，
它与树路径组成奇圈，矛盾。因此每条边异色。孤立点单独分部即可。

### claim:opg434-c01-cycle-transfer
对固定 i，H_i=(V,E\setminus F_i) 的奇圈恰是 G 中避开 F_i 的奇圈。

H_i 的一条简单圈使用的顶点、边均在 G 中，且所有边不属于 F_i，
所以同一顶点序列在 G 中仍是相同长度的简单圈。反向，若 G 中简单圈
C 的边都避开 F_i，则这些边都保留在 H_i 中，所有顶点也保留，
所以相同顶点序列仍在 H_i 中构成圈。两方向都保留长度，故保留奇偶性。

### claim:opg434-c01-equivalence
若 H_i 二分，则由二分图判据 H_i 无奇圈。若 G 有奇圈避开 F_i，
圈对应引理会将它保留在 H_i 中，矛盾；故 F_i 击中 G 的每个奇圈。

反之，若 F_i 击中 G 的每个奇圈，而 H_i 有奇圈，圈对应引理将它视为
G 中避开 F_i 的奇圈，矛盾。因此 H_i 无奇圈，再由二分图判据 H_i 二分。
i 任意，故同时适用于五种颜色。三正则和无三角形均未用于本等价引理。

### claim:opg434-c01-labelled-partition
每条边被 c 赋予唯一颜色，故 \(E=F_1\mathbin{\dot\cup}\cdots
\mathbin{\dot\cup}F_5\)。结合上一引理，每个 F_i 都是奇圈边横截集。

反向，给定并为 E 的两两不交有标号五元组 (F_1,...,F_5)，且每项击中
所有奇圈，以边所属的唯一项定义 c。上述等价引理给出每个 H_i 二分。
因此原题等价于在其指定图类上普遍存在这样的五元组；本文没有给出
该普遍存在性。若 G 二分，空集也满足横截条件。

## 3. 直接推论及适用范围

### claim:opg434-c01-rainbow-five
合法赋值下，每个奇圈都含全部五色。若 C 长为 5，其五条边已须分别
提供五色，因此五色各恰出现一次。更一般地，存在奇圈时最短奇圈长度
至少为 5；三角形不可能满足该条件。在合同图类中，这只是必要条件。

一个非二分连通分量包含奇圈，因而在该分量内每个颜色类都非空。
二分分量则不存在这样的非空要求。任意合法赋值在每个 5-圈上 proper，
不能由此推出全图的赋值 proper。

## 4. 最便宜的反驳测试与修订

**空颜色类/不 proper 测试。** 在 K_{3,3} 上把所有边赋色 1。
删除色 1 得到无边生成子图；删除任意其他颜色得到原二分图。
这是真正位于合同图类内的合法赋值，但四个颜色类为空，且相邻边同色。
因此任何附加“满射”“每类非空”或“颜色类是匹配”的版本均不等价于
合同对固定赋值的条件。已将分拆约定明确写入第 1 节。

**只检查 5-圈及 proper 着色的失败见证。** 设
\(V=\{a_j,b_j:j\in\mathbb Z/7\mathbb Z\}\)，边为
\(a_ja_{j+1}, b_jb_{j+1}, a_jb_j\)。
这是有限简单三正则图。在任何闭合游走中，改变 a/b 层的边数为偶数。
若它是长度 3 或 5 的圈，水平步数 r 为奇数且不超过 5；
水平步的带符号总和必须为 0 模 7，但它是绝对值不超过 5 的奇数，
不可能为 0 模 7。因此该图无三角形、无 5-圈，而含两个水平 7-圈。

给上下两圈的第 j 条边都赋序列
\((1,2,1,2,1,2,3)_j\)；a_0b_0 赋色 5，其余竖边赋色 4。
各顶点的两个水平边颜色不同，竖边颜色又不同于它们；故赋值 proper，
且五色都用到。但删色 5 保留完整的 a 层 7-圈，生成子图非二分。
“所有 5-圈五色各一次”在此真空成立。因此该局部检查和 properness，
即使合用，也不能替代所有奇圈的条件。
这是对错误判定规则的见证，不是原题的反例。

**其他边界。** 无边图、森林、孤立点、非连通图均由逐分量判据覆盖。
一个长为 5 的圈赋五个不同颜色时，每次删除至少一条圈边，所得为路径；
若缺少某色，则删除该色保留奇圈。未以有限测试代替普遍推导。

## 5. 复核与下一义务

人工逐条检查：生成子图定义、圈对应的两个方向、两次二分图判据、
颜色函数与有标号分拆的互逆、K_{3,3} 边界和 7-棱柱见证。
来源及定义差异见
`research/artifacts/source-notes/opg434-a01-c01-statement-comparison.md`。

依赖图：bipartite-criterion + cycle-transfer -> equivalence ->
labelled-partition -> rainbow-five。它是本文内部的 claim 分解，
没有向仓库添加或关闭任何 Obligation。

下一步：审查“奇圈边横截集”与“cut complement”的区别，给出存在性
重述所需的显式正规化；随后申请对冻结文本的 kernel_check、
axiom_escape_audit、statement_faithfulness。当前目标和 root 在仓库中
都保持开放，best_verified_result=none。
