# Induction 

## 1 Induction 

A professor brings to class a bottomless bag of assorted miniature candy bars. She offers to share in accordance with two rules. First, she numbers the students $0, 1, 2, 3, \dots$ for convenient reference. Now here are the two rules: 
1. Student $0$ gets candy. 
2. For all $n \in \mathbb{N}$, if student $n$ gets candy, then student $n + 1$ also gets candy. 

You can think of the second rule as a compact way of writing a whole sequence of statements, one for each natural value of $n$: 
* If student $0$ gets candy, then student $1$ also gets candy. 
* If student $1$ gets candy, then student $2$ also gets candy. 
* If student $2$ gets candy, then student $3$ also gets candy, and so forth. 

Now suppose you are student $17$. By these rules, are you entitled to a miniature candy bar? Well, student $0$ gets candy by the first rule. Therefore, by the second rule, student $1$ also gets candy, which means student $2$ gets candy as well, which means student $3$ gets candy, and so on. So the professor’s two rules actually guarantee candy for every student, no matter how large the class. You win! 

This reasoning generalizes to a principle called induction: 

**Principle of Induction.** Let $P(n)$ be a predicate. If 
* $P(0)$ is true, and 
* for all $n \in \mathbb{N}$, $P(n)$ implies $P(n + 1)$, 
then $P(n)$ is true for all $n \in \mathbb{N}$. 

Here’s the correspondence between the induction principle and sharing candy bars. Suppose that $P(n)$ is the predicate, “student $n$ gets candy”. Then the professor’s first rule asserts that $P(0)$ is true, and her second rule is that for all $n \in \mathbb{N}$, $P(n)$ implies $P(n + 1)$. Given these facts, the induction principle says that $P(n)$ is true for all $n \in \mathbb{N}$. In other words, everyone gets candy. 

The intuitive justification for the general induction principle is the same as for everyone getting a candy bar under the professor’s two rules. So the Principle of Induction is universally accepted as an obvious, sound proof method. What’s not so obvious is how much mileage we get by using it. 

---

## 2 Using Induction 

Induction is by far the most powerful and commonly-used proof technique in Discrete Mathematics and Computer Science. In fact, the use of induction is a defining characteristic of discrete—as opposed to continuous—Mathematics. 

Induction often works directly in proving that some statement about natural numbers holds for all of them. For example, here is a classic formula: 

**Theorem 2.1.** For all $n \in \mathbb{N}$, 
$$1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2} \qquad (1)$$

The left side of equation (1) represents the sum of all the numbers from $1$ to $n$. You’re supposed to guess the pattern and mentally replace the dots ($\dots$) with the other terms. We could eliminate the need for guessing by rewriting the left side with summation notation: 
$$\sum_{i=1}^n i \quad\text{or}\quad \sum_{1 \le i \le n} i \quad\text{or}\quad \sum_{i \in \{1, \dots, n\}} i$$

Each of these expressions denotes the sum of all values taken on by the expression to the right of the sigma as the variable, $i$, ranges from $1$ to $n$. The meaning of the sum in Theorem 2.1 is not so obvious in a couple of special cases: 
* If $n = 1$, then there is only one term in the summation, and so $1 + 2 + 3 + \dots + n = 1$. Don’t be misled by the appearance of $2$ and $3$ and the suggestion that $1$ and $n$ are distinct terms! 
* If $n \le 0$, then there are no terms at all in the summation, and so $1 + 2 + 3 + \dots + n = 0$. 

The dots notation is convenient, but watch out for these special cases where the notation is misleading! 

Now let’s use the induction principle to prove Theorem 2.1. Suppose that we define predicate $P(n)$ to be “$1 + 2 + 3 + \dots + n = n(n + 1)/2$”. Recast in terms of this predicate, the theorem claims that $P(n)$ is true for all $n \in \mathbb{N}$. This is great, because the induction principle lets us reach precisely that conclusion, provided we establish two simpler facts: 
* $P(0)$ is true. 
* For all $n \in \mathbb{N}$, $P(n)$ implies $P(n + 1)$. 

So now our job is reduced to proving these two statements. The first is true because $P(0)$ asserts that a sum of zero terms is equal to $0(0 + 1)/2 = 0$. 

The second statement is more complicated. But remember the basic plan for proving the validity of any implication: assume the statement on the left and then prove the statement on the right. In this case, we assume $P(n)$: 
$$1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2}$$
in order to prove $P(n + 1)$: 
$$1 + 2 + 3 + \dots + n + (n + 1) = \frac{(n + 1)(n + 2)}{2}$$

These two equations are quite similar; in fact, adding $(n + 1)$ to both sides of the first equation and simplifying the right side gives the second equation: 
$$1 + 2 + 3 + \dots + n + (n + 1) = \frac{n(n + 1)}{2} + (n + 1)$$
$$= \frac{(n + 2)(n + 1)}{2}$$
Thus, if $P(n)$ is true, then so is $P(n + 1)$. This argument is valid for every natural number $n$, so this establishes the second fact required by the induction principle. In effect, we’ve just proved that $P(0)$ implies $P(1)$, $P(1)$ implies $P(2)$, $P(2)$ implies $P(3)$, etc. all in one fell swoop. 

With these two facts in hand, the induction principle says that the predicate $P(n)$ is true for all natural $n$. And so the theorem is proved! 

### 2.1 A Template for Induction Proofs 

The proof of Theorem 2.1 was relatively simple, but even the most complicated induction proof follows exactly the same template. There are five components: 
1. **State that the proof uses induction.** This immediately conveys the overall structure of the proof, which helps the reader understand your argument. 
2. **Define an appropriate predicate $P(n)$.** The eventual conclusion of the induction argument will be that $P(n)$ is true for all natural $n$. Thus, you should define the predicate $P(n)$ so that your theorem is equivalent to (or follows from) this conclusion. Often the predicate can be lifted straight from the claim, as in the example above. The predicate $P(n)$ is called the “induction hypothesis”. Sometimes the induction hypothesis will involve several variables, in which case you should indicate which variable serves as $n$. 
3. **Prove that $P(0)$ is true.** This is usually easy, as in the example above. This part of the proof is called the “base case” or “basis step”. (Sometimes the base case will be $n = 1$ or even some larger number, in which case the starting value of $n$ also should be stated.) 
4. **Prove that $P(n)$ implies $P(n + 1)$ for every natural number $n$.** This is called the “inductive step” or “induction step”. The basic plan is always the same: assume that $P(n)$ is true and then use this assumption to prove that $P(n + 1)$ is true. These two statements should be fairly similar, but bridging the gap may require some ingenuity. Whatever argument you give must be valid for every natural number $n$, since the goal is to prove the implications $P(0) \longrightarrow P(1), P(1) \longrightarrow P(2), P(2) \longrightarrow P(3)$, etc. all at once. 
5. **Invoke induction.** Given these facts, the induction principle allows you to conclude that $P(n)$ is true for all natural $n$. This is the logical capstone to the whole argument, but many writers leave this step implicit. 

Explicitly labeling the base case and inductive step may make your proofs clearer. 

### 2.2 A Clean Writeup 

The proof of Theorem 2.1 given above is perfectly valid; however, it contains a lot of extraneous explanation that you won’t usually see in induction proofs. The writeup below is closer to what you might see in print and should be prepared to produce yourself. 

**Proof.** We use induction. The induction hypothesis, $P(n)$, will be equation (1). 

**Base case:** $P(0)$ is true, because both sides of equation (1) equal zero when $n = 0$. 

**Inductive step:** Assume that $P(n)$ is true, where $n$ is any natural number. Then: 
$$1 + 2 + 3 + \dots + n + (n + 1) = \frac{n(n + 1)}{2} + (n + 1) \quad \text{by induction hypothesis}$$
$$= \frac{(n + 1)(n + 2)}{2} \quad \text{by simple algebra}$$
which proves $P(n + 1)$. 

So it follows by induction that $P(n)$ is true for all natural $n$. $\blacksquare$

Induction was helpful for proving the correctness of this summation formula, but not helpful for discovering the formula in the first place. There are some tricks for finding such formulas, which we’ll show you in a few weeks. 

### 2.3 A Fibonacci Identity 

For another simple example of the use of induction, we’ll consider the Fibonacci numbers. The first two Fibonacci numbers are $0$ and $1$, and each subsequent Fibonacci number is the sum of the two previous ones. The $n$th Fibonacci number is denoted $F_n$. In other words, the Fibonacci numbers are defined recursively by the rules: 
$$F_0 ::= 0$$
$$F_1 ::= 1$$
$$F_i ::= F_{i-1} + F_{i-2} \qquad \text{for } i \ge 2 \qquad (2)$$

The first few Fibonacci numbers are: 
$$0, 1, 1, 2, 3, 5, 8, 13, 21, \dots$$

Fibonacci numbers come up naturally in several ways, but they have captivated a continued mathematical following out of proportion to their importance in applications because they have a rich and surprising collection of properties, such as the one expressed in the following theorem. The theorem is a good thing to forget if you run low on brain space, its proof just provides a nice illustration of induction. 

**Theorem 2.2.** For all $n \ge 0$: 
$$\sum_{i=0}^n F_i^2 = F_n F_{n+1} \qquad (3)$$

For example, for $n = 4$ we have $0^2 + 1^2 + 1^2 + 2^2 + 3^2 = 15 = 3 \cdot 5$. 

Let’s look for a proof by induction. First, the theorem statement suggests that the induction hypothesis $P(n)$ be equation (3). 

Second, we want to identify the gap between $P(n)$ and $P(n + 1)$. The predicate $P(n + 1)$ states that: 
$$\sum_{i=0}^{n+1} F_i^2 = F_{n+1} F_{n+2} \qquad (4)$$

Now the plan is to use $P(n)$ to reduce this statement to a simpler assertion. An easy way is to subtract equation (3) from (4). This gives: 
$$F_{n+1}^2 = F_{n+1} F_{n+2} - F_n F_{n+1} \qquad (5)$$

This is the Fibonacci recurrence in disguise; dividing both sides of (5) by $F_{n+1}$ and moving a term gives $F_n + F_{n+1} = F_{n+2}$. This is the extra fact needed to bridge the gap between $P(n)$ and $P(n + 1)$ in the inductive step. The full proof is written below. 

**Proof.** The proof is by induction. Let $P(n)$ be equation (3). 

**Base case:** $P(0)$ is true because: 
$$F_0^2 = 0^2 = 0 = 0 \cdot 1 = F_0 F_1$$

**Inductive step:** We assume equation (3) holds for some $n \ge 0$, and prove that $\sum_{i=0}^{n+1} F_i^2 = F_{n+1} F_{n+2}$. 

For all $n \ge 0$, the equation $F_n + F_{n+1} = F_{n+2}$ holds by the definition of the Fibonacci numbers. Multiplying both sides by $F_{n+1}$ and rearranging terms gives $F_{n+1}^2 = F_{n+1} F_{n+2} - F_n F_{n+1}$. Adding this identity to equation (3) gives: 
$$\sum_{i=0}^{n+1} F_i^2 = \left(F_{n+1} F_{n+2} - F_n F_{n+1}\right) + F_n F_{n+1}$$
$$\sum_{i=0}^{n+1} F_i^2 = F_{n+1} F_{n+2}$$
as required. 

So by induction, we conclude that equation (3) holds for all $n \in \mathbb{N}$. $\blacksquare$

### 2.4 Courtyard Tiling 

Induction served purely as a proof technique in the preceding examples. But induction sometimes can serve as a more general reasoning tool. 

MIT recently constructed a new computer science building. As the project went further and further over budget, there were some radical fundraising ideas. One plan was to install a big courtyard with dimensions $2^n \times 2^n$. 

One of the central squares would be occupied by a statue of a wealthy potential donor. Let’s call him “Bill”. (In the special case $n = 0$, the whole courtyard consists of a single central square; otherwise, there are four central squares.) A complication was that the building’s unconventional architect, Frank Gehry, insisted that only special L-shaped tiles be used (each tile consisting of 3 squares). 

For larger values of $n$, is there a way to tile a $2^n \times 2^n$ courtyard with L-shaped tiles and a statue in the center? Let’s try to prove that this is so. 

**Theorem 2.3.** For all $n \ge 0$ there exists a tiling of a $2^n \times 2^n$ courtyard with Bill in a central square. 

**Proof.** (doomed attempt) The proof is by induction. Let $P(n)$ be the proposition that there exists a tiling of a $2^n \times 2^n$ courtyard with Bill in the center. 

**Base case:** $P(0)$ is true because Bill fills the whole courtyard. 

**Inductive step:** Assume that there is a tiling of a $2^n \times 2^n$ courtyard with Bill in the center for some $n \ge 0$. We must prove that there is a way to tile a $2^{n+1} \times 2^{n+1}$ courtyard with Bill in the center... 

Now we’re in trouble! The ability to tile a smaller courtyard with Bill in the center isn’t much help in tiling a larger courtyard with Bill in the center. We haven’t figured out how to bridge the gap between $P(n)$ and $P(n + 1)$. 

So if we’re going to prove Theorem 2.3 by induction, we’re going to need some other induction hypothesis than simply the statement about $n$ that we’re trying to prove. 

When this happens, your first fallback should be to look for a stronger induction hypothesis; that is, one which implies your previous hypothesis. For example, we could make $P(n)$ the proposition that for every location of Bill in a $2^n \times 2^n$ courtyard, there exists a tiling of the remainder. 

This advice may sound bizarre: “If you can’t prove something, try to prove something more grand!” But for induction arguments, this makes sense. In the inductive step, where you have to prove $P(n) \longrightarrow P(n + 1)$, you’re in better shape because you can assume $P(n)$, which is now a more general, more useful statement. Let’s see how this plays out in the case of courtyard tiling. 

**Proof.** (successful attempt) The proof is by induction. Let $P(n)$ be the proposition that for every location of Bill in a $2^n \times 2^n$ courtyard, there exists a tiling of the remainder. 

**Base case:** $P(0)$ is true because Bill fills the whole courtyard. 

**Inductive step:** Assume that $P(n)$ is true for some $n \ge 0$; that is, for every location of Bill in a $2^n \times 2^n$ courtyard, there exists a tiling of the remainder. Divide the $2^{n+1} \times 2^{n+1}$ courtyard into four quadrants, each $2^n \times 2^n$. One quadrant contains Bill ($B$). Place a temporary Bill ($X$) in each of the three central squares lying outside this quadrant. 

Now we can tile each of the four quadrants by the induction assumption. Replacing the three temporary Bills with a single L-shaped tile completes the job. This proves that $P(n)$ implies $P(n + 1)$ for all $n \ge 0$. The theorem follows as a special case. $\blacksquare$

This proof has two nice properties. First, not only does the argument guarantee that a tiling exists, but also it gives a recursive procedure for finding such a tiling. Second, we have a stronger result: if Bill wanted a statue on the edge of the courtyard, away from the pigeons, we could accommodate him! 

Strengthening the induction hypothesis is often a good move when an induction proof won’t go through. But keep in mind that the stronger assertion must actually be true; otherwise, there isn’t much hope of constructing a valid proof! Sometimes finding just the right induction hypothesis requires trial, error, and insight. For example, mathematicians spent almost twenty years trying to prove or disprove the conjecture that “Every planar graph is 5-choosable”. Then, in 1994, Carsten Thomassen gave an induction proof simple enough to explain on a napkin. The key turned out to be finding an extremely clever induction hypothesis; with that in hand, completing the argument is easy! 

### 2.5 A Faulty Induction Proof 

**False Theorem.** All horses are the same color. 

Notice that no $n$ is mentioned in this assertion, so we’re going to have to reformulate it in a way that makes an $n$ explicit. In particular, we’ll (falsely) prove that: 

**False Theorem 2.4.** In every set of $n \ge 1$ horses, all are the same color. 

This is a statement about all integers $n \ge 1$ rather than $\ge 0$, so it’s natural to use a slight variation on induction: prove $P(1)$ in the base case and then prove that $P(n)$ implies $P(n + 1)$ for all $n \ge 1$ in the inductive step. This is a perfectly valid variant of induction and is not the problem with the proof below. 

**Proof.** The proof is by induction. The induction hypothesis, $P(n)$, will be: 
$$\text{In every set of } n \text{ horses, all are the same color.} \qquad (6)$$

**Base case:** ($n = 1$). $P(1)$ is true, because in a set of horses of size 1, there’s only one horse, and this horse is definitely the same color as itself. 

**Inductive step:** Assume that $P(n)$ is true for some $n \ge 1$; that is, assume that in every set of $n$ horses, all are the same color. Now consider a set of $n + 1$ horses: 
$$h_1, h_2, \dots, h_n, h_{n+1}$$
By our assumption, the first $n$ horses are the same color: 
$$h_1, h_2, \dots, h_n$$
Also by our assumption, the last $n$ horses are the same color: 
$$h_2, \dots, h_n, h_{n+1}$$
Therefore, horses $h_1, h_2, \dots, h_{n+1}$ must all be the same color, and so $P(n + 1)$ is true. Thus, $P(n)$ implies $P(n + 1)$. 

By the principle of induction, $P(n)$ is true for all $n \ge 1$. $\blacksquare$

We’ve proved something false! Is Math broken? Should we all become poets? 

The error in this argument is in the sentence that begins, “Therefore, horses $h_1, h_2, \dots, h_{n+1}$ must all be the same color.” The $\dots$ notation creates the impression that the sets $\{h_1, h_2, \dots, h_n\}$ and $\{h_2, \dots, h_n, h_{n+1}\}$ overlap. However, this is not true when $n = 1$. In that case, the first set is just $\{h_1\}$ and the second is $\{h_2\}$, and these do not overlap at all! 

This mistake knocks a critical link out of our induction argument. We proved $P(1)$ and we correctly proved $P(2) \longrightarrow P(3), P(3) \longrightarrow P(4)$, etc. But we failed to prove $P(1) \longrightarrow P(2)$, and so everything falls apart: we cannot conclude that $P(2), P(3)$, etc., are true. And, of course, these propositions are all false; there are horses of a different color. 

Students sometimes claim that the mistake in the proof is because $P(n)$ is false for $n \ge 2$, and the proof assumes something false, namely, $P(n)$, in order to prove $P(n + 1)$. You should think about how to explain to such a student why this claim would get no credit on a 6.042 exam. 

---

## 3 Strong Induction 

### 3.1 The Strong Induction Principle 

A useful variant of induction is called strong induction. Strong induction and ordinary induction are used for exactly the same thing: proving that a predicate $P(n)$ is true for all $n \in \mathbb{N}$. 

**Principle of Strong Induction.** Let $P(n)$ be a predicate. If 
* $P(0)$ is true, and 
* for all $n \in \mathbb{N}$, $P(0), P(1), \dots, P(n)$ together imply $P(n + 1)$, 
then $P(n)$ is true for all $n \in \mathbb{N}$. 

The only change from the ordinary induction principle is that strong induction allows you to assume more stuff in the inductive step of your proof! In an ordinary induction argument, you assume that $P(n)$ is true and try to prove that $P(n+1)$ is also true. In a strong induction argument, you may assume that $P(0), P(1), \dots$, and $P(n)$ are all true when you go to prove $P(n + 1)$. These extra assumptions can only make your job easier. 

### 3.2 Products of Primes 

As a first example, we’ll use strong induction to prove one of those familiar facts that is almost, but maybe not entirely, obvious: 

**Lemma 3.1.** Every integer greater than 1 is a product of primes. 

Note that, by convention, any number is considered to be a product consisting of one term, namely itself. In particular, every prime is considered to be a product whose terms are all primes. 

**Proof.** We will prove Lemma 3.1 by strong induction, letting the induction hypothesis, $P(n)$, be: 
$$n + 2 \text{ is a product of primes.}$$
So Lemma 3.1 will follow if we prove that $P(n)$ holds for all $n \ge 0$. 

**Base Case:** $P(0)$ is true because $0 + 2 = 2$ is prime, and so is a product of primes by convention. 

**Inductive step:** Suppose that $n \ge 0$ and that $i + 2$ is a product of primes for every natural number $i < n + 1$. We must show that $P(n + 1)$ holds, namely, that $n + 3$ is also a product of primes. We argue by cases: 
* If $n + 3$ is itself prime, then it is a product of primes by convention, so $P(n + 1)$ holds in this case. 
* Otherwise, $n + 3$ is not prime, which by definition means $n + 3 = km$ for some natural numbers $k, m$ such that $2 \le k, m < n + 3$. So $k - 2$ is a natural number less than $n + 1$, which means that $(k - 2) + 2$ is a product of primes by the induction hypothesis. That is, $k$ is a product of primes. Likewise, $m$ is a product of primes. So $km = n + 3$ is also a product of primes. Therefore, $P(n + 1)$ holds in this case as well. 

So $P(n + 1)$ holds in any case, which completes the proof by strong induction that $P(n)$ holds for all natural numbers, $n$. $\blacksquare$

Despite the name, strong induction is actually no more powerful than ordinary induction. In other words, any theorem that can be proved with strong induction could also be proved with ordinary induction (using a slightly more complicated induction hypothesis). But strong induction can make some proofs a bit easier. On the other hand, if $P(n)$ is easily sufficient to prove $P(n + 1)$, then it’s better to use ordinary induction for simplicity. 

### 3.3 Making Change 

The country Inductia, whose unit of currency is the Strong, has coins worth $6S$ (6 Strongs), $10S$ and $15S$. Although the Inductians have some trouble making small change like $11S$ or $29S$, it turns out that they can collect coins to make change for any number of Strongs greater than $29S$. 

Strong induction makes this easy to prove for $n + 1 > 35$, because then $(n + 1) - 6 > 29$, so by strong induction the Inductians can make change for exactly $((n + 1) - 6)S$, and then they can add a $6S$ coin to get $(n + 1)S$. So the only thing to do is check that they can make change for all the amounts from $30$ to $35$, which is not too hard to do. 

Here’s a detailed writeup using the official format: 

**Proof.** We prove the Inductians can make change for any amount greater than $29S$ by strong induction. The induction hypothesis, $P(n)$ will be: 
$$\text{If } n > 29\text{, then there is a collection of coins whose value is } n \text{ Strongs.}$$

Notice that $P(n)$ is an implication. When the hypothesis of an implication is false, we know the whole implication is true. In this situation, the implication is said to be vacuously true. So $P(n)$ will be vacuously true whenever $n \le 29$. 

We now proceed with the induction proof: 

**Base case:** $P(0)$ is vacuously true. 

**Inductive step:** We assume $P(i)$ holds for all $i \le n$, and prove that $P(n + 1)$ holds. We argue by cases: 
* **Case ($n + 1 \le 29$):** $P(n + 1)$ is vacuously true in this case. 
* **Case ($n + 1 = 30$):** $P(30)$ holds because the Inductians can use five $6S$ coins. 
* **Case ($n + 1 = 31$):** Use a $6S$ coin, a $10S$ coin, and a $15S$ coin. 
* **Case ($n + 1 = 32$):** Use two $6S$ coins, and two $10S$ coins. 
* **Case ($n + 1 = 33$):** Use three $6S$ coins, and a $15S$ coin. 
* **Case ($n + 1 = 34$):** Use four $6S$ coins, and a $10S$ coin. 
* **Case ($n + 1 = 35$):** Use two $10S$ coins and a $15S$ coin. 
* **Case ($n + 1 > 35$):** Then $n \ge (n + 1) - 6 > 29$, so by the strong induction hypothesis, the Inductians can make change for $((n + 1) - 6)S$. Now by adding a $6S$ coin, they can make change for $(n + 1)S$. 

So in any case, $P(n + 1)$ is true, and we conclude by strong induction that for all $n > 29$, the Inductians can make change for $nS$. $\blacksquare$

Note that, as with tiling with L-shaped pieces, this proof also yields a recursive procedure for making change. In fact, it shows even more: the Inductians can make change for any amount greater than $29S$ using only one $15S$ coin, at most two $10S$ coins, and lots of $6S$ coins. 

### 3.4 Unstacking 

You begin with a stack of $n$ boxes. Then you make a sequence of moves. In each move, you divide one stack of boxes into two nonempty stacks. The game ends when you have $n$ stacks, each containing a single box. You earn points for each move; in particular, if you divide one stack of height $a + b$ into two stacks with heights $a$ and $b$, then you score $ab$ points for that move. Your overall score is the sum of the points that you earn for each move. What strategy should you use to maximize your total score? 

As an example, suppose that we begin with a stack of $n = 10$ boxes. Then the game might proceed as follows: 

| Stack Heights | Score |
| :--- | :--- |
| <u>10</u> | |
| <u>5</u>, 5 | 25 points |
| 5, <u>3</u>, 2 | 6 points |
| <u>5</u>, 3, 2, 1 | 4 points |
| 2, 3, 2, <u>1</u>, 2 | 4 points |
| 2, <u>2</u>, 2, 1, 2, 1 | 2 points |
| 1, 2, <u>2</u>, 1, 2, 1, 1 | 2 points |
| 1, 1, <u>2</u>, 1, 2, 1, 1, 1 | 2 points |
| 1, 1, 1, 1, <u>2</u>, 1, 1, 1, 1 | 1 point |
| 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 | 1 point |
| **Total Score** | **45 points** |

On each line, the underlined stack is divided in the next step. Can you find a better strategy? 

#### 3.4.1 Analyzing the Game 

Let’s use strong induction to analyze the unstacking game. We’ll prove that your score is determined entirely by the number of boxes—your strategy is irrelevant! 

**Theorem 3.2.** Every way of unstacking $n$ blocks gives a score of $n(n - 1)/2$ points. 

**Proof.** The proof is by strong induction. Let $P(n)$ be the proposition that every way of unstacking $n$ blocks gives a score of $n(n - 1)/2$. 

**Base case:** If $n = 1$, then there is only one block. No moves are possible, and so the total score for the game is $1(1 - 1)/2 = 0$. Therefore, $P(1)$ is true. 

**Inductive step:** Now we must show that $P(1), \dots, P(n - 1)$ imply $P(n)$ for all $n \ge 2$. So assume that $P(1), \dots, P(n - 1)$ are all true and that we have a stack of $n$ blocks. The first move must split this stack into substacks with sizes $k$ and $n - k$ for some $k$ strictly between $0$ and $n$. Now the total score for the game is the sum of points for this first move plus points obtained by unstacking the two resulting substacks: 
$$\text{total score} = (\text{score for 1st move}) + (\text{score for unstacking } k \text{ blocks}) + (\text{score for unstacking } n - k \text{ blocks})$$
$$= k(n - k) + \frac{k(k - 1)}{2} + \frac{(n - k)(n - k - 1)}{2}$$
$$= \frac{2nk - 2k^2 + k^2 - k + n^2 - nk - n - nk + k^2 + k}{2}$$
$$= \frac{n(n - 1)}{2}$$

The second equation uses the assumptions $P(k)$ and $P(n - k)$ and the rest is simplification. This shows that $P(1), P(2), \dots, P(n - 1)$ imply $P(n)$. 

Therefore, the claim is true by strong induction. $\blacksquare$

---

## 4 The Well Ordering Principle 

**Well Ordering Principle.** Every nonempty subset of natural numbers has a smallest element. 

The Well Ordering Principle looks nothing like the induction axiom, and it may seem obvious but useless. 

But as for obvious, note that this axiom would be false if the set of non-negative integers, $\mathbb{N}$, were replaced by, say, the set, $\mathbb{Z}$, of all integers, or the set, $\mathbb{Q}^+$, of positive rational numbers. Neither of these sets has a least element. So the Well Ordering Principle does capture something special about the natural numbers. 

As for useless, it turns out that there’s a routine way to transform any proof using the Well Ordering Principle into a proof using Strong Induction, and vice-versa. So Well Ordering could have been used instead of induction in all the previous proofs. 

In fact, looking back, we implicitly relied on the Well Ordering Principle in the proof in the Week 2 Notes that $\sqrt{2}$ is irrational. That proof assumed that any rational number, $q$, could be written as a fraction in lowest terms, that is, $q = m/n$ where $m$ and $n$ are integers with no common factors. How do we know this is always possible? 

First, we can assume $m \ge 0$ (otherwise, replace $m/n$ by $-m/(-n)$), so the set of natural numbers, $m$, such that $q = m/n$ for some integer, $n$, is not empty. Therefore, by Well Ordering, there must be a least natural number, $m_0$, such that $q = m_0/n_0$ for some integer, $n_0$. Now if $m_0$ and $n_0$ had a common factor, $p > 1$, then $(m_0/p)/(n_0/p)$ would be another way to express $q$ as a quotient of integers. But since $0 \le (m_0/p) < m_0$, this contradicts the minimality of $m_0$. 

We’ve been using the Well-ordering Principle on the sly from early on! 

Mathematicians often use Well Ordering because it often leads to shorter proofs than induction. On the other hand, Well Ordering proofs typically involve proof by contradiction, so using it is not always the best approach. The choice of method is really a matter of style—but style does matter. 
