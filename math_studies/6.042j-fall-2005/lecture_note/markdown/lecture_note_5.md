# Graphs 

As in the previous notes, we’ll refer to undirected graphs simply as “graphs.” 

## 1 Counting by Degrees 

### 1.1 Sex in America 

A 1994 University of Chicago study entitled *The Social Organization of Sexuality* found that on average men have 74% more opposite-gender partners than women, confirming a view that men are more promiscuous. But whoever reported this finding was lying or confused! We’ll show you how to use the properties of vertex degrees in a graph to prove this. 

Let’s recast opposite-gender partnering in graph theoretic terms. Let $G$ be a graph where the set of vertices $V$ consists of everyone in America. Now each vertex represents either a male or a female, so we can partition $V$ into two subsets: $M$, which contains all the male vertices, and $F$, which contains all the female vertices. Let’s draw all the $M$ vertices on the left and the $F$ vertices on the right. 

Since we’re only considering opposite-gender relationships, every edge connects an $M$ vertex on the left to an $F$ vertex on the right. So the sum of the degrees of the $M$ vertices equals the number of edges, and so does the sum of the degrees of the $F$ vertices. Thus, these sums are equal: 
$$\sum_{x \in M} \text{deg}(x) = \sum_{y \in F} \text{deg}(y)$$

Now suppose we divide both sides of this equation by the product of the sizes of the two sets, $|M| \cdot |F|$: 
$$\frac{1}{|F|} \cdot \left( \frac{\sum_{x \in M} \text{deg}(x)}{|M|} \right) = \frac{1}{|M|} \cdot \left( \frac{\sum_{y \in F} \text{deg}(y)}{|F|} \right)$$

The terms in parentheses are the average degree of an $M$ vertex and the average degree of an $F$ vertex. So we know: 
$$\frac{\text{Avg. degree in } M}{|F|} = \frac{\text{Avg. degree in } F}{|M|}$$
$$\text{Avg. degree in } M = \frac{|F|}{|M|} \cdot \text{Avg. degree in } F$$

In other words, we’ve proved that the average number of opposite-gender partners of males in the population compared to those of females is determined solely by the relative number of males and females in the population. 

Now the Census Bureau reports that there are slightly more females than males in America; in particular $|F| / |M|$ is about $1.035$. So we know that on average, males have 3.5% more opposite-gender partners than females, and this tells us nothing about any sex’s predilection toward promiscuity. We can only wonder where the University of Chicago researchers got their 74% difference. 

### 1.2 Handshaking Lemma 

The previous argument hinged on the connection between a sum of degrees and the number of edges. There is a simple connection between these in any graph: 

**Theorem 1.1 (Handshaking Lemma).** The sum of the degrees of the vertices in a graph equals twice the number of edges: 
$$\sum_{v \in V} \text{deg}(v) = 2|E|$$

**Proof.** Every edge contributes two to the sum of the degrees, one for each of its endpoints. $\blacksquare$

---

## 2 Connectedness 

### 2.1 Paths and Simple Cycles 

Paths in graphs are defined in pretty much the same way as for digraphs, but they are going to be particularly important, so let’s define them precisely. 

**Definition 2.1.** Let $G$ be a graph with vertices, $V$, and edges, $E$. A path in $G$ is a sequence of vertices: 
$$v_0, v_1, \dots, v_k$$
with $k \ge 0$ such that $v_i—v_{i+1}$ is an edge in $E$ for $0 \le i < k$. The path is **simple** iff all the $v_i$’s are different (i.e., $v_i = v_j$ only if $i = j$). 

The path is said to start at $v_0$, to end at $v_k$, and the length of the path is defined to be $k$. 

For example, the graph in Figure 1 has a length 6 simple path $A, B, C, D, E, F, G$. This is the longest simple path in the graph. 

```
       A
       |
       B ------- H
      / \       /
     /   \     /
    C     \   /
   / \     \ /
  D --- E --- F --- G
```
*Figure 1: A graph with 3 simple cycles.*

Notice that the length of a path is the total number of times it traverses edges, which is one less than its length as a sequence of vertices. 

Cycles are paths that begin and end with the same vertex. Simple cycles are cycles that don’t cross themselves. For example, the graph in Figure 1 has three simple cycles: $B,H,E,C,B$ and $C,D,E,C$ and $B,C,D,E,H,B$. 

To capture this precisely, we define a simple cycle to be a subgraph isomorphic to the simple cycle graph, $C_n$. 

**Definition 2.2.** A subgraph, $G'$, of a graph, $G$, is a graph whose vertices, $V'$, are a nonempty subset of the vertices of $G$ and whose edges are a subset of the edges of $G$. 

**Definition 2.3.** For $n \ge 3$, let $C_n$ be the graph with vertices $1, 2, \dots, n$ and edges: 
$$1—2, 2—3, \dots, (n-1)—n, n—1$$
A graph, $C$, is a simple cycle of length $n$ iff it is isomorphic to $C_n$ for some $n \ge 3$. A simple cycle of a graph, $G$, is a subgraph of $G$ that is a simple cycle. 

### 2.2 Connected Components 

**Definition 2.4.** Two vertices in a graph are said to be **connected** if there is a path that begins at one and ends at the other. 

**Lemma.** Connectedness is an equivalence relation on the vertices of any graph. 

The diagram in Figure 2 represents one graph consisting of three connected components. 

```
Component 1:       Component 2:       Component 3:
   o---o              o                  o---o
   |   |             / \                     |
   o---o            o---o                    o
```
*Figure 2: A graph with 3 connected components.*

**Definition 2.5.** A graph is said to be **connected** if every pair of vertices are connected. 

The connected components of a graph are the equivalence classes of its connectedness relation. A graph is connected iff it has exactly one connected component. 

### 2.3 How Well Connected? 

**Definition 2.6.** Two vertices in a graph are $k$-connected if they remain connected in any subgraph obtained by deleting at most $k - 1$ edges. A graph is $k$-connected if every pair of its vertices are $k$-connected. 

In Figure 1, vertices $B$ and $E$ are 2-connected, $G$ and $E$ are 1-connected, and no vertices are 3-connected. The graph as a whole is 1-connected. 

Any simple cycle is 2-connected, and the complete graph, $K_n$, is $(n - 1)$-connected. 

A fundamental fact, known as **Menger’s Theorem**, states that two vertices are $k$-connected if and only if there are $k$ edge-disjoint paths connecting them. 

### 2.4 Connection by Simple Path 

**Lemma 2.7.** If vertex $u$ is connected to vertex $v$ in a graph, then there is a simple path from $u$ to $v$. 

**Proof.** Since there is a path from $u$ to $v$, there must, by the Well Ordering Principle, be a minimum length path from $u$ to $v$: 
$$v_0, v_1, \dots, v_k$$
where $u = v_0$ and $v = v_k$. We claim this path must be simple. 

Suppose to the contrary that the path is not simple, meaning some vertex occurs twice: $v_i = v_j$ for some $0 \le i < j \le k$. Then deleting the subsequence $v_{i+1}, \dots, v_j$ yields a strictly shorter path from $u$ to $v$, contradicting the minimality of the path. $\blacksquare$

**Corollary 2.8.** For any path of length $k$ in a graph, there is a simple path of length at most $k$ with the same endpoints. 

### 2.5 The Minimum Number of Edges in a Connected Graph 

**Theorem 2.9.** Every graph with $k$ vertices and $n$ edges has at least $k - n$ connected components. 

**Proof.** We use induction on the number of edges. Let $P(n)$ be the proposition that for every $k$, every graph with $k$ vertices and $n$ edges has at least $k - n$ connected components. 
* **Base case ($n = 0$):** A graph with 0 edges and $k$ vertices has each vertex as a separate component, so there are exactly $k = k - 0$ components. 
* **Inductive step:** Assume $P(n)$ is true. Consider a graph $G$ with $n + 1$ edges and $k$ vertices. Remove an arbitrary edge $u—v$ to get a graph $G'$. By the induction hypothesis, $G'$ has at least $k - n$ connected components. Now add back the edge $u—v$ to obtain $G$. If $u$ and $v$ were already in the same component of $G'$, the number of components is unchanged ($\ge k - n > k - (n + 1)$). If they were in different components, these two components merge into one, reducing the number of components by 1. Thus, $G$ has at least $(k - n) - 1 = k - (n + 1)$ connected components. 

The theorem follows by induction. $\blacksquare$

**Corollary 2.10.** Every connected graph with $n$ vertices has at least $n - 1$ edges. 

---

## 3 Trees 

Trees are acyclic connected graphs. 

### 3.1 Tree Properties 

**Theorem 3.1.** Every tree has the following properties: 
1. Any connected subgraph is a tree. 
2. There is a unique simple path between every pair of vertices. 
3. Adding an edge between two vertices creates a cycle. 
4. Removing any edge disconnects the graph. 
5. If it has at least two vertices, then it has at least two leaves (vertices of degree 1). 
6. The number of vertices is one larger than the number of edges ($|V| = |E| + 1$). 

**Proof.** 
1. Subgraphs of acyclic graphs must be acyclic. If connected, it is a tree. 
2. Suppose there are two different simple paths between $u$ and $v$. Let $x$ be the first vertex where they diverge, and $y$ the next vertex they share. The two paths from $x$ to $y$ form a simple cycle, contradicting the acyclic property. 
3. Adding an edge $u—v$ completes a cycle with the unique path between $u$ and $v$. 
4. Removing $u—v$ leaves no path between $u$ and $v$, disconnecting the graph. 
5. Let $v_1, \dots, v_m$ be a longest simple path. If $v_1$ had any other neighbor $u$, either $u$ is on the path (creating a cycle) or off the path (making it longer), both contradictions. So $\text{deg}(v_1) = 1$. Similarly, $v_m$ is a leaf. 
6. By induction on vertices: a 1-vertex tree has 0 edges ($1 = 0 + 1$). For an $(n+1)$-vertex tree, removing a leaf $v$ and its incident edge yields an $n$-vertex tree, which has $n - 1$ edges by induction. Reattaching the leaf increases both vertices and edges by 1, so the formula holds. $\blacksquare$

### 3.2 Spanning Trees 

**Definition 3.2.** A spanning tree for a connected graph $G$ is a subgraph of $G$ that is a tree and contains all the vertices of $G$. 

**Theorem 3.2.** Every connected graph contains a spanning tree. 

**Proof.** Let $T$ be a connected subgraph of $G$ containing all vertices of $G$ with the minimum number of edges. If $T$ had a cycle, removing any edge of the cycle would leave the graph connected, contradicting the minimality of $T$. Thus, $T$ is acyclic and therefore a tree. $\blacksquare$

---

## 4 Coloring Graphs 

**Definition 4.0.** A coloring of a graph assigns a color to each vertex such that adjacent vertices receive different colors. The minimum number of colors needed to color a graph $G$ is its **chromatic number**. 

### 4.1 $k$-Coloring 

**Theorem 4.1.** A graph with maximum degree at most $k$ is $(k + 1)$-colorable. 

**Proof.** We use induction on the number of vertices, $n$. 
* **Base case ($n = 1$):** A 1-vertex graph is 1-colorable, and the maximum degree is $0$, so $1 \le 0 + 1$ holds. 
* **Inductive step:** Assume $P(n)$ is true. Let $G$ be an $(n + 1)$-vertex graph with maximum degree at most $k$. Remove a vertex $v$ and its incident edges, leaving an $n$-vertex graph $G'$. The maximum degree of $G'$ is at most $k$, so $G'$ is $(k + 1)$-colorable by the induction hypothesis. Now put back $v$ and its incident edges. Since $v$ is adjacent to at most $k$ vertices, at least one of the $k + 1$ colors is not used by its neighbors. Assigning this color to $v$ completes the coloring. $\blacksquare$

### 4.2 Bipartite Graphs 

**Definition 4.2.** A graph is **bipartite** iff it is 2-colorable. This means the vertex set can be partitioned into two sets, $L$ and $R$, such that every edge has one endpoint in $L$ and the other in $R$. 

**Theorem 4.2.** A graph is bipartite if and only if it contains no odd length cycle. 

---

## 5 Planar Graphs 

A **planar graph** is a graph that can be drawn in the plane so that no edges intersect (except at common vertices). Such a drawing is called a **planar embedding**. 

A drawing of a planar graph divides the plane into **faces**, which are connected regions bounded by the edges. The unbounded region extending to infinity is the **outside face**. 

### 5.1 Euler’s Formula 

**Theorem 5.1 (Euler’s Formula).** For every drawing of a connected planar graph: 
$$v - e + f = 2$$
where $v$ is the number of vertices, $e$ is the number of edges, and $f$ is the number of faces. 

**Proof.** We use induction on the number of edges, $e$. 
* **Base case ($e = 0$):** A connected graph with 0 edges has $v = 1$ vertex and $f = 1$ face (the outside face). Indeed, $1 - 0 + 1 = 2$. 
* **Inductive step:** Assume $P(e)$ holds. Consider a connected graph $G$ with $e + 1$ edges. 
  1. If $G$ is a tree, it has $v = e + 2$ vertices and $f = 1$ face. Indeed, $(e + 2) - (e + 1) + 1 = 2$. 
  2. If $G$ contains a cycle, select an edge $u—v$ in the cycle. Removing $u—v$ merges the two faces on either side of the edge and leaves a connected graph $G'$ with $e$ edges, $v$ vertices, and $f$ faces. By induction, $v - e + f = 2$. The original graph $G$ had $v$ vertices, $e + 1$ edges, and $f + 1$ faces. Since $v - (e + 1) + (f + 1) = v - e + f = 2$, the formula holds. $\blacksquare$

### 5.2 Number of Edges versus Vertices 

**Lemma 5.2.** If a connected, planar graph has $v > 2$ vertices and $e$ edges, then: 
$$e \le 3v - 6$$

**Proof.** Every edge is on the boundary of exactly two faces, so summing the lengths of all face boundaries yields $2e$. Since $v > 2$, each face boundary must contain at least 3 edges, so $2e \ge 3f$. Substituting $f = e - v + 2$ from Euler's formula: 
$$2e \ge 3(e - v + 2) \implies e \le 3v - 6 \qquad \blacksquare$$

Since the complete graph $K_5$ has $v = 5$ vertices and $e = 10$ edges, and $10 > 3(5) - 6 = 9$, $K_5$ is not planar. 

### 5.3 Classifying Regular Polyhedra 

A regular polyhedron is a convex 3D region bounded by identical regular polygons such that the same number of faces meet at each corner. 

Let $m$ be the number of faces meeting at each corner ($m \ge 3$), and $n$ the number of sides of each face ($n \ge 3$). In the corresponding planar graph, we have: 
$$mv = 2e \quad \text{and} \quad nf = 2e$$

Substituting these into Euler's formula gives: 
$$\frac{2e}{m} - e + \frac{2e}{n} = 2 \implies \frac{1}{m} + \frac{1}{n} = \frac{1}{e} + \frac{1}{2}$$

Since $1/e > 0$, we must have $\frac{1}{m} + \frac{1}{n} > \frac{1}{2}$. Solving this inequality for integers $m, n \ge 3$ yields exactly five solutions: 

| $n$ | $m$ | $v$ | $e$ | $f$ | Polyhedron |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 3 | 3 | 4 | 6 | 4 | Tetrahedron |
| 4 | 3 | 8 | 12 | 6 | Cube |
| 3 | 4 | 6 | 12 | 8 | Octahedron |
| 3 | 5 | 12 | 30 | 20 | Icosahedron |
| 5 | 3 | 20 | 30 | 12 | Dodecahedron |

---

## 6 Hall’s Marriage Theorem 

Consider pairing up a set of girls $G$ and boys $B$ where each girl likes some subset of boys. 

### 6.1 The Marriage Condition 

For a complete matching to exist, the **marriage condition** must hold: every subset of girls likes at least as large a set of boys. 

**Theorem 6.1.** A matching for a set of girls $G$ with a set of boys $B$ can be found if and only if the marriage condition holds. 

**Proof.** 
* **Necessity:** If a matching exists, each girl is matched to a unique boy she likes. Thus, any subset of girls $S$ must like at least the $|S|$ boys they are matched with. 
* **Sufficiency:** By strong induction on $|G|$. 
  * **Base case ($|G| = 1$):** The girl likes at least one boy, so a matching exists. 
  * **Inductive step:** Assume sufficiency for all $|G| < n$. Let $|G| = n \ge 2$. 
    1. **Case 1:** Every proper subset of girls likes a strictly larger set of boys. Match an arbitrary girl with a boy she likes, and remove them. The marriage condition still holds for the remaining $n - 1$ girls, who can be matched by induction. 
    2. **Case 2:** Some proper subset of girls $X \subset G$ likes an equal-size set of boys $Y \subset B$ ($|X| = |Y|$). Match $X$ with $Y$ by induction and remove them. For any remaining subset of girls $X' \subseteq G \setminus X$, let $Y'$ be the remaining boys they like. Since $X \cup X'$ originally liked at least $|X \cup X'| = |X| + |X'|$ boys, and we removed $|Y| = |X|$ boys, the remaining girls must like at least $(|X| + |X'|) - |X| = |X'|$ remaining boys. Thus, the marriage condition holds for the remaining group, and they can be matched by induction. $\blacksquare$

### 6.2 A Formal Statement 

Let $S$ be a set of vertices in a graph. Define $N(S)$ to be the set of all neighbors of $S$ (vertices adjacent to some vertex in $S$, but not in $S$ itself). 

**Theorem 6.2 (Hall's Theorem).** Let $G$ be a bipartite graph with partition sets $L$ and $R$. There is a matching for $L$ if and only if: 
$$|N(S)| \ge |S| \quad \text{for every set } S \subseteq L \qquad \blacksquare$$
