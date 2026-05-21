# State Machines: Invariants and Termination 

## 1 State Machines 

State machines are an abstract model of step-by-step processes, and accordingly, they come up in many areas of Computer Science. You may already have seen them in a digital logic course, a compiler course, or a probability course. 

### 1.1 Basic Definitions 

A state machine is really nothing more than a digraph, except that the vertices are called “states” and the edges are called “transitions.” The transition from state $p$ to state $q$ is written $p \longrightarrow q$. 

A state machine also comes equipped with a designated start state. 

### 1.2 Examples 

**Example 1.1 (Bounded Counter).** A bounded counter counts from 0 to 99 and overflows at 100. 
```
(0) --start--> (1) ----> (2) ----> ... ----> (99) ----> (overflow)
                                                           ^
                                                           |
                                                           \-- (loop)
```
*Figure 1: The state graph of the 99-bounded counter.*

This machine has no way to get out of its overflow state once reached. 

**Example 1.2 (Unbounded Counter).** An unbounded counter is similar, but has an infinite state set: $\{0, 1, 2, 3, \dots\}$. 

**Example 1.3 (Die Hard 3 Scenario).** We can model the 3 and 5 gallon jugs as a state machine. 
* **States:** Pairs $(b, l)$ of real numbers such that $0 \le b \le 5$ and $0 \le l \le 3$. 
* **Start state:** $(0, 0)$. 
* **Transitions:** 
  1. Fill the little jug: $(b, l) \longrightarrow (b, 3)$ for $l < 3$. 
  2. Fill the big jug: $(b, l) \longrightarrow (5, l)$ for $b < 5$. 
  3. Empty the little jug: $(b, l) \longrightarrow (b, 0)$ for $l > 0$. 
  4. Empty the big jug: $(b, l) \longrightarrow (0, l)$ for $b > 0$. 
  5. Pour from the little jug into the big jug: for $l > 0$, 
     * $(b, l) \longrightarrow (b + l, 0)$ if $b + l \le 5$, 
     * $(b, l) \longrightarrow (5, l - (5 - b))$ otherwise. 
  6. Pour from the big jug into the little jug: for $b > 0$, 
     * $(b, l) \longrightarrow (0, b + l)$ if $b + l \le 3$, 
     * $(b, l) \longrightarrow (b - (3 - l), 3)$ otherwise. 

### 1.3 Executions of State Machines 

A (possibly infinite) path through the state machine graph beginning at the start state corresponds to a possible system behavior; such a path is called an **execution** of the state machine. A state is called **reachable** if there is a path to it starting from the start state. 

---

## 2 Reachability and Invariants 

**Definition 2.1.** An **invariant** for a state machine is a predicate, $P$, on states, such that whenever $P(q)$ is true of a state $q$, and $q \longrightarrow r$ is a transition to state $r$, then $P(r)$ holds. 

**Theorem 2.2 (Invariant Theorem).** Let $P$ be an invariant predicate for a state machine. If $P$ holds for the start state, then $P$ holds for all reachable states. 

### 2.1 Die Hard Once and For All 

Suppose there is a 9 gallon jug instead of the 5 gallon jug. We model this with a state machine where all occurrences of “5” are replaced by “9.” 

We claim that reaching any state of the form $(4, l)$ is impossible. 

**Proof.** Define the invariant predicate $P((b, l))$ to be: $b$ and $l$ are nonnegative integer multiples of 3. 
* **Base case:** $P((0, 0))$ holds since $0$ is a multiple of 3. 
* **Inductive step:** Assume $P((b, l))$ holds and $(b, l) \longrightarrow (b', l')$. 
  * If the transition is *Fill the little jug*, the new state is $(b, 3)$. Since $b$ is a multiple of 3 and 3 is a multiple of 3, $P((b, 3))$ holds. 
  * If the transition is *Pour from big to little* with $b + l > 3$, the new state is $(b - (3 - l), 3)$. Since $b$ and $l$ are multiples of 3, $b - (3 - l) = b + l - 3$ is also a multiple of 3. 
  * All other transitions similarly preserve the multiple-of-3 property. 

By the Invariant Theorem, every reachable state satisfies $P$. Since no state of the form $(4, l)$ satisfies $P$ (as 4 is not a multiple of 3), Bruce can never reach a state with exactly 4 gallons. $\blacksquare$

### 2.2 The Robot 

A robot starts at position $(0, 0)$ on a two-dimensional grid. At each step, it moves one unit north or south and one unit east or west: $(i, j) \longrightarrow (i \pm 1, j \pm 1)$. Can the robot reach $(1, 0)$? 

**Theorem 2.3.** The sum of the robot’s coordinates is always even. 

**Proof.** We use the Invariant Theorem. Let $P((i, j))$ be the predicate that $i + j$ is even. 
* **Base case:** $P((0, 0))$ is true because $0 + 0 = 0$ is even. 
* **Inductive step:** Assume $i + j$ is even. For any transition $(i, j) \longrightarrow (i', j')$, we have $i' = i \pm 1$ and $j' = j \pm 1$. Thus, $i' + j' = (i \pm 1) + (j \pm 1) = i + j + c$ where $c \in \{-2, 0, 2\}$. Since $i + j$ is even and $c$ is even, $i' + j'$ is also even. 

By the Invariant Theorem, $P$ holds for all reachable states. $\blacksquare$

**Corollary 2.4.** The robot cannot reach $(1, 0)$ (since $1 + 0 = 1$ is odd). 

---

## 3 Sequential Algorithms 

We distinguish two aspects of algorithm correctness: 
1. **Partial Correctness:** The property that if the process terminates, the final result satisfies the requirements. 
2. **Termination:** The property that the process is guaranteed to halt. 

### 3.1 The Euclidean Algorithm 

We represent the Euclidean GCD algorithm as a state machine. 
* **States:** Pairs of integers $(x, y)$. 
* **Transitions:** $(x, y) \longrightarrow (y, x \text{ rem } y)$ if $y \neq 0$. 

#### 3.1.1 Partial Correctness of GCD 

Let $d ::= \text{gcd}(a, b)$. We want to prove that if the machine terminates at $(x, y)$, then $x = d$. 

**Proof.** Define the state predicate: 
$$P((x, y)) ::= [\text{gcd}(x, y) = d \wedge (x > 0 \vee y > 0)]$$
* **Base case:** $P((a, b))$ holds by definition of $d$. 
* **Inductive step:** Since $\text{gcd}(x, y) = \text{gcd}(y, x \text{ rem } y)$ for all $y \neq 0$, the predicate is invariant. 

By the Invariant Theorem, $P$ holds for all reachable states. Upon termination, we must have $y = 0$. Since $P((x, 0))$ holds, we have $\text{gcd}(x, 0) = d$ and $x > 0$, which implies $x = d$. $\blacksquare$

#### 3.1.2 Termination of GCD 

After any transition $(x, y) \longrightarrow (y, x \text{ rem } y)$, the value of the second coordinate strictly decreases because $(x \text{ rem } y) < y$. Since $y \in \mathbb{N}$, by the Well Ordering Principle, $y$ must eventually reach a minimum value (which is 0, the termination condition). Thus, the algorithm terminates. 

### 3.2 The Extended Euclidean Algorithm 

Given natural numbers $a, b$ with $b > 0$, the following register program halts with $S, T$ containing the coefficients such that $sa + tb = \text{gcd}(a, b)$. 

* **Inputs:** $a, b \in \mathbb{N}, b > 0$. 
* **Registers:** $X, Y, S, T, U, V, Q$. 
* **Initialization:** 
  $$X := a, \quad Y := b, \quad S := 0, \quad T := 1, \quad U := 1, \quad V := 0$$
* **Loop:** 
  * `if Y divides X, then halt` 
  * `else` 
    * $Q := \lfloor X/Y \rfloor$ 
    * Simultaneous assignments: 
      $$\{X := Y, \quad Y := X \text{ rem } Y, \quad U := S, \quad V := T, \quad S := U - Q \cdot S, \quad T := V - Q \cdot T\}$$

We claim the invariant properties are: 
1. $\text{gcd}(X, Y) = \text{gcd}(a, b)$ 
2. $S \cdot a + T \cdot b = Y$ 
3. $U \cdot a + V \cdot b = X$ 

**Proof of Invariants:** 
Invariant (1) is preserved as in the Euclidean algorithm. 
For (2) and (3), let $x, y, s, t, u, v$ be the register values at the start of a loop iteration. After the simultaneous update: 
* $u' = s$, $v' = t$, $x' = y$. Thus, $u'a + v'b = sa + tb = y = x'$, so (3) holds. 
* $s' = u - qs$, $t' = v - qt$, $y' = x - qy$. Thus: 
  $$s'a + t'b = (u - qs)a + (v - qt)b = (ua + vb) - q(sa + tb) = x - qy = y'$$
  So (2) holds. 

At the start, $S \cdot a + T \cdot b = 0 \cdot a + 1 \cdot b = b = Y$, and $U \cdot a + V \cdot b = 1 \cdot a + 0 \cdot b = a = X$. So all invariants hold initially. By the Invariant Theorem, they hold upon termination, giving $\text{gcd}(a, b) = Y = S \cdot a + T \cdot b$. $\blacksquare$

---

## 4 Derived Variables 

A derived variable assigns a value to each state (a function $f : \text{states} \longrightarrow A$). 

**Definition 4.1.** Let $\preceq$ be a partial order on a set $A$. A derived variable $f : \text{states} \longrightarrow A$ is **strictly decreasing** iff: 
$$q \longrightarrow q' \implies f(q') \prec f(q)$$
It is **weakly decreasing** iff: 
$$q \longrightarrow q' \implies f(q') \preceq f(q)$$

**Theorem 4.2.** If $f$ is a strictly decreasing derived variable of a state machine taking values in $\mathbb{N}$, then the length of any execution starting at state $q$ is at most $f(q)$. 

**Corollary 4.3.** If there exists a strictly decreasing natural-number-valued derived variable, then every execution of that machine terminates. 

---

## 5 The Stable Marriage Problem 

Suppose there are $n$ boys and $n$ girls. Each boy ranks all the girls, and each girl ranks all the boys, with no ties. 

**Definition 5.1.** A set of marriages is **unstable** if there is a boy and a girl who prefer each other to their current spouses (called a **rogue couple**). Otherwise, the set of marriages is **stable**. 

### 5.1 The Preferences 

As an example, consider the preferences below: 

#### Boys' Preferences
* **1:** C, B, E, A, D 
* **2:** A, B, E, C, D 
* **3:** D, C, B, A, E 
* **4:** A, C, D, B, E 
* **5:** A, B, D, E, C 

#### Girls' Preferences
* **A:** 3, 5, 2, 1, 4 
* **B:** 5, 2, 1, 4, 3 
* **C:** 4, 3, 5, 1, 2 
* **D:** 1, 2, 3, 4, 5 
* **E:** 2, 3, 4, 1, 5 

### 5.2 The Mating Algorithm 

The Gale-Shapley Mating Algorithm runs in daily rounds: 
* **Morning:** Each girl stands on her balcony. Each boy stands under the balcony of his favorite girl remaining on his list and serenades her. (If his list is empty, he stays home). 
* **Afternoon:** Each girl who has suitors says to her favorite suitor: “Maybe... come back tomorrow.” To the others, she says: “No, take a hike!” 
* **Evening:** Any boy told to take a hike crosses that girl off his list. 
* **Termination:** When every girl has at most one suitor, the ritual ends, and each girl marries her suitor. 

### 5.3 Termination 

There are $n$ girls on each of the $n$ boys’ lists, for a total of $n^2$ list entries. Since at least one girl is crossed off some boy's list each day the algorithm continues, it must terminate in at most $n^2$ days. 

### 5.4 Correctness 

**Invariant:** For every girl $G$ and every boy $B$, if $G$ is crossed off $B$’s list, then $G$ has a favorite suitor and she prefers him over $B$. 

**Theorem 5.4.** Everyone is married by the Mating Algorithm. 

**Proof.** Suppose for contradiction some boy is unmarried at termination. His list must be empty. By the invariant, every girl must have a suitor she prefers to him, meaning every girl has a suitor and is married. Since there are equal numbers of boys and girls, all boys must also be married, a contradiction. $\blacksquare$

**Theorem 5.5.** The Mating Algorithm produces stable marriages. 

**Proof.** Suppose Bob is married to Alice, but Bob prefers Carole. This means Carole must have been higher on Bob's list than Alice, so Bob must have proposed to Carole and been rejected (crossed Carole off his list). By the invariant, Carole must prefer her husband to Bob. Thus, Bob and Carole cannot form a rogue couple. $\blacksquare$

### 5.5 Optimal and Pessimal Spouses 

**Definition 5.6.** If there is some stable matching in which girl $G$ and boy $B$ are married, then $G$ is a **possible spouse** for $B$, and $B$ is a possible spouse for $G$. 

**Definition 5.7.** A person’s **optimal spouse** is their most preferred possible spouse. A person’s **pessimal spouse** is their least preferred possible spouse. 

**Theorem 5.8.** The Mating Algorithm marries every boy to his optimal spouse, and every girl to her pessimal spouse. 

**Proof.** 
1. **Boys are optimal:** Suppose for contradiction some boy is rejected by his optimal girl. Let $B$ be the first boy rejected by his optimal girl $G$. $G$ rejected $B$ because she received a proposal from some boy $B'$ whom she preferred to $B$. Since $B$ is the first boy rejected by an optimal girl, $B'$ has not yet been rejected by his optimal girl, meaning $B'$ prefers $G$ to any other possible spouse. In any stable matching where $B$ is married to $G$, $B'$ must be married to some other girl $G'$ whom $B'$ likes less than $G$. Since $G$ also prefers $B'$ to $B$, $B'$ and $G$ form a rogue couple, contradicting stability. 
2. **Girls are pessimal:** Suppose in some stable matching $M$, a girl $G$ is married to a boy $B'$ whom she likes less than her Mating Algorithm husband $B$. In the Mating Algorithm, $G$ is $B$'s optimal spouse. Thus, $B$ prefers $G$ to his spouse in $M$. Since $G$ also prefers $B$ to $B'$, $B$ and $G$ form a rogue couple in $M$, contradicting stability. $\blacksquare$
