# 横截集正规化与四位证书 — Candidate c02

- candidate_id: `candidate:opg434-a01-c02-normalization`
- problem_id: `problem:opg-434-weak-pentagon`
- attempt_id: `attempt:web-20260906-opg434-a01`
- route_id: `route:odd-cycle-transversal-equivalence-v1`
- graph_id: `graph:opg434-initial-v1`
- obligation_id: `obligation:opg434-five-transversals-equivalence`
- primary_owner: `math-derivation`; verdict: `candidate_only`
- 基线：`5ca1f7011229855ba1681f33d9ec68e0dbba96f4`
- 这是 c01 的陈述忠实性细化；未运行数学程序或内核，没有关闭义务。

## 1. 固定定义、依赖与要排除的错误

G=(V,E) 是有限简单图；合同的额外限制是无三角形三正则。
\(\delta(U)=\{uv\in E:|\{u,v\}\cap U|=1\}\) 是 U 的完整割。
割补集是 \(E\setminus\delta(U)\)；奇圈边横截集 F 是使
\((V,E\setminus F)\) 二分的集合，等价于击中所有奇圈（c01）。

错误的逐项加强：“每个合法颜色类 F_i 自己就是割补集”。
正确的一般关系只有：每个横截集包含某个割补集。
本节先攻击错误加强，再证明存在性层面的正规化。

## 2. 合同图类内的明确攻击见证

取 7-棱柱，顶点为 \(a_j,b_j\)，j 模 7；边为两个水平 7-圈及
\(a_jb_j\)。三正则、简单、无三角形的检查见 c01，顶点数为 14。

先给 C7 的边 \(e_j=\{j,j+1\}\) 赋色
\((1,1,2,2,3,4,5)_j\)。每种颜色至少出现一次，故删任意一种颜色
后的 C7 是森林。映射
\[
 q(a_j)=j,\qquad q(b_j)=j+1
\]
是棱柱到 C7 的顶点同态：上边映到 e_j，下边映到 e_{j+1}，
竖边映到 e_j。将 C7 的边颜色拉回，即得棱柱的合法五色赋值。
理由是每个删色子图仍同态到对应的森林，合成森林的二着色即可。

但是，上层 7-圈恰有两条色 1 边，故其余五条边属于 E\F_1。
任何割沿圈被穿越偶数次，因此 E\F_1 不可能是割，F_1 不是割补集。
这个合法且五色全用到的赋值否定上述逐项加强；它不否定原题。

## 3. claim:opg434-c02-shrink

若 F 是奇圈边横截集，选 H=(V,E\F) 的任意二分 U 与 V\U；
孤立点也分入某一部。H 中每条边都跨部，所以
\[
 E\setminus F\subseteq\delta_G(U),\qquad
 S=E\setminus\delta_G(U)\subseteq F.
\]
S 是割补集，且删 S 后的图由割 \(\delta_G(U)\) 构成，确实二分。
由此得到包含关系，不是未经证明的相等关系。

## 4. claim:opg434-c02-normalize-four

给定四个两两不交的奇圈边横截集 F_1,...,F_4，不要求并为 E。
按上一引理分别取得 \(S_i=E\setminus D_i\subseteq F_i\)，
其中 \(D_i=\delta(U_i)\)。S_i 仍两两不交。定义
\[
 T_i=S_i\ (1\le i\le4),\qquad
 T_5=E\setminus\bigcup_{i=1}^4 S_i.
\]
对边逐个取模 2 可验证割恒等式
\(\delta(U)\triangle\delta(W)=\delta(U\triangle W)\)。
四次取补时 E 的项相消，加上 S_i 不交，有
\[
 \bigcup_{i=1}^4S_i
 =\mathop{\triangle}_{i=1}^4 S_i
 =\mathop{\triangle}_{i=1}^4 D_i
 =\delta(U_1\triangle U_2\triangle U_3\triangle U_4).
\]
因此 T_5 也是割补集，且 T_1,...,T_5 构成 E 的有标号分拆，允许空项。
删任意 T_i 二分，所以它们给出一个合法赋值。

反向，由合法五色赋值保留其前四类，即取得四个不交横截集。
所以，对每个固定 G，“存在合法五色赋值”“存在四个不交奇圈边
横截集”“存在五个分拆 E 的割补集”等价。
若起点是原五类 F_1,...,F_5，上述算法满足
\(T_i\subseteq F_i\) (i<=4) 和 \(F_5\subseteq T_5\)，仅把部分前四色边改为色5。
不能声称它保持原赋值，也不能将任意图上的存在性当成已证明。

## 5. claim:opg434-c02-binary-certificate

定义有限图 B：顶点为 \(\mathbb F_2^4\)，两顶点相邻当且仅当
汉明距离为 3 或 4。下面不依赖目标图名称，直接给出构造。

由四个不交横截集及其二分 U_i，令
\(b(v)=(1_{U_1}(v),...,1_{U_4}(v))\)。
任一边至多属于一个 F_i，因而至少在三个二分中跨部，
所以其端点标签距离为 3 或 4。b 是 G 到 B 的同态。

反之，若给定此种 b，对距离3的边按唯一相等坐标 i 赋色 i；
距离4的边赋色5。删色 i<=4 后，每条剩余边的第 i 位改变，
故第 i 位给出二分。删色5后，每条剩余边恰改变3位，
故四位之和模2给出二分。这是无需枚举奇圈的显式正证书。

为识别 B，映射 \(x\mapsto(x,\sum_{i=1}^4x_i)\) 将其双射到
五位偶重量向量，邻接恰为距离4，即“恰一位相同”的偶重量分量。
这与 DeVos–Šámal Observation 3.1 的 \(H_5^e\) 模型一致，
即 PQ4/Clebsch；我们的构造已单独证明所需的证书性质。

## 6. claim:opg434-c02-parity-and-palette-boundary

正规化后的每个 T_i 为割补集，所以任意简单圈 C 都满足
\[
 |E(C)\cap T_i|\equiv |E(C)|\pmod2.
\]
奇圈上各色出现奇数次，偶圈上各色出现偶数次。
第2节见证说明原赋值不一定具有这个附加奇偶性质。

正规化依赖取四次补集的偶数性。相同推导对 q=2k+1、k>=1 成立，
其中从 2k 个不交横截集出发。不能原样推广到偶数 q：
C3 可用三种不同边色，取得三个不交横截集，却不能获得合法四色赋值，
因为三条边的奇圈不可能包含四种颜色。这只攻击偶数版推广。

## 7. 复核请求及开放边界

复核顺序：第2节合法性和割穿圈奇偶；第3节包含方向；第4节四次
对称差；第5节两方向局部证书；第6节区分原赋值和正规化赋值。
只需 finite-graph-basic 和 finite-combinatorics；无三正则特殊定理。

来源比较见 `research/artifacts/source-notes/opg434-a01-c02-cut-comparison.md`。
本候选不能取代对冻结文本的 kernel_check、axiom_escape_audit、
statement_faithfulness，也没有自动添加 DAG 节点。
best_verified_result=none；原目标及 root 均开放。
下一步是固定输入的正/负证书及精确约束编码，明确区分“一个赋值失败”
与“图根本不存在合法赋值”。
