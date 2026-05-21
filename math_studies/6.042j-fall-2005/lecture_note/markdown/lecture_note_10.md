# Counting II 

## 1 Counting Subsets 

How many $k$-element subsets of an $n$-element set are there? 
This number comes up so often that there is a special notation for it: 
$$\binom{n}{k} ::= \text{the number of } k\text{-element subsets of an } n\text{-element set.}$$
The expression $\binom{n}{k}$ is read "$n$-choose-$k$." 

### 1.1 The Subset Rule 

We can derive a formula for $\binom{n}{k}$ using the Division Rule. Consider mapping any permutation of an $n$-element set $\{a_1, \dots, a_n\}$ to a $k$-element subset by taking the first $k$ elements: $\{a_1, \dots, a_k\}$. 

Any permutation with the same first $k$ elements (in any order) and the same remaining $n-k$ elements (in any order) will map to this same subset. 
* There are $k!$ ways to order the first $k$ elements. 
* There are $(n-k)!$ ways to order the remaining $n-k$ elements. 

By the Product Rule, exactly $k!(n-k)!$ permutations map to the same subset. Since there are $n!$ total permutations, the mapping is $k!(n-k)!$-to-1. Applying the Division Rule: 

**Rule 1 (Subset Rule).** The number of $k$-element subsets of an $n$-element set is: 
$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

### 1.2 Bit Sequences 

By mapping a subset $S \subseteq \{x_1, \dots, x_n\}$ to a bit sequence where the $i$-th bit is $1$ iff $x_i \in S$, we establish a bijection: 
$$\text{The number of } n\text{-bit sequences with exactly } k \text{ ones is } \binom{n}{k}$$

---

## 2 Bipartite Matching: The 5-Card Magic Trick 

### 2.1 Bipartite Formulation 

A magician and an assistant perform a card trick. Five cards are chosen by the audience from a standard 52-card deck. The assistant looks at the 5 cards, selects 4 of them, and reveals them in some order to the magician. The magician then names the hidden 5th card. 

We can analyze this trick using bipartite matching: 
* Let $X$ be the set of all subsets of 5 cards: $|X| = \binom{52}{5} = 2,598,960$. 
* Let $Y$ be the set of all sequences of 4 distinct cards: $|Y| = 52 \cdot 51 \cdot 50 \cdot 49 = 6,497,400$. 
* Put an edge between $x \in X$ and $y \in Y$ if the 4 cards in sequence $y$ are all present in the set $x$. 

To perform the trick, we need a matching for all vertices in $X$. By Hall's Marriage Theorem, a matching exists because the marriage condition is satisfied: 
* The degree of every vertex in $X$ is $5 \cdot 4! = 120$ (5 choices for the hidden card, and $4!$ permutations of the remaining 4). 
* The degree of every vertex in $Y$ is $48$ (since there are 48 options for the 5th card). 

For any set of vertices $S \subseteq X$, the number of incident edges is $120 |S|$. Since each vertex in $Y$ has degree 48, the size of the neighborhood $N(S) \subseteq Y$ satisfies: 
$$|N(S)| \ge \frac{120 |S|}{48} = 2.5 |S| \ge |S|$$
Thus, a matching exists. 

### 2.2 The Strategy 

Since the magician and assistant cannot memorize an arbitrary matching, they use the following deterministic rule: 
1. **Suit Matching:** By the Pigeonhole Principle, among the 5 cards, at least two must share a suit. The assistant identifies two cards of the same suit. One will be the first card shown, and the other will be the hidden card. 
2. **Cycle Ordering:** The values $A, 2, \dots, K$ are ordered in a cycle of length 13. For any two values on this cycle, one is at most 6 steps clockwise from the other. The assistant chooses the counterclockwise card to show first, and the clockwise card to hide. This ensures the hidden card's value is $1$ to $6$ steps clockwise from the first card shown. 
3. **Permutation Coding:** The assistant encodes the step difference (1 to 6) using the relative order of the remaining 3 cards. By ordering the three cards as Small ($S$), Medium ($M$), and Large ($L$), there are $3! = 6$ possible permutations: 
   * $(S, M, L) = 1$ 
   * $(S, L, M) = 2$ 
   * $(M, S, L) = 3$ 
   * $(M, L, S) = 4$ 
   * $(L, S, M) = 5$ 
   * $(L, M, S) = 6$ 

#### Example: 
Suppose the audience selects $\{10\heartsuit, 9\diamondsuit, 3\heartsuit, Q\spadesuit, J\diamondsuit\}$. 
* The assistant pairs $10\heartsuit$ and $3\heartsuit$ (same suit). On the cycle, $3$ is 6 steps clockwise from $10$. 
* The first card shown is $10\heartsuit$, and the hidden card is $3\heartsuit$. 
* The remaining cards $\{9\diamondsuit, Q\spadesuit, J\diamondsuit\}$ have the sorted order $9\diamondsuit < J\diamondsuit < Q\spadesuit$. To encode the value $6$, the assistant orders them as $(L, M, S) \to (Q\spadesuit, J\diamondsuit, 9\diamondsuit)$. 
* The magician sees: $10\heartsuit, Q\spadesuit, J\diamondsuit, 9\diamondsuit$. 
* The magician starts at $10\heartsuit$, determines the suit is $\heartsuit$, and counts 6 steps clockwise to find $3\heartsuit$. 

### 2.3 Limits of the Trick 

Could the trick work if only 4 cards were selected and 3 revealed? 
* Here $|X| = \binom{52}{4} = 270,725$ sets of 4 cards. 
* $|Y| = 52 \cdot 51 \cdot 50 = 132,600$ sequences of 3 cards. 
Since $|X| > |Y|$, by the Pigeonhole Principle, some sequence of 3 cards must correspond to multiple distinct sets of 4 cards. Thus, no such matching can exist. 

---

## 3 The Bookkeeper Rule 

### 3.1 Sequences of Subsets 

A $(k_1, k_2, \dots, k_m)$-split of an $n$-element set $A$ (where $\sum k_i = n$) is a sequence of disjoint subsets $(A_1, \dots, A_m)$ such that $|A_i| = k_i$. 

**Rule 2 (Subset Split Rule).** The number of $(k_1, k_2, \dots, k_m)$-splits of an $n$-element set is: 
$$\binom{n}{k_1, k_2, \dots, k_m} = \frac{n!}{k_1! \cdot k_2! \dots k_m!}$$

### 3.2 Sequences with Repetitions 

We can map splits of positions to arrangements of letters. For example, to find the number of permutations of the letters in `BOOKKEEPER` (1 B, 2 O, 2 K, 3 E, 1 P, 1 R): 

**Rule 3 (Bookkeeper Rule).** Let $l_1, \dots, l_m$ be distinct elements. The number of sequences with $k_1$ occurrences of $l_1$, $k_2$ occurrences of $l_2$, $\dots$, and $k_m$ occurrences of $l_m$ is: 
$$\frac{(k_1 + k_2 + \dots + k_m)!}{k_1! \cdot k_2! \dots k_m!}$$

For `BOOKKEEPER`, this is: 
$$\frac{10!}{1! \cdot 2! \cdot 2! \cdot 3! \cdot 1! \cdot 1!} = 151,200$$

#### Example: Walks in a Grid
A 20-mile walk consisting of 5 north, 5 east, 5 south, and 5 west steps corresponds to sequences with 5 $N$'s, 5 $E$'s, 5 $S$'s, and 5 $W$'s. By the Bookkeeper Rule: 
$$\text{Total Walks} = \frac{20!}{(5!)^4}$$

---

## 4 Poker Hands 

In a standard 52-card deck, there are 4 suits ($\spadesuit, \heartsuit, \clubsuit, \diamondsuit$) and 13 values ($2, \dots, 10, J, Q, K, A$). The total number of 5-card poker hands is: 
$$\binom{52}{5} = 2,598,960$$

### 4.1 Four of a Kind 
A hand containing 4 cards of one value and 1 card of another. 
* Choose the value of the four cards: 13 ways. 
* Choose the value of the extra card: 12 ways. 
* Choose the suit of the extra card: 4 ways. 
$$\text{Total} = 13 \cdot 12 \cdot 4 = 624 \text{ hands}$$

### 4.2 Full House 
A hand containing 3 cards of one value and 2 of another. 
* Choose the value of the triple: 13 ways. 
* Choose the suits of the triple: $\binom{4}{3}$ ways. 
* Choose the value of the pair: 12 ways. 
* Choose the suits of the pair: $\binom{4}{2}$ ways. 
$$\text{Total} = 13 \cdot \binom{4}{3} \cdot 12 \cdot \binom{4}{2} = 3,744 \text{ hands}$$

### 4.3 Two Pairs 
A hand containing 2 cards of one value, 2 of another, and 1 of a third. 
* Choose the values of the two pairs: $\binom{13}{2}$ ways. 
* Choose the suits of the lower-value pair: $\binom{4}{2}$ ways. 
* Choose the suits of the higher-value pair: $\binom{4}{2}$ ways. 
* Choose the value of the extra card: 11 ways. 
* Choose the suit of the extra card: 4 ways. 
$$\text{Total} = \binom{13}{2} \cdot \binom{4}{2} \cdot \binom{4}{2} \cdot 11 \cdot 4 = 123,552 \text{ hands}$$

### 4.4 Every Suit 
A hand containing at least one card from each of the 4 suits. 
* Choose the value of the card for each of the 4 suits: $13^4$ ways. 
* Choose which suit has the 5th card: 4 ways. 
* Choose the value of the 5th card: 12 ways. 
Since the two cards in the doubled suit are indistinguishable, this mapping is 2-to-1. Dividing by 2: 
$$\text{Total} = \frac{13^4 \cdot 4 \cdot 12}{2} = 685,464 \text{ hands}$$

---

## 5 Binomial and Multinomial Theorems 

### 5.1 Binomial Theorem 

By expanding $(a+b)^n$, the coefficient of $a^{n-k}b^k$ is the number of sequences of length $n$ with $k$ $b$'s, which is $\binom{n}{k}$: 

**Theorem 5.1 (Binomial Theorem).** For all $n \in \mathbb{N}$ and $a, b \in \mathbb{R}$: 
$$(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$

### 5.2 Multinomial Theorem 

By expanding $(z_1 + \dots + z_m)^n$, the coefficient of $z_1^{k_1} \dots z_m^{k_m}$ is the number of sequences with $k_i$ occurrences of $z_i$: 

**Theorem 5.2 (Multinomial Theorem).** For all $n \in \mathbb{N}$ and $z_1, \dots, z_m \in \mathbb{R}$: 
$$(z_1 + z_2 + \dots + z_m)^n = \sum_{\substack{k_1, \dots, k_m \ge 0 \\ k_1 + \dots + k_m = n}} \binom{n}{k_1, \dots, k_m} z_1^{k_1} \dots z_m^{k_m}$$
where the multinomial coefficient is defined as: 
$$\binom{n}{k_1, \dots, k_m} = \frac{n!}{k_1! \dots k_m!}$$

---

## 6 Combinatorial Proofs 

A combinatorial proof is an argument that establishes an algebraic identity by showing that both sides count the size of the same set $S$ in two different ways. 

### 6.1 Pascal's Identity 

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

**Combinatorial Proof.** Let $S$ be the collection of all $k$-element subsets of $\{1, 2, \dots, n\}$. By definition, $|S| = \binom{n}{k}$. 
Alternatively, partition $S$ into two disjoint cases based on whether a specific element (say, $n$) is chosen: 
* **Case 1 (contains $n$):** We must choose $k-1$ remaining elements from $\{1, \dots, n-1\}$. There are $\binom{n-1}{k-1}$ ways. 
* **Case 2 (does not contain $n$):** We must choose all $k$ elements from $\{1, \dots, n-1\}$. There are $\binom{n-1}{k}$ ways. 

By the Sum Rule, $|S| = \binom{n-1}{k-1} + \binom{n-1}{k}$. Equating the two expressions yields the identity. $\blacksquare$

### 6.2 Vandermonde's Identity (Example Variation) 

**Theorem 6.1.** 
$$\sum_{r=0}^n \binom{n}{r} \binom{2n}{n-r} = \binom{3n}{n}$$

**Combinatorial Proof.** Let $S$ be the set of all $n$-card hands chosen from a deck of $3n$ cards containing $n$ red cards and $2n$ black cards. 
* **Counting Method 1:** We choose $n$ cards out of $3n$ total cards. There are $\binom{3n}{n}$ ways. 
* **Counting Method 2:** We can partition the selection based on the number of red cards $r$ chosen, where $0 \le r \le n$. For a fixed $r$, we choose $r$ red cards (in $\binom{n}{r}$ ways) and $n-r$ black cards (in $\binom{2n}{n-r}$ ways). 

Summing over all possible values of $r$ gives $\sum_{r=0}^n \binom{n}{r} \binom{2n}{n-r}$. 
Both methods count the size of $S$, so their values must be equal. $\blacksquare$
