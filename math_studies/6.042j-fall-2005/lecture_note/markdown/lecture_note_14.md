# Missed Expectations?

## 1 Linearity of Expectation

### 1.1 Expectation of a Sum

Expected values obey a simple, very helpful rule called **Linearity of Expectation**. Its simplest form says that the expected value of a sum of random variables is the sum of the expected values of the variables.

**Theorem 1.1.** For any random variables $R_1$ and $R_2$,
$$\mathbb{E}[R_1 + R_2] = \mathbb{E}[R_1] + \mathbb{E}[R_2].$$

*Proof.* Let $T = R_1 + R_2$. By rearranging terms from the definition of $\mathbb{E}[T]$ we obtain:
$$\mathbb{E}[R_1 + R_2] = \sum_{s\in S} (R_1(s) + R_2(s))\,\Pr\{s\}
= \sum_{s\in S} R_1(s)\,\Pr\{s\} + \sum_{s\in S} R_2(s)\,\Pr\{s\}
= \mathbb{E}[R_1] + \mathbb{E}[R_2].$$

---

### Lemma 1.2
For any random variable $R$ and constant $a\in\mathbb{R}$,
$$\mathbb{E}[aR] = a\,\mathbb{E}[R].$$
(The proof follows directly from the definition of expectation.)

### Theorem 1.3 (Linearity of Expectation)
For any random variables $R_1,\dots,R_k$ and constants $a_1,\dots,a_k\in\mathbb{R}$,
$$\mathbb{E}\Big[\sum_{i=1}^k a_i R_i\Big] = \sum_{i=1}^k a_i\,\mathbb{E}[R_i].$$
No independence assumption is required.

---

## 1.2 Expected Value of Two Dice

Let $R_1$ and $R_2$ be the numbers on two fair dice. Since $\mathbb{E}[R_i]=3.5$, linearity gives
$$\mathbb{E}[R_1+R_2] = 3.5 + 3.5 = 7.$$
This holds even if the dice are not independent, as long as each die remains fair.

---

## 1.3 The Hat‑Check Problem

Consider $n$ men checking their hats. After mixing, each man receives a random hat; the probability he gets his own hat is $1/n$. Let $R$ be the number of men who receive their own hat. Express $R$ as a sum of indicator variables $I_i$, where $I_i=1$ if man $i$ gets his own hat and $0$ otherwise. Then
$$\mathbb{E}[R] = \sum_{i=1}^n \mathbb{E}[I_i] = n\cdot\frac{1}{n}=1.$$
Thus on average one man gets his own hat back.

---

## 1.4 Expectation of a Binomial Distribution

If we flip $n$ independent biased coins with success probability $p$, let $H$ be the number of heads. Writing $H=\sum_{k=1}^n I_k$ where $I_k$ is the indicator of the $k$‑th coin landing heads, linearity yields
$$\mathbb{E}[H] = \sum_{k=1}^n \mathbb{E}[I_k] = np.$$

---

## 2 The Coupon Collector Problem

There are $n$ distinct types of coupons (or “Racin’ Rocket” cars). Let $X_k$ be the number of purchases needed after having collected $k$ distinct types to obtain a new type. The probability of getting a new type is $(n-k)/n$, so by the mean‑time‑to‑failure formula $\mathbb{E}[X_k]=\frac{n}{n-k}$. The total number of purchases $T$ to collect all $n$ types satisfies
$$\mathbb{E}[T] = \sum_{k=0}^{n-1} \frac{n}{n-k} = n\,H_n,$$
where $H_n$ is the $n$‑th harmonic number (approximately $\ln n$).

---

## 3 Conditional Expectation

**Definition 3.1.** For a random variable $R$ and event $A$ with $\Pr(A)>0$,
$$\mathbb{E}[R\mid A] = \sum_{r} r\,\Pr\{R=r\mid A\}.$$
Conditional expectation is linear and satisfies the Law of Total Expectation:
$$\mathbb{E}[R] = \sum_{i} \mathbb{E}[R\mid A_i] \Pr(A_i),$$
for any partition $\{A_i\}$ of the sample space.

---

## 4 The Expected Value of a Product

If $R_1$ and $R_2$ are independent, then
$$\mathbb{E}[R_1R_2] = \mathbb{E}[R_1] \mathbb{E}[R_2].$$
The result extends to any collection of mutually independent variables.

---

## 5 Expect the Mean

Markov’s Theorem provides a simple upper bound for a non‑negative random variable $R$:
$$\Pr\{R \ge x\} \le \frac{\mathbb{E}[R]}{x},\quad x>0.$$
A corollary gives $\Pr\{R \ge c\,\mathbb{E}[R]\} \le \frac{1}{c}$ for $c\ge1$.

---

## 6 Markov’s Theorem for Bounded Variables

If $R$ is non‑negative and we know a lower bound $\ell>0$, then applying Markov to $R-\ell$ often yields a tighter bound.

---

## 7 Chebyshev’s Theorem

With variance $\operatorname{Var}[R]$, Chebyshev’s inequality states
$$\Pr\{|R-\mathbb{E}[R]| \ge x\} \le \frac{\operatorname{Var}[R]}{x^2}.$$
In terms of standard deviation $\sigma_R$, this becomes
$$\Pr\{|R-\mathbb{E}[R]| \ge c\,\sigma_R\} \le \frac{1}{c^2}.$$

---

## 8 Properties of Variance

- **Alternative definition:** $\operatorname{Var}[R] = \mathbb{E}[R^2] - (\mathbb{E}[R])^2$.
- **Scaling:** $\operatorname{Var}[aR+b] = a^2\operatorname{Var}[R]$.
- **Additivity for pairwise independent variables:** If $R_1,\dots,R_n$ are pairwise independent, then $\operatorname{Var}\big[\sum_i R_i\big] = \sum_i \operatorname{Var}[R_i]$.

---

## 9 Variance of Common Distributions

For a Bernoulli variable $B$ with $\Pr(B=1)=p$, $\operatorname{Var}[B]=p(1-p)$. For a Binomial$(n,p)$ variable $H$, $\operatorname{Var}[H]=np(1-p)$. The variance of a sum of independent variables is the sum of their variances.

---

## 10 Estimation by Random Sampling

### 10.1 Estimating Voting Preferences
To estimate the unknown fraction $p$ of a population supporting a candidate (e.g., from Lecture 13), we poll $n$ randomly selected voters. Let $S_n$ be the number of voters in the sample who support the candidate. We use the sample proportion $S_n/n$ as our estimate for $p$.

The variance of $S_n$ (which is binomially distributed) is:
$$\operatorname{Var}[S_n] = n p (1 - p) \le \frac{n}{4},$$
since $p(1-p)$ is maximized at $p = 1/2$.

The variance of our estimate $S_n/n$ is:
$$\operatorname{Var}\left[\frac{S_n}{n}\right] = \frac{1}{n^2} \operatorname{Var}[S_n] \le \frac{1}{4n}.$$

Applying Chebyshev's Theorem to find the probability that our estimate deviates from $p$ by $\ge 0.04$:
$$\Pr\left( \left| \frac{S_n}{n} - p \right| \ge 0.04 \right) \le \frac{\operatorname{Var}[S_n/n]}{(0.04)^2} \le \frac{1}{4n(0.0016)} = \frac{156.25}{n}.$$

To achieve a $95\%$ confidence level (meaning the error probability is $\le 0.05$):
$$\frac{156.25}{n} \le 0.05 \implies n \ge 3125.$$

*Note:* While the binomial distribution method in Lecture 13 required only $n \approx 664$ samples for the same confidence, Chebyshev’s inequality is more general and does not assume a binomial distribution, though it yields a looser bound.

### 10.2 Birthday Matching
Consider $n$ people with independent and uniformly distributed birthdays in a $365$-day year. Let $E_{i,j}$ be the indicator variable for the event that person $i$ and person $j$ share a birthday ($1 \le i < j \le n$).
- $\Pr(E_{i,j} = 1) = \frac{1}{365}$.
- The events $E_{i,j}$ are pairwise independent but not mutually independent (e.g., if $E_{1,2} = 1$ and $E_{2,3} = 1$, then $E_{1,3} = 1$).

Let $M_n$ be the random variable for the number of matching pairs:
$$M_n = \sum_{1 \le i < j \le n} E_{i,j}.$$

By linearity of expectation:
$$\mathbb{E}[M_n] = \sum_{1 \le i < j \le n} \mathbb{E}[E_{i,j}] = \binom{n}{2} \frac{1}{365}.$$

Since the $E_{i,j}$ variables are pairwise independent, their variances are additive:
$$\operatorname{Var}[M_n] = \sum_{1 \le i < j \le n} \operatorname{Var}[E_{i,j}] = \binom{n}{2} \frac{1}{365}\left(1 - \frac{1}{365}\right).$$

For a class of $n = 100$ students:
$$\mathbb{E}[M_{100}] = \binom{100}{2} \frac{1}{365} \approx 13.56 \approx 14,$$
$$\operatorname{Var}[M_{100}] = 4950 \cdot \frac{364}{365^2} \approx 13.52 < 14.$$

Applying Chebyshev's Theorem:
$$\Pr(|M_{100} - 14| \ge x) \le \frac{\operatorname{Var}[M_{100}]}{x^2} < \frac{14}{x^2}.$$
Setting $x = 6$, there is a $> 61\%$ chance (since $1 - 14/36 \approx 0.611$) that the number of matching birthday pairs is between $8$ and $20$.

---

## 11 Pairwise Independent Sampling

The method of using Chebyshev's inequality on pairwise independent indicators generalizes to arbitrary random variables.

**Theorem (Pairwise Independent Sampling).** Let $G_1, \dots, G_n$ be pairwise independent random variables with the same mean $\mu$ and standard deviation $\sigma$. Define:
$$S_n = \sum_{i=1}^n G_i.$$
Then:
$$\Pr\left( \left| \frac{S_n}{n} - \mu \right| \ge x \right) \le \frac{1}{n} \left( \frac{\sigma}{x} \right)^2.$$

This theorem shows that for any pairwise independent samples, the sample average $\frac{S_n}{n}$ converges to the true mean $\mu$ as $n \to \infty$.

---

*Copyright © 2005, Prof. Albert R. Meyer and Prof. Ronitt Rubinfeld.*
