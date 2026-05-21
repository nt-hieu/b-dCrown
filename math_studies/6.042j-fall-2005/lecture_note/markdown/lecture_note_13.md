# Random Variables, Distributions, and Expectation 

Events represent binary states—either they happen or they do not. To model degrees of outcomes (e.g., how much money is won, how long a system runs), we use random variables. 

---

## 1 Random Variables 

### 1.1 Definition 
A **random variable** $R$ is a function mapping outcomes of a sample space $S$ to a codomain $V$ (usually a subset of the real numbers $\mathbb{R}$): 
$$R : S \longrightarrow V$$

For example, if we flip three independent, unbiased coins: 
* The sample space is $S = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$. 
* Let $C(w)$ be the number of heads in outcome $w$. $C$ is a random variable mapping each outcome to $\{0, 1, 2, 3\}$. 
* Let $M(w)$ be $1$ if the coins are all the same (all heads or all tails) and $0$ otherwise. $M$ is an indicator random variable. 

### 1.2 Indicator Random Variables 
An **indicator random variable** (or Bernoulli random variable) is a random variable that maps every outcome to either $0$ or $1$. 

Every event $E \subseteq S$ has an associated indicator variable $I_E$: 
$$I_E(w) = \begin{cases} 
1 & \text{if } w \in E \\ 
0 & \text{if } w \notin E 
\end{cases}$$

### 1.3 Random Variables and Events 
Any equation or inequality involving random variables defines an event. For example, if $C$ is the number of heads in three coin flips: 
* The event $C = 2$ is $\{THH, HTH, HHT\}$, with probability: 
  $$\Pr(C = 2) = \Pr(THH) + \Pr(HTH) + \Pr(HHT) = \frac{3}{8}$$
* The event $C \le 1$ is $\{TTT, TTH, THT, HTT\}$, with probability: 
  $$\Pr(C \le 1) = \frac{4}{8} = \frac{1}{2}$$

### 1.4 Independence 
Two random variables $R_1$ and $R_2$ are independent if for all $x_1 \in \text{Range}(R_1)$ and $x_2 \in \text{Range}(R_2)$: 
$$\Pr(R_1 = x_1 \cap R_2 = x_2) = \Pr(R_1 = x_1) \cdot \Pr(R_2 = x_2)$$

A set of random variables $R_1, \dots, R_n$ is mutually independent if for all $x_1, \dots, x_n$ in their respective ranges: 
$$\Pr\left(\bigcap_{i=1}^n R_i = x_i \right) = \prod_{i=1}^n \Pr(R_i = x_i)$$

---

## 2 The Birthday Principle 

Let $n$ be the number of people in a room and $d$ be the number of days in the year. Assuming birthdays are independent and uniformly distributed, the probability $\Pr(D)$ that everyone has a distinct birthday is: 
$$\Pr(D) = \frac{d(d-1)(d-2)\dots(d-n+1)}{d^n} = \prod_{i=0}^{n-1} \left(1 - \frac{i}{d}\right)$$

Using the approximation $1 - x \approx e^{-x}$ for small $x$: 
$$\Pr(D) \approx \prod_{i=0}^{n-1} e^{-i/d} = e^{-\sum_{i=0}^{n-1} i/d} = e^{-\frac{n(n-1)}{2d}}$$

Setting the probability of distinct birthdays to $1/2$ yields: 
$$e^{-\frac{n(n-1)}{2d}} \approx \frac{1}{2} \implies n \approx \sqrt{2d \ln 2} \approx \sqrt{2d}$$

**The Birthday Principle:** If there are $d$ options and we choose $\sqrt{2d}$ items, the probability of at least one collision is approximately $1 - 1/e \approx 0.632$. 

---

## 3 Probability Distributions 

A probability distribution characterizes the behavior of a random variable without reference to its underlying sample space. 

### 3.1 Probability Density Function (PDF) 
The probability density function of a random variable $R$ with range $V$ is $\text{PDF}_R : V \longrightarrow [0, 1]$: 
$$\text{PDF}_R(x) = \Pr(R = x)$$
By definition, $\sum_{x \in V} \text{PDF}_R(x) = 1$. 

### 3.2 Cumulative Distribution Function (CDF) 
The cumulative distribution function is $\text{CDF}_R : \mathbb{R} \longrightarrow [0, 1]$: 
$$\text{CDF}_R(x) = \Pr(R \le x) = \sum_{y \le x} \text{PDF}_R(y)$$

### 3.3 Common Distributions 
* **Bernoulli Distribution (Parameter $p$):** For indicator variables. $\text{PDF}(1) = p$, $\text{PDF}(0) = 1 - p$. 
* **Uniform Distribution (Range $\{1, \dots, N\}$):** $\text{PDF}(k) = \frac{1}{N}$. 
* **Binomial Distribution (Parameters $n, p$):** The number of successes in $n$ independent trials, each with success probability $p$: 
  $$\text{PDF}(k) = \binom{n}{k} p^k (1-p)^{n-k}$$

---

## 4 The Envelope Numbers Game 

Two envelopes contain distinct integers $L$ and $H$ (where $L < H$). You choose one envelope at random and peek at its value. You must then guess if it is the larger value. 

### 4.1 Strategy 
1. Select a threshold $x$ from the half-integers $\{ \frac{1}{2}, \frac{3}{2}, \dots, n - \frac{1}{2} \}$ uniformly at random. 
2. Peek at one envelope, seeing value $p$. 
3. If $p > x$, guess that this envelope contains the larger number ($H$). If $p < x$, guess that the other envelope contains the larger number. 

### 4.2 Analysis of Success 

| Choice of $x$ | Envelope Peeked | Peek Value $p$ | Decision | Outcome | Path Probability |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $x < L$ (too low) | Low ($L$) | $L$ | Guess $L$ is larger (since $L > x$) | Lose | $\frac{L}{n} \cdot \frac{1}{2}$ |
| $x < L$ (too low) | High ($H$) | $H$ | Guess $H$ is larger (since $H > x$) | Win | $\frac{L}{n} \cdot \frac{1}{2}$ |
| $L < x < H$ (just right) | Low ($L$) | $L$ | Guess other is larger (since $L < x$) | Win | $\frac{H-L}{n} \cdot \frac{1}{2}$ |
| $L < x < H$ (just right) | High ($H$) | $H$ | Guess $H$ is larger (since $H > x$) | Win | $\frac{H-L}{n} \cdot \frac{1}{2}$ |
| $x > H$ (too high) | Low ($L$) | $L$ | Guess other is larger (since $L < x$) | Win | $\frac{n-H}{n} \cdot \frac{1}{2}$ |
| $x > H$ (too high) | High ($H$) | $H$ | Guess other is larger (since $H < x$) | Lose | $\frac{n-H}{n} \cdot \frac{1}{2}$ |

Summing the win probabilities: 
$$\Pr(\text{win}) = \frac{L}{2n} + \frac{H-L}{2n} + \frac{H-L}{2n} + \frac{n-H}{2n} = \frac{n + H - L}{2n} = \frac{1}{2} + \frac{H - L}{2n}$$

Since $H \ge L + 1$, we have: 
$$\Pr(\text{win}) \ge \frac{1}{2} + \frac{1}{2n} > \frac{1}{2}$$
This guarantees a win probability strictly greater than $50\%$. 

---

## 5 Approximating the Binomial Distribution 

### 5.1 Entropy and Stirling Bounds 
For $\alpha \in (0, 1)$, we approximate the binomial coefficient using the binary entropy function: 
$$H(\alpha) = \alpha \log_2 \left(\frac{1}{\alpha}\right) + (1-\alpha) \log_2 \left(\frac{1}{1-\alpha}\right)$$
$$\binom{n}{\alpha n} \le \frac{2^{n H(\alpha)}}{\sqrt{2 \pi \alpha (1-\alpha) n}}$$

### 5.2 Binomial Density Approximation 
The probability of getting exactly $\alpha n$ successes in $n$ trials with success probability $p$ is: 
$$\text{PDF}(a n) \le \frac{2^{n H(\alpha)} p^{\alpha n} (1-p)^{(1-\alpha)n}}{\sqrt{2\pi \alpha(1-\alpha)n}}$$

### 5.3 Cumulative Binomial Distribution Bound 
If the fraction of successes $\alpha$ is strictly less than the trial success probability $p$ ($\alpha < p$): 
$$\text{CDF}(\alpha n) = \Pr(J \le \alpha n) \le \left(\frac{1-\alpha}{1 - \alpha/p}\right) \text{PDF}(\alpha n)$$

---

## 6 Polling and Sampling 

To estimate the fraction $p$ of a population that supports a candidate, we sample $n$ random voters independently. Let $S_n = \sum_{i=1}^n K_i$ be the sum of their indicator responses ($K_i = 1$ if they support the candidate). 

We want our sample estimate $\frac{S_n}{n}$ to be within a margin of error $\epsilon$ of the true fraction $p$ with confidence level $1 - \delta$: 
$$\Pr\left( \left| \frac{S_n}{n} - p \right| \ge \epsilon \right) \le \delta$$

### 6.1 Binomial Sampling Theorem 
For any true fraction $p$, the error probability $\delta$ is maximized when $p = 1/2$. For $0 < \epsilon < 1/2$: 
$$\Pr\left( \left| \frac{S_n}{n} - p \right| \ge \epsilon \right) \le \left(\frac{1 + 2\epsilon}{2\epsilon}\right) \frac{2^{-n \left(1 - H\left(1/2 - \epsilon\right)\right)}}{\sqrt{2\pi (1/4 - \epsilon^2)n}}$$

For a margin of error $\epsilon = 0.04$ and confidence level $95\%$ ($\delta \le 0.05$): 
$$\text{Required Sample Size } n \approx 664$$
Notice that the population size does not affect the required sample size. 

---

## 7 Expected Value 

The expected value (or expectation or mean) of a random variable $R$ is the probability-weighted average: 
$$\mathbb{E}[R] ::= \sum_{w \in S} R(w) \Pr(w)$$

### 7.1 Equivalent Formulations 
$$\mathbb{E}[R] = \sum_{x \in \text{Range}(R)} x \cdot \Pr(R = x)$$

For a random variable $R$ taking values in the natural numbers $\mathbb{N} = \{0, 1, 2, \dots\}$: 
$$\mathbb{E}[R] = \sum_{i=0}^\infty \Pr(R > i)$$

### 7.2 Expectation of an Indicator Variable 
If $I_A$ is the indicator variable for event $A$, then: 
$$\mathbb{E}[I_A] = 1 \cdot \Pr(A) + 0 \cdot \Pr(\overline{A}) = \Pr(A)$$

### 7.3 Mean Time to Failure 
Suppose a system fails at each time step independently with probability $p$. Let $R$ be the number of steps until failure. 
$$\Pr(R > i) = (1-p)^i$$
$$\mathbb{E}[R] = \sum_{i=0}^\infty \Pr(R > i) = \sum_{i=0}^\infty (1-p)^i = \frac{1}{1 - (1-p)} = \frac{1}{p}$$

Thus, the expected number of trials until the first failure is $\frac{1}{p}$. 
