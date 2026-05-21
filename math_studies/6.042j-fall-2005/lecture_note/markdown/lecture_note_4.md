# Binary Relations 

## 1 Are We Related? 

Questions about how two things are related are bound to come up whatever you’re doing. For two people, you might ask if they’re related (as family), if they know each other, if one is older than the other, if they’re the same sex, race, age, etc. For two countries, you might ask if they trade with each other, if the first has a higher per capita income, if a visa is required to visit one from the other, etc. In Mathematics or Computer Science, if two variables are assigned values, we’re used to asking if the values are the same, if the first value is bigger than the second (assuming both values are real numbers), if the values have a common divisor (assuming both values are integers), if the first value is a member of the second (assuming the second value is a set), if the first value is the domain of the second (assuming the first is a set and the second is a function). These are all examples of binary relations. 

The concept of binary relation is as fundamental mathematically as the concept of function or set. In these Notes we’ll define some basic terminology for binary relations, and then we’ll focus on two especially important kinds of binary relations: equivalence relations and partial orders. 

### 1.1 Relations and Functions 

Here’s the official definition: 

**Definition 1.1.** A binary relation, $R$, consists of a set, $A$, called the domain of $R$, a set, $B$, called the codomain of $R$, and a subset of $A \times B$ called the graph of $R$. 

For example, we can define an “is teaching relation” for Fall ’05 at MIT to have domain equal to the names of all the teaching staff (faculty, T.A.’s, etc.) and codomain equal to all the subject numbers in the current catalogue. Its graph would look like: 
$$\{(\text{Albert R. Meyer}, 6.042), (\text{David Shin}, 18.062), (\text{Sayan Mitra}, 6.042), (\text{Albert R. Meyer}, 18.062), (\text{Charles E. Leiserson}, 6.046), (\text{Donald Sadoway}, 3.091), \dots\}$$

Notice that Definition 1.1 is exactly the same as the definition of a function, except that it doesn’t require the functional condition that, for each domain element, $a$, there is at most one pair in the graph whose first coordinate is $a$. So a function is a special case of a binary relation. 

A relation whose domain is $A$ and codomain is $B$ is said to be “between $A$ and $B$”, or “from $A$ to $B$.” When the domain and codomain are the same set, $A$, we simply say the relation is “on $A$.” It’s common to use infix notation “$a R b$” to mean that the pair $(a, b)$ is in the graph of $R$. 

### 1.2 Images and Inverse Images 

Before we go any further, it’s worth introducing some notation that we’ll get a lot of mileage out of. If $R$ is a binary relation from $A$ to $B$, and $C$ is any set, define: 
$$CR ::= \{b \in B \mid c R b \text{ for some } c \in C\}$$
$$RC ::= \{a \in A \mid a R c \text{ for some } c \in C\}$$

The set $CR$ is called the **image** of $C$ under $R$. Notice that if $R$ happened to be a function, the notation $R(C)$ would also describe the image of $C$ under $R$. 

The set $RC$ is called the **inverse image** of $C$ under $R$. Notice the clash in notation when $R$ happens to be a function: $R(C) = CR$, not $RC$. 

### 1.3 Surjective and Total Relations 

A relation with the property that every codomain element is related to some domain element is called a **surjective** (or onto) relation—again, the same definition as for functions. More concisely, a relation, $R$, between $A$ and $B$ is surjective iff $AR = B$. 

Likewise, a relation with the property that every domain element is related to some codomain element is called a **total** relation; more concisely, $R$ is total iff $A = RB$. 

The Fall ’05 “is teaching relation” relation above is not surjective since none of the Spring term-only subjects are being taught. It’s not total either, since not all the eligible teaching staff are actually teaching this term. 

---

## 2 Equivalence Relations 

An equivalence relation on a set of objects comes about when all we care about is some property—say the size, shape, or color—of the objects rather than the objects themselves. We say two objects with the same property value are “equivalent.” Of course this happens all the time, which is why equivalence relations appear everywhere. 

For example, two triangles in the plane are congruent iff they have the same three lengths of sides. They are similar iff they have the same three sizes of angles. 

Representation-equivalence comes up in Computer Science as the relation between representations of the same abstract data type. For example, the simplest way of representing a finite set of numbers is as an unsorted list. The two lists $(3, 4, -2, 177, 5)$ and $(177, -2, 3, 5, 4)$ are “representation-equivalent” because they represent the same set. 

### 2.1 Equivalence by Function 

Abstractly, we assume there is some function that extracts the angles, size, color, or whatever other property of elements we’re interested in. Two elements would be considered equivalent iff the function extracts the same value for each. 

For example, if $f_c$ is the function mapping a triangle to the lengths of its sides, then $f_c$ determines the congruence relation. If $f_s$ is the function mapping a triangle to the sizes of its angles, then $f_s$ determines the similarity relation. 

**Definition 2.1.** Given any total function, $f$, with domain $A$, define the binary relation $\equiv_f$ on $A$ by the rule: 
$$a \equiv_f b \iff f(a) = f(b) \qquad (1)$$
for all $a, b \in A$. 

A binary relation is an equivalence relation iff it equals $\equiv_f$ for some $f$. 

So congruence of triangles is an equivalence relation because it is $\equiv_{f_c}$, as is triangle similarity because it is $\equiv_{f_s}$. Likewise representation-equivalence on number lists is an equivalence relation because it is $\equiv_{f_r}$, where $f_r$ maps a representation to the set it represents. 

**Quick exercise:** Show that the equality relation on elements of a set, $A$, is actually an equivalence relation according to Definition 2.1 by describing an $I : A \longrightarrow A$ such that equality is $\equiv_I$. 

Congruence modulo $n$ is another equivalence that we will explore in detail when we introduce elementary number theory and its role in modern cryptography. Integers $k$ and $m$ are congruent modulo an integer $n > 1$, written: 
$$m \equiv k \pmod n$$
iff $m$ and $k$ have the same remainder on division by $n$. So congruence modulo $n$ is the equivalence relation determined by the remainder-on-division-by-$n$ function. This relation is called a congruence because adding or multiplying equivalent integers yields equivalent integers. That is: 

**Lemma 2.2.** If $m_1 \equiv k_1 \pmod n$ and $m_2 \equiv k_2 \pmod n$, then: 
$$m_1 + m_2 \equiv k_1 + k_2 \pmod n$$
$$m_1 m_2 \equiv k_1 k_2 \pmod n$$

### 2.2 Partitions 

Cutting up a set into a bunch of pieces is called partitioning the set. The pieces are called blocks of the partition. More formally, 

**Definition 2.3.** A partition of a set, $A$, is a collection, $\mathcal{A}$, of nonempty sets called the blocks of the partition such that: 
1. $A = \bigcup_{B \in \mathcal{A}} B$, and 
2. if $B_1 \neq B_2$ are blocks of $\mathcal{A}$, then $B_1$ and $B_2$ are disjoint[^1]. 

[^1]: Two sets are said to be disjoint when they have no elements in common, that is, their intersection is empty.

**Example 2.4.** We can partition the integers into four blocks according to whether their remainder on division by 4 is 0, 1, 2, or 3: 
* $\{0, 4, -4, 8, -8, 12, \dots\}$ 
* $\{1, -3, 5, -7, 9, -11, \dots\}$ 
* $\{2, -2, 6, -6, 10, -10, \dots\}$ 
* $\{3, -1, 7, -5, 11, -9, \dots\}$ 

**Example 2.5.** We can partition the real line into blocks by cutting it at integer points. Namely, the $n$th block, $B_n$, would be $\{r \in \mathbb{R} \mid n \le r < n + 1\}$. So $B_n$ could also be described as the set of real numbers $r$ that are $\equiv_f n$, where $f$ is the floor function: $f(r) = \lfloor r \rfloor$, the largest integer $\le r$. 

**Example 2.6.** We can partition the pixels in an image according to their color (so there will be somewhere between 2 and several millions blocks depending on whether the image is pure black and white or is “true color”). 

The relation of being in the same block of a partition is an equivalence relation. This is the equivalence relation defined by the function that maps each element to the block it’s in. More precisely, suppose $\mathcal{A}$ partitions a set, $A$, and define $[a]_{\mathcal{A}}$ to be the block with $a$ in it. Note that every $a \in A$ belongs to some block by Definition 2.3.1, and there is only one such block by Definition 2.3.2, so $[a]_{\mathcal{A}}$ is unambiguously defined for each element, $a$. So being-in-the-same-block is $\equiv_{\text{blk}}$, where $\text{blk}(a) ::= [a]_{\mathcal{A}}$. 

Conversely, an equivalence relation, $\equiv_f$, given by a total function, $f$, on a set, $A$, determines a partition of $A$, where the block containing $a \in A$ is: 
$$\{a' \in A \mid f(a') = f(a)\}$$

For example, there are four equivalence classes of integers under congruence mod 4. These are exactly the blocks of the partition based on remainder-by-4 of Example 2.4. 

So we can extract an equivalence relation from any partition, and conversely, we can define a partition determined by any equivalence relation. Partitions and equivalence relations are really interchangeable ways of talking about the same thing. 

### 2.3 Properties of Equivalence Relations 

Equivalence relations have some obvious properties that occur so frequently they merit names: 

**Definition 2.7.** A binary relation $R$ on a set $A$ is: 
* **reflexive** iff for every $a \in A$, $a R a$. 
* **symmetric** iff for every $a, a' \in A$, $a R a'$ implies $a' R a$. 
* **transitive** iff for every $a, b, c \in A$, $[a R b \text{ and } b R c]$ implies $a R c$. 

**Example 2.8.** Let $R_1$ be the less-than relation, $<$, on the natural numbers. Then $R_1$ is transitive. It is not reflexive (since $0 < 0$ is false) and not symmetric (since $0 < 1$ but not $1 < 0$). 

**Example 2.9.** We know that if $A, B, C$ are sets and $A \subset B$ and $B \subset C$, then $A \subset C$. That is, the proper subset relation, $\subset$, is transitive. It is not reflexive (since a set is never a proper subset of itself) and not symmetric. 

**Example 2.10.** Let $R_2$ be the “implies” relation on the set of propositional formulas, that is, define $p R_2 q$ iff $p \longrightarrow q$ is propositionally valid. Now $R_2$ is reflexive and transitive. However, it isn’t symmetric, since false $\longrightarrow$ true is valid, but true $\longrightarrow$ false is not. 

**Example 2.11.** Let $R_3$ be the relation on sets $C, D$ of natural numbers such that $C R_3 D$ iff $C \cap D$ is finite. Then $R_3$ is symmetric, but not reflexive (for example, $\mathbb{N} R_3 \mathbb{N}$ is not true). 

**Quick exercise:** Explain why $R_3$ is not transitive. 

**Example 2.12.** Let $R_4$ be the relation on complex numbers such that $a R_4 b$ iff the distance from $a$ to $b$ in the complex plane is $\le 1$, that is, $|a - b| \le 1$. Then $R_4$ is reflexive and symmetric, but not transitive (because $1 R_4 2$ and $2 R_4 3$, but not $1 R_4 3$). 

**Lemma 2.13.** Every equivalence relation is reflexive, symmetric, and transitive. 

**Proof.** Consider any equivalence relation, $\equiv_f$, determined by some function, $f$, with domain $A$. Since $f(a) = f(a)$, it follows trivially that $\equiv_f$ is reflexive. Likewise, if $f(a) = f(a')$, then $f(a') = f(a)$, which implies that $\equiv_f$ is symmetric. Finally, if $f(a) = f(b)$ and $f(b) = f(c)$, then obviously $f(a) = f(c)$, which implies that $\equiv_f$ is transitive. $\blacksquare$

### 2.4 Equivalence by Axioms 

**Theorem 2.14.** Any relation on a set that is reflexive, symmetric and transitive is an equivalence relation on the set. 

**Proof.** Suppose $R$ is a relation on a set, $A$, and $R$ is reflexive, symmetric, and transitive. Define the function, $f$, with domain, $A$, by the rule: 
$$f(a) ::= [a]_R$$
where $[a]_R$ denotes the set $\{x \in A \mid a R x\}$. We will prove that $R$ is $\equiv_f$, and hence $R$ is an equivalence relation. That is, we have to show that: 
$$a R b \iff [a]_R = [b]_R \qquad (2)$$
for all $a, b \in A$. 

First we prove (2) from right to left. Namely, suppose $[a]_R = [b]_R$. Since $R$ is reflexive, we have $b \in [b]_R$. This means $b \in [a]_R$. So $a R b$ holds by definition of $[a]_R$, which completes the proof from right to left. 

To prove the converse, suppose: 
$$a R b \qquad (3)$$
We’ll first prove that: 
$$[b]_R \subseteq [a]_R \qquad (4)$$
To do this, let $c$ be an element of $[b]_R$; we must show that $c \in [a]_R$. But by definition of $[b]_R$, we know that: 
$$b R c \qquad (5)$$
But (3) and (5) together imply $a R c$ because $R$ is transitive. So $c \in [a]_R$ by definition. This proves (4). 

Finally, (3) implies $b R a$, because $R$ is symmetric. So by the same argument used to prove (4), we can conclude that: 
$$[a]_R \subseteq [b]_R$$
But this together with (4) implies that $[a]_R = [b]_R$, completing the proof of (2) from left to right. $\blacksquare$

---

## 3 Partial Orders 

Partial orders are another class of binary relations that are particularly important in Computer Science, with applications that include task scheduling, database concurrency control, and proving that computations terminate. 

A general example of a partial order is the subset relation, $\subset$, on sets. In fact, we will define partial orders via the subset relation in much the same way we defined equivalence relations. Namely, for any element, $a$, we think of a function, $g$, such that $g(a)$ is the set of properties that $a$ has. Then we relate different elements according to how their properties compare. 

### 3.1 Partial Order by Function 

For partial orders we’ll often use the symbols $\preceq$ or $\prec$ because they resemble the symbols used for subset and less-or-equal. 

**Definition 3.1.** Given any total function, $g$, from a set, $A$, to a collection of sets, define the binary relation $\prec_g$ on $A$ by the rule: 
$$a \prec_g b \iff g(a) \subset g(b) \qquad (6)$$
for $a, b \in A$. A binary relation, $R$, on a set, $A$, is a partial order iff there is a $g$ such that $R$ agrees with $\prec_g$ for every pair of distinct elements. That is, 
$$a R b \iff a \prec_g b \qquad (7)$$
for all $a \neq b \in A$. 

An immediate consequence of Definition 3.1 is that the subset relation itself is a partial order. Specifically, if $A$ is any collection of sets, then the proper subset relation, $\subset$, is a partial order on $A$. 

The most familiar examples of partial orders are “less than” relations, for example, the relation, $<$, on real numbers. To see that $<$ is indeed a partial order, just define $h(r) ::= \{q \in \mathbb{Q} \mid q < r\}$. Since there is a rational number between any two real numbers, it follows that $<$ is simply $\prec_h$. Likewise, the relation, $\le$, is a partial order because it agrees with $\prec_h$ for all pairs of distinct real numbers. 

Our general definition of partial order leaves unspecified whether elements are related to themselves. 

**Definition 3.2.** A partial order is called **weak** iff it is reflexive. (e.g., $\le$ and $\subseteq$) 

**Definition 3.3.** A binary relation, $R$, on a set $A$, is **irreflexive** iff for all $a \in A$ it is not true that $a R a$. A partial order is **strict** iff it is irreflexive. (e.g., $<$ and $\subset$) 

**Example 3.4.** Let $A$ be some family of sets and define $a R b \iff a \supset b$. Then $R$ is a strict partial order. 

**Proof.** Define $p(a) ::= \overline{a}$ (the complement of $a$), and note that: 
$$a R b \iff a \supset b \iff \overline{a} \subset \overline{b} \iff p(a) \subset p(b)$$
So $R$ equals $\prec_p$ and is a partial order. It is strict since no set is a proper subset of itself. $\blacksquare$

**Example 3.5.** The divides relation ($m \mid n$, meaning $n = km$ for some integer $k$) is a weak partial order on the natural numbers. 

**Proof.** Let $v(n) ::= \{d \in \mathbb{N} \mid d \mid n\}$. Then divides is $\prec_v$, and so is a partial order. Since $m \mid m$, it is a weak partial order. $\blacksquare$

### 3.2 Total Orders 

**Definition 3.6.** Let $R$ be a binary relation on a set, $A$, and let $a, b$ be elements of $A$. Then $a$ and $b$ are comparable with respect to $R$ iff ($a R b \vee b R a$). A partial order under which every two distinct elements are comparable is called a total order[^2]. 

[^2]: “Total” is an overloaded term when talking about partial orders: being a total order is a much stronger condition than being a partial order that is a total relation. For example, any weak partial order such as $\subseteq$ is a total relation.

So $<$ and $\le$ are total orders on $\mathbb{R}$. On the other hand, the subset relation is generally not total. 

### 3.3 Properties of Partial Orders 

**Lemma 3.7.** Every partial order is transitive. 

**Definition 3.8.** A binary relation, $R$, on a set, $A$, is **antisymmetric** if: 
$$a R b \text{ implies } \neg(b R a)$$
for all $a \neq b \in A$. 

**Lemma 3.9.** Every partial order is antisymmetric. 

**Proof.** Suppose $R$ is a partial order on $A$. So there is a set-valued total function, $g$, with domain $A$ and $R$ agrees with $\prec_g$ on pairs of distinct elements in $A$. We want to show that $aRb$ and $bRa$ cannot both hold for elements $a \neq b$. But if they did both hold, then (6) would imply that $g(a)$ and $g(b)$ are proper subsets of each other, which is impossible. $\blacksquare$

### 3.4 Partial Orders by Axioms 

**Theorem 3.10.** A binary relation is a partial order iff it is transitive and antisymmetric. 

**Proof.** Let $R$ be a binary relation on a set $A$. The preceding two Lemmas imply the left to right direction. 

To prove the Theorem in the right to left direction, assume $R$ is transitive and antisymmetric. Define: 
$$g(a) ::= \{x \in A \mid x R a\} \cup \{a\} \qquad (8)$$
We claim that $R$ is a partial order because it agrees with $\prec_g$ on distinct elements of $A$. That is, if $a \neq b \in A$, then: 
$$a R b \iff g(a) \subset g(b) \qquad (9)$$

To prove (9) from right to left, note that: 
* $g(a) \subset g(b) \implies a \in g(b)$ (since $a \in g(a)$ by (8)) 
* $\implies a \in \{x \in A \mid x R b\} \cup \{b\}$ (by definition of $g(b)$) 
* $\implies a \in \{x \in A \mid x R b\}$ (since $a \neq b$) 
* $\implies a R b$. $\blacksquare$

**Theorem 3.11.** A binary relation is a strict partial order iff it is transitive and irreflexive. 

For weak partial orders, we write $\succeq$ or $\preceq$, and $\prec$ or $\succ$ for strict ones. 

### 3.5 Products and Restrictions of Relations 

#### 3.5.1 Products 

The product, $R_1 \times $R_2$, of relations $R_1$ and $R_2$ is defined to be the relation with: 
$$\text{domain}(R_1 \times R_2) ::= \text{domain}(R_1) \times \text{domain}(R_2)$$
$$\text{codomain}(R_1 \times R_2) ::= \text{codomain}(R_1) \times \text{codomain}(R_2)$$
$$(a_1, a_2) (R_1 \times R_2) (b_1, b_2) \iff [a_1 R_1 b_1 \wedge a_2 R_2 b_2]$$

**Example 3.12.** Define a relation, $Y$, on age-height pairs of being younger and shorter. This is the relation on the set of pairs $(y, h)$ where $y$ is a natural number $\le 2400$ (age in months), and $h \le 120$ (height in inches): 
$$(y_1, h_1) Y (y_2, h_2) \iff y_1 \le y_2 \wedge h_1 \le h_2$$

If $R_1$ and $R_2$ are both partial orders, then so is $R_1 \times R_2$. Likewise for equivalence relations. 

#### 3.5.2 Restrictions 

**Definition 3.13.** Let $R$ be a relation on a set, $A$, and let $B$ be a subset of $A$. The restriction of $R$ to $B$ is the relation on $B$ whose graph is $\text{graph}(R) \cap (B \times B)$. 

Restrictions preserve transitivity, symmetry, antisymmetry, reflexivity, and irreflexivity. 

---

## 4 Digraphs 

A directed graph (digraph for short) is formally the same as a binary relation on a set, $A$, but we picture the digraph geometrically by representing elements of $A$ as vertices, with an arrow from $a$ to $b$ exactly when $a R b$. 

For example, the divisibility relation on $\{1, 2, \dots, 12\}$ can be represented by a digraph where arrows connect divisors to their multiples (e.g., $1 \longrightarrow 2$, $2 \longrightarrow 4$, $3 \longrightarrow 6$, etc.).

### 4.1 Paths in Digraphs 

**Definition 4.2.** A path in a digraph, $R$, is a sequence of vertices $a_0, a_1, \dots, a_k$ with $k \ge 0$ such that $a_i R a_{i+1}$ for every $0 \le i < k$. The path is said to start at $a_0$, to end at $a_k$, and the length of the path is defined to be $k$. 

We can define some new relations based on paths. Let $R$ be a digraph with vertices, $A$. Define relations $R^*$ and $R^+$ on $A$ by: 
$$a R^* b \iff \text{there is a path in } R \text{ from } a \text{ to } b$$
$$a R^+ b \iff \text{there is a positive length path in } R \text{ from } a \text{ to } b$$

$R^*$ is the reflexive transitive closure (path relation) of $R$. $R^+$ is the positive-length path relation. 

### 4.2 Directed Acyclic Graphs 

Scheduling problems: there is a set, $A$, of tasks and a set of constraints specifying that starting a certain task depends on other tasks being completed beforehand. 

**Example 4.3.** Order of putting on clothes: 
```
left sock  -------> left shoe  ------\
                                      -----> belt -----> jacket
right sock -------> right shoe ------/      /
                                           /
underwear --------> pants ----------------/
                                         /
shirt -----------> sweater -------------/
```

**Definition 4.4.** A cycle is a positive length path in a digraph that begins and ends at the same vertex. A directed acyclic graph (DAG) is a directed graph with no cycles. 

**Lemma 4.5.** If $D$ is a DAG, then $D^+$ is a strict partial order. 

**Proof.** We know that $D^+$ is transitive. Also, a positive length path from a vertex to itself would be a cycle, so there are no such paths. This means $D^+$ is irreflexive, and so by Theorem 3.11, it is a strict partial order. $\blacksquare$

### 4.3 Topological Sorting 

**Definition 4.6.** A topological sort of a partial order, $\preceq$, on a set, $A$, is a total ordering, $\preceq'$, on $A$ such that: 
$$a \preceq b \implies a \preceq' b$$

One topological sort of dressing: 
$$\text{shirt} \preceq' \text{sweater} \preceq' \text{underwear} \preceq' \text{left sock} \preceq' \text{right sock} \preceq' \text{pants} \preceq' \text{left shoe} \preceq' \text{right shoe} \preceq' \text{belt} \preceq' \text{jacket}$$

**Definition 4.7.** Let $\preceq$ be a partial order on a set, $A$, and let $a \in A$. Then $a$ is minimal iff no other element is $\preceq a$. Similarly, $a$ is maximal iff no other element is $\succeq a$. 

**Lemma 4.8.** Every partial order on a nonempty finite set has a minimal element. 

**Proof.** Let $R$ be a partial order on a set, $A$. For any element, $a \in A$, let $g(a) ::= \{x \in A \mid x R a\} \cup \{a\}$. If $b R a$ and $b \neq a$, then $g(b) \subset g(a)$ since $R$ is antisymmetric and transitive. So if $a$ is not minimal, there is some $b$ such that $g(b) \subset g(a)$, which implies $|g(b)| < |g(a)|$. If $A$ is finite, the Well Ordering Principle implies there must be an $a_0$ such that $g(a_0)$ has minimum size, which means $a_0$ must be minimal. $\blacksquare$

**Theorem 4.9.** Every partial order on a finite set has a topological sort. 

**Proof.** We use induction on $n$ with hypothesis: 
$$P(n) ::= [\text{any partial order on a set with } n \text{ elements has a topological sort}].$$
* **Base case ($n = 1$):** A topological sort of a set with one element is simply that element. 
* **Inductive step:** Assume $P(n)$. Consider a partial order on a set, $A$, with $n + 1$ elements. By Lemma 4.8, $A$ must have a minimal element, $a_0$. The restriction of the partial order to $A \setminus \{a_0\}$ is also a partial order. By the inductive hypothesis, $A \setminus \{a_0\}$ has a topological sort $\preceq_n$. We define $\preceq'$ on $A$ by the rule that $a \preceq' b$ iff $[a \preceq_n b \vee a = a_0]$. It is easy to check that $\preceq'$ is a topological sort of $A$. $\blacksquare$

### 4.4 Parallel Task Scheduling 

If we have the ability to execute more than one task at the same time: 

**Definition 4.10.** A chain in a partial order is a set of elements such that any two elements in the set are comparable. 

A largest chain is also known as a critical path. If $t$ is the size of the largest chain[^3], we need at least $t$ steps. 

[^3]: The size of a chain is the number of elements in it (e.g., $k + 1$ for a path traversing $k$ arrows).

**Theorem 4.11.** Let $R$ be a strict partial order on a set, $A$. If the longest chain in $A$ is of size $t$, then there is a partition of $A$ into $t$ blocks, $B_1, B_2, \dots, B_t$, such that for each block, $B_i$, all tasks that have to precede tasks in $B_i$ are in smaller-numbered groups: 
$$R(B_1) = \emptyset \qquad (10)$$
$$R(B_i) \subseteq B_1 \cup B_2 \cup \dots \cup B_{i-1} \qquad (11)$$
for $1 < i \le t$. 

**Corollary 4.12.** It is possible to schedule all tasks in $t$ steps (by scheduling elements of $B_i$ at time $i$). 

```
B1: left sock, right sock, underwear, shirt
B2: pants, sweater
B3: left shoe, right shoe, belt
B4: jacket
```

**Proof.** Construct the sets $B_i$ as: 
$$B_i ::= \{a \in A \mid \text{the largest chain ending in } a \text{ is of size } i\}$$
This gives just $t$ sets. If $a \in B_1$, then $a$ must be minimal, so $R(B_1) = \emptyset$. For $1 < i \le t$, if there was some $b R a$ with $b \notin B_1 \cup \dots \cup B_{i-1}$, then $b$ would end a chain of size $\ge i$. Adding $a$ would make a chain of size $\ge i + 1$ ending in $a$, contradicting $a \in B_i$. $\blacksquare$

**Definition 4.14.** An antichain in a partial order is a set of elements such that any two elements in the set are incomparable. 

**Corollary 4.15.** If the largest chain in a partial order is of size $t$, then the domain can be partitioned into $t$ antichains. 

### 4.5 Dilworth’s Lemma 

**Lemma 4.16 (Dilworth).** For all $t$, every partially ordered set with $n$ elements must have either a chain of size greater than $t$ or an antichain of size at least $n/t$. 

**Proof.** Assume the largest chain is of size $\le t$. By Corollary 4.15, the $n$ elements can be partitioned into at most $t$ antichains. Let $\alpha$ be the size of the largest antichain. Since every element belongs to exactly one antichain, we have $\alpha t \ge n \implies \alpha \ge n/t$. $\blacksquare$

**Corollary 4.17.** Every partially ordered set with $n$ elements has a chain of size greater than $\sqrt{n}$ or an antichain of size at least $\sqrt{n}$. (Proof: Set $t = \sqrt{n}$ in Lemma 4.16). 

**Corollary 4.20.** In any sequence of $n$ different numbers, there is either an increasing subsequence of length greater than $\sqrt{n}$ or a decreasing subsequence of length at least $\sqrt{n}$. 

**Proof.** Define a partial order on pairs $(i, a_i)$ where $(i, a_i) \prec (j, a_j) \iff i < j \wedge a_i < a_j$. A chain corresponds to an increasing subsequence, and an antichain (when sorted by index) corresponds to a decreasing subsequence. The result follows by Dilworth's Lemma. $\blacksquare$

---

## 5 Undirected Graphs 

**Definition 5.1.** An undirected graph (graph for short), $G$, consists of a set, $V$, called the vertices of $G$, and a collection, $E$, of two-element subsets of $V$. The elements of $E$ are called the edges of $G$. 

An example of a graph: 
```
B --- D
|     |
A --- C --- E --- F
            |
            G

H --- I
```
Here: 
$$V = \{A, B, C, D, E, F, G, H, I\}$$
$$E = \{\{A, B\}, \{A, C\}, \{B, D\}, \{C, D\}, \{C, E\}, \{E, F\}, \{E, G\}, \{H, I\}\}$$

We use the notation $A—B$ for the edge $\{A, B\}$. Two vertices are **adjacent** if they are joined by an edge. An edge is **incident** to the vertices it joins. The **degree** of a vertex is the number of incident edges. 

### 5.1 Some Common Graphs 

* **Complete graph** $K_n$: has an edge between every two vertices. 
* **Empty graph**: has no edges at all. 
* **Line graph** $L_n$: a single line path of vertices. 
* **Cycle graph** $C_n$: a simple closed cycle of vertices. 

### 5.2 Isomorphism 

**Definition 5.2.** Graphs $G_1$ and $G_2$ are **isomorphic** iff there exists a bijective function $f : V_1 \longrightarrow V_2$ such that for every pair of vertices $u, v \in V_1$: 
$$u—v \in E_1 \iff f(u)—f(v) \in E_2$$
The function $f$ is called an **isomorphism**. 

Isomorphism captures all the connection properties of a graph, abstracting out what the vertices are called, what they are made of, or how they are drawn. 
