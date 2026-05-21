# Generating Functions 

Generating functions transform problems about sequences into problems about functions, allowing us to apply algebraic machinery to solve counting and recurrence problems. 

In these notes, we represent sequences using angle brackets $\langle g_0, g_1, g_2, \dots \rangle$. 

---

## 1 Generating Functions 

The ordinary generating function for the infinite sequence $\langle g_0, g_1, g_2, g_3, \dots \rangle$ is the formal power series: 
$$G(x) = \sum_{i=0}^\infty g_i x^i = g_0 + g_1 x + g_2 x^2 + g_3 x^3 + \dots$$

We denote the correspondence between a sequence and its generating function using a double-sided arrow: 
$$\langle g_0, g_1, g_2, g_3, \dots \rangle \longleftrightarrow g_0 + g_1 x + g_2 x^2 + g_3 x^3 + \dots$$

### Examples: 
* $\langle 0, 0, 0, 0, \dots \rangle \longleftrightarrow 0$ 
* $\langle 1, 0, 0, 0, \dots \rangle \longleftrightarrow 1$ 
* $\langle 3, 2, 1, 0, \dots \rangle \longleftrightarrow 3 + 2x + x^2$ 

Recall the infinite geometric series sum: 
$$\sum_{i=0}^\infty z^i = 1 + z + z^2 + z^3 + \dots = \frac{1}{1 - z}$$

Using this, we can find closed forms for standard sequences: 
* $\langle 1, 1, 1, 1, \dots \rangle \longleftrightarrow 1 + x + x^2 + x^3 + \dots = \frac{1}{1 - x}$ 
* $\langle 1, -1, 1, -1, \dots \rangle \longleftrightarrow 1 - x + x^2 - x^3 + \dots = \frac{1}{1 + x}$ 
* $\langle 1, a, a^2, a^3, \dots \rangle \longleftrightarrow 1 + ax + a^2 x^2 + a^3 x^3 + \dots = \frac{1}{1 - ax}$ 
* $\langle 1, 0, 1, 0, 1, \dots \rangle \longleftrightarrow 1 + x^2 + x^4 + x^6 + \dots = \frac{1}{1 - x^2}$ 

---

## 2 Operations on Generating Functions 

### 2.1 Scaling 

**Rule 1 (Scaling Rule).** If $\langle f_0, f_1, f_2, \dots \rangle \longleftrightarrow F(x)$, then: 
$$\langle c f_0, c f_1, c f_2, \dots \rangle \longleftrightarrow c \cdot F(x)$$

### 2.2 Addition 

**Rule 2 (Addition Rule).** If $\langle f_0, f_1, f_2, \dots \rangle \longleftrightarrow F(x)$ and $\langle g_0, g_1, g_2, \dots \rangle \longleftrightarrow G(x)$, then: 
$$\langle f_0 + g_0, f_1 + g_1, f_2 + g_2, \dots \rangle \longleftrightarrow F(x) + G(x)$$

#### Example: 
$$\langle 1, 1, 1, 1, \dots \rangle \longleftrightarrow \frac{1}{1-x}$$
$$\langle 1, -1, 1, -1, \dots \rangle \longleftrightarrow \frac{1}{1+x}$$
Adding these yields: 
$$\langle 2, 0, 2, 0, \dots \rangle \longleftrightarrow \frac{1}{1-x} + \frac{1}{1+x} = \frac{2}{1-x^2}$$

### 2.3 Right Shifting 

**Rule 3 (Right-Shift Rule).** If $\langle f_0, f_1, f_2, \dots \rangle \longleftrightarrow F(x)$, then: 
$$\langle \underbrace{0, 0, \dots, 0}_{k \text{ zeros}}, f_0, f_1, f_2, \dots \rangle \longleftrightarrow x^k F(x)$$

### 2.4 Differentiation 

**Rule 4 (Derivative Rule).** If $\langle f_0, f_1, f_2, f_3, \dots \rangle \longleftrightarrow F(x)$, then: 
$$\langle f_1, 2f_2, 3f_3, 4f_4, \dots \rangle \longleftrightarrow F'(x)$$

#### Example: 
Starting with $\langle 1, 1, 1, 1, \dots \rangle \longleftrightarrow \frac{1}{1-x}$, differentiating both sides gives: 
$$\langle 1, 2, 3, 4, \dots \rangle \longleftrightarrow \frac{d}{dx} \left(\frac{1}{1-x}\right) = \frac{1}{(1-x)^2}$$

#### Generating the Sequence of Squares: $\langle 0, 1, 4, 9, 16, \dots \rangle$ 
1. Start with constants: $\langle 1, 1, 1, 1, \dots \rangle \longleftrightarrow \frac{1}{1-x}$ 
2. Differentiate: $\langle 1, 2, 3, 4, \dots \rangle \longleftrightarrow \frac{1}{(1-x)^2}$ 
3. Multiply by $x$ (right shift): $\langle 0, 1, 2, 3, \dots \rangle \longleftrightarrow \frac{x}{(1-x)^2}$ 
4. Differentiate: $\langle 1, 4, 9, 16, \dots \rangle \longleftrightarrow \frac{d}{dx}\left(\frac{x}{(1-x)^2}\right) = \frac{1+x}{(1-x)^3}$ 
5. Multiply by $x$ (right shift): $\langle 0, 1, 4, 9, 16, \dots \rangle \longleftrightarrow \frac{x(1+x)}{(1-x)^3}$ 

### 2.5 Products (Convolution) 

**Rule 5 (Product Rule / Convolution).** If $\langle a_0, a_1, a_2, \dots \rangle \longleftrightarrow A(x)$ and $\langle b_0, b_1, b_2, \dots \rangle \longleftrightarrow B(x)$, then: 
$$\langle c_0, c_1, c_2, \dots \rangle \longleftrightarrow A(x) \cdot B(x)$$
where: 
$$c_n = \sum_{i=0}^n a_i b_{n-i} = a_0 b_n + a_1 b_{n-1} + \dots + a_n b_0$$

This product can be visualized using a grid of term combinations: 

| | $b_0 x^0$ | $b_1 x^1$ | $b_2 x^2$ | $b_3 x^3$ | $\dots$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$a_0 x^0$** | $a_0 b_0 x^0$ | $a_0 b_1 x^1$ | $a_0 b_2 x^2$ | $a_0 b_3 x^3$ | $\dots$ |
| **$a_1 x^1$** | $a_1 b_0 x^1$ | $a_1 b_1 x^2$ | $a_1 b_2 x^3$ | $\dots$ | $\dots$ |
| **$a_2 x^2$** | $a_2 b_0 x^2$ | $a_2 b_1 x^3$ | $\dots$ | $\dots$ | $\dots$ |
| **$a_3 x^3$** | $a_3 b_0 x^3$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |

---

## 3 The Fibonacci Sequence 

The Fibonacci numbers are defined by the recurrence: 
$$f_0 = 0, \quad f_1 = 1$$
$$f_n = f_{n-1} + f_{n-2} \quad (\text{for } n \ge 2)$$

### 3.1 Finding the Generating Function 

Let $F(x) = \sum_{n=0}^\infty f_n x^n$. Consider: 
$$\begin{array}{rcrccccccc}
F(x)   & = & f_0 & + & f_1 x   & + & f_2 x^2   & + & f_3 x^3   & + \dots \\
x F(x) & = &     &   & f_0 x   & + & f_1 x^2   & + & f_2 x^3   & + \dots \\
x^2 F(x) & = &   &   &         &   & f_0 x^2   & + & f_1 x^3   & + \dots
\end{array}$$

Subtracting $x F(x)$ and $x^2 F(x)$ from $F(x)$: 
$$F(x) - x F(x) - x^2 F(x) = f_0 + (f_1 - f_0)x + \sum_{n=2}^\infty (f_n - f_{n-1} - f_{n-2})x^n$$
Since $f_0 = 0$, $f_1 = 1$, and $f_n - f_{n-1} - f_{n-2} = 0$ for $n \ge 2$: 
$$F(x)(1 - x - x^2) = x \implies F(x) = \frac{x}{1 - x - x^2}$$

### 3.2 Finding Binet's Closed Form 

To extract the coefficients of $F(x)$, we factor the denominator: 
$$1 - x - x^2 = (1 - \alpha_1 x)(1 - \alpha_2 x)$$
where $\alpha_1 = \frac{1 + \sqrt{5}}{2}$ (the golden ratio) and $\alpha_2 = \frac{1 - \sqrt{5}}{2}$. 

Using partial fractions: 
$$\frac{x}{1 - x - x^2} = \frac{A_1}{1 - \alpha_1 x} + \frac{A_2}{1 - \alpha_2 x}$$
Solving the system yields $A_1 = \frac{1}{\sqrt{5}}$ and $A_2 = -\frac{1}{\sqrt{5}}$. Thus: 
$$F(x) = \frac{1}{\sqrt{5}} \left( \frac{1}{1 - \alpha_1 x} - \frac{1}{1 - \alpha_2 x} \right)$$
$$F(x) = \frac{1}{\sqrt{5}} \left( \sum_{n=0}^\infty \alpha_1^n x^n - \sum_{n=0}^\infty \alpha_2^n x^n \right)$$
Equating the coefficients of $x^n$ gives Binet's Formula: 
$$f_n = \frac{\alpha_1^n - \alpha_2^n}{\sqrt{5}} = \frac{1}{\sqrt{5}}\left[ \left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n \right]$$

---

## 4 Counting with Generating Functions 

### 4.1 Choosing Distinct Items from a Set 

The generating function for selecting $n$ distinct items from a set of size $k$ is $(1+x)^k$: 
$$\langle \binom{k}{0}, \binom{k}{1}, \binom{k}{2}, \dots, \binom{k}{k}, 0, 0, \dots \rangle \longleftrightarrow (1 + x)^k$$

### 4.2 The Convolution Rule for Disjoint Unions 

**Rule 6 (Convolution Rule).** Let $A(x)$ and $B(x)$ be the generating functions for selecting items from disjoint sets $A$ and $B$, respectively. The generating function for selecting items from $A \cup B$ is: 
$$C(x) = A(x) \cdot B(x)$$

For example, selecting from a $k$-element set $\{a_1, \dots, a_k\}$ is the union of $k$ disjoint single-element sets. For each $\{a_i\}$, the generating function for selecting at most one item is $(1+x)$. The product for the $k$ sets is $(1+x)^k$. 

### 4.3 Choosing Items with Repetition 

If we can select an item any number of times, the generating function for a single-element set is: 
$$1 + x + x^2 + x^3 + \dots = \frac{1}{1 - x}$$
By the Convolution Rule, the generating function for choosing $n$ items with repetition from a $k$-element set is: 
$$\left(\frac{1}{1-x}\right)^k = \frac{1}{(1-x)^k}$$

By the Bookkeeper Rule, the coefficient of $x^n$ in $\frac{1}{(1-x)^k}$ is: 
$$\binom{n + k - 1}{n}$$

---

## 5 An "Impossible" Counting Problem 

In how many ways can we fill a bag with $n$ fruits subject to the following constraints? 
* The number of apples must be even. 
* The number of bananas must be a multiple of 5. 
* There can be at most four oranges. 
* There can be at most one pear. 

We construct generating functions for each fruit: 
* **Apples:** $A(x) = 1 + x^2 + x^4 + x^6 + \dots = \frac{1}{1-x^2}$ 
* **Bananas:** $B(x) = 1 + x^5 + x^{10} + x^{15} + \dots = \frac{1}{1-x^5}$ 
* **Oranges:** $O(x) = 1 + x + x^2 + x^3 + x^4 = \frac{1-x^5}{1-x}$ 
* **Pears:** $P(x) = 1 + x$ 

By the Convolution Rule, the generating function for the combined fruit bag is: 
$$F(x) = A(x) B(x) O(x) P(x) = \frac{1}{1-x^2} \cdot \frac{1}{1-x^5} \cdot \frac{1-x^5}{1-x} \cdot (1+x)$$
Observe the algebraic cancellations: 
$$F(x) = \frac{1}{(1-x)(1+x)} \cdot \frac{1}{1-x^5} \cdot \frac{1-x^5}{1-x} \cdot (1+x) = \frac{1}{(1-x)^2}$$

The power series for $\frac{1}{(1-x)^2}$ is: 
$$\frac{1}{(1-x)^2} = \sum_{n=0}^\infty (n+1)x^n = 1 + 2x + 3x^2 + 4x^3 + \dots$$
Thus, there are exactly $n+1$ ways to fill the bag with $n$ fruits. 
