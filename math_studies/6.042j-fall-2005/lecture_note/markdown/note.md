# lecture_note_1.md

## Removed Content: The ZFC Axioms Section
```markdown
### The ZFC Axioms

For the record, we list the axioms of Zermelo-Fraenkel Set Theory. Essentially all of mathematics can be derived from these axioms together with a few logical deduction rules.

**Extensionality.** Two sets are equal if they have the same members. In formal logical notation, this would be stated as: 
$$(\forall z. (z \in x \longleftrightarrow z \in y)) \longrightarrow x = y$$

**Pairing.** For any two sets $x$ and $y$, there is a set, $\{x, y\}$, with $x$ and $y$ as its only elements. 

**Union.** The union of a collection, $z$, of sets is also a set. 
$$\exists u \forall x. (\exists y. x \in y \wedge y \in z) \longleftrightarrow x \in u$$

**Infinity.** There is an infinite set; specifically, a nonempty set, $x$, such that for any set $y \in x$, the set $\{y\}$ is also a member of $x$. 

**Subset.** Given any set, $x$, and any proposition $P(y)$, there is a set containing precisely those elements $y \in x$ for which $P(y)$ holds. 

**Power Set.** All the subsets of a set form another set. 

**Replacement.** The image of a set under a function is a set. 

**Foundation.** For every non-empty set, $x$, there is a set $y \in x$ such that $x$ and $y$ are disjoint. (In particular, this axiom prevents a set from being a member of itself.) 

**Choice.** We can choose one element from each set in a collection of nonempty sets. More precisely, if $f$ is a function on a set, and the result of applying $f$ to any element in the set is always a nonempty set, then there is a “choice” function $g$ such that $g(y) \in y$ for every $y$ in the set. 

We’re not going to be working with the ZFC axioms in this course. We just thought you might like to see them.
```
### Reason for Removal
The course notes explicitly state: *"We’re not going to be working with the ZFC axioms in this course. We just thought you might like to see them."* These axioms are used for the logical construction of mathematics from first principles (which is too low-level/primitive for 6.042J context) and are not needed for learning practical computer science proofs.

---

## Removed Content: Footnote 2 (Book Recommendation)
```markdown
[^2]: The story of the four-color proof is told in a well-reviewed recent popular (non-technical) book: “Four Colors Suffice. How the Map Problem was Solved.” Robin Wilson. Princeton Univ. Press, 2003, 276pp. ISBN 0-691-11533-8.
```
### Reason for Removal
This is a bibliographic citation and a popular reading recommendation. It has no bearing on understanding the mathematical formulation or implications of the four-color theorem.

---

# lecture_note_2.md

## Removed Content: Section 4 ("Does All This Really Work?")
```markdown
## 4 Does All This Really Work? 

So this is where mainstream mathematics stands today: there is a handful of axioms from which everything else in mathematics can be logically derived. This sounds like a rosy situation, but there are several dark clouds, suggesting that the essence of truth in mathematics is not completely resolved. 
* The ZFC axioms weren’t etched in stone by God. Instead, they were mostly made up by some guy named Zermelo. Probably some days he forgot his house keys. 
* No one knows whether the ZFC axioms are logically consistent; there is some possibility that one person might prove a proposition $P$ and another might prove the proposition $\neg P$. Then Math would be broken. This sounds like a crazy situation, but it has happened before. At the beginning of the 20th century, the logician Gotlob Frege made an initial attempt to axiomatize set theory using a few very plausible axioms. Several mathematicians—most famously Bertrand Russell—discovered that Frege’s axioms actually were self-contradictory! 
* While the ZFC axioms largely generate the mathematics everyone wants—where $3 + 3 = 6$ and other basic facts are true—they also imply some disturbing conclusions. For example, the Banach-Tarski Theorem says that a ball can be divided into six pieces and then the pieces can be rearranged to give two balls, each the same size as the original! 
* In the 1930s, Gödel proved that, assuming the ZFC axioms are consistent, then they are not complete: that is, there exist propositions that are true, but do not logically follow from the axioms. As a matter of fact, the proposition that ZFC is consistent (which is not too hard to express as a formula about sets) is an example of a true proposition that cannot be proved. There seems to be no way out of this disturbing situation; simply adding more axioms does not eliminate the problem. 

These problems will not trouble us in 6.042, but they are interesting to think about! 
```
### Reason for Removal
The section discusses meta-mathematical debates about ZFC consistency, Banach-Tarski paradox, and Gödel's incompleteness theorem. As the text itself states: *"These problems will not trouble us in 6.042"*, making them optional background material not required for the learning objectives of the course.

---

## Removed Content: Russell’s Paradox
```markdown
### Russell’s Paradox

Reasoning naively about sets quickly leads to the following contradiction—known as Russell’s Paradox: 

Let $S$ be a variable ranging over all sets, and define 
$$W ::= \{S \mid S \notin S\}$$
So by definition, 
$$S \in W \iff S \notin S$$
for every set $S$. In particular, we can let $S$ be $W$, and obtain the contradictory result that 
$$W \in W \iff W \notin W$$

This paradox revealed a fatal flaw in Frege’s initial effort to axiomatize set theory. This was an astonishing blow to efforts to provide an axiomatic foundation for Mathematics. 

But a way out was clear at the time: we cannot assume that $W$ is a set. So the step in the proof where we let $S$ be $W$ is invalid, because $S$ ranges over sets, and $W$ is not a set. 

But denying that $W$ is a set means we must reject the axiom that every mathematically well-defined collection of elements is actually a set. 

The problem faced by Logicians was how to axiomatize rules determining which well-defined collections are sets. Russell and his colleague Whitehead immediately went to work on this problem and spent a dozen years developing a huge new axiom system in an even huger monograph called *Principia Mathematica*. 

The modern ZFC axioms for set theory are much simpler than the Russell/Whitehead system and are close to Frege’s original axioms. They specify that sets must be built up from “simpler” sets in certain standard ways. In particular, no set is ever a member of itself. So the modern resolution of Russell’s paradox goes as follows: since $S \notin S$ for all sets $S$, it follows that $W$, defined above, contains every set. So $W$ can’t be a set or it would be a member of itself. 

These issues rarely come up in mainstream Mathematics. And they don’t come up at all in Computer Science, where the focus is generally on “countable,” and often just finite, sets. In practice, only Logicians and Set Theorists have to worry about collections that are too big to be sets.
```
### Reason for Removal
This is a detailed historical detour into set-theoretic paradoxes. The text explicitly points out: *"they don’t come up at all in Computer Science, where the focus is generally on 'countable,' and often just finite, sets. In practice, only Logicians and Set Theorists have to worry about collections that are too big to be sets."* As a result, it is not necessary for computer science students in this course.

---

## Removed Content: Footnote 3 (Bertrand Russell Biography)
```markdown
[^3]: Bertrand Russell was a Mathematician/Logician at Oxford University at the turn of the Twentieth Century. He reported that when he felt too old to do Mathematics, he began to study and write about Philosophy, and when he was no longer smart enough to do Philosophy, he began writing about Politics. He was jailed as a conscientious objector during World War I. He won two Nobel Prizes—one Literature Prize and one Peace Prize.
```
### Reason for Removal
This is a brief biographical footnote about Bertrand Russell and has no educational relevance to learning set theory or predicate logic.

---

# lecture_note_3.md

## Removed Content: Footnote 1 (Fibonacci Rabbit Growth History)
```markdown
[^1]: Fibonacci was a thirteenth century mathematician who came up with his numbers in modelling growth of a rabbit population. A simple model for rabbit population growth assumes that at the age of one month, a pair of rabbits will give birth to another pair of rabbits, and will continue producing a pair of rabbits every month after that. We let Fn be the total number of rabbit pairs at the start of the nth month, and Bn be the number of breeding pairs, that is, pairs that are at least one month old. Now the pairs at the nth month are the Fn−1 pairs we had the previous month, plus the Bn−1 newborn pairs produced by the previous month’s breeding pairs, so Fn = Fn−1 + Bn−1. Also, the set of breeding pairs at the nth month is simply the set of all the pairs we had the previous month, so Bn = Fn−1. Replacing Bn−1 by Fn−2 yield (2).
```
### Reason for Removal
This footnote tells a motivational/historical story of breeding rabbits to explain the recursive formula for Fibonacci numbers. While interesting, it is not required for learning or applying the induction principle or understanding properties of Fibonacci numbers in the course.

---

# lecture_note_4.md

## Removed Content: Footnote 4 (Dilworth’s Theorem Reference)
```markdown
[^4]: Lemma 4.16 also follows from a more general result known as Dilworth’s Theorem which we will not discuss.
```
### Reason for Removal
This is a bibliographic note indicating that Dilworth’s Lemma is a corollary of a more general theorem that the course does not discuss. It has no educational bearing on understanding or applying Dilworth’s Lemma in the context of the course.

---

# lecture_note_5.md

## Removed Content: Appendix A (Drawing Planar Graphs)
```markdown
## A Appendix: Drawing Planar Graphs 
[Optional] 

A planar drawing script, PDS for short, deﬁnes how to draw a connected graph in the plane. It speciﬁes the order in which to draw the edges, and, as each edge is drawn, which face of the current drawing that the edge goes into. It also speciﬁes the one or two new faces that result from drawing the edge. This is illustrated in animated slides at http://theory.csail.mit.edu/classes/6.042/fall05/planar­animation.pdf. 

It’s worth viewing these slides before trying to study the following formal deﬁnitions. 

Formally a PDS will consist of a sequence of distinct edges, and a set of cycles called boundaries. Intuitively , the edges are listed in the order in which they should be drawn in the plane, and the boundaries of the PDS describe the successive vertices on the boundaries of each of the faces of the planar drawing. 

PDS’s are ofﬁcially deﬁned recursively as follows: 
1. A single edge v—w is a PDS. It has one boundary , namely the length two cycle described by the path v, w, v. 
2. (Attaching an edge with a new endpoint to a face.) Suppose S is a PDS, and a boundary of S is described by a path of the form vxv, where v is a vertex and x is a positive length sequence of vertices. If w is a “fresh” vertex to which none of the edges of S are incident, then we can obtain another PDS, T , by adding edge v—w to the list of edges of S. The boundaries of T will be the same as those of S, except that boundary described by vxv is replaced by a boundary described by the path vxvwv . (Notice that two traversals of the new edge are actually added to the cycle.) 
3. (Attaching an edge between two vertices on a face.) Suppose S is a PDS and the edge v—w is not in the edge­list of S. Also suppose some boundary of S is represented by a path of the form vxwyv , where x and y are positive length sequences of vertices. Then we can obtain another PDS, T , by adding edge v—w to the list of edges of S. The boundaries of T will be the same as those of S, except that boundary described by vxwyv is replaced by two boundaries described by the two paths vxwv and wyvw . [^2]

The graph of a PDS is deﬁned to be the graph whose edges are those listed in the PDF and whose vertices are exactly those to which these edges are incident. 

There are a bunch of properties of any PDS that can be proved easily by induction on the length of its edge­list. 

**Lemma.** 
* No edge appears more than once in the edge­list. 
* Every boundary is a cycle that traverses only edges in the edge­list. 
* Every edge in the edge­list is traversed exactly twice by one boundary, or exactly once by each of two boundaries, and is not traversed by any other boundaries. 
* If the graph of the PDS has 3 or more vertices, then every boundary traverses at least three edges. 
* The graph of the PDS is connected. 
* If e is the length of the edge­list, v is the number of distinct vertices to which these edges are incident, and f is the number of boundaries, then:
$$v − e + f = 2$$

These properties support the intuitive claim that all connected planar drawings are captured by PDS’s. We will accept this without proof: 

**Theorem.** A graph is connected and planar iff it is the graph of a PDS. 

PDS’s are a data structure based only on the connection properties of a graph, and they are nicely suited to proving planar properties by induction without the need for any geometric facts or assumptions. However, there are still some important properties of planarity that are awkward to prove using PDS’s. An example is the fact noted earlier that any subgraph of a planar graph is planar.

[^2]: There is one minor exception to this rule. If vxwv and wyvw turn out to be the same cycle, then both “copies” of this cycle must be considered boundaries of T . Technically , this means that the set of boundaries must be a “multiset” which can contain elements more than once. But the only situation in which this occurs is when there is when the graph is a simple cycle, Cn whose embedding wil have two faces —an “inside” face and an “outside” face —that share the same boundary , this exception is so special that it is better handled in a footnote.
```
### Reason for Removal
Planar Drawing Scripts (PDS) are an optional mathematical construct designed to formalize planar graph drawings recursively without using plane geometry. The text itself marks this appendix as `[Optional]`, and notes that we accept the connection between PDS and planar graphs without proof. Thus, it is not necessary to remember or study PDS to learn the core concepts of graph theory, planarity, and Euler's formula in the course.

---

# lecture_note_6.md

## Removed Content: Hardy's Pacifism
```markdown
After all, the mathematician G. H. Hardy wrote: 
> [Number theorists] may be justiﬁed in rejoicing that there is one science, at any rate, and that their own, whose very remoteness from ordinary human activities should keep it gentle and clean. 
What most concerned Hardy was that number theory not be used in warfare; he was a pacifist. Good for him, but if number theory is remote from all human activity, then why study it? We’ll come back to that question later on, but ironically, we’ll see that poor Hardy must be turning in his grave.
```
### Reason for Removal
This is a brief historical quote and reflection on Hardy's pacifist views and hopes for number theory. It provides no technical value for understanding mathematical divisibility or cryptography.

---

## Removed Content: Famous Problems in Number Theory
```markdown
### Famous Problems in Number Theory 

* **Fermat’s Last Theorem:** Do there exist positive integers $x, y,$ and $z$ such that $x^n + y^n = z^n$ for some integer $n > 2$? In a book he was reading around 1630, Fermat claimed to have a proof, but not enough space in the margin to write it down. Wiles finally gave a proof of the theorem in 1994, after seven years of working in secrecy and isolation in his attic. His proof did not fit in any margin. 
* **Goldbach Conjecture:** Is every even integer greater than or equal to 4 the sum of two primes? For example, $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$, etc. The conjecture holds for all numbers up to $10^{16}$. In 1939 Schnirelman proved that every even number can be written as the sum of not more than 300,000 primes, which was a start. Today, we know that every even number is the sum of at most 6 primes. 
* **Twin Prime Conjecture:** Are there infinitely many primes $p$ such that $p + 2$ is also a prime? In 1966 Chen showed that there are infinitely many primes $p$ such that $p + 2$ is the product of at most two primes. So the conjecture is known to be almost true! 
* **Primality Testing:** Is there an efficient way to determine whether $n$ is prime? An amazingly simple, yet efficient method was finally discovered in 2002 by Agrawal, Kayal, and Saxena. Their paper began with a quote from Gauss emphasizing the importance and antiquity of the problem even in his time—two centuries ago. 
* **Factoring:** Given the product of two large primes $n = pq$, is there an efficient way to recover the primes $p$ and $q$? The best known algorithm is the “number field sieve”, which runs in time proportional to $e^{1.9(\ln n)^{1/3} (\ln \ln n)^{2/3}}$. This is infeasible when $n$ has a couple hundred digits or more.
```
### Reason for Removal
This sidebar details major historical unsolved (or recently solved) problems in number theory. They serve as motivational context but are not part of the active curriculum or required learning objectives of the course.

---

## Removed Content: Alan Turing Biography
```markdown
## 5 Alan Turing 

The man pictured above is Alan Turing, the most important ﬁgure in the history of computer science. For decades, his fascinating life story was shrouded by government secrecy , societal taboo, and even his own deceptions. 

At 24 Turing wrote a paper entitled *On Computable Numbers, with an Application to the Entscheidungsproblem*. The crux of the paper was an elegant way to model a computer in mathematical terms. This was a breakthrough, because it allowed the tools of mathematics to be brought to bear on questions of computation. For example, with his model in hand, Turing immediately proved that there exist problems that no computer can solve— no matter how ingenius the programmer. Turing’s paper is all the more remarkable because he wrote it in 1936, a full decade before any computer actually existed. 

The word “Entscheidungsproblem” in the title refers to one of the 28 mathematical problems posed by David Hilbert in 1900 as challenges to mathematicians of the 20th century . Turing knocked that one off in the same paper. And perhaps you’ve heard of the “Church­Turing thesis”? Same paper. So Turing was obviously a brilliant guy who generated lots of amazing ideas. 

But this lecture is about one of Turing’s less­amazing ideas. It involved codes. It involved number theory . And it was sort of stupid.
```
```markdown
## 9 Turing Postscript 

A few years after the war, Turing’s home was robbed. Detectives soon determined that a former homosexual lover of Turing’s had conspired in the robbery . So they arrested him; that is, they arrested Alan Turing. Because, at that time, homosexuality was a crime in Britain, punishable by up to two years in prison. Turing was sentenced to a humiliating hormonal “treatment” for his homosexuality: he was given estrogen injections. He began to develop breasts. 

Three years later, Alan Turing, the founder of computer science, was dead. His mother explained what happened in a biography of her own son. Despite her repeated warnings, Turing carried out chemistry experiments in his own home. Apparently , her worst fear was realized: by working with potassium cyanide while eating an apple, he poisoned himself. 

However, Turing remained a puzzle to the very end. His mother was a devoutly religious woman who considered suicide a sin. And, other biographers have pointed out, Turing had previously discussed committing suicide by eating a poisoned apple. Evidently , Alan Turing, who founded computer science and saved his country , took his own life in the end, and in just such a way that his mother could believe it was an accident.
```
### Reason for Removal
These sections present detailed biographical details on Alan Turing's research history, Bletchley Park decryption, legal prosecution, and tragic suicide. They are highly interesting and historically significant but entirely unrelated to the mathematical concepts of divisibility, modular arithmetic, and RSA encryption algorithms taught in the course.

---

## Removed Content: The Prime Number Theorem Sidebar
```markdown
### The Prime Number Theorem 

Let $\pi(x)$ denote the number of primes less than or equal to $x$. For example, $\pi(10) = 4$ because 2, 3, 5, and 7 are the primes less than or equal to 10. Primes are very irregularly distributed, so the growth of $\pi$ is similarly erratic. However, the Prime Number Theorem gives an approximate answer: 
$$\lim_{x \to \infty} \frac{\pi(x)}{x/\ln x} = 1$$
Thus, primes gradually taper off. As a rule of thumb, about 1 integer out of every $\ln x$ in the vicinity of $x$ is a prime. 

The Prime Number Theorem was conjectured by Legendre in 1798 and proved a century later by de la Vallee Poussin and Hadamard in 1896. However, after his death, a notebook of Gauss was found to contain the same conjecture, which he apparently made in 1791 at age 15. 

In late 2004 a billboard appeared in various locations around the country: 
> {first 10­digit prime found in consecutive digits of e}.com 
Substituting the correct number for the expression in curly­braces produced the URL for a Google employment page. The idea was that Google was interested in hiring the sort of people that could and would solve such a problem. 

How hard is this problem? Would you have to look through thousands or millions or billions of digits of $e$ to find a 10­digit prime? The rule of thumb derived from the Prime Number Theorem says that among 10­digit numbers, about 1 in $\ln 10^{10} \approx 23$ is prime. This suggests that the problem isn’t really so hard! Sure enough, the ﬁrst 10­digit prime in consecutive digits of $e$ appears quite early: 
$$e = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434 \dots$$
```
### Reason for Removal
This is a sidebar detailing the Prime Number Theorem, history, and a trivia puzzle from Google recruitment. It is not necessary for understanding or applying prime factorization or modular arithmetic.

---

## Removed Content: The Riemann Hypothesis Sidebar
```markdown
### The Riemann Hypothesis

Turing’s last project before he disappeared from public view in 1939 involved the construction of an elaborate mechanical device to test a mathematical conjecture called the Riemann Hypothesis. This conjecture ﬁrst appeared in a sketchy paper by Bernhard Riemann in 1859 and is now one of the most famous unsolved problems in mathematics. The formula for the sum of an inﬁnite geometric series says: 
$$\frac{1}{1-x} = 1 + x + x^2 + x^3 + \dots$$
Substituting $x = 1/2^s$, $x = 1/3^s$, $x = 1/5^s$, and so on for each prime number gives a sequence of equations: 
$$\frac{1}{1 - 1/2^s} = 1 + \frac{1}{2^s} + \frac{1}{2^{2s}} + \frac{1}{2^{3s}} + \dots$$
$$\frac{1}{1 - 1/3^s} = 1 + \frac{1}{3^s} + \frac{1}{3^{2s}} + \frac{1}{3^{3s}} + \dots$$
$$\frac{1}{1 - 1/5^s} = 1 + \frac{1}{5^s} + \frac{1}{5^{2s}} + \frac{1}{5^{3s}} + \dots$$
etc. 

Multiplying together all the left sides and all the right sides gives: 
$$\sum_{n=1}^\infty \frac{1}{n^s} = \prod_{p \in \text{primes}} \frac{1}{1 - 1/p^s}$$
The sum on the left is obtained by multiplying out all the inﬁnite series and applying the Fundamental Theorem of Arithmetic. Riemann noted that every prime appears in the expression on the right. So he proposed to learn about the primes by studying the equivalent, but simpler expression on the left. In particular, he regarded $s$ as a complex number and the left side as a function, $\zeta(s)$. 

Riemann found that the distribution of primes is related to values of $s$ for which $\zeta(s) = 0$, which led to his famous conjecture: 
> **The Riemann Hypothesis:** Every nontrivial zero of the zeta function $\zeta(s)$ lies on the line $s = 1/2 + ci$ in the complex plane. 

A proof would immediately imply, among other things, a strong form of the Prime Number Theorem.
```
### Reason for Removal
This is a sidebar detailing the Riemann Hypothesis and the Riemann zeta function. It is a highly advanced mathematical conjecture that is not part of the active syllabus or needed for learning discrete mathematics.

---

# lecture_note_7.md

## Removed Content: Floyd and Meyer Biography & Carnegie Tech Footnote
```markdown
The Invariant Theorem was formulated by Robert Floyd at Carnegie Tech in 1967[^1]. Floyd was already famous for work on formal grammars that had wide inﬂuence in the design of programming language syntax and parsers; in fact, that was how he got to be a professor even though he never got a Ph.D. 

In that same year, Albert R. Meyer was appointed Assistant Professor in the Carnegie Tech Computation Science department where he ﬁrst met Floyd. Floyd and Meyer were the only theoreticians in the department, and they were both delighted to talk about their many shared interests. After just a few conversations, Floyd’s new junior colleague decided that Floyd was the smartest person he had ever met. 

Naturally , one of the ﬁrst things Floyd wanted to tell Meyer about was his new, as yet unpublished, Invariant Theorem. Floyd explained the result to Meyer, and Meyer could not understand what Floyd was so excited about. In fact, Meyer wondered (privately) how someone as brilliant as Floyd could be excited by such a trivial observation. Floyd had to show Meyer a bunch of examples like the ones that follow in these notes before Meyer realized that Floyd’s excitement was legitimate —not at the truth of the utterly obvious Invariant Theorem, but rather at the insight that such a simple theorem could be so widely and easily applied in verifying programs. 

Floyd left for Stanford the following year. He won the Turing award —the “Nobel prize” of Computer Science— in the late 1970’s, in recognition both of his work on grammars and on the foundations of program veriﬁcation. He remained at Stanford from 1968 until his death in September, 2001. A eulogy describing Floyd’s life and work by his closest colleague, Don Knuth, can be found at http://www.acm.org/pubs/membernet/stories/floyd.pdf.

[^1]: The following year, Carnegie Tech was renamed Carnegie-Mellon Univ.
```
### Reason for Removal
This is a purely biographical and historical anecdote regarding Robert Floyd, Albert R. Meyer, and Carnegie Tech history. It contains no core mathematical definition, proof, or algorithmic detail needed for understanding state machines, reachability, or invariants.

---

# lecture_note_8.md

## Removed Content: Footnote 1 (U.S. and Japanese Interest Rates)
```markdown
[^1]: U.S. interest rates have dropped steadily for several years, and ordinary bank deposits now earn around 3%. But just a few years ago the rate was 8%; this rate makes some of our examples a little more dramatic. The rate has been as high as 17% in the past twenty years. In Japan, the standard interest rate is near zero%, and on a few occasions in the past few years has even been slightly negative. It’s a mystery to U.S. economists why the Japanese populace keeps any money in their banks.
```
### Reason for Removal
This footnote is a purely economic commentary and historical trivia regarding bank deposit rates in the U.S. and Japan. It has no mathematical relevance to learning geometric sums, annuities, or asymptotes.

---

# lecture_note_9.md

## Removed Content: Sets with Distinct Subset Sums
```markdown
### Sets with Distinct Subset Sums

How can we construct a set of $n$ positive integers such that all its subsets have distinct sums? One way is to use powers of two:
$$\{1, 2, 4, 8, 16\}$$
This approach is so natural that one suspects all other such sets must involve larger numbers. (For example, we could safely replace 16 by 17, but not by 15.) Remarkably, there are examples involving smaller numbers. Here is one:
$$\{6, 9, 11, 12, 13\}$$
One of the top mathematicians of the century, Paul Erdős, conjectured in 1931 that there are no such sets involving significantly smaller numbers. More precisely, he conjectured that the largest number must be $\ge c 2^n$ for some constant $c > 0$. He offered $500 to anyone who could prove or disprove his conjecture, but the problem remains unsolved.
```
### Reason for Removal
This is a sidebar context detailing Paul Erdős's conjecture on subset sums. It is interesting but serves as motivational context rather than a core topic or required material for learning counting rules, bijections, or inclusion-exclusion in the course.

---

## Removed Content: MIT Class Humor / Joke Awards
```markdown
Sets with Distinct Subset Sums...
Best Administrative Critique We asserted that the quiz was closed-book. On the cover page, one strong candidate for this award wrote, “There is no book.” 
Awkward Question Award “Okay, the left sock, right sock, and pants are in an antichain, but how— even with assistance— could I put on all three at once?” 
Best Collaboration Statement Inspired by a student who wrote “I worked alone” on Quiz 1.
```
### Reason for Removal
These award categories and administrative critiques are non-educational course jokes and humor specific to the Fall '05 6.042 class, and are completely irrelevant to learning discrete mathematics or counting.

---

# lecture_note_10.md

## Removed Content: A Word about Words & Bookkeeper Nomenclature
```markdown
### A Word about Words

Someday you might refer to the Subset Split Rule or the Bookkeeper Rule in front of a roomful of colleagues and discover that they’re all staring back at you blankly. This is not because they’re dumb, but rather because we made up the name “Bookkeeper Rule”. However, the rule is excellent and the name is apt, so we suggest that you play through: “You know? The Bookkeeper Rule? Don’t you guys know anything???”

The Bookkeeper Rule is sometimes called the “formula for permutations with indistinguishable objects.” The size k subsets of an n-element set are sometimes called k-combinations. Other similar-sounding descriptions are “combinations with repetition, permutations with repetition, r-permutations, permutations with indistinguishable objects,” and so on.
```
### Reason for Removal
This is meta-commentary about the naming of the "Bookkeeper Rule" and other standard combinatorics terminology. It has no mathematical relevance to learning or applying the formulas.

---

## Removed Content: Olympic Boxing Tryouts TA Characters
```markdown
### Olympic Boxing Tryouts

Ishan, famed 6.042 TA, has decided to try out for the US Olympic boxing team. After all, he’s watched all of the Rocky movies and spent hours in front of a mirror sneering, “Yo, you wanna piece a’ me?!” Ishan ﬁgures that n people (including himself) are competing for spots on the team and only k will be selected. As part of maneuvering for a spot on the team, he need to work out how many different teams are possible.

Sayan, equally-famed 6.042 TA, thinks Ishan isn’t so tough and so he might as well try out also. He reasons that n people (including himself) are trying out for k spots.
```
### Reason for Removal
These details form a humorous storyline about 6.042 TAs Ishan and Sayan competing for an Olympic boxing team. They are non-educational and not needed to understand the partition proof of Pascal's Identity.

---

# lecture_note_11.md

## Removed Content: Taylor's Theorem Algebraic Derivation
```markdown
### Taylor’s Theorem Algebraic Derivation

On the other hand, it’s instructive to derive this coefﬁcient algebraically, which we can do using Taylor’s Theorem: 

**Theorem 4.1 (Taylor’s Theorem).** 
$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!} x^2 + \frac{f'''(0)}{3!} x^3 + \dots + \frac{f^{(n)}(0)}{n!} x^n + \dots$$

This theorem says that the $n$-th coefﬁcient of $1/(1 - x)^k$ is equal to its $n$-th derivative evaluated at 0 and divided by $n!$. Computing the $n$-th derivative is straightforward. Let: 
$$G(x) ::= (1 - x)^{-k}$$

Then we have: 
$$G'(x) = k(1 - x)^{-(k+1)}$$
$$G''(x) = k(k + 1)(1 - x)^{-(k+2)}$$
$$G'''(x) = k(k + 1)(k + 2)(1 - x)^{-(k+3)}$$
$$G^{(n)}(x) = k(k + 1) \dots (k + n - 1)(1 - x)^{-(k+n)}$$

Thus, the coefﬁcient of $x^n$ in the generating function is: 
$$\frac{G^{(n)}(0)}{n!} = \frac{k(k + 1) \dots (k + n - 1)}{n!} = \frac{(k + n - 1)!}{(k - 1)! n!} = \binom{n + k - 1}{n}$$
```
### Reason for Removal
This is an algebraic derivation of the coefficient of a generating function using Taylor's Theorem. While mathematically sound, it is taught in standard calculus and is an optional alternative proof of the coefficient formula, which can already be derived combinatorial-wise via the Bookkeeper Rule / stars-and-bars. It is not necessary for understanding generating functions or solving discrete math problems.

---

# lecture_note_12.md

## Removed Content: Hockey Team Naming Trivia
```markdown
### Hockey Team Naming Trivia

The Halting Problem is the canonical undecidable problem in computation theory that was ﬁrst introduced by Alan Turing in his seminal 1936 paper. The problem is to determine whether a Turing machine halts on a given input. Anyway, much more importantly, it is the name of the MIT EECS department’s famed C-league hockey team.
```
### Reason for Removal
This is a brief joke relating the theoretical halting problem to a local MIT intramural hockey team. It contains no educational value.

---

## Removed Content: O.J. Simpson DNA Trial Transcript & DNA Frequency Discussion
```markdown
### O.J. Simpson DNA Trial Transcript & DNA Frequency Discussion

This is testimony from the O. J. Simpson murder trial on May 15, 1995: 

MR. CLARKE: When you make these estimations of frequency— and I believe you touched a little bit on a concept called independence? 
DR. COTTON: Yes, I did. 
MR. CLARKE: And what is that again? 
DR. COTTON: It means whether or not you inherit one allele that you have is not— does not affect the second allele that you might get. That is, if you inherit a band at 5,000 base pairs, that doesn’t mean you’ll automatically or with some probability inherit one at 6,000. What you inherit from one parent is what you inherit from the other. 
MR. CLARKE: Why is that important? 
DR. COTTON: Mathematically that’s important because if that were not the case, it would be improper to multiply the frequencies between the different genetic locations. 
MR. CLARKE: How do you— well, ﬁrst of all, are these markers independent that you’ve described in your testing in this case? 

The jury was told that genetic markers in blood found at the crime scene matched Simpson’s. Furthermore, the probability that the markers would be found in a randomly-selected person was at most 1 in 170 million. This astronomical ﬁgure was derived from statistics such as: 
* 1 person in 100 has marker A. 
* 1 person in 50 has marker B. 
* 1 person in 40 has marker C. 
* 1 person in 5 has marker D. 
* 1 person in 170 has marker E. 

Then these numbers were multiplied to give the probability that a randomly-selected person would have all ﬁve markers: 
$$\Pr(A \cap B \cap C \cap D \cap E) = \Pr(A) \cdot \Pr(B) \cdot \Pr(C) \cdot \Pr(D) \cdot \Pr(E) = \frac{1}{100} \cdot \frac{50} \cdot \frac{1}{40} \cdot \frac{1}{5} \cdot \frac{1}{170} = \frac{1}{170,000,000}$$

The defense pointed out that this assumes that the markers appear mutually independently. Furthermore, all the statistics were based on just a few hundred blood samples. 

If the prosecutors in the O. J. Simpson trial were wrong and markers A, B, C, D, and E appear only pairwise independently, then the probability that a randomly-selected person has all ﬁve markers is no more than: 
$$\Pr(A \cap B \cap C \cap D \cap E) \le \Pr(A \cap E) = \Pr(A) \cdot \Pr(E) = \frac{1}{100} \cdot \frac{1}{170} = \frac{1}{17,000}$$
```
### Reason for Removal
This is a case study of DNA evidence and court transcripts from the O.J. Simpson murder trial. While illustrating why mutual vs. pairwise independence matters in practice, the transcripts and details of this legal case are historical background and not needed to learn the definition and theorems of pairwise and mutual independence.

---

# lecture_note_13.md

## Removed Content: Polling Context on Hillary Clinton and Rudy Giuliani in 2008
```markdown
### Polling Context on Hillary Clinton and Rudy Giuliani in 2008

Suppose we want to estimate the fraction of the U.S. voting population who would favor Hillary Clinton over Rudy Giuliani in the year 2008 presidential election. Let p be this unknown fraction. We can only keep our ﬁngers crossed for this race to happen – when they ran against each other for the U.S. Senate in 2000, they generated some of the best entertainment in TV history.
```
### Reason for Removal
This is political commentary and humor specific to the 2008 U.S. presidential election and 2000 Senate race. It contains no educational value.

---

## Removed Content: Problem 1. Explaining Sampling to a Jury
```markdown
### Problem 1. Explaining Sampling to a Jury

We just showed that merely sampling 662 voters will yield a fraction that, 95% of the time, is within 0.04 of the of the actual fraction of voters who prefer Clinton. The actual size of the voting population (10’s of millions) was never considered because it did not matter. Suppose you were going to serve as an expert witness in a trial. How would you explain why the number of people necessary to poll does not depend on the population size?
```
### Reason for Removal
This is a discussion question for a class problem session. It is not a mathematical proof or explanation.

---

## Removed Content: Making a Baby Girl Strategy Question
```markdown
### Making a Baby Girl Strategy Question

A couple really wants to have a baby girl. There is a 50% chance that each child they have is a girl, and the genders of their children are mutually independent. If the couple insists on having children until they get a girl, then how many baby boys should they expect ﬁrst? 

Something to think about: If every couple follows the strategy of having children until they get a girl, what will eventually happen to the fraction of girls born in this world?
```
### Reason for Removal
This is an informal question posing a puzzle for students to think about after applying the mean time to failure formula. While interesting, the math of the coin flips/Bernoulli process is already fully covered.

---

# lecture_note_14.md

## Removed Content: Introductory Paragraphs and Proofs of Theorems/Lemmas
```markdown
Massachusetts Institute of Technology
6.042J/18.062J, Fall ’05: Mathematics for Computer Science
Prof. Albert R. Meyer and Prof. Ronitt Rubinfeld

Course Notes, Week 14
December 2
revised December 8, 2005, 61 minutes

Missed Expectations?
In the previous notes, we saw that the average value of a random quantity is captured by the mathematical concept of the expectation of a random variable, and we calculated expectations for several kinds of random variables. Now we will see two things that make expectations so useful. First, they are often very easy to calculate due to the fact that they obey linearity. Second, once you know what the expectation is, you can also get some type of bound on the probability that you are far from the expectation —that is, you can show that really weird things are not that likely to happen. How good a bound you can get depends on what you know about your distribution, but don’t worry, even if you know next to nothing, you can still say something relatively interesting.
```

```markdown
### Theorem 3.4 (Law of Total Expectation) Proof
E [R] = \sum_{r} r \cdot \Pr \{R = r\}
= \sum_{r} r \cdot \sum_{i} \Pr \{R = r \mid A_i\} \Pr \{A_i\}
= \sum_{r} \sum_{i} r \cdot \Pr \{R = r \mid A_i\} \Pr \{A_i\}
= \sum_{i} \sum_{r} r \cdot \Pr \{R = r \mid A_i\} \Pr \{A_i\}
= \sum_{i} \Pr \{A_i\} \sum_{r} r \cdot \Pr \{R = r \mid A_i\}
= \sum_{i} \Pr \{A_i\} \mathbb{E}[R \mid A_i].
```

```markdown
### Theorem 4.2 (Product of Independent Expectations) Proof
E [R_1 \cdot R_2] = \sum_{r\in\text{range}(R_1)} E [R_1 \cdot R_2 \mid R_1 = r] \cdot \Pr \{R_1 = r\}
= \sum_{r} E [r \cdot R_2 \mid R_1 = r] \cdot \Pr \{R_1 = r\}
= \sum_{r} r \cdot E [R_2 \mid R_1 = r] \cdot \Pr \{R_1 = r\}
= \sum_{r} r \cdot E [R_2] \cdot \Pr \{R_1 = r\}
= E [R_2] \sum_{r} r \cdot \Pr \{R_1 = r\}
= E [R_2] \cdot E [R_1].
```

```markdown
### Theorem 6.1 (Markov's Theorem) Proof
We will show that E [R] >= x Pr {R >= x}.
Let Ix be the indicator variable for the event [R >= x], and consider the random variable xIx. Note that R >= xIx, because at any sample point, w:
- if R(w) >= x then R(w) >= x = x * 1 = xIx(w), and
- if R(w) < x then R(w) >= 0 = x * 0 = xIx(w).
Therefore, E [R] >= E [xIx] = x E [Ix] = x Pr {Ix = 1} = x Pr {R >= x}.
```

```markdown
### Theorem 8.1 (Alternative Definition of Variance) Proof
Var [R] = E [(R - E [R])^2] = E [(R - \mu)^2]
= E [R^2 - 2\mu R + \mu^2]
= E [R^2] - 2\mu E [R] + \mu^2
= E [R^2] - 2\mu^2 + \mu^2
= E [R^2] - \mu^2
= E [R^2] - E^2 [R].
```

```markdown
### Lemma 8.2 (Zero Variance) Proof
Var [R] = 0 iff E [(R - E [R])^2] = 0.
The inner expression is always nonnegative because of the square, so E [(R - E [R])^2] = 0 iff Pr {(R - E [R])^2 = 0} = 1.
But (R - E [R])^2 = 0 and R = E [R] describe the same event.
Therefore, Var [R] = 0 iff Pr {R = E [R]} = 1.
```

```markdown
### Theorem 8.3 (Dealing with Constants) Proof
Var [aR + b] = E [(aR + b)^2] - E^2 [aR + b]
For the first term: E [(aR + b)^2] = E [a^2 R^2 + 2abR + b^2] = a^2 E [R^2] + 2ab E [R] + b^2.
For the second term: E^2 [aR + b] = (a E [R] + b)^2 = a^2 E^2 [R] + 2ab E [R] + b^2.
Subtracting the second term from the first:
Var [aR + b] = a^2 E [R^2] - a^2 E^2 [R] = a^2 (E [R^2] - E^2 [R]) = a^2 Var [R].
```

```markdown
### Theorem 8.5 (Pairwise Independent Additivity of Variance) Proof
E [(\sum_i R_i)^2] = E [\sum_i \sum_j R_i R_j] = \sum_i \sum_j E [R_i R_j]
= \sum_{1<=i!=j<=n} E [R_i] E [R_j] + \sum_i E [R_i^2]
Also, E^2 [\sum_i R_i] = (\sum_i E [R_i])^2 = \sum_i \sum_j E [R_i] E [R_j]
= \sum_{1<=i!=j<=n} E [R_i] E [R_j] + \sum_i E^2 [R_i]
Subtracting the two:
Var [\sum_i R_i] = \sum_i (E [R_i^2] - E^2 [R_i]) = \sum_i Var [R_i].
```

```markdown
### Theorem (Pairwise Independent Sampling) Proof
E [Sn/n] = E [\sum_i Gi / n] = \sum_i E [Gi] / n = n\mu / n = \mu.
Var [Sn/n] = (1/n^2) Var [\sum_i Gi] = (1/n^2) \sum_i Var [Gi] = n\sigma^2 / n^2 = \sigma^2 / n.
Applying Chebyshev's Bound:
Pr {|Sn/n - \mu| >= x} <= Var [Sn/n] / x^2 = \sigma^2 / (n x^2) = (1/n) (\sigma / x)^2.
```
### Reason for Removal
The introductory MIT course details are administrative, and the opening paragraph is purely motivational overview. The proofs of the theorems and lemmas are standard algebraic expansions or definition manipulations; they are not required to understand or apply the mathematical properties and formulas in discrete mathematics.

---

## Removed Content: Detailed Analytical Examples and Visual Layouts
```markdown
### Hat-Check Problem Alternative Summation Method
Let the random variable R be the number of men that get their own hat. We want to compute E [R]. By the definition of expectation, we have:
E [R] = \sum_{k=0}^{\infty} k \cdot \Pr \{R = k\}
Now we’re in trouble, because evaluating Pr {R = k} is a mess and we then need to substitute this mess into a summation.
```

```markdown
### Coupon Collector Colored Cars Visualization
Suppose there are five different types of Racin’ Rocket, and I receive this sequence:
blue, green, green, red, blue, orange, blue, orange, gray
Let’s partition the sequence into 5 segments:
blue (X0), green (X1), green red (X2), blue orange (X3), blue orange gray (X4)
```

```markdown
### Section 4.2: The Product of Two Dice
Suppose we throw two independent, fair dice and multiply the numbers that come up. What is the expected value of this product?
E [R_1 \cdot R_2] = E [R_1] \cdot E [R_2] = 3.5 \cdot 3.5 = 12.25.
Now suppose that the two dice are not independent; in fact, assume that the second die is always the same as the first.
E [R_1 \cdot R_2] = E [R_1^2] = \sum_{i=1}^6 i^2 \cdot \Pr \{R_1 = i\} = 91/6 \approx 15.17 \neq 12.25.
```

```markdown
### Chinese Appetizer Game (Markov tightness example)
What probability do we get from Markov’s Theorem? Let the random variable, R, be the number of people that get the right appetizer. You can show that E [R] = 1. Applying Markov’s Theorem, we find:
Pr {R >= n} <= E [R] / n = 1/n.
So for the Chinese appetizer problem, Markov’s Theorem is tight!
```

```markdown
### IQ Bounds Shifting
No MIT student has an IQ less than 100. This means that if we let T ::= R − 100, then T is nonnegative and E [T ] = 50, so we can apply Markov’s Theorem to T and conclude:
Pr {R > 200} = Pr {T > 100} <= E [T] / 100 = 50/100 = 1/2.
```

```markdown
### Variance of Gambling Games (Game A vs Game B)
Game A: We win $2 with probability 2/3 and lose $1 with probability 1/3.
Game B: We win $1002 with probability 2/3 and lose $2001 with probability 1/3.
E[A] = 1, E[B] = 1.
Var[A] = 2.
Var[B] = 2,004,002.
High variance is often associated with high risk. In ten rounds of Game B, we expect to make $10, but could actually lose more than $20,000!
```

```markdown
### Standard Deviation Dimensional Analysis
From a dimensional analysis viewpoint, the “units” of variance are wrong: if the random variable is in dollars, then the expectation is also in dollars, but the variance is in square dollars.
```

```markdown
### IQ Chebyshev Example
Suppose that, in addition to the national average IQ being 100, we also know the standard deviation of IQ’s is 10. How rare is an IQ of 200 or more?
Pr {R >= 200} = Pr {|R − 100| >= 100} <= Var [R] / 100^2 = 10^2 / 100^2 = 1/100.
```

```markdown
### Section 8.1: Why Variance?
Why not simply compute the average deviation from the mean? That is, why not define variance to be E [R - E [R]]?
E [R - E [R]] = E [R] - E [E [R]] = E [R] - E [R] = 0.
By this definition, every random variable has zero variance.
Of course, we could also prevent positive and negative deviations from canceling by taking an absolute value. That is, we could define variance to be E [|R - E [R]|]. However, the conventional version of variance has some valuable mathematical properties which the absolute value version does not.
```
### Reason for Removal
These are illustrative games, analytical examples, and intuitive visualizations. While they are useful for conveying conceptual meaning (e.g., explaining why squaring is used in variance, showing why Markov can be loose or tight, and demonstrating risk through standard deviation), the mathematical statements and formulas summarized in the lecture notes are sufficient for reference and application.

---
