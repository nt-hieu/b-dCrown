# Sums, Products & Asymptotics 

## 1 Closed Forms and Approximations 

Sums and products arise regularly in the analysis of algorithms and in other technical areas such as finance and probabilistic systems. We have already seen that: 
$$\sum_{i=1}^n i = \frac{n(n + 1)}{2}$$

Having a simple closed form expression such as $n(n+1)/2$ makes the sum a lot easier to understand and evaluate. Even when there are no closed forms exactly equal to a sum, we may still be able to find a closed form that approximates it with useful accuracy. 

The product we focus on in these notes is the familiar factorial: 
$$n! ::= \prod_{i=1}^n i = 1 \cdot 2 \dots (n - 1) \cdot n$$
We will describe a closed form approximation for it called **Stirling’s Formula**. 

Finally, when there isn't a good closed form approximation, we can use asymptotic notation (like "Big Oh") to describe its growth rate. 

---

## 2 The Value of an Annuity 

An annuity is a financial instrument that pays out a fixed amount of money at the beginning of every year for some specified number of years. In particular, an $n$-year, $m$-payment annuity pays $m$ dollars at the start of each year for $n$ years. 

To determine the value of such an annuity, let's assume that money can be invested at a fixed annual interest rate $p$ (e.g., 8%, or $p = 0.08$). 

### 2.1 The Future Value of Money 

Ten dollars invested today at interest rate $p$ will become $10 \cdot (1 + p)$ dollars in a year, $10 \cdot (1 + p)^2$ in two years, and so forth. Conversely, ten dollars paid out a year from now is only worth $10 / (1 + p)$ dollars today. 

The total present value $V$ of the annuity is equal to the sum of the payment values: 
$$V = \sum_{i=1}^n \frac{m}{(1+p)^{i-1}}$$

Let's simplify this summation with some substitutions: 
$$V = m \sum_{j=0}^{n-1} \left(\frac{1}{1+p}\right)^j \quad (\text{substituting } j = i-1)$$
$$V = m \sum_{j=0}^{n-1} x^j \quad \left(\text{substituting } x = \frac{1}{1+p}\right)$$

### 2.2 Geometric Sums 

**Theorem 2.1.** For all $n \ge 1$ and all $x \neq 1$, 
$$\sum_{i=0}^{n-1} x^i = \frac{1 - x^n}{1 - x}$$

**Proof.** Let $S$ be the value of the sum: 
$$S = 1 + x + x^2 + \dots + x^{n-1}$$
$$-xS = -x - x^2 - x^3 - \dots - x^n$$
Adding these two equations gives: 
$$S - xS = 1 - x^n \implies S(1 - x) = 1 - x^n \implies S = \frac{1 - x^n}{1 - x}$$
$\blacksquare$

### 2.3 Return of the Annuity Problem 

We can now solve the annuity pricing problem by applying Theorem 2.1: 
$$V = m \sum_{j=0}^{n-1} x^j = m \frac{1 - x^n}{1 - x}$$
Undo the substitution $x = 1/(1+p)$: 
$$V = m \frac{1 - \left(\frac{1}{1+p}\right)^n}{1 - \frac{1}{1+p}} = m \frac{1+p - \left(\frac{1}{1+p}\right)^{n-1}}{p}$$

For example, a lottery ticket paying $m = \$50,000$ per year for $n = 20$ years at interest rate $p = 0.08$ is worth: 
$$V = 50000 \cdot \frac{1.08 - (1.08)^{-19}}{0.08} \approx \$530,180$$

### 2.4 Infinite Geometric Series 

If an annuity pays out forever ($n \to \infty$), we take the limit of the geometric sum: 

**Theorem 2.2.** If $|x| < 1$, then: 
$$\sum_{i=0}^\infty x^i = \frac{1}{1 - x}$$

**Proof.** 
$$\sum_{i=0}^\infty x^i = \lim_{n \to \infty} \sum_{i=0}^{n-1} x^i = \lim_{n \to \infty} \frac{1 - x^n}{1 - x} = \frac{1}{1 - x}$$
since $x^n \to 0$ when $|x| < 1$. $\blacksquare$

For our infinite annuity: 
$$V = m \cdot \frac{1}{1 - x} = m \cdot \frac{1}{1 - 1/(1+p)} = m \frac{1+p}{p}$$
If $m = \$50,000$ and $p = 0.08$, the present value is only $\$675,000$. 

### 2.5 Examples 

* **Finite / Infinite Sums:** 
  $$\sum_{i=0}^\infty \left(\frac{1}{2}\right)^i = \frac{1}{1 - 1/2} = 2$$
  $$0.999\dots = 0.9 \sum_{i=0}^\infty \left(\frac{1}{10}\right)^i = 0.9 \cdot \frac{1}{1 - 1/10} = 1$$
  $$\sum_{i=0}^\infty \left(-\frac{1}{2}\right)^i = \frac{1}{1 - (-1/2)} = \frac{2}{3}$$
  $$\sum_{i=0}^{n-1} 2^i = 2^n - 1$$
  $$\sum_{i=0}^{n-1} 3^i = \frac{3^n - 1}{2}$$

**Rule of Thumb:** A geometric sum or series is approximately equal to the term with the greatest absolute value. 

### 2.6 Bounding and Differentiating Sums 

A useful way to obtain new summation formulas from old is by differentiating both sides of a formula with respect to $x$. 

Consider the sum $\sum_{i=1}^n i x^i = x + 2x^2 + 3x^3 + \dots + n x^n$. 
Start with the geometric sum formula: 
$$\sum_{i=0}^n x^i = \frac{1 - x^{n+1}}{1 - x}$$
Differentiating both sides with respect to $x$: 
$$\sum_{i=1}^n i x^{i-1} = \frac{-(n+1)x^n(1-x) - (-1)(1-x^{n+1})}{(1-x)^2} = \frac{1 - (n+1)x^n + n x^{n+1}}{(1-x)^2}$$
Multiplying by $x$: 
$$\sum_{i=1}^n i x^i = \frac{x - (n+1)x^{n+1} + n x^{n+2}}{(1-x)^2}$$

**Theorem 2.3.** If $|x| < 1$, then: 
$$\sum_{i=1}^\infty i x^i = \frac{x}{(1 - x)^2}$$

---

## 3 Book Stacking 

Suppose we want to stack $n$ books on a table in some off-center way so the top book sticks out past the edge of the table as far as possible without the stack tipping over. 

### 3.1 Formalizing the Overhang 

Let's define the overhang of a stable stack of $n$ books, $B_n$, recursively: 
* The overhang of 1 book is $B_1 = 1/2$. 
* The maximum overhang $B_{n+1}$ of a stack of $n+1$ books is obtained by placing a maximum overhang stable stack of $n$ books on top of the bottom book, placing the center of mass of the top $n$ books right over the edge of the bottom book. 

Choosing the center of mass of the top $n$ books as the origin, the horizontal coordinate of the bottom book is $1/2$. The center of mass of the whole stack of $n+1$ books is: 
$$\frac{n \cdot 0 + 1 \cdot (1/2)}{n + 1} = \frac{1}{2(n+1)}$$
Thus, the increase in overhang is $1/(2(n+1))$. This gives: 
$$B_{n+1} = B_n + \frac{1}{2(n+1)}$$
Expanding this recurrence: 
$$B_n = \frac{1}{2} \sum_{i=1}^n \frac{1}{i}$$

We define the $n$-th **Harmonic number** $H_n$ as: 
$$H_n ::= \sum_{i=1}^n \frac{1}{i}$$
So the maximum overhang is $B_n = \frac{H_n}{2}$. 

### 3.2 Bounding the Harmonic Numbers: The Integral Method 

We can bound the harmonic number using integration: 
$$H_n \le 1 + \int_1^n \frac{1}{x} \, dx = 1 + \ln n$$
$$H_n \ge \int_0^n \frac{1}{x+1} \, dx = \ln(n+1)$$

Since $\ln n$ grows without bound, we can achieve any arbitrary overhang by stacking enough books. 

### 3.3 Asymptotic Behavior 

An even better approximation of $H_n$ is: 
$$H_n = \ln n + \gamma + \frac{1}{2n} - \frac{1}{12n^2} + \frac{\epsilon(n)}{120n^4}$$
where $\gamma \approx 0.577215664\dots$ is Euler's constant and $0 < \epsilon(n) < 1$. 

We use the notation $f(x) \sim g(x)$ to denote asymptotic equality: 

**Definition 3.1.** We say $f(x)$ is asymptotically equal to $g(x)$ (denoted $f(x) \sim g(x)$) iff: 
$$\lim_{x \to \infty} \frac{f(x)}{g(x)} = 1$$

Thus, $H_n \sim \ln n$. 

---

## 4 Finding Summation Formulas 

To find an exact summation formula when the general growth rate is known, we can guess the general form of the solution with parameters and solve a system of linear equations. 

For example, to find a formula for $\sum_{i=1}^n i^2$: 
The integral method bounds it by $\approx n^3/3$. We guess: 
$$\sum_{i=1}^n i^2 = a n^3 + b n^2 + c n + d$$
Evaluate this guess for $n = 0, 1, 2, 3$: 
* $n = 0 \implies 0 = d$ 
* $n = 1 \implies 1 = a + b + c + d$ 
* $n = 2 \implies 5 = 8a + 4b + 2c + d$ 
* $n = 3 \implies 14 = 27a + 9b + 3c + d$ 

Solving this system gives $a = 1/3$, $b = 1/2$, $c = 1/6$, and $d = 0$. This yields: 
$$\sum_{i=1}^n i^2 = \frac{n^3}{3} + \frac{n^2}{2} + \frac{n}{6} = \frac{n(n+1)(2n+1)}{6}$$

---

## 5 Double Sums 

A useful trick for evaluating double sums is exchanging the order of summation. 

Consider $\sum_{k=1}^n H_k = \sum_{k=1}^n \sum_{j=1}^k \frac{1}{j}$. The pairs $(k, j)$ over which we sum form a triangular grid: 

| $k$ | $j=1$ | $j=2$ | $j=3$ | $\dots$ | $j=n$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | $1$ | | | | |
| **2** | $1$ | $1/2$ | | | |
| **3** | $1$ | $1/2$ | $1/3$ | | |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ | |
| **$n$** | $1$ | $1/2$ | $\dots$ | $\dots$ | $1/n$ |

Summing columns first instead of rows: 
$$\sum_{k=1}^n H_k = \sum_{j=1}^n \sum_{k=j}^n \frac{1}{j} = \sum_{j=1}^n \frac{n - j + 1}{j}$$
$$= \sum_{j=1}^n \left(\frac{n+1}{j} - 1\right) = (n+1)H_n - n$$

---

## 6 Stirling’s Approximation 

To estimate $n!$, we take its natural logarithm: 
$$\ln(n!) = \sum_{i=1}^n \ln i$$
Using the integral method to bound the sum: 
$$\int_1^n \ln x \, dx \le \sum_{i=1}^n \ln i \le \int_0^n \ln(x+1) \, dx$$
Exponentiating the evaluated integrals yields: 
$$\left(\frac{n}{e}\right)^n e \le n! \le \left(\frac{n+1}{e}\right)^{n+1} e$$

A more precise analysis yields: 

**Theorem 6.1 (Stirling’s Formula).** 
$$n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$$

**Fact (Stirling’s Approximation).** 
$$\sqrt{2\pi n}\left(\frac{n}{e}\right)^n e^{\frac{1}{12n+1}} \le n! \le \sqrt{2\pi n}\left(\frac{n}{e}\right)^n e^{\frac{1}{12n}}$$

---

## 7 Asymptotic Notation 

### 7.1 Little Oh 

**Definition 7.1.** We say $f(x)$ is asymptotically smaller than $g(x)$ (denoted $f(x) = o(g(x))$) iff: 
$$\lim_{x \to \infty} \frac{f(x)}{g(x)} = 0$$

* **Examples:** 
  * $1000 x^{1.9} = o(x^2)$ 
  * $x^a = o(x^b)$ for all $0 \le a < b$ 
  * $\log x = o(x^\epsilon)$ for all $\epsilon > 0$ 
  * $x^b = o(a^x)$ for all $a > 1, b \in \mathbb{R}$ 

### 7.2 Big Oh 

Big Oh is used to give an upper bound on the growth of a function. 

**Definition 7.2.** We say $f(x) = O(g(x))$ iff: 
$$\limsup_{x \to \infty} \frac{|f(x)|}{g(x)} < \infty$$

**Equivalent Definition:** $f(x) = O(g(x))$ iff there exists a constant $c \ge 0$ and a value $x_0$ such that for all $x \ge x_0$: 
$$|f(x)| \le c \cdot g(x)$$

* **Examples:** 
  * $100x^2 = O(x^2)$ 
  * $x^2 + 100x + 10 = O(x^2)$ 
  * For any polynomial, $a_k x^k + a_{k-1} x^{k-1} + \dots + a_0 = O(x^k)$ (if $a_k \neq 0$) 

### 7.3 Theta 

**Definition 7.3.** We say $f(x) = \Theta(g(x))$ iff $f(x) = O(g(x)) \wedge g(x) = O(f(x))$. 

Intuitively, $f(x) = \Theta(g(x))$ means $f$ and $g$ grow at the same rate up to a constant factor. 

### 7.4 Pitfalls with Big Oh 

1. **The Exponential Fiasco:** $4^x \neq O(2^x)$ because $\lim_{x\to\infty} \frac{4^x}{2^x} = \lim_{x\to\infty} 2^x = \infty$. 
2. **Constant Confusion:** We cannot add $O(1)$ terms infinitely: $\sum_{i=1}^n i \neq O(n)$ because the number of terms depends on $n$. 
3. **Lower Bound Blunder:** Do not write "the running time is at least $O(n^2)$". Instead, write $T(n) = \Omega(n^2)$ or $n^2 = O(T(n))$. 
4. **Equality Blunder:** The relation is asymmetric; do not write $O(n) = 2n$. 
