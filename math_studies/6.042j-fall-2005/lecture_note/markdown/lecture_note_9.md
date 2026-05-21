# Counting I 

Two different subsets of the ninety 25-digit numbers shown below have the same sum: 

```
20480135385502964448038  3171004832173501394113017  5763257331083479647409398  8247331000042995311646021 
489445991866915676240992  3208234421597368647019265  5800949123548989122628663  8496243997123475922766310 
1082662032430379651370981  3437254656355157864869113  6042900801199280218026001  8518399140676002660747477 
1178480894769706178994993  3574883393058653923711365  6116171789137737896701405  8543691283470191452333763 
1253127351683239693851327  3644909946040480189969149  6144868973001582369723512  8675309258374137092461352 
1301505129234077811069011  3790044132737084094417246  6247314593851169234746152  8694321112363996867296665 
1311567111143866433882194  3870332127437971355322815  6814428944266874963488274  8772321203608477245851154 
1470029452721203587686214  4080505804577801451363100  6870852945543886849147881  8791422161722582546341091 
1578271047286257499433886  4167283461025702348124920  6914955508120950093732397  9062628024592126283973285 
1638243921852176243192354  4235996831123777788211249  6949632451365987152423541  9137845566925526349897794 
1763580219131985963102365  4670939445749439042111220  7128211143613619828415650  9153762966803189291934419 
1826227795601842231029694  4815379351865384279613427  7173920083651862307925394  9270880194077636406984249 
1843971862675102037201420  4837052948212922604442190  7215654874211755676220587  9324301480722103490379204 
2396951193722134526177237  5106389423855018550671530  7256932847164391040233050  9436090832146695147140581 
2781394568268599801096354  5142368192004769218069910  7332822657075235431620317  9475308159734538249013238 
2796605196713610405408019  5181234096130144084041856  7426441829541573444964139  9492376623917486974923202 
2931016394761975263190347  5198267398125617994391348  7632198126531809327186321  9511972558779880288252979 
2933458058294405155197296  5317592940316231219758372  7712154432211912882310511  9602413424619187112552264 
3075514410490975920315348  5384358126771794128356947  7858918664240262356610010  9631217114906129219461111 
3111474985252793452860017  5439211712248901995423441  7898156786763212963178679  9908189853102753335981319 
3145621587936120118438701  5610379826092838192760458  8147591017037573337848616  9913237476341764299813987 
3148901255628881103198549  5632317555465228677676044  8149436716871371161932035 
3157693105325111284321993  5692168374637019617423712  8176063831682536571306791 
```

Can you find two such subsets? This is a very difficult computational problem, but we will prove that such subsets must exist. 

---

## 1 Counting One Thing by Counting Another 

In formal terms, every counting problem comes down to determining the size of some set. The size or cardinality of a set $S$ is the number of elements in $S$ and is denoted $|S|$. 

### 1.1 The Bijection Rule 

**Rule 1 (Bijection Rule).** If there exists a bijection $f : A \longrightarrow B$, then $|A| = |B|$. 

#### Example: Doughnuts and Bit Sequences
* **Set A:** All ways to select 12 doughnuts when 5 varieties (chocolate, lemon-filled, sugar, glazed, plain) are available. 
* **Set B:** All 16-bit sequences with exactly 4 ones. 

We can map a doughnut selection to a bit sequence by using `0`s for doughnuts and `1`s for the transitions between categories. For example, 2 chocolate, 0 lemon-filled, 6 sugar, 2 glazed, and 2 plain corresponds to: 
$$\underbrace{00}_{\text{choc}} \ 1 \ \underbrace{}}_{\text{lemon}} \ 1 \ \underbrace{000000}_{\text{sugar}} \ 1 \ \underbrace{00}_{\text{glazed}} \ 1 \ \underbrace{00}_{\text{plain}}$$
which is the binary sequence `0011000000100100`. 

Since this mapping is a bijection, $|A| = |B|$. Once we know how to count sequences of this type, we can count doughnut selections. 

---

## 2 Two Basic Counting Rules 

### 2.1 The Sum Rule 

**Rule 2 (Sum Rule).** If $A_1, A_2, \dots, A_n$ are disjoint sets, then: 
$$|A_1 \cup A_2 \cup \dots \cup A_n| = |A_1| + |A_2| + \dots + |A_n|$$

### 2.2 The Product Rule 

**Rule 3 (Product Rule).** If $P_1, P_2, \dots, P_n$ are sets, then: 
$$|P_1 \times P_2 \times \dots \times P_n| = |P_1| \cdot |P_2| \dots |P_n|$$

### 2.3 Putting Rules Together 

#### Passwords
A valid password is a sequence of between 6 and 8 characters. The first character must be a letter (52 choices), and the remaining characters must be letters or digits (62 choices). 

The set of valid passwords is $(F \times S^5) \cup (F \times S^6) \cup (F \times S^7)$, where $|F| = 52$ and $|S| = 62$. By the Sum and Product Rules: 
$$\text{Total Passwords} = 52 \cdot 62^5 + 52 \cdot 62^6 + 52 \cdot 62^7 \approx 1.8 \times 10^{14}$$

#### Subsets of an $n$-element Set
There is a bijection between subsets of $\{x_1, \dots, x_n\}$ and $n$-bit sequences (where the $i$-th bit is $1$ if $x_i$ is in the subset, and $0$ otherwise). Since the set of $n$-bit sequences is $\{0,1\}^n$, the product rule tells us there are: 
$$|\{0,1\}|^n = 2^n \text{ subsets}$$

---

## 3 More Functions: Injections and Surjections 

**Rule 4 (Mapping Rule).** 
1. If $f : X \longrightarrow Y$ is surjective, then $|X| \ge |Y|$. 
2. If $f : X \longrightarrow Y$ is injective, then $|X| \le |Y|$. 
3. If $f : X \longrightarrow Y$ is bijective, then $|X| = |Y|$. 

### 3.1 The Pigeonhole Principle 

The Pigeonhole Principle is the contrapositive of part (2) of the Mapping Rule: 

**Rule 5 (Pigeonhole Principle).** If $|X| > |Y|$, then for every function $f : X \longrightarrow Y$, there exist two different elements of $X$ that map to the same element of $Y$. 

#### Hairs on Heads
**Rule 6 (Generalized Pigeonhole Principle).** If $|X| > k \cdot |Y|$, then every function $f : X \longrightarrow Y$ maps at least $k + 1$ different elements of $X$ to the same element of $Y$. 

In Boston (population $\approx 500,000$ non-bald people), the number of hairs on a head is at most 200,000. Let $X$ be the set of people and $Y = \{1, \dots, 200,000\}$. Since $|X| > 2|Y|$, at least $\lfloor |X|/|Y| \rfloor + 1 = 3$ people in Boston have the exact same number of hairs on their heads. 

#### Subsets with the Same Sum
Let $A$ be the collection of all subsets of the 90 numbers listed at the start. So $|A| = 2^{90} \approx 1.237 \times 10^{27}$. 
The sum of any subset is at most $90 \cdot 10^{25}$. Let $B = \{0, 1, \dots, 90 \cdot 10^{25}\}$. So $|B| = 90 \cdot 10^{25} + 1 \approx 0.901 \times 10^{27}$. 

Since $|A| > |B|$, by the Pigeonhole Principle, there must be two different subsets with the same sum. 

---

## 4 The Generalized Product Rule 

**Rule 7 (Generalized Product Rule).** Let $S$ be a set of length-$k$ sequences. If there are: 
* $n_1$ possible first entries, 
* $n_2$ possible second entries for each first entry, 
* $n_3$ possible third entries for each combination of first and second entries, etc. 
then: 
$$|S| = n_1 \cdot n_2 \cdot n_3 \dots n_k$$

#### Example: Prizes
If 3 distinct prizes are awarded to different students in a class of $n$ students, the number of assignments is: 
$$n(n - 1)(n - 2)$$

#### Defective Dollars
A serial number is an 8-digit sequence. The total number of serial numbers is $10^8$. The number of serial numbers with all digits different is: 
$$10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 = 1,814,400$$
Thus, the fraction of nondefective dollars is $1,814,400 / 10^8 = 1.8144\%$. 

#### Chess Configurations
How many ways can we place a pawn ($p$), knight ($k$), and bishop ($b$) on a chessboard so no two pieces share a row or column? 
* $r_p$ is one of 8 rows, $c_p$ is one of 8 columns. 
* $r_k$ is one of 7 rows, $c_k$ is one of 7 columns. 
* $r_b$ is one of 6 rows, $c_b$ is one of 6 columns. 
Total configurations = $(8 \cdot 7 \cdot 6)^2 = 112,896$. 

### 4.1 Permutations 

A permutation of a set $S$ is a sequence containing every element of $S$ exactly once. The number of permutations of an $n$-element set is: 
$$n! = n(n - 1)(n - 2) \dots 3 \cdot 2 \cdot 1$$

---

## 5 The Division Rule 

**Rule 8 (Division Rule).** If $f : A \longrightarrow B$ is $k$-to-1, then $|A| = k \cdot |B|$, or $|B| = \frac{|A|}{k}$. 

#### Identical Rooks on a Chessboard
In how many ways can we place two identical rooks on a chessboard so they do not share a row or column? 
Let $A$ be the set of sequences $(r_1, c_1, r_2, c_2)$ with $r_1 \neq r_2$ and $c_1 \neq c_2$. So $|A| = (8 \cdot 7)^2$. 
The mapping to identical rook configurations is 2-to-1 because the rooks are indistinguishable. Thus: 
$$\text{Total configurations} = \frac{|A|}{2} = \frac{(8 \cdot 7)^2}{2} = 1568$$

#### Circular Seating
In how many ways can King Arthur seat $n$ different knights at his round table up to rotation? 
Let $A$ be the set of all $n!$ permutations. The mapping to circular tables is $n$-to-1 because there are $n$ cyclic shifts of any sequence. Thus: 
$$\text{Total arrangements} = \frac{n!}{n} = (n - 1)!$$

---

## 6 Inclusion-Exclusion 

### 6.1 Two Sets 
$$|S_1 \cup S_2| = |S_1| + |S_2| - |S_1 \cap S_2|$$

### 6.2 Three Sets 
$$|S_1 \cup S_2 \cup S_3| = |S_1| + |S_2| + |S_3| - |S_1 \cap S_2| - |S_1 \cap S_3| - |S_2 \cap S_3| + |S_1 \cap S_2 \cap S_3|$$

#### Permutations containing consecutive patterns
In how many permutations of $\{0, 1, \dots, 9\}$ do either $42$, $04$, or $60$ appear consecutively? 
Let $P_{42}, P_{04}, P_{60}$ be the sets of permutations containing these patterns. 
* $|P_{42}| = |P_{04}| = |P_{60}| = 9!$ (by treating the consecutive block as a single symbol). 
* $|P_{42} \cap P_{60}| = 8!$ (treating both $42$ and $60$ as symbols). 
* $|P_{60} \cap P_{04}| = 8!$ (treating $604$ as a symbol). 
* $|P_{42} \cap P_{04}| = 8!$ (treating $042$ as a symbol). 
* $|P_{60} \cap P_{04} \cap P_{42}| = 7!$ (treating $6042$ as a symbol). 
Using the formula: 
$$\text{Total} = 3 \cdot 9! - 3 \cdot 8! + 7!$$

### 6.3 General Formula 

**Rule 9 (Inclusion-Exclusion Principle).** 
$$|S_1 \cup S_2 \cup \dots \cup S_n| = \sum_{i} |S_i| - \sum_{i < j} |S_i \cap S_j| + \sum_{i < j < k} |S_i \cap S_j \cap S_k| - \dots + (-1)^{n-1} |S_1 \cap \dots \cap S_n|$$

#### Counting Primes Up to 100
How many primes are in the range $1, \dots, 100$? 
Let $C$ be the set of composite numbers in this range. A composite number $n \le 100$ must have a prime factor $\le \sqrt{100} = 10$. The only primes $\le 10$ are 2, 3, 5, and 7. Thus: 
$$C = A_2 \cup A_3 \cup A_5 \cup A_7$$
where $A_m = \{x \in \{2, \dots, 100\} \mid m \mid x \wedge x \neq m\}$. 
The size of each $A_m$ is $|A_m| = \lfloor 100/m \rfloor - 1$: 
* $|A_2| = 49$, $|A_3| = 32$, $|A_5| = 19$, $|A_7| = 13$. 
Intersections: 
* $|A_2 \cap A_3| = \lfloor 100/6 \rfloor = 16$ 
* $|A_2 \cap A_5| = \lfloor 100/10 \rfloor = 10$ 
* $|A_2 \cap A_7| = \lfloor 100/14 \rfloor = 7$ 
* $|A_3 \cap A_5| = \lfloor 100/15 \rfloor = 6$ 
* $|A_3 \cap A_7| = \lfloor 100/21 \rfloor = 4$ 
* $|A_5 \cap A_7| = \lfloor 100/35 \rfloor = 2$ 
Three-way: 
* $|A_2 \cap A_3 \cap A_5| = 3$, $|A_2 \cap A_3 \cap A_7| = 2$, $|A_2 \cap A_5 \cap A_7| = 1$, $|A_3 \cap A_5 \cap A_7| = 0$. 
Four-way: 
* $|A_2 \cap A_3 \cap A_5 \cap A_7| = 0$. 

Using Inclusion-Exclusion: 
$$|C| = (49+32+19+13) - (16+10+7+6+4+2) + (3+2+1+0) - 0 = 74 \text{ composites}$$
Since $1$ is neither prime nor composite, the number of primes is: 
$$100 - 74 - 1 = 25 \text{ primes}$$
