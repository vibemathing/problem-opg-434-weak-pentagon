# 固定着色证书与存在性编码 — Candidate c03

- candidate_id: `candidate:opg434-a01-c03-certificates`
- problem_id: `problem:opg-434-weak-pentagon`
- attempt_id: `attempt:web-20260906-opg434-a01`
- route_id: `route:odd-cycle-transversal-equivalence-v1`
- graph_id: `graph:opg434-initial-v1`
- obligation_id: `obligation:opg434-five-transversals-equivalence`
- primary_owner: `math-derivation`; verdict: `candidate_only`
- base_revision: `3f43a8cfbd895f55be52d2219c25727a93c9e154`

这是逻辑编码及算法正确性的纸面候选，不是 SAT、BFS 或内核运行结果。
依赖 c01 的等价引理与 c02 的正规化/四位标号构造；不新增真相记录。

## 1. 输入及两个不同量词层

输入为有限简单图 G=(V,E)，n=|V|、m=|E|。顶点、无向边有固定顺序。
若作为原题实例，还须另验无三角形及三正则；以下等价对一般有限简单图成立。

固定着色问题输入还含函数 c:E->[5]，询问此 c 是否合法。
存在性问题只输入 G，询问是否存在合法 c。
无效输入（自环、重边、越界颜色等）须报告输入错误，不是数学反例。
空颜色类、同色相邻边、孤立点不能因定义外的要求被拒绝。

## 2. claim:opg434-c03-fixed-certificates

固定 c 的正证书是五个函数 \(b_i:V\to\{0,1\}\)，满足
\[
 \forall e=uv\in E,\ \forall i\in[5],\
 c(e)\ne i\Longrightarrow b_i(u)\ne b_i(v).
\]
逐边逐色检查即可。条件说每个 b_i 是 H_i=(V,{e:c(e)!=i}) 的二着色，
故它充分；若 c 合法，分别取五个 H_i 的二分便说明它必要。
证书只需5n个位值，检查在输入已校验且按邻接表给定时为 O(5(n+m))。

负证书是颜色 i 与顶点序列 \(v_0,\ldots,v_{\ell-1}\)，其中
\(\ell\ge3\) 为奇数，顶点互异，首尾相接的每条边在 G 中且颜色均不是 i。
c01 保证它恰见证 H_i 非二分。此证书只否定给定 c。

### 确定性生成方法及正确性

按 i=1,...,5，在 H_i 的各连通分量按固定顺序选根，广度优先建立生成树，
给顶点标记树深度模2。若所有边都连接异色顶点，输出该 b_i。
若某边 uv 两端同色，则 uv 不是树边；取树中 u 到 v 的唯一路径加 uv。
树路径长度为
depth(u)+depth(v)-2depth(LCA(u,v))，故为偶数；
路径无重复顶点，与 uv 构成所需奇圈，且所有边都在 H_i 中。
若五轮均无冲突，则输出五个 b_i。每轮只扫描该有限图一次；
出现冲突时只需沿父指针恢复一次路径。
这是算法证明，没有保存任何虚构的实例运行日志。

## 3. claim:opg434-c03-faithful-cnf

用布尔变量 y_{e,i} 表示 e 取色 i，用 x_{v,i} 表示二分位 b_i(v)。
每条边 e 加入以下子句，所有子句合取：

(A) 至少一个颜色：\(\bigvee_{i=1}^5 y_{e,i}\)。

(B) 至多一个颜色：对1<=i<j<=5，\(\neg y_{e,i}\vee\neg y_{e,j}\)。

(C) 对 e=uv 及每个 i，加入
\[
 y_{e,i}\vee x_{u,i}\vee x_{v,i},\qquad
 y_{e,i}\vee\neg x_{u,i}\vee\neg x_{v,i}.
\]
(C) 在 y_{e,i}=false 时恰要求两个端点位不同；在其为 true 时没有限制。
所以 (A)(B) 唯一确定 c，(C) 恰给出第2节的正证书。
反向由任意合法 c 及其五个二分直接赋值 x,y，满足全部子句。
因此该公式可满足，当且仅当 G 存在合同意义的五色赋值。

变量数5m+5n；每条边的子句数1+10+10=21，共21m条。
没有给颜色类加非空约束，没有给相邻边加不同色约束。
把 y 固定为给定 c 时，该公式就精确检查此 c；不固定 y 时才能解释为搜索。

## 4. claim:opg434-c03-four-bit-cnf

存在性还可用 c02 的四位顶点变量 z_{v,j}，j=1,...,4。
每条边增加四个变量 d_{e,j}，令其等价于 z_{u,j} XOR z_{v,j}。
对 x=z_{u,j}, z=z_{v,j}, d=d_{e,j}，等价关系的四条子句是
\[
 (\neg x\vee\neg z\vee\neg d),\quad
 (x\vee z\vee\neg d),\quad
 (x\vee\neg z\vee d),\quad
 (\neg x\vee z\vee d).
\]
x=z 时前两条强制 d=0，x!=z 时后两条之一强制 d=1；
另一些子句在相应赋值中自动成立，故这四条恰好表达 XOR。

再对每条边和1<=j<k<=4加入 \((d_{e,j}\vee d_{e,k})\)。
六条子句禁止任何两个差异位同时为0，等价于至少三位为1，
即端点汉明距离3或4。由 c02，该公式的可满足性与存在合法 c 等价。
变量数4n+4m；子句数每边4*4+6=22，共22m。
这是变量更少而子句略多的精确编码，不是运行性能结论。

## 5. 对“固定 c 只验前四色”的明确攻击

取5-棱柱，顶点 a_j,b_j（j模5），边为两层5-圈及 a_jb_j。
该图简单、三正则、无三角形：一个三角形的换层步数为0或2；
前者不能在5-圈中形成，后者只剩一步水平移动，不能回到原索引。

令 q(a_j)=j，q(b_j)=j+1，映到 C5。
给 C5 的顺序边赋色 (1,2,3,4,1)，再拉回棱柱。
对 i=1,...,4，删色后的 C5 为森林，所以相应 H_i 都二分；
色5不存在，H_5=G 保留5-圈，故原 c 不合法。
这说明省略第五项会错误验收一个固定输入，尽管前四色的二分能被
c02 转化为这个图的另一个合法着色。两个量词层不能混用。
这不是原题的反例，也不否定第4节存在性编码。

## 6. 最便宜的编码审计与未来复现

逐个手工检查 (C) 的三类：y=true；y=false且端点同位；y=false且异位。
分别检查 XOR 的四种端点组合；检查差异向量有0、1、2、3、4个1时
六条“至少三位”子句的语义。以上是推导的有限分类，不是程序输出。

完整计算复现需由获准 runtime 记录输入图和颜色的摘要、编码器摘要、
实际工具版本、命令、资源限额和原始退出/输出摘要。
正 SAT 返回值应解码为5n位或4n位证书并用另一个小检查器逐边验收。
负 SAT 返回值需要可重放的不可满足证书及其检查；仅有 UNSAT 文本不够。
若目标是反例，还须证明输入图属于合同图类，且公式表达的是存在性，
而不是只否定某一次着色。当前没有发起或伪造这些执行。

引用的仓库推导：
`research/artifacts/candidates/opg434-a01-c01-equivalence.md`；
`research/artifacts/candidates/opg434-a01-c02-normalization.md`。
两者是候选依赖，不是已验收定理。本文件同样需要 kernel_check、
axiom_escape_audit 和 statement_faithfulness；目标与 root 均保持开放。
下一步：给出可移植的形式化接口，并把图模型忠实性与纯逻辑推导分开审计。
