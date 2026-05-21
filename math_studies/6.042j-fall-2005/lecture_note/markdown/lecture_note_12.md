# Introduction to Probability 

Probability theory provides a framework for analyzing randomized algorithms, cryptosystems, and complex computer systems (like memory management or branch prediction). 

---

## 1 The Four-Step Method: Monty Hall 

A game show contestant is presented with three doors. Behind one is a car; behind the other two are goats. The contestant picks a door (e.g., Door 1). The host, who knows what is behind each door, opens another door (e.g., Door 3) to reveal a goat, then offers the contestant the option to switch to the remaining closed door (Door 2). 

To find the probability of winning the car by switching, we use a systematic four-step method: 

### 1.1 Step 1: Find the Sample Space 
An outcome of the experiment is defined by a triple: 
$$(\text{Car Location}, \text{Player's Initial Guess}, \text{Door Opened by Host})$$
Let the doors be $A, B$, and $C$. 

We assume: 
* The car is placed uniformly at random: $\Pr(\text{Car at } A) = \Pr(\text{Car at } B) = \Pr(\text{Car at } C) = 1/3$. 
* The player picks a door uniformly at random, independently of the car's location: probability $1/3$. 
* The host must open a different door showing a goat. If the host has a choice (when the player's initial guess was correct), he picks uniformly at random with probability $1/2$. 

The outcomes and their path probabilities are summarized below: 

| Car Location | Initial Guess | Door Opened | Path Probability | Switching Wins? |
| :---: | :---: | :---: | :---: | :---: |
| $A$ | $A$ | $B$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{18}$ | No |
| $A$ | $A$ | $C$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{18}$ | No |
| $A$ | $B$ | $C$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot 1 = \frac{1}{9}$ | Yes |
| $A$ | $C$ | $B$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot 1 = \frac{1}{9}$ | Yes |
| $B$ | $A$ | $C$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot 1 = \frac{1}{9}$ | Yes |
| $B$ | $B$ | $A$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{18}$ | No |
| $B$ | $B$ | $C$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{18}$ | No |
| $B$ | $C$ | $A$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot 1 = \frac{1}{9}$ | Yes |
| $C$ | $A$ | $B$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot 1 = \frac{1}{9}$ | Yes |
| $C$ | $B$ | $A$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot 1 = \frac{1}{9}$ | Yes |
| $C$ | $C$ | $A$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{18}$ | No |
| $C$ | $C$ | $B$ | $\frac{1}{3} \cdot \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{18}$ | No |

The set of all 12 outcomes forms the sample space $S$. 

### 1.2 Step 2: Define Events of Interest 
An event is a subset of the sample space. The event $E$ that "the player wins by switching" contains the outcomes: 
$$E = \{(A,B,C), (A,C,B), (B,A,C), (B,C,A), (C,A,B), (C,B,A)\}$$

### 1.3 Step 3: Determine Outcome Probabilities 
The probability of an outcome is the product of the edge probabilities on the decision tree path (listed in the table under Path Probability). The sum of all outcome probabilities is 1: 
$$\sum_{x \in S} \Pr(x) = 1$$
A sample space $S$ and a probability function $\Pr : S \longrightarrow [0, 1]$ form a probability space. 

### 1.4 Step 4: Compute Event Probabilities 
The probability of an event is the sum of the probabilities of its constituent outcomes: 
$$\Pr(E) = \sum_{x \in E} \Pr(x)$$
For the event $E$ (switching wins): 
$$\Pr(E) = \frac{1}{9} + \frac{1}{9} + \frac{1}{9} + \frac{1}{9} + \frac{1}{9} + \frac{1}{9} = \frac{2}{3}$$
Thus, switching doors wins the car with probability $2/3$. 

### 1.5 Probability Identities 
* **Complementary Events:** $\Pr(E) + \Pr(\overline{E}) = 1$ 
* **Sum Rule (Disjoint Events):** If $E_1, \dots, E_n$ are pairwise disjoint, then: 
  $$\Pr(E_1 \cup \dots \cup E_n) = \sum_{i=1}^n \Pr(E_i)$$
* **Inclusion-Exclusion:** 
  $$\Pr(E_1 \cup E_2) = \Pr(E_1) + \Pr(E_2) - \Pr(E_1 \cap E_2)$$
* **Union Bound:** For any events $E_1, \dots, E_n$: 
  $$\Pr(E_1 \cup \dots \cup E_n) \le \sum_{i=1}^n \Pr(E_i)$$

---

## 2 Infinite Sample Spaces 

Suppose two players take turns flipping a fair coin. Whoever flips heads ($H$) first wins. What is the probability that the first player wins? 
The game has an infinite sample space of outcomes: $\{H, TH, TTH, TTTH, \dots\}$. 
* The first player wins on outcomes: $\{H, TTH, TTTTH, \dots\}$ 
* The probabilities of these outcomes are: $\frac{1}{2}, \frac{1}{8}, \frac{1}{32}, \dots$ 

Summing this infinite geometric series: 
$$\Pr(\text{First player wins}) = \sum_{k=0}^\infty \frac{1}{2^{2k+1}} = \frac{1}{2} \sum_{k=0}^\infty \left(\frac{1}{4}\right)^k = \frac{1}{2} \left( \frac{1}{1 - 1/4} \right) = \frac{2}{3}$$
$$\Pr(\text{Second player wins}) = \sum_{k=1}^\infty \frac{1}{2^{2k}} = \frac{1}{4} \sum_{k=0}^\infty \left(\frac{1}{4}\right)^k = \frac{1}{3}$$

---

## 3 Conditional Probability 

Conditional probability measures the probability of an event $A$, given that another event $B$ has occurred: 
$$\Pr(A \mid B) ::= \frac{\Pr(A \cap B)}{\Pr(B)} \quad (\text{defined only if } \Pr(B) > 0)$$

### 3.1 Best-of-Three Tournament Example 
A team plays a best-of-three tournament. They win the first game with probability $1/2$. In subsequent games, the probability of winning is: 
* $2/3$ if they won the previous game (positive momentum). 
* $1/3$ if they lost the previous game (negative momentum). 

What is the probability that the team wins the tournament (event $A$), given that they won the first game (event $B$)? 
The tournament outcomes and their probabilities are: 

| Game 1 | Game 2 | Game 3 | Path Probability | Series Winner? |
| :---: | :---: | :---: | :---: | :---: |
| $W$ | $W$ | — | $\frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3}$ | Yes |
| $W$ | $L$ | $W$ | $\frac{1}{2} \cdot \frac{1}{3} \cdot \frac{1}{3} = \frac{1}{18}$ | Yes |
| $W$ | $L$ | $L$ | $\frac{1}{2} \cdot \frac{1}{3} \cdot \frac{2}{3} = \frac{1}{9}$ | No |
| $L$ | $W$ | $W$ | $\frac{1}{2} \cdot \frac{1}{3} \cdot \frac{2}{3} = \frac{1}{9}$ | Yes |
| $L$ | $W$ | $L$ | $\frac{1}{2} \cdot \frac{1}{3} \cdot \frac{1}{3} = \frac{1}{18}$ | No |
| $L$ | $L$ | — | $\frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3}$ | No |

* Event $B$ (wins 1st game) $= \{WW, WLW, WLL\}$. Thus, $\Pr(B) = \frac{1}{3} + \frac{1}{18} + \frac{1}{9} = \frac{1}{2}$. 
* Event $A \cap B$ (wins tournament and wins 1st game) $= \{WW, WLW\}$. Thus, $\Pr(A \cap B) = \frac{1}{3} + \frac{1}{18} = \frac{7}{18}$. 

Applying the definition: 
$$\Pr(A \mid B) = \frac{\Pr(A \cap B)}{\Pr(B)} = \frac{7/18}{1/2} = \frac{7}{9}$$

### 3.2 The Product Rule for Probabilities 
Rearranging the conditional probability definition gives the product rule: 
$$\Pr(A_1 \cap A_2) = \Pr(A_1) \cdot \Pr(A_2 \mid A_1)$$
Generally, for $n$ events: 
$$\Pr(A_1 \cap \dots \cap A_n) = \Pr(A_1) \cdot \Pr(A_2 \mid A_1) \cdot \Pr(A_3 \mid A_1 \cap A_2) \dots \Pr(A_n \mid A_1 \cap \dots \cap A_{n-1})$$

### 3.3 The Law of Total Probability 
For case analysis based on whether event $E$ occurs: 
$$\Pr(A) = \Pr(A \mid E) \cdot \Pr(E) + \Pr(A \mid \overline{E}) \cdot \Pr(\overline{E})$$
Generally, if $E_1, \dots, E_n$ form a partition of the sample space: 
$$\Pr(A) = \sum_{i=1}^n \Pr(A \mid E_i) \cdot \Pr(E_i)$$

### 3.4 A Posteriori Probability: The Coin Problem 
Suppose you are handed either a fair coin (probability $p$) or a double-headed trick coin (probability $1-p$). You flip the coin 100 times and get heads ($H$) every time. What is the probability that the coin is fair? 

Let $A$ be the event that the coin is fair, and $B$ be the event of 100 heads. 
* $\Pr(B \mid A) = 2^{-100}$ 
* $\Pr(B \mid \overline{A}) = 1$ 

By Bayes' Rule / Conditional Probability: 
$$\Pr(A \mid B) = \frac{\Pr(A \cap B)}{\Pr(B)} = \frac{\Pr(B \mid A)\Pr(A)}{\Pr(B \mid A)\Pr(A) + \Pr(B \mid \overline{A})\Pr(\overline{A})} = \frac{p \cdot 2^{-100}}{p \cdot 2^{-100} + (1-p)}$$
$$\Pr(A \mid B) = \frac{p}{p + (1-p)2^{100}}$$
Unless $p$ is extremely close to 1, this probability is virtually zero, meaning the coin is almost certainly the trick coin. 

### 3.5 Medical Testing 
A disease $X$ affects 10% of the population. A diagnostic test has: 
* A 10% false negative rate: $\Pr(\text{negative} \mid \text{sick}) = 0.10$. 
* A 30% false positive rate: $\Pr(\text{positive} \mid \text{healthy}) = 0.30$. 

If a random person tests positive, what is the probability they actually have the disease? 
Let $A$ be the event of having the disease, and $B$ be the event of testing positive. 
$$\Pr(A) = 0.10, \quad \Pr(\overline{A}) = 0.90$$
$$\Pr(B \mid A) = 1 - 0.10 = 0.90, \quad \Pr(B \mid \overline{A}) = 0.30$$

Using the Law of Total Probability for the denominator: 
$$\Pr(A \mid B) = \frac{\Pr(B \mid A)\Pr(A)}{\Pr(B \mid A)\Pr(A) + \Pr(B \mid \overline{A})\Pr(\overline{A})} = \frac{0.90 \cdot 0.10}{0.90 \cdot 0.10 + 0.30 \cdot 0.90} = \frac{0.09}{0.09 + 0.27} = \frac{0.09}{0.36} = 25\%$$
Thus, there is only a 25% chance that a person testing positive is sick. 

---

## 4 Independence 

### 4.1 Definition 
Two events $A$ and $B$ are independent if and only if: 
$$\Pr(A \cap B) = \Pr(A) \cdot \Pr(B)$$

If $\Pr(B) > 0$, this is equivalent to: 
$$\Pr(A \mid B) = \Pr(A)$$

### 4.2 Disjointness vs. Independence 
If $A$ and $B$ are disjoint, $\Pr(A \cap B) = 0$. If both have positive probabilities, then $\Pr(A)\Pr(B) > 0$. Thus, disjoint events are **never** independent. 

---

## 5 Mutual vs. Pairwise Independence 

### 5.1 Mutual Independence 
A set of events $E_1, \dots, E_n$ is mutually independent if and only if for every subset $I \subseteq \{1, \dots, n\}$: 
$$\Pr\left(\bigcap_{i \in I} E_i\right) = \prod_{i \in I} \Pr(E_i)$$

### 5.2 Pairwise Independence 
A set of events is pairwise independent if every pair is independent: $\Pr(E_i \cap E_j) = \Pr(E_i)\Pr(E_j)$ for all $i \neq j$. 

#### Example: Pairwise but not Mutually Independent
Flip three independent, fair coins. Define events: 
* $A_1$: Coin 1 and Coin 2 match. 
* $A_2$: Coin 2 and Coin 3 match. 
* $A_3$: Coin 3 and Coin 1 match. 

The probability of each event is $1/2$. For any pair, e.g., $A_1$ and $A_2$: 
$$\Pr(A_1 \cap A_2) = \Pr(HHH \text{ or } TTT) = \frac{2}{8} = \frac{1}{4} = \Pr(A_1)\Pr(A_2)$$
Thus, the events are pairwise independent. 

However, if $A_1$ and $A_2$ both occur, then Coin 1 matches Coin 2, and Coin 2 matches Coin 3. This forces Coin 3 to match Coin 1, meaning $A_3$ must occur: 
$$\Pr(A_1 \cap A_2 \cap A_3) = \Pr(HHH \text{ or } TTT) = \frac{1}{4} \neq \Pr(A_1)\Pr(A_2)\Pr(A_3) = \frac{1}{8}$$
Thus, $A_1, A_2, A_3$ are not mutually independent. 
