# Introduction to Number Theory 

Number theory is the study of the integers. 

## 1 Divisibility 

We say that $a$ divides $b$ if there is an integer $k$ such that $a k = b$. This is denoted $a \mid b$. For example: 
$$7 \mid 63 \quad \text{because} \quad 7 \cdot 9 = 63$$

A consequence of this definition is that every number divides zero since $a \cdot 0 = 0$ for every integer $a$. If $a$ divides $b$, then $b$ is a multiple of $a$. For example, 63 is a multiple of 7. 

Every time you buy a book from Amazon, check your grades on WebSIS, or use a PayPal account, you are relying on number theoretic algorithms. 

### 1.1 Facts About Divisibility 

**Lemma 1.1.** The following statements about divisibility hold: 
1. If $a \mid b$, then $a \mid bc$ for all $c$. 
2. If $a \mid b$ and $b \mid c$, then $a \mid c$. 
3. If $a \mid b$ and $a \mid c$, then $a \mid (sb + tc)$ for all $s$ and $t$. 
4. For all $c \neq 0$, $a \mid b$ if and only if $ca \mid cb$. 

**Proof.** We’ll only prove part (2); the other proofs are similar. 

*Proof of (2):* Since $a \mid b$, there exists an integer $k_1$ such that $a k_1 = b$. Since $b \mid c$, there exists an integer $k_2$ such that $b k_2 = c$. Substituting $a k_1$ for $b$ in the second equation gives $a k_1 k_2 = c$, which implies that $a \mid c$. $\blacksquare$

A number $p > 1$ with no positive divisors other than 1 and itself is called a **prime**. Every other number greater than 1 is called **composite**. The number 1 is considered neither prime nor composite. 

### 1.2 When Divisibility Goes Bad 

If one number does not evenly divide another, then there is a remainder left over. 

**Theorem 1.2 (Division Theorem).** Let $n$ and $d$ be integers such that $d > 0$. Then there exists a unique pair of integers $q$ and $r$ such that $n = qd + r$ and $0 \le r < d$. 

As an example, suppose that $a = 10$ and $b = 2716$. Then the quotient is $q = 271$ and the remainder is $r = 6$, since $2716 = 271 \cdot 10 + 6$. 

The remainder $r$ in the Division Theorem is denoted $n \text{ rem } d$. In other words, $n \text{ rem } d$ is the remainder when $n$ is divided by $d$. For example, $32 \text{ rem } 5 = 2$. Similarly, $-11 \text{ rem } 7 = 3$, since $-11 = (-2) \cdot 7 + 3$. 

The proof of such an "existence and uniqueness" theorem always has two parts: 
* A proof that something exists, such as the quotient $q$ and remainder $r$. 
* A proof that nothing else fits the bill; that is, there is no other quotient $q'$ and remainder $r'$. 

---

## 2 The Water Jugs Problem 

Suppose that we have water jugs with capacities $a$ and $b$. Let’s carry out a few arbitrary operations and see what happens. The state of the system at each step is described with a pair of numbers $(x, y)$, where $x$ is the amount of water in the jug with capacity $a$ and $y$ is the amount in the jug with capacity $b$. 
$$(0, 0) \longrightarrow (a, 0) \quad \text{fill first jug}$$
$$\longrightarrow (0, a) \quad \text{pour first into second}$$
$$\longrightarrow (a, a) \quad \text{fill first jug}$$
$$\longrightarrow (2a-b, b) \quad \text{pour first into second}$$
$$\longrightarrow (2a-b, 0) \quad \text{empty second jug}$$
$$\longrightarrow (0, 2a-b) \quad \text{pour first into second}$$
$$\longrightarrow (a, 2a-b) \quad \text{fill first}$$
$$\longrightarrow (3a-2b, b) \quad \text{pour first into second}$$

At every step, the amount of water in each jug is of the form: 
$$s \cdot a + t \cdot b \qquad (1)$$
for some integers $s$ and $t$. An expression of the form (1) is called an **integer linear combination** of $a$ and $b$. 

**Lemma 2.1.** Suppose that we have water jugs with capacities $a$ and $b$. Then the amount of water in each jug is always a linear combination of $a$ and $b$. 

---

## 3 The Greatest Common Divisor 

The greatest common divisor of $a$ and $b$ is the largest number that is a divisor of both $a$ and $b$. It is denoted $\text{gcd}(a, b)$. For example, $\text{gcd}(18, 24) = 6$. 

### 3.1 Linear Combinations and the GCD 

**Theorem 3.1.** The greatest common divisor of $a$ and $b$ is equal to the smallest positive linear combination of $a$ and $b$. 

For example, the greatest common divisor of 52 and 44 is 4. And, sure enough, 4 is a linear combination of 52 and 44: 
$$6 \cdot 52 + (-7) \cdot 44 = 4$$
Furthermore, no linear combination of 52 and 44 is equal to a smaller positive integer. 

**Proof.** Let $m$ be the smallest positive linear combination of $a$ and $b$. We’ll prove that $m = \text{gcd}(a, b)$ by showing both $\text{gcd}(a, b) \le m$ and $m \le \text{gcd}(a, b)$. 

First, we show that $\text{gcd}(a, b) \le m$. By the definition of common divisor, $\text{gcd}(a, b) \mid a$ and $\text{gcd}(a, b) \mid b$. Therefore, for every pair of integers $s$ and $t$: 
$$\text{gcd}(a, b) \mid (sa + tb)$$
Thus, in particular, $\text{gcd}(a, b)$ divides $m$, and so $\text{gcd}(a, b) \le m$. 

Now, we show that $m \le \text{gcd}(a, b)$. We do this by showing that $m \mid a$. A symmetric argument shows that $m \mid b$, which means that $m$ is a common divisor of $a$ and $b$. Thus, $m$ must be less than or equal to the greatest common divisor of $a$ and $b$. 

All that remains is to show that $m \mid a$. By the Division Theorem, there exists a quotient $q$ and remainder $r$ such that: 
$$a = q \cdot m + r \quad (\text{where } 0 \le r < m)$$
Recall that $m = sa + tb$ for some integers $s$ and $t$. Substituting in for $m$ and rearranging terms gives: 
$$a = q \cdot (sa + tb) + r$$
$$r = (1 - qs)a + (-qt)b$$
We’ve just expressed $r$ as a linear combination of $a$ and $b$. However, $m$ is the smallest positive linear combination and $0 \le r < m$. The only possibility is that the remainder $r$ is 0. This implies $m \mid a$. $\blacksquare$

**Corollary 3.2.** Every linear combination of $a$ and $b$ is a multiple of $\text{gcd}(a, b)$ and vice versa. 

**Corollary 3.3.** Suppose that we have water jugs with capacities $a$ and $b$. Then the amount of water in each jug is always a multiple of $\text{gcd}(a, b)$. 

For example, there is no way to form 4 gallons using 3 and 6 gallon jugs, because 4 is not a multiple of $\text{gcd}(3, 6) = 3$. 

### 3.2 Properties of the Greatest Common Divisor 

**Lemma 3.4.** The following statements about the greatest common divisor hold: 
1. Every common divisor of $a$ and $b$ divides $\text{gcd}(a, b)$. 
2. $\text{gcd}(ka, kb) = k \cdot \text{gcd}(a, b)$ for all $k > 0$. 
3. If $\text{gcd}(a, b) = 1$ and $\text{gcd}(a, c) = 1$, then $\text{gcd}(a, bc) = 1$. 
4. If $a \mid bc$ and $\text{gcd}(a, b) = 1$, then $a \mid c$. 
5. $\text{gcd}(a, b) = \text{gcd}(b, a \text{ rem } b)$. 

**Proof.** We prove only parts (3) and (4). 

*Proof of (3):* The assumptions together with Theorem 3.1 imply that there exist integers $s, t, u,$ and $v$ such that: 
$$sa + tb = 1$$
$$ua + vc = 1$$
Multiplying these two equations gives: 
$$(sa + tb)(ua + vc) = 1$$
The left side can be rewritten as $a \cdot (asu + btu + csv) + bc \cdot (tv)$. This is a linear combination of $a$ and $bc$ that is equal to 1, so $\text{gcd}(a, bc) = 1$ by Theorem 3.1. 

*Proof of (4):* Theorem 3.1 says that $\text{gcd}(ac, bc)$ is equal to a linear combination of $ac$ and $bc$. Now $a \mid ac$ trivially and $a \mid bc$ by assumption. Therefore, $a$ divides every linear combination of $ac$ and $bc$. In particular, $a$ divides $\text{gcd}(ac, bc) = c \cdot \text{gcd}(a, b) = c$. $\blacksquare$

Part (5) of the lemma is useful for quickly computing the greatest common divisor of two numbers via Euclid’s algorithm. For example: 
$$\text{gcd}(1147, 899) = \text{gcd}(899, 1147 \text{ rem } 899) = \text{gcd}(899, 248)$$
$$= \text{gcd}(248, 899 \text{ rem } 248) = \text{gcd}(248, 155)$$
$$= \text{gcd}(155, 248 \text{ rem } 155) = \text{gcd}(155, 93)$$
$$= \text{gcd}(93, 155 \text{ rem } 93) = \text{gcd}(93, 62)$$
$$= \text{gcd}(62, 93 \text{ rem } 62) = \text{gcd}(62, 31)$$
$$= \text{gcd}(31, 62 \text{ rem } 31) = \text{gcd}(31, 0) = 31$$

### 3.3 One Solution for All Water Jug Problems 

To form $g$ gallons using jugs with capacities $a$ and $b$: 
* Repeat until the desired amount of water is obtained: 
  * Fill the smaller jug. 
  * Pour all the water in the smaller jug into the larger jug. Whenever the larger jug becomes full, empty it out. 

This method eventually generates every multiple of the greatest common divisor of the jug capacities—all the quantities we can possibly produce. 

### 3.3 The Pulverizer 

We can compute the coefficients $s$ and $t$ such that $\text{gcd}(a, b) = sa + tb$ using the extended Euclidean GCD algorithm, traditionally called "The Pulverizer." 

For example, we can compute the GCD of 259 and 70 as follows: 
$$\text{gcd}(259, 70) = \text{gcd}(70, 49) = \text{gcd}(49, 21) = \text{gcd}(21, 7) = 7$$

Here is the Pulverizer bookkeeping: 

| $x$ | $y$ | $(x \text{ rem } y) = x - q \cdot y$ |
| :--- | :--- | :--- |
| 259 | 70 | $49 = 259 - 3 \cdot 70$ |
| 70 | 49 | $21 = 70 - 1 \cdot 49 = 70 - 1 \cdot (259 - 3 \cdot 70) = -1 \cdot 259 + 4 \cdot 70$ |
| 49 | 21 | $7 = 49 - 2 \cdot 21 = (259 - 3 \cdot 70) - 2 \cdot (-1 \cdot 259 + 4 \cdot 70) = 3 \cdot 259 - 11 \cdot 70$ |
| 21 | 7 | $0$ |

The final solution is $7 = 3 \cdot 259 - 11 \cdot 70$. 

---

## 4 The Fundamental Theorem of Arithmetic 

**Theorem 4.3 (Fundamental Theorem of Arithmetic).** Every positive integer $n$ can be written in a unique way as a product of primes: 
$$n = p_1 \cdot p_2 \dots p_j \quad (p_1 \le p_2 \le \dots \le p_j)$$

**Lemma 4.1.** If $p$ is a prime and $p \mid ab$, then $p \mid a$ or $p \mid b$. 

**Proof.** The greatest common divisor of $a$ and $p$ must be either 1 or $p$. If $\text{gcd}(a, p) = p$, then $p \mid a$. Otherwise, $\text{gcd}(a, p) = 1$ and so $p \mid b$ by Lemma 3.4.4. $\blacksquare$

**Lemma 4.2.** Let $p$ be a prime. If $p \mid a_1 a_2 \dots a_n$, then $p$ divides some $a_i$. 

**Proof of Theorem 4.3.** We must prove two things: (1) every positive integer can be expressed as a product of primes, and (2) this expression is unique. 

First, we use strong induction to prove that every positive integer $n$ is a product of primes. As a base case, $n = 1$ is the product of the empty set of primes. For the inductive step, suppose that every $k < n$ is a product of primes. If $n$ is prime, the claim holds. Otherwise, $n = ab$ for some $a, b < n$. By the induction assumption, $a$ and $b$ are both products of primes, so $a \cdot b = n$ is also a product of primes. 

Second, we use the Well Ordering Principle to prove uniqueness. Assume there exist positive integers that can be written as products of primes in more than one way. Let $n$ be the smallest such integer: 
$$n = p_1 \cdot p_2 \dots p_j = q_1 \cdot q_2 \dots q_k$$
Then $p_1 \mid n \implies p_1 \mid q_1 q_2 \dots q_k$. Lemma 4.2 implies that $p_1$ divides some $q_i$. Since $q_i$ is prime, $p_1 = q_i$. Deleting $p_1$ from the first product and $q_i$ from the second yields $n/p_1$, which is a smaller positive integer that can be written as a product of primes in two distinct ways, a contradiction. $\blacksquare$

---

## 5 Cryptography and Modular Arithmetic 

### 5.1 Turing's Code (Version 1.0) 

Suppose the unencoded message $m$ is a prime number. 
* **Beforehand:** The sender and receiver agree on a secret key, which is a large prime $k$. 
* **Encryption:** The sender encrypts the message $m$ by computing: 
  $$m^* = m \cdot k$$
* **Decryption:** The receiver decrypts $m^*$ by computing: 
  $$\frac{m^*}{k} = m$$

A major flaw in this code is that if the sender transmits two encrypted messages: 
$$m_1^* = m_1 \cdot k \quad \text{and} \quad m_2^* = m_2 \cdot k$$
the receiver (or an interceptor) can retrieve the key $k$ easily by computing: 
$$\text{gcd}(m_1^*, m_2^*)$$

### 5.2 Modular Arithmetic 

**Definition 5.2.** $a$ is congruent to $b$ modulo $n$ (written $a \equiv b \pmod n$) iff $n \mid (a - b)$. 

For example, $29 \equiv 15 \pmod 7$ because $7 \mid (29 - 15)$. 

Modulo $3$ partitions the integers into three sets: 
$$\{\dots, -6, -3, 0, 3, 6, 9, \dots\}$$
$$\{\dots, -5, -2, 1, 4, 7, 10, \dots\}$$
$$\{\dots, -4, -1, 2, 5, 8, 11, \dots\}$$

**Lemma 7.1 (Facts About Congruences).** The following hold for $n \ge 1$: 
1. $a \equiv a \pmod n$ 
2. $a \equiv b \pmod n$ implies $b \equiv a \pmod n$ 
3. $a \equiv b \pmod n$ and $b \equiv c \pmod n$ implies $a \equiv c \pmod n$ 
4. $a \equiv b \pmod n$ implies $a + c \equiv b + c \pmod n$ 
5. $a \equiv b \pmod n$ implies $ac \equiv bc \pmod n$ 
6. $a \equiv b \pmod n$ and $c \equiv d \pmod n$ imply $a + c \equiv b + d \pmod n$ 
7. $a \equiv b \pmod n$ and $c \equiv d \pmod n$ imply $ac \equiv bd \pmod n$ 

**Lemma 7.2 (Congruences and Remainders).** The following assertions hold: 
1. $a \equiv (a \text{ rem } n) \pmod n$ 
2. $a \equiv b \pmod n$ if and only if $(a \text{ rem } n) = (b \text{ rem } n)$ 

### 5.3 Turing's Code (Version 2.0) 

* **Beforehand:** Agree on a large prime $p$ (public modulus) and a secret key $k \in \{1, 2, \dots, p - 1\}$. 
* **Encryption:** The message $m \in \{0, 1, \dots, p - 1\}$ is encrypted to: 
  $$m^* = (m \cdot k) \text{ rem } p$$

### 5.4 Multiplicative Inverses 

The multiplicative inverse of $x$ is $x^{-1}$ such that $x \cdot x^{-1} = 1$. Multiplicative inverses do not generally exist over the integers, but they do exist modulo a prime $p$ for any element not congruent to 0. 

**Lemma 8.1.** If $p$ is prime and $k$ is not a multiple of $p$, then $k$ has a multiplicative inverse modulo $p$. 

**Proof.** Since $p$ is prime and $k$ is not a multiple, $\text{gcd}(p, k) = 1$. Thus: 
$$sp + tk = 1 \implies tk \equiv 1 \pmod p$$
Hence $t$ is a multiplicative inverse of $k$. $\blacksquare$

To decrypt, we compute: 
$$m = (m^* \cdot k^{-1}) \text{ rem } p$$

### 5.5 Cancellation 

**Lemma 8.2.** Suppose $p$ is a prime and $k$ is not a multiple of $p$. Then: 
$$ak \equiv bk \pmod p \implies a \equiv b \pmod p$$

**Corollary 8.3.** Suppose $p$ is a prime and $k$ is not a multiple of $p$. Then the sequence: 
$$(0 \cdot k) \text{ rem } p, (1 \cdot k) \text{ rem } p, \dots, ((p - 1) \cdot k) \text{ rem } p$$
is a permutation of the sequence: 
$$0, 1, \dots, p - 1$$

### 5.6 Fermat's Theorem 

**Theorem 8.4 (Fermat's Theorem).** Suppose $p$ is a prime and $k$ is not a multiple of $p$. Then: 
$$k^{p-1} \equiv 1 \pmod p$$

**Proof.** By Corollary 8.3: 
$$1 \cdot 2 \dots (p-1) \equiv (k \text{ rem } p) \cdot (2k \text{ rem } p) \dots ((p - 1)k \text{ rem } p) \pmod p$$
$$\equiv (p-1)! \cdot k^{p-1} \pmod p$$
Since $\text{gcd}((p-1)!, p) = 1$, we can cancel $(p-1)!$ to get $k^{p-1} \equiv 1 \pmod p$. $\blacksquare$

Consequently, $k^{p-2}$ is a multiplicative inverse of $k$ modulo $p$. For example, to find the inverse of $6$ modulo $17$, we compute $6^{15} \text{ rem } 17$: 
$$6^2 \equiv 36 \equiv 2 \pmod{17}$$
$$6^4 \equiv 2^2 \equiv 4 \pmod{17}$$
$$6^8 \equiv 4^2 \equiv 16 \pmod{17}$$
$$6^{15} \equiv 6^8 \cdot 6^4 \cdot 6^2 \cdot 6 \equiv 16 \cdot 4 \cdot 2 \cdot 6 \equiv 3 \pmod{17}$$
So $3$ is the multiplicative inverse of $6$ modulo $17$. 

### 5.7 Breaking Turing's Code (Version 2.0) 

Under a known-plaintext attack, the adversary knows $m$ and $m^* \equiv mk \pmod p$. They can recover the key $k$ by computing: 
$$k \equiv m^{p-2} m^* \pmod p$$

---

## 6 Arithmetic with an Arbitrary Modulus 

### 6.1 Relative Primality and Euler's Phi Function 

Integers $a$ and $b$ are **relatively prime** if $\text{gcd}(a, b) = 1$. 

The function $\varphi(n)$ denotes the number of integers in $\{1, 2, \dots, n-1\}$ that are relatively prime to $n$. 

**Theorem 10.1.** The function $\varphi$ obeys the following relationships: 
1. If $a$ and $b$ are relatively prime, then $\varphi(ab) = \varphi(a)\varphi(b)$. 
2. If $p$ is a prime, then $\varphi(p^k) = p^k - p^{k-1}$ for $k \ge 1$. 

For example: 
$$\varphi(300) = \varphi(2^2 \cdot 3 \cdot 5^2) = \varphi(2^2) \cdot \varphi(3) \cdot \varphi(5^2)$$
$$= (2^2 - 2^1) \cdot (3^1 - 3^0) \cdot (5^2 - 5^1) = 2 \cdot 2 \cdot 20 = 80$$

### 6.2 Generalizing to an Arbitrary Modulus 

**Lemma 10.2.** Let $n$ be a positive integer. If $k$ is relatively prime to $n$, then there exists an integer $k^{-1}$ such that $k \cdot k^{-1} \equiv 1 \pmod n$. 

**Corollary 10.3.** Suppose $n$ is a positive integer and $k$ is relatively prime to $n$. If $ak \equiv bk \pmod n$, then $a \equiv b \pmod n$. 

### 6.3 Euler's Theorem 

**Lemma 10.4.** Suppose $n$ is a positive integer and $k$ is relatively prime to $n$. Let $k_1, \dots, k_r$ denote all the integers relatively prime to $n$ in the range $0 \le k_i < n$. Then the sequence: 
$$(k_1 \cdot k) \text{ rem } n, (k_2 \cdot k) \text{ rem } n, \dots, (k_r \cdot k) \text{ rem } n$$
is a permutation of the sequence $k_1, k_2, \dots, k_r$. 

**Theorem 10.5 (Euler's Theorem).** Suppose $n$ is a positive integer and $k$ is relatively prime to $n$. Then: 
$$k^{\varphi(n)} \equiv 1 \pmod n$$

**Proof.** Let $k_1, \dots, k_r$ denote all integers relatively prime to $n$ such that $0 \le k_i < n$. So $r = \varphi(n)$. By Lemma 10.4: 
$$k_1 \cdot k_2 \dots k_r \equiv (k_1 k \text{ rem } n) \cdot (k_2 k \text{ rem } n) \dots (k_r k \text{ rem } n) \pmod n$$
$$\equiv (k_1 k_2 \dots k_r) \cdot k^{\varphi(n)} \pmod n$$
Since the product $k_1 k_2 \dots k_r$ is relatively prime to $n$, we can cancel it to get $k^{\varphi(n)} \equiv 1 \pmod n$. $\blacksquare$

### 6.4 The RSA Cryptosystem 

The RSA public-key encryption scheme works as follows: 
* **Beforehand:** The receiver creates public and secret keys: 
  1. Generate two distinct large primes, $p$ and $q$. 
  2. Let $n = pq$. 
  3. Select an integer $e$ such that $\text{gcd}(e, (p - 1)(q - 1)) = 1$. The public key is $(e, n)$. 
  4. Compute $d$ such that $de \equiv 1 \pmod{(p - 1)(q - 1)}$. The secret key is $(d, n)$. 
* **Encoding:** The sender encrypts message $m$ to produce $m'$: 
  $$m' = m^e \text{ rem } n$$
* **Decoding:** The receiver decrypts $m'$ back to $m$: 
  $$m = (m')^d \text{ rem } n$$
