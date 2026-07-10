---
pdf_source: David J. Griffiths, Darrell F. Schroeter - David J. Griffiths, Darrell F. Schroeter - Introduction to Quantum Mechanics - Cambridge University Press (2018) (2018, Cambridge University Press) - libgen.li (1).pdf
converted_at: 2026-06-26T13:14:53.161267
backend: pipeline
parse_method: auto
formula_enabled: True
table_enabled: True
language: en
elapsed_sec: 380.16
---



---
> 📄 **Página 1**
---

## 1.1 THE SCHRÖDINGER EQUATION

Imagine a particle of mass m, constrained to move along the x axis, subject to some specified force $\boldsymbol { F } ( \boldsymbol { x } , t )$ (Figure 1.1). The program of classical mechanics is to determine the position of the particle at any given time: x(t). Once we know that, we can figure out the velocity $( v =$ $d x / d t )$ , the momentum $( p = m v )$ , the kinetic energy $\left( T = ( 1 / 2 ) m v ^ { 2 } \right)$ , or any other dynamical variable of interest. And how do we go about determining $x ( t ) ?$ We apply Newton’s second law: $F = m a$ . (For conservative systems—the only kind we shall consider, and, fortunately, the only kind that occur at the microscopic level—the force can be expressed as the derivative of a potential energy function,<sup>1</sup> $F = - \partial V / \partial x$ , and Newton’s law reads m $d ^ { 2 } x / d t ^ { 2 } = - \partial V / \partial x . )$ This, together with appropriate initial conditions (typically the position and velocity at $t = 0 )$ , determines x(t).

Quantum mechanics approaches this same problem quite differently. In this case what we’re looking for is the particle’s wave function, $\Psi ( x , t )$ , and we get it by solving the Schrödinger equation:

$$
{ \boxed { i \hbar { \frac { \partial \Psi } { \partial t } } = - { \frac { \hbar ^ { 2 } } { 2 m } } { \frac { \partial ^ { 2 } \Psi } { \partial x ^ { 2 } } } + V \Psi . } }\tag{1.1}
$$

Here i is the square root of −1, and <sup>-</sup> is Planck’s constant—or rather, his original constant (h) divided by 2π:

$$
\hbar = { \frac { h } { 2 \pi } } = 1 . 0 5 4 5 7 3 \times 1 0 ^ { - 3 4 } { \mathrm { J } } { \mathrm { s } } .\tag{1.2}
$$

The Schrödinger equation plays a role logically analogous to Newton’s second law: Given suitable initial conditions (typically, $\Psi ( x , 0 ) )$ , the Schrödinger equation determines $\Psi ( x , t )$ for all future time, just as, in classical mechanics, Newton’s law determines x(t) for all future time.<sup>2</sup>

## 1.2 THE STATISTICAL INTERPRETATION

But what exactly is this “wave function,” and what does it do for you once you’ve got it? After all, a particle, by its nature, is localized at a point, whereas the wave function (as its name suggests) is spread out in space (it’s a function of x, for any given t). How can such an object represent the state of a particle? The answer is provided by Born’s statistical interpretation, which says that $| \Psi ( x , t ) | ^ { 2 }$ gives the probability of finding the particle at point x, at time $t { \mathrm { - } } 0 \Gamma ,$ more precisely,<sup>3</sup>

<sup>1</sup> Magnetic forces are an exception, but let’s not worry about them just yet. By the way, we shall assume throughout this book that the motion is nonrelativistic $( v \ll c )$

<sup>2</sup> For a delightful first-hand account of the origins of the Schrödinger equation see the article by Felix Bloch in Physics Today, December 1976.



---
> 📄 **Página 2**
---

![](images/2d36663bdfa43ce6e2edbfef4928396dbcae06b4163cb77773ece112c5322d03.jpg)  
Figure 1.1: A “particle” constrained to move in one dimension under the influence of a specified force.

![](images/9a9da766b3c210de48e78d0d6a3a61f90300810acc026f7ddb17ccfe7dd9e782.jpg)  
Figure 1.2: A typical wave function. The shaded area represents the probability of finding the particle between a and b. The particle would be relatively likely to be found near A, and unlikely to be found near B.

$$
\int _ { a } ^ { b } \vert \Psi ( x , t ) \vert ^ { 2 } d x = { \left\{ \begin{array} { l l } { { \mathrm { p r o b a b i l i t y ~ o f ~ f i n d i n g ~ t h e ~ p a r t i c l e } } } \\ { { \mathrm { b e t w e e n } } a { \mathrm { ~ a n d } } b , { \mathrm { ~ a t ~ t i m e } } t . } \end{array} \right. }\tag{1.3}
$$

Probability is the area under the graph of $| \Psi | ^ { 2 }$ . For the wave function in Figure 1.2, you would be quite likely to find the particle in the vicinity of point A, where $| \Psi | ^ { 2 }$ is large, and relatively unlikely to find it near point B.

The statistical interpretation introduces a kind of indeterminacy into quantum mechanics, for even if you know everything the theory has to tell you about the particle (to wit: its wave function), still you cannot predict with certainty the outcome of a simple experiment to measure its position—all quantum mechanics has to offer is statistical information about the possible results. This indeterminacy has been profoundly disturbing to physicists and philosophers alike, and it is natural to wonder whether it is a fact of nature, or a defect in the theory.

Suppose I do measure the position of the particle, and I find it to be at point $C . ^ { 4 }$ Question: Where was the particle just before I made the measurement? There are three plausible answers to this question, and they serve to characterize the main schools of thought regarding quantum indeterminacy:

<sup>3</sup> The wave function itself is complex, but $| \Psi | ^ { 2 } = \Psi ^ { * } \Psi$ (where $\Psi ^ { * }$ is the complex conjugate of $\Psi )$ is real and non-negative—as a probability, of course, must be.

<sup>4</sup> Of course, no measuring instrument is perfectly precise; what I mean is that the particle was found in the vicinity of C, as defined by the precision of the equipment.



---
> 📄 **Página 3**
---

1. The realist position: The particle was at C. This certainly seems reasonable, and it is the response Einstein advocated. Note, however, that if this is true then quantum mechanics is an incomplete theory, since the particle really was at C, and yet quantum mechanics was unable to tell us so. To the realist, indeterminacy is not a fact of nature, but a reflection of our ignorance. As d’Espagnat put it, “the position of the particle was never indeterminate, but was merely unknown to the experimenter.”<sup>5</sup> Evidently  is not the whole story—some additional information (known as a hidden variable) is needed to provide a complete description of the particle.

2. The orthodox position: The particle wasn’t really anywhere. It was the act of measurement that forced it to “take a stand” (though how and why it decided on the point C we dare not ask). Jordan said it most starkly: “Observations not only disturb what is to be measured, they produce it . . . We compel [the particle] to assume a definite position.”<sup>6</sup> This view (the so-called Copenhagen interpretation), is associated with Bohr and his followers. Among physicists it has always been the most widely accepted position. Note, however, that if it is correct there is something very peculiar about the act of measurement—something that almost a century of debate has done precious little to illuminate.

3. The agnostic position: Refuse to answer. This is not quite as silly as it sounds—after all, what sense can there be in making assertions about the status of a particle before a measurement, when the only way of knowing whether you were right is precisely to make a measurement, in which case what you get is no longer “before the measurement”? It is metaphysics (in the pejorative sense of the word) to worry about something that cannot, by its nature, be tested. Pauli said: “One should no more rack one’s brain about the problem of whether something one cannot know anything about exists all the same, than about the ancient question of how many angels are able to sit on the point of a needle.”<sup>7</sup> For decades this was the “fall-back” position of most physicists: they’d try to sell you the orthodox answer, but if you were persistent they’d retreat to the agnostic response, and terminate the conversation.

Until fairly recently, all three positions (realist, orthodox, and agnostic) had their partisans. But in 1964 John Bell astonished the physics community by showing that it makes an observable difference whether the particle had a precise (though unknown) position prior to the measurement, or not. Bell’s discovery effectively eliminated agnosticism as a viable option, and made it an experimental question whether 1 or 2 is the correct choice. I’ll return to this story at the end of the book, when you will be in a better position to appreciate Bell’s argument; for now, suffice it to say that the experiments have decisively confirmed the orthodox interpretation:<sup>8</sup> a particle simply does not have a precise position prior to measurement, any more than the ripples on a pond do; it is the measurement process that insists on one particular number, and thereby in a sense creates the specific result, limited only by the statistical weighting imposed by the wave function.

<sup>5</sup> Bernard d’Espagnat, “The Quantum Theory and Reality” (Scientific American, November 1979, p. 165).

<sup>6</sup> Quoted in a lovely article by N. David Mermin, “Is the moon there when nobody looks?” (Physics Today, April 1985, p. 38).

<sup>7</sup> Ibid., p. 40.



---
> 📄 **Página 4**
---

![](images/a900a0f8b43f40f5fe912da2d265ae9fefa2a9451e726211be535d0441dc8ff0.jpg)  
Figure 1.3: Collapse of the wave function: graph of $| \Psi | ^ { 2 }$ immediately after a measurement has found the particle at point C.

What if I made a second measurement, immediately after the first? Would I get C again, or does the act of measurement cough up some completely new number each time? On this question everyone is in agreement: A repeated measurement (on the same particle) must return the same value. Indeed, it would be tough to prove that the particle was really found at C in the first instance, if this could not be confirmed by immediate repetition of the measurement. How does the orthodox interpretation account for the fact that the second measurement is bound to yield the value C? It must be that the first measurement radically alters the wave function, so that it is now sharply peaked about C (Figure 1.3). We say that the wave function collapses, upon measurement, to a spike at the point C (it soon spreads out again, in accordance with the Schrödinger equation, so the second measurement must be made quickly). There are, then, two entirely distinct kinds of physical processes: “ordinary” ones, in which the wave function evolves in a leisurely fashion under the Schrödinger equation, and “measurements,” in which  suddenly and discontinuously collapses.<sup>9</sup>

8 This statement is a little too strong: there exist viable nonlocal hidden variable theories (notably David Bohm’s), and other formulations (such as the many worlds interpretation) that do not fit cleanly into any of my three categories. But I think it is wise, at least from a pedagogical point of view, to adopt a clear and coherent platform at this stage, and worry about the alternatives later.

<sup>9</sup> The role of measurement in quantum mechanics is so critical and so bizarre that you may well be wondering what precisely constitutes a measurement. I’ll return to this thorny issue in the Afterword; for the moment let’s take the naive view: a measurement is the kind of thing that a scientist in a white coat does in the laboratory, with rulers, stopwatches, Geiger counters, and so on.



---
> 📄 **Página 5**
---

## Example 1.1

Electron Interference. I have asserted that particles (electrons, for example) have a wave nature, encoded in . How might we check this, in the laboratory?

The classic signature of a wave phenomenon is interference: two waves in phase interfere constructively, and out of phase they interfere destructively. The wave nature of light was confirmed in 1801 by Young’s famous double-slit experiment, showing interference “fringes” on a distant screen when a monochromatic beam passes through two slits. If essentially the same experiment is done with electrons, the same pattern develops,<sup>10</sup> confirming the wave nature of electrons.

Now suppose we decrease the intensity of the electron beam, until only one electron is present in the apparatus at any particular time. According to the statistical interpretation each electron will produce a spot on the screen. Quantum mechanics cannot predict the precise location of that spot—all it can tell us is the probability of a given electron landing at a particular place. But if we are patient, and wait for a hundred thousand electrons—one at a time—to make the trip, the accumulating spots reveal the classic two-slit interference pattern (Figure 1.4).<sup>11</sup>

![](images/bc836861acb2b63461874237e6e3e1705378013f13dd17a947ef1677ca651f10.jpg)

![](images/dd79cd00c0daefe73156f7cd74d0ac0ecabc05df701b0cf939f5f5ca9c7fce51.jpg)

![](images/b0b17f86580ca8bb25d50c1f4440f00b9680834eade77816a993d28b88ce7b3f.jpg)  
Figure 1.4: Build-up of the electron interference pattern. (a) Eight electrons, (b) 270 electrons, (c) 2000 electrons, (d) 160,000 electrons. Reprinted courtesy of the Central Research Laboratory, Hitachi, Ltd., Japan.

![](images/d6828bd49b99d926f58a8afb383be8153da5742230454203c29810bcb8c49f6d.jpg)

<sup>10</sup> Because the wavelength of electrons is typically very small, the slits have to be extremely close together. Historically, this was first achieved by Davisson and Germer, in 1925, using the atomic layers in a crystal as “slits.” For an interesting account, see R. K. Gehrenbeck, Physics Today, January 1978, page 34.

11 See Tonomura et al., American Journal of Physics, Volume 57, Issue 2, pp. 117–120 (1989), and the amazing associated video at www.hitachi.com/rd/portal/highlight/quantum/doubleslit/. This experiment can now be done with much more massive particles, including “Bucky-balls”; see M. Arndt, et al., Nature 40, 680 (1999). Incidentally, the same thing can be done with light: turn the intensity so low that only one “photon” is present at a time and you get an identical point-by-point assembly of the interference pattern. See R. S. Aspden, M. J. Padgett, and G. C. Spalding, Am. J. Phys. 84, 671 (2016).



---
> 📄 **Página 6**
---

Of course, if you close off one slit, or somehow contrive to detect which slit each electron passes through, the interference pattern disappears; the wave function of the emerging particle is now entirely different (in the first case because the boundary conditions for the Schrödinger equation have been changed, and in the second because of the collapse of the wave function upon measurement). But with both slits open, and no interruption of the electron in flight, each electron interferes with itself; it didn’t pass through one slit or the other, but through both at once, just as a water wave, impinging on a jetty with two openings, interferes with itself. There is nothing mysterious about this, once you have accepted the notion that particles obey a wave equation. The truly astonishing thing is the blip-by-blip assembly of the pattern. In any classical wave theory the pattern would develop smoothly and continuously, simply getting more intense as time goes on. The quantum process is more like the pointillist painting of Seurat: The picture emerges from the cumulative contributions of all the individual dots.<sup>12</sup>

## 1.3 PROBABILITY

## 1.3.1 Discrete Variables

Because of the statistical interpretation, probability plays a central role in quantum mechanics, so I digress now for a brief discussion of probability theory. It is mainly a question of introducing some notation and terminology, and I shall do it in the context of a simple example.

Imagine a room containing fourteen people, whose ages are as follows:

one person aged 14,   
one person aged 15,   
three people aged 16,   
two people aged 22,   
two people aged 24,   
five people aged 25.

If we let N ( j) represent the number of people of age j, then

$$
\begin{array} { r l } & { N ( 1 4 ) = 1 , } \\ & { N ( 1 5 ) = 1 , } \\ & { N ( 1 6 ) = 3 , } \\ & { N ( 2 2 ) = 2 , } \\ & { N ( 2 4 ) = 2 , } \\ & { N ( 2 5 ) = 5 , } \end{array}
$$

<sup>12</sup> I think it is important to distinguish things like interference and diffraction that would hold for any wave theory from the uniquely quantum mechanical features of the measurement process, which derive from the statistical interpretation.



---
> 📄 **Página 7**
---

![](images/a0c7e000ffac3c80cf123f3d938cf19178f16de9335d18d730c9bad341a7c5e8.jpg)  
Figure 1.5: Histogram showing the number of people, $N ( j )$ , with age j , for the example in Section 1.3.1.

while N (17), for instance, is zero. The total number of people in the room is

$$
N = \sum _ { j = 0 } ^ { \infty } N ( j ) .\tag{1.4}
$$

(In the example, of course, $N = 1 4 . )$ Figure 1.5 is a histogram of the data. The following are some questions one might ask about this distribution.

Question 1 If you selected one individual at random from this group, what is the probability that this person’s age would be 15?

Answer One chance in 14, since there are 14 possible choices, all equally likely, of whom only one has that particular age. If $P ( j )$ is the probability of getting age j, then $P ( 1 4 ) =$ $1 / 1 4 , P ( 1 5 ) = 1 / 1 4 , P ( 1 6 ) = 3 / 1 4$ , and so on. In general,

$$
P ( j ) = \frac { N ( j ) } { N } .\tag{1.5}
$$

Notice that the probability of getting either 14 or 15 is the sum of the individual probabilities (in this case, 1/7). In particular, the sum of all the probabilities is 1—the person you select must have some age:

$$
\sum _ { j = 0 } ^ { \infty } P ( j ) = 1 .\tag{1.6}
$$

Question 2 What is the most probable age?

Answer 25, obviously; five people share this age, whereas at most three have any other age.   
The most probable j is the j for which $P ( j )$ is a maximum.

Question 3 What is the median age?

Answer 23, for 7 people are younger than 23, and 7 are older. (The median is that value of j such that the probability of getting a larger result is the same as the probability of getting a smaller result.)

Question 4 What is the average (or mean) age?

Answer

$$
{ \frac { ( 1 4 ) + ( 1 5 ) + 3 ( 1 6 ) + 2 ( 2 2 ) + 2 ( 2 4 ) + 5 ( 2 5 ) } { 1 4 } } = { \frac { 2 9 4 } { 1 4 } } = 2 1 .
$$



---
> 📄 **Página 8**
---

In general, the average value of j (which we shall write thus: $\langle j \rangle )$ is

$$
\langle j \rangle = \frac { \sum j N ( j ) } { N } = \sum _ { j = 0 } ^ { \infty } j P ( j ) .\tag{1.7}
$$

Notice that there need not be anyone with the average age or the median age—in this example nobody happens to be 21 or 23. In quantum mechanics the average is usually the quantity of interest; in that context it has come to be called the expectation value. It’s a misleading term, since it suggests that this is the outcome you would be most likely to get if you made a single measurement (that would be the most probable value, not the average value)—but I’m afraid we’re stuck with it.

Question 5 What is the average of the squares of the ages?

Answer You could get $1 4 ^ { 2 } = 1 9 6$ , with probability 1/14, or $1 5 ^ { 2 } = 2 2 5$ , with probability 1/14, or $1 6 ^ { 2 } = 2 5 6$ , with probability 3/14, and so on. The average, then, is

$$
\left. j ^ { 2 } \right. = \sum _ { j = 0 } ^ { \infty } j ^ { 2 } P ( j ) .\tag{1.8}
$$

In general, the average value of some function of j is given by

$$
\boxed { \langle f ( j ) \rangle = \sum _ { j = 0 } ^ { \infty } f ( j ) P ( j ) . }\tag{1.9}
$$

(Equations 1.6, 1.7, and 1.8 are, if you like, special cases of this formula.) Beware: The average of the squares, $\left. j ^ { 2 } \right.$ , is not equal, in general, to the square of the average, $\langle j \rangle ^ { 2 }$ . For instance, if the room contains just two babies, aged 1 and 3, then $\left. j ^ { 2 } \right. = 5$ , but $\langle j \rangle ^ { 2 } = 4 .$

Now, there is a conspicuous difference between the two histograms in Figure 1.6, even though they have the same median, the same average, the same most probable value, and the same number of elements: The first is sharply peaked about the average value, whereas the second is broad and flat. (The first might represent the age profile for students in a big-city classroom, the second, perhaps, a rural one-room schoolhouse.) We need a numerical measure of the amount of “spread” in a distribution, with respect to the average. The most obvious way to do this would be to find out how far each individual is from the average,

![](images/b983c88a77760e04667bbb153b68f3ba4b27ee9b1d61c6e724b067c33551a5a1.jpg)

![](images/ea7e970710eb5074e074fba12f4827954c66059038991cc9cfc326794acc0de2.jpg)  
Figure 1.6: Two histograms with the same median, same average, and same most probable value, but different standard deviations.

$$


---
> 📄 **Página 9**
---

\Delta j = j - \left. j \right. ,\tag{1.10}
$$

and compute the average of $\Delta j$ . Trouble is, of course, that you get zero:

$$
\begin{array} { c } { { \langle \Delta j \rangle = \displaystyle \sum ( j - \langle j \rangle ) P ( j ) = \displaystyle \sum j P ( j ) - \langle j \rangle \sum P ( j ) } } \\ { { = \langle j \rangle - \langle j \rangle = 0 . } } \end{array}
$$

(Note that $\langle j \rangle$ is constant—it does not change as you go from one member of the sample to another—so it can be taken outside the summation.) To avoid this irritating problem you might decide to average the absolute value of $\Delta j$ . But absolute values are nasty to work with; instead, we get around the sign problem by squaring before averaging:

$$
\sigma ^ { 2 } \equiv \big \langle ( \Delta j ) ^ { 2 } \big \rangle .\tag{1.11}
$$

This quantity is known as the variance of the distribution; σ itself (the square root of the average of the square of the deviation from the average—gulp!) is called the standard deviation. The latter is the customary measure of the spread about $\langle j \rangle$

There is a useful little theorem on variances:

$$
\begin{array} { l } { { \displaystyle \sigma ^ { 2 } = \left. ( \Delta j ) ^ { 2 } \right. = \sum ( \Delta j ) ^ { 2 } P ( j ) = \sum ( j - \left. j \right. ) ^ { 2 } P ( j ) } } \\ { { \displaystyle ~ = \sum \left( j ^ { 2 } - 2 j \left. j \right. + \left. j \right. ^ { 2 } \right) P ( j ) } } \\ { { \displaystyle ~ = \sum j ^ { 2 } P ( j ) - 2 \left. j \right. \sum j P ( j ) + \left. j \right. ^ { 2 } \sum P ( j ) } } \\ { { \displaystyle ~ = \left. j ^ { 2 } \right. - 2 \left. j \right. \left. j \right. + \left. j \right. ^ { 2 } = \left. j ^ { 2 } \right. - \left. j \right. ^ { 2 } . } } \end{array}
$$

Taking the square root, the standard deviation itself can be written as

$$
\sigma = { \sqrt { \left. j ^ { 2 } \right. - \left. j \right. ^ { 2 } } } .\tag{1.12}
$$

In practice, this is a much faster way to get σ than by direct application of Equation 1.11: simply calculate $\left. j ^ { 2 } \right.$ and $\langle j \rangle ^ { 2 }$ , subtract, and take the square root. Incidentally, I warned you a moment ago that $\dot { \langle j ^ { 2 } \rangle }$ is not, in general, equal to $\langle j \rangle ^ { 2 }$ . Since $\sigma ^ { 2 }$ is plainly non-negative (from its definition 1.11), Equation 1.12 implies that

$$
\left. j ^ { 2 } \right. \geq \left. j \right. ^ { 2 } ,\tag{1.13}
$$

and the two are equal only when $\sigma = 0$ , which is to say, for distributions with no spread at all (every member having the same value).

## 1.3.2 Continuous Variables

So far, I have assumed that we are dealing with a discrete variable—that is, one that can take on only certain isolated values (in the example, j had to be an integer, since I gave ages only in years). But it is simple enough to generalize to continuous distributions. If I select a random person off the street, the probability that her age is precisely 16 years, 4 hours, 27 minutes, and 3.333. . . seconds is zero. The only sensible thing to speak about is the probability that her age lies in some interval—say, between 16 and 17. If the interval is sufficiently short, this probability is proportional to the length of the interval. For example, the chance that her age is between 16 and 16 plus two days is presumably twice the probability that it is between 16 and



---
> 📄 **Página 10**
---

16 plus one day. (Unless, I suppose, there was some extraordinary baby boom 16 years ago, on exactly that day—in which case we have simply chosen an interval too long for the rule to apply. If the baby boom lasted six hours, we’ll take intervals of a second or less, to be on the safe side. Technically, we’re talking about infinitesimal intervals.) Thus

$$
{ \left\{ \begin{array} { l } { \operatorname { p r o b a b i l i t y } \operatorname { t h a t } \operatorname { a n } \operatorname { i n d i v i d u a l } \ ( \operatorname { c h o s e n } } \\ { \operatorname { a t } \operatorname { r a n d o m } ) \operatorname { l i e s } \operatorname { b e t w e e n } x \operatorname { a n d } ( x + d x ) } \end{array} \right\} } = \rho ( x ) d x .\tag{1.14}
$$

The proportionality factor, $\rho ( x )$ , is often loosely called “the probability of getting x,” but this is sloppy language; a better term is probability density. The probability that x lies between a and b (a finite interval) is given by the integral of $\rho ( x )$

$$
P _ { a b } = \int _ { a } ^ { b } \rho ( x ) d x ,\tag{1.15}
$$

and the rules we deduced for discrete distributions translate in the obvious way:

$$
\int _ { - \infty } ^ { + \infty } \rho ( x ) d x = 1 ,\tag{1.16}
$$

$$
\langle x \rangle = \int _ { - \infty } ^ { + \infty } x \rho ( x ) d x ,\tag{1.17}
$$

$$
\langle f ( x ) \rangle = \int _ { - \infty } ^ { + \infty } f ( x ) \rho ( x ) d x ,\tag{1.18}
$$

$$
\sigma ^ { 2 } \equiv \left. ( \Delta x ) ^ { 2 } \right. = \left. x ^ { 2 } \right. - \left. x \right. ^ { 2 } .\tag{1.19}
$$

## Example 1.2

Suppose someone drops a rock off a cliff of height h. As it falls, I snap a million photographs, at random intervals. On each picture I measure the distance the rock has fallen. Question: What is the average of all these distances? That is to say, what is the time average of the distance traveled?<sup>13</sup>

Solution: The rock starts out at rest, and picks up speed as it falls; it spends more time near the top, so the average distance will surely be less than $h / 2$ . Ignoring air resistance, the distance x at time t is

$$
x ( t ) = \frac { 1 } { 2 } g t ^ { 2 } .
$$

The velocity is $d x / d t = g t$ , and the total flight time is $T = { \sqrt { 2 h / g } }$ . The probability that a particular photograph was taken between t and $t + d t$ is $d t / T$ , so the probability that it shows a distance in the corresponding range x to $x + d x$ is

$$
\frac { d t } { T } = \frac { d x } { g t } \sqrt { \frac { g } { 2 h } } = \frac { 1 } { 2 \sqrt { h x } } d x .
$$

13 A statistician will complain that I am confusing the average of a finite sample (a million, in this case) with the “true” average (over the whole continuum). This can be an awkward problem for the experimentalist, especially when the sample size is small, but here I am only concerned with the true average, to which the sample average is presumably a good approximation.



---
> 📄 **Página 11**
---

Thus the probability density (Equation 1.14) is

$$
\rho ( x ) = \frac { 1 } { 2 \sqrt { h x } } , \quad ( 0 \leq x \leq h )
$$

(outside this range, of course, the probability density is zero).

We can check this result, using Equation 1.16:

$$
\int _ { 0 } ^ { h } { \frac { 1 } { 2 { \sqrt { h x } } } } d x = { \frac { 1 } { 2 { \sqrt { h } } } } \left( 2 x ^ { 1 / 2 } \right) { \Biggl | } _ { 0 } ^ { h } = 1 .
$$

The average distance (Equation 1.17) is

$$
\left. x \right. = \int _ { 0 } ^ { h } x \frac 1 { 2 \sqrt { h x } } d x = \frac 1 { 2 \sqrt { h } } \left( \frac 2 3 x ^ { 3 / 2 } \right) \bigg | _ { 0 } ^ { h } = \frac h 3 ,
$$

which is somewhat less than $h / 2 ,$ , as anticipated.

Figure 1.7 shows the graph of $\rho ( x )$ . Notice that a probability density can be infinite, though probability itself (the integral of $\rho )$ must of course be finite (indeed, less than or equal to 1).

![](images/d8c587d6cc828cadf55537605b471708a0025ab4f57f4d93f306c8d0e29d91f5.jpg)  
Figure 1.7: The probability density in Example 1.2: $\rho ( x ) = 1 { \Big / } \left( 2 { \sqrt { h x } } \right)$

Problem 1.1 For the distribution of ages in the example in Section 1.3.1:

∗

(a) Compute $\left. j ^ { 2 } \right.$ and $\langle j \rangle ^ { 2 }$

(b) Determine $\Delta j$ for each $j .$ , and use Equation 1.11 to compute the standard deviation.

(c) Use your results in (a) and (b) to check Equation 1.12.

## Problem 1.2

(a) Find the standard deviation of the distribution in Example 1.2.

(b) What is the probability that a photograph, selected at random, would show a distance x more than one standard deviation away from the average?

Problem 1.3 Consider the gaussian distribution   
ρ(x) = Ae<sup>−λ(x−a)2</sup> ,   
where A, a, and λ are positive real constants. (The necessary integrals are inside the   
back cover.)   
(a) Use Equation 1.16 to determine A.   
(b) Find $\langle { \bar { x } } \rangle , \left. x ^ { 2 } \right. .$ , and $\sigma .$   
(c) Sketch the graph of $\rho ( x )$



---
> 📄 **Página 12**
---

## 1.4 NORMALIZATION

We return now to the statistical interpretation of the wave function (Equation 1.3), which says that $| \Psi ( x , t ) | ^ { 2 }$ is the probability density for finding the particle at point x, at time t. It follows (Equation 1.16) that the integral of $| \Psi | ^ { 2 }$ over all x must be 1 (the particle’s got to be somewhere):

$$
\boxed { \int _ { - \infty } ^ { + \infty } | \Psi ( x , t ) | ^ { 2 } d x = 1 . }\tag{1.20}
$$

Without this, the statistical interpretation would be nonsense.

However, this requirement should disturb you: After all, the wave function is supposed to be determined by the Schrödinger equation—we can’t go imposing an extraneous condition on  without checking that the two are consistent. Well, a glance at Equation 1.1 reveals that if $\Psi ( x , t )$ is a solution, so too is $A \Psi ( x , t )$ , where A is any (complex) constant. What we must do, then, is pick this undetermined multiplicative factor so as to ensure that Equation 1.20 is satisfied. This process is called normalizing the wave function. For some solutions to the Schrödinger equation the integral is infinite; in that case no multiplicative factor is going to make it 1. The same goes for the trivial solution $\Psi = 0$ . Such non-normalizable solutions cannot represent particles, and must be rejected. Physically realizable states correspond to the square-integrable solutions to Schrödinger’s equation.<sup>14</sup>

But wait a minute! Suppose I have normalized the wave function at time $t ~ = ~ 0$ . How do I know that it will stay normalized, as time goes on, and  evolves? (You can’t keep renormalizing the wave function, for then A becomes a function of $t ,$ and you no longer have a solution to the Schrödinger equation.) Fortunately, the Schrödinger equation has the remarkable property that it automatically preserves the normalization of the wave function— without this crucial feature the Schrödinger equation would be incompatible with the statistical interpretation, and the whole theory would crumble.

This is important, so we’d better pause for a careful proof. To begin with,

$$
{ \frac { d } { d t } } \int _ { - \infty } ^ { + \infty } \left| \Psi ( x , t ) \right| ^ { 2 } d x = \int _ { - \infty } ^ { + \infty } { \frac { \partial } { \partial t } } \left| \Psi ( x , t ) \right| ^ { 2 } d x .\tag{1.21}
$$

14 Evidently $\Psi ( x , t )$ must go to zero faster than $1 / { \sqrt { | x | } } ,$ , as $| x |  \infty$ . Incidentally, normalization only fixes the modulus of A; the phase remains undetermined. However, as we shall see, the latter carries no physical significance anyway.



---
> 📄 **Página 13**
---

(Note that the integral is a function only of t, so I use a total derivative $( d / d t )$ on the left, but the integrand is a function of x as well as $t ,$ so it’s a partial derivative $( \partial / \partial t )$ on the right.) By the product rule,

$$
{ \frac { \partial } { \partial t } } \left| \Psi \right| ^ { 2 } = { \frac { \partial } { \partial t } } \left( \Psi ^ { * } \Psi \right) = \Psi ^ { * } { \frac { \partial \Psi } { \partial t } } + { \frac { \partial \Psi ^ { * } } { \partial t } } \Psi .\tag{1.22}
$$

Now the Schrödinger equation says that

$$
{ \frac { \partial \Psi } { \partial t } } = { \frac { i \hbar } { 2 m } } { \frac { \partial ^ { 2 } \Psi } { \partial x ^ { 2 } } } - { \frac { i } { \hbar } } V \Psi ,\tag{1.23}
$$

and hence also (taking the complex conjugate of Equation 1.23)

$$
\frac { \partial \Psi ^ { * } } { \partial t } = - \frac { i \hbar } { 2 m } \frac { \partial ^ { 2 } \Psi ^ { * } } { \partial x ^ { 2 } } + \frac { i } { \hbar } V \Psi ^ { * } ,\tag{1.24}
$$

so

$$
\frac { \partial } { \partial t } \left| \Psi \right| ^ { 2 } = \frac { i \hbar } { 2 m } \left( \Psi ^ { * } \frac { \partial ^ { 2 } \Psi } { \partial x ^ { 2 } } - \frac { \partial ^ { 2 } \Psi ^ { * } } { \partial x ^ { 2 } } \Psi \right) = \frac { \partial } { \partial x } \left[ \frac { i \hbar } { 2 m } \left( \Psi ^ { * } \frac { \partial \Psi } { \partial x } - \frac { \partial \Psi ^ { * } } { \partial x } \Psi \right) \right] .\tag{1.25}
$$

The integral in Equation 1.21 can now be evaluated explicitly:

$$
\frac { d } { d t } \int _ { - \infty } ^ { + \infty } | \Psi ( x , t ) | ^ { 2 } \ d x = \frac { i \hbar } { 2 m } \left. \left( \Psi ^ { * } \frac { \partial \Psi } { \partial x } - \frac { \partial \Psi ^ { * } } { \partial x } \Psi \right) \right| _ { - \infty } ^ { + \infty } .\tag{1.26}
$$

But $\Psi ( x , t )$ must go to zero as x goes to (±) infinity—otherwise the wave function would not be normalizable.<sup>15</sup> It follows that

$$
\frac { d } { d t } \int _ { - \infty } ^ { + \infty } | \Psi ( x , t ) | ^ { 2 } ~ d x = 0 ,\tag{1.27}
$$

and hence that the integral is constant (independent of time); if $\Psi$ is normalized at $t = 0 ,$ , it stays normalized for all future time. QED

Problem 1.4 At time $t = 0$ a particle is represented by the wave function

$$
\Psi ( x , 0 ) = \left\{ \begin{array} { l l } { A ( x / a ) , } & { 0 \leq x \leq a , } \\ { A ( b - x ) / ( b - a ) , } & { a \leq x \leq b , } \\ { 0 , } & { \mathrm { o t h e r w i s e } , } \end{array} \right.
$$

where $A , a ,$ and b are (positive) constants.

(a) Normalize  (that is, find A, in terms of a and $^ { b ) }$

(b) Sketch $\Psi ( x , 0 )$ , as a function of x.

(c) Where is the particle most likely to be found, at $t = 0 ?$

(d) What is the probability of finding the particle to the left of $a \mathrm { ? }$ Check your result in the limiting cases $b = a$ and $b = 2 a$

(e) What is the expectation value of $x ?$

<sup>15</sup> A competent mathematician can supply you with pathological counterexamples, but they do not arise in physics; for us the wave function and all its derivatives go to zero at infinity.



---
> 📄 **Página 14**
---

## Problem 1.5 Consider the wave function

∗

$$
\Psi ( x , t ) = A e ^ { - \lambda \left| x \right| } e ^ { - i \omega t } ,
$$

where A, λ, and ω are positive real constants. (We’ll see in Chapter 2 for what potential (V ) this wave function satisfies the Schrödinger equation.)

(a) Normalize .

(b) Determine the expectation values of x and $x ^ { 2 } .$

(c) Find the standard deviation of x. Sketch the graph of $| \Psi | ^ { 2 }$ , as a function of x, and mark the points $( \langle x \rangle + \sigma )$ and $( \langle x \rangle - \sigma )$ , to illustrate the sense in which σ represents the “spread” in x. What is the probability that the particle would be found outside this range?

## 1.5 MOMENTUM

For a particle in state , the expectation value of x is

$$
\langle x \rangle = \int _ { - \infty } ^ { + \infty } x | \Psi ( x , t ) | ^ { 2 } d x .\tag{1.28}
$$

What exactly does this mean? It emphatically does not mean that if you measure the position of one particle over and over again, $\textstyle \int x | \Psi | ^ { 2 } d x$ is the average of the results you’ll get. On the contrary: The first measurement (whose outcome is indeterminate) will collapse the wave function to a spike at the value actually obtained, and the subsequent measurements (if they’re performed quickly) will simply repeat that same result. Rather, x is the average of measurements performed on particles all in the state , which means that either you must find some way of returning the particle to its original state after each measurement, or else you have to prepare a whole ensemble of particles, each in the same state $\Psi ,$ , and measure the positions of all of them: $\langle x \rangle$ is the average of these results. I like to picture a row of bottles on a shelf, each containing a particle in the state  (relative to the center of the bottle). A graduate student with a ruler is assigned to each bottle, and at a signal they all measure the positions of their respective particles. We then construct a histogram of the results, which should match $| \Psi | ^ { 2 }$ and compute the average, which should agree with x. (Of course, since we’re only using a finite sample, we can’t expect perfect agreement, but the more bottles we use, the closer we ought to come.) In short, the expectation value is the average of measurements on an ensemble of identically-prepared systems, not the average of repeated measurements on one and the same system.

Now, as time goes on, x will change (because of the time dependence of ), and we might be interested in knowing how fast it moves. Referring to Equations 1.25 and 1.28, we see that<sup>16</sup>

$$
\frac { d \langle x \rangle } { d t } = \int x \frac { \partial } { \partial t } \left| \Psi \right| ^ { 2 } d x = \frac { i \hbar } { 2 m } \int x \frac { \partial } { \partial x } \left( \Psi ^ { * } \frac { \partial \Psi } { \partial x } - \frac { \partial \Psi ^ { * } } { \partial x } \Psi \right) d x .\tag{1.29}
$$

<sup>16</sup> To keep things from getting too cluttered, I’ll suppress the limits of integration (±∞).



---
> 📄 **Página 15**
---

This expression can be simplified using integration-by-parts:<sup>17</sup>

$$
\frac { d \langle x \rangle } { d t } = - \frac { i \hbar } { 2 m } \int \left( \Psi ^ { * } \frac { \partial \Psi } { \partial x } - \frac { \partial \Psi ^ { * } } { \partial x } \Psi \right) d x .\tag{1.30}
$$

(I used the fact that $\partial x / \partial x = 1$ , and threw away the boundary term, on the ground that  goes to zero at (±) infinity.) Performing another integration-by-parts, on the second term, we conclude:

$$
\frac { d \langle x \rangle } { d t } = - \frac { i \hbar } { m } \int \Psi ^ { * } \frac { \partial \Psi } { \partial x } d x .\tag{1.31}
$$

What are we to make of this result? Note that we’re talking about the “velocity” of the expectation value of x, which is not the same thing as the velocity of the particle. Nothing we have seen so far would enable us to calculate the velocity of a particle. It’s not even clear what velocity means in quantum mechanics: If the particle doesn’t have a determinate position (prior to measurement), neither does it have a well-defined velocity. All we could reasonably ask for is the probability of getting a particular value. We’ll see in Chapter 3 how to construct the probability density for velocity, given ; for the moment it will suffice to postulate that the expectation value of the velocity is equal to the time derivative of the expectation value of position:

$$
\langle v \rangle = { \frac { d \langle x \rangle } { d t } } .\tag{1.32}
$$

Equation 1.31 tells us, then, how to calculate v directly from .

Actually, it is customary to work with momentum $( p = m v )$ , rather than velocity:

$$
\begin{array}{c} \langle p \rangle = m { \frac { d \langle x \rangle } { d t } } = - i \hbar \int \left( \Psi ^ { * } { \frac { \partial \Psi } { \partial x } } \right) d x .  \end{array}\tag{1.33}
$$

Let me write the expressions for x and $\langle p \rangle$ in a more suggestive way:

$$
\langle x \rangle = \int \Psi ^ { * } \left[ x \right] \Psi d x ,\tag{1.34}
$$

$$
\left. p \right. = \int \Psi ^ { * } \left[ - i \hbar \left( \partial / \partial x \right) \right] \Psi d x .\tag{1.35}
$$

We say that the operator<sup>18</sup> x “represents” position, and the operator $- i \hbar ( \partial / \partial x )$ “represents” momentum; to calculate expectation values we “sandwich” the appropriate operator between $\Psi ^ { * }$ and , and integrate.

<sup>17</sup> The product rule says that

$$
{ \frac { d } { d x } } ( f g ) = f { \frac { d g } { d x } } + { \frac { d f } { d x } } g ,
$$

from which it follows that

$$
\int _ { a } ^ { b } f { \frac { d g } { d x } } d x = - \int _ { a } ^ { b } { \frac { d f } { d x } } g d x + f g \left| _ { a } ^ { b } \right. .
$$

Under the integral sign, then, you can peel a derivative off one factor in a product, and slap it onto the other one—it’ll cost you a minus sign, and you’ll pick up a boundary term.

<sup>18</sup> An “operator” is an instruction to do something to the function that follows; it takes in one function, and spits out some other function. The position operator tells you to multiply by x; the momentum operator tells you to differentiate with respect to x (and multiply the result by −i<sup>-</sup>).



---
> 📄 **Página 16**
---

That’s cute, but what about other quantities? The fact is, all classical dynamical variables can be expressed in terms of position and momentum. Kinetic energy, for example, is

$$
T = { \frac { 1 } { 2 } } m v ^ { 2 } = { \frac { p ^ { 2 } } { 2 m } } ,
$$

and angular momentum is

$$
\mathbf { L } = \mathbf { r } \times m \mathbf { v } = \mathbf { r } \times \mathbf { p }
$$

(the latter, of course, does not occur for motion in one dimension). To calculate the expectation value of $a n y$ such quantity, $Q ( x , p )$ , we simply replace every $p$ by $- i \hbar ( \partial / \partial x )$ , insert the resulting operator between $\Psi ^ { * }$ and , and integrate:

$$
\left. Q ( x , p ) \right. = \int \Psi ^ { * } \left[ Q ( x , - i \hbar \partial / \partial x ) \right] \Psi d x .\tag{1.36}
$$

For example, the expectation value of the kinetic energy is

$$
\langle T \rangle = - { \frac { \hbar ^ { 2 } } { 2 m } } \int \Psi ^ { * } { \frac { \partial ^ { 2 } \Psi } { \partial x ^ { 2 } } } d x .\tag{1.37}
$$

Equation 1.36 is a recipe for computing the expectation value of any dynamical quantity, for a particle in state $\Psi ;$ it subsumes Equations 1.34 and 1.35 as special cases. I have tried to make Equation 1.36 seem plausible, given Born’s statistical interpretation, but in truth this represents such a radically new way of doing business (as compared with classical mechanics) that it’s a good idea to get some practice using it before we come back (in Chapter 3) and put it on a firmer theoretical foundation. In the mean time, if you prefer to think of it as an axiom, that’s fine with me.

Problem 1.6 Why can’t you do integration-by-parts directly on the middle expression in Equation 1.29—pull the time derivative over onto x, note that $\partial x / \partial t = 0$ and conclude that ${ d \langle x \rangle } / { d t } = 0 ?$

Problem 1.7 Calculate $d \langle p \rangle / d t$ . Answer:

∗

$$
\frac { d \langle p \rangle } { d t } = \left. - \frac { \partial V } { \partial x } \right. .\tag{1.38}
$$

This is an instance of Ehrenfest’s theorem, which asserts that expectation values obey the classical laws.<sup>19</sup>

Problem 1.8 Suppose you add a constant $V _ { 0 }$ to the potential energy (by “constant” I mean independent of x as well as $t )$ . In classical mechanics this doesn’t change anything, but what about quantum mechanics? Show that the wave function picks up a time-dependent phase factor: exp $( - i V _ { 0 } t / \hbar )$ . What effect does this have on the expectation value of a dynamical variable?

<sup>19</sup> Some authors limit the term to the pair of equations $\langle p \rangle = m d \langle x \rangle / d t$ and $\langle - \partial V / \partial x \rangle = d \langle p \rangle / d t$



---
> 📄 **Página 17**
---

![](images/885c39f593e286404a26a93d172c97366e6cc42e8dbe5325133b7d2b6a8aa646.jpg)  
Figure 1.8: A wave with a (fairly) well-defined wavelength, but an ill-defined position.

![](images/bc8b21329980a33bf98b65a68fcdd95dad5fda41376610203a313a9118c00fc1.jpg)  
Figure 1.9: A wave with a (fairly) well-defined position, but an ill-defined wavelength.

## 1.6 THE UNCERTAINTY PRINCIPLE

Imagine that you’re holding one end of a very long rope, and you generate a wave by shaking it up and down rhythmically (Figure 1.8). If someone asked you “Precisely where is that wave?” you’d probably think he was a little bit nutty: The wave isn’t precisely anywhere—it’s spread out over 50 feet or so. On the other hand, if he asked you what its wavelength is, you could give him a reasonable answer: it looks like about 6 feet. By contrast, if you gave the rope a sudden jerk (Figure 1.9), you’d get a relatively narrow bump traveling down the line. This time the first question (Where precisely is the wave?) is a sensible one, and the second (What is its wavelength?) seems nutty—it isn’t even vaguely periodic, so how can you assign a wavelength to it? Of course, you can draw intermediate cases, in which the wave is fairly well localized and the wavelength is fairly well defined, but there is an inescapable trade-off here: the more precise a wave’s position is, the less precise is its wavelength, and vice versa.<sup>20</sup> A theorem in Fourier analysis makes all this rigorous, but for the moment I am only concerned with the qualitative argument.

This applies, of course, to any wave phenomenon, and hence in particular to the quantum mechanical wave function. But the wavelength of  is related to the momentum of the particle by the de Broglie formula:<sup>21</sup>

$$
p = { \frac { h } { \lambda } } = { \frac { 2 \pi \hbar } { \lambda } } .\tag{1.39}
$$

Thus a spread in wavelength corresponds to a spread in momentum, and our general observation now says that the more precisely determined a particle’s position is, the less precisely is its momentum. Quantitatively,

$$
\boxed { \sigma _ { x } \sigma _ { p } \geq \frac { \hbar } { 2 } , }\tag{1.40}
$$

<sup>20</sup> That’s why a piccolo player must be right on pitch, whereas a double-bass player can afford to wear garden gloves. For the piccolo, a sixty-fourth note contains many full cycles, and the frequency (we’re working in the time domain now, instead of space) is well defined, whereas for the bass, at a much lower register, the sixty-fourth note contains only a few cycles, and all you hear is a general sort of “oomph,” with no very clear pitch.

<sup>21</sup> I’ll explain this in due course. Many authors take the de Broglie formula as an axiom, from which they then deduce the association of momentum with the operator $- i \hbar ( \partial / \partial x )$ . Although this is a conceptually cleaner approach, it involves diverting mathematical complications that I would rather save for later.



---
> 📄 **Página 18**
---

where $\sigma _ { x }$ is the standard deviation in x, and $\sigma _ { p }$ is the standard deviation in $p .$ . This is Heisenberg’s famous uncertainty principle. (We’ll prove it in Chapter 3, but I wanted to mention it right away, so you can test it out on the examples in Chapter 2.)

Please understand what the uncertainty principle means: Like position measurements, momentum measurements yield precise answers—the “spread” here refers to the fact that measurements made on identically prepared systems do not yield identical results. You can, if you want, construct a state such that position measurements will be very close together (by making  a localized “spike”), but you will pay a price: Momentum measurements on this state will be widely scattered. Or you can prepare a state with a definite momentum (by making  a long sinusoidal wave), but in that case position measurements will be widely scattered. And, of course, if you’re in a really bad mood you can create a state for which neither position nor momentum is well defined: Equation 1.40 is an inequality, and there’s no limit on how big $\sigma _ { x }$ and $\sigma _ { p }$ can be—just make  some long wiggly line with lots of bumps and potholes and no periodic structure.

## Problem 1.9 A particle of mass m has the wave function

∗

$$
\Psi ( x , t ) = A e ^ { - a \left[ \left( m x ^ { 2 } / \hbar \right) + i t \right] } ,
$$

where A and a are positive real constants.

(a) Find A.

(b) For what potential energy function, $V ( x )$ , is this a solution to the Schrödinger equation?

(c) Calculate the expectation values of $x , x ^ { 2 } , p ,$ and $p ^ { 2 }$

(d) Find $\sigma _ { x }$ and $\sigma _ { p } .$ . Is their product consistent with the uncertainty principle?

## FURTHER PROBLEMS ON CHAPTER 1

Problem 1.10 Consider the first 25 digits in the decimal expansion of π (3, 1, 4, 1, 5, 9, . . .).

(a) If you selected one number at random, from this set, what are the probabilities of getting each of the 10 digits?

(b) What is the most probable digit? What is the median digit? What is the average value?

(c) Find the standard deviation for this distribution.

Problem 1.11 [This problem generalizes Example 1.2.] Imagine a particle of mass m and energy E in a potential well V (x), sliding frictionlessly back and forth between the classical turning points (a and b in Figure 1.10). Classically, the probability of finding the particle in the range dx (if, for example, you took a snapshot at a random time t) is equal to the fraction of the time T it takes to get from a to b that it spends in the interval dx:

$$
\rho ( x ) d x = { \frac { d t } { T } } = { \frac { ( d t / d x ) d x } { T } } = { \frac { 1 } { v ( x ) T } } d x ,\tag{1.41}
$$



---
> 📄 **Página 19**
---

![](images/21596a3f0786c25efefaf8d8359245159eed4cd70ec4d41e6ecd2fd3ab89dbe4.jpg)  
Figure 1.10: Classical particle in a potential well.

where v(x) is the speed, and

$$
T = \int _ { 0 } ^ { T } d t = \int _ { a } ^ { b } { \frac { 1 } { v ( x ) } } d x .\tag{1.42}
$$

Thus

$$
\rho ( x ) = \frac { 1 } { v ( x ) T } .\tag{1.43}
$$

This is perhaps the closest classical anal $\log ^ { 2 2 }$ to $| \Psi | ^ { 2 }$

(a) Use conservation of energy to express $v ( x )$ in terms of E and $V ( x )$

(b) As an example, find $\rho ( x )$ for the simple harmonic oscillator, $V ( x ) = k x ^ { 2 } / 2$ . Plot $\rho ( x )$ , and check that it is correctly normalized.

(c) For the classical harmonic oscillator in part (b), find $\langle x \rangle , \left. x ^ { 2 } \right.$ , and $\sigma _ { x }$

Problem 1.12 What if we were interested in the distribution of momenta $( p = m v )$ , for the classical harmonic oscillator (Problem 1.11(b)).

∗∗

(a) Find the classical probability distribution $\rho ( p )$ (note that p ranges from $- { \sqrt { 2 m E } }$ $\scriptstyle { \mathrm { t o } + { \sqrt { 2 m E } } }$

(b) Calculate $\langle p \rangle , \left. p ^ { 2 } \right.$ , and $\sigma _ { p }$

(c) What’s the classical uncertainty product, $\sigma _ { x } \sigma _ { p } .$ , for this system? Notice that this product can be as small as you like, classically, simply by sending $E  0 .$ But in quantum mechanics, as we shall see in Chapter 2, the energy of a simple harmonic oscillator cannot be less than $\hbar \omega / 2 ,$ , where $\omega = \sqrt { k / m }$ is the classical frequency. In that case what can you say about the product $\sigma _ { x } \sigma _ { p } ?$

![](images/4ff1398e186146ac6c1d3736309c37abaddb8abcf4e1f074ef7fb97017b89778.jpg)

Problem 1.13 Check your results in Problem 1.11(b) with the following “numerical experiment.” The position of the oscillator at time t is

$$
x ( t ) = A \cos ( \omega t ) .\tag{1.44}
$$

<sup>22</sup> If you like, instead of photos of one system at random times, picture an ensemble of such systems, all with the same energy but with random starting positions, and photograph them all at the same time. The analysis is identical, but this interpretation is closer to the quantum notion of indeterminacy.



---
> 📄 **Página 20**
---

You might as well take $\omega = 1$ (that sets the scale for time) and $A = 1$ (that sets the scale for length). Make a plot of x at 10,000 random times, and compare it with $\rho ( x )$ Hint: In Mathematica, first define

$x[t\_] := Cos[t]$

then construct a table of positions:

snapshots = $Table[x[πRandomReal[j]], {j, 10000}]$

and finally, make a histogram of the data:

Histogram[snapshots, 100, PDF , PlotRange → {0,2}]

Meanwhile, make a plot of the density function, $\rho ( x )$ , and, using Show, superimpose the two.

Problem 1.14 Let $P _ { a b } ( t )$ be the probability of finding the particle in the range $( a < x <$ b), at time t .

(a) Show that

$$
\frac { d P _ { a b } } { d t } = J ( a , t ) - J ( b , t ) ,
$$

where

$$
J ( x , t ) \equiv \frac { i \hbar } { 2 m } \left( \Psi \frac { \partial \Psi ^ { * } } { \partial x } - \Psi ^ { * } \frac { \partial \Psi } { \partial x } \right) .
$$

What are the units of $J ( x , t ) ?$ Comment: J is called the probability current, because it tells you the rate at which probability is “flowing” past the point x. If $P _ { a b } ( t )$ is increasing, then more probability is flowing into the region at one end than flows out at the other.

(b) Find the probability current for the wave function in Problem 1.9. (This is not a very pithy example, I’m afraid; we’ll encounter more substantial ones in due course.)

Problem 1.15 Show that

$$
\frac { d } { d t } \int _ { - \infty } ^ { \infty } \Psi _ { 1 } ^ { * } \Psi _ { 2 } d x = 0
$$

for any two (normalizable) solutions to the Schrödinger equation (with the same V (x)), $\Psi _ { 1 }$ and $\Psi _ { 2 }$

Problem 1.16 A particle is represented (at time $t = 0 )$ by the wave function

$$
\Psi ( x , 0 ) = \left\{ { \begin{array} { l l } { A \left( a ^ { 2 } - x ^ { 2 } \right) , } & { - a \leq x \leq + a , } \\ { 0 , } & { { \mathrm { o t h e r w i s e } } . } \end{array} } \right.
$$

(a) Determine the normalization constant A.

(b) What is the expectation value of $x ?$

(c) What is the expectation value of $p \mathrm { ? }$ (Note that you cannot get it from $\langle p \rangle =$ md $\left. { x } \right. / d t$ . Why not?)



---
> 📄 **Página 21**
---

(d) Find the expectation value of $x ^ { 2 } .$

(e) Find the expectation value of $p ^ { 2 }$

(f) Find the uncertainty in x $( \sigma _ { x } )$ .

(g) Find the uncertainty in $p \left( \sigma _ { p } \right)$ .

(h) Check that your results are consistent with the uncertainty principle.

Problem 1.17 Suppose you wanted to describe an unstable particle, that spontaneously disintegrates with a “lifetime” τ . In that case the total probability of finding the particle somewhere should not be constant, but should decrease at (say) an exponential rate:

∗∗

$$
P ( t ) \equiv \int _ { - \infty } ^ { + \infty } | \Psi ( x , t ) | ^ { 2 } ~ d x = e ^ { - t / \tau } .
$$

A crude way of achieving this result is as follows. In Equation 1.24 we tacitly assumed that V (the potential energy) is real. That is certainly reasonable, but it leads to the “conservation of probability” enshrined in Equation 1.27. What if we assign to V an imaginary part:

$$
V = V _ { 0 } - i \Gamma ,
$$

where $V _ { 0 }$ is the true potential energy and 
 is a positive real constant?

(a) Show that (in place of Equation 1.27) we now get

$$
\frac { d P } { d t } = - \frac { 2 \Gamma } { \hbar } P .
$$

(b) Solve for $P ( t )$ , and find the lifetime of the particle in terms of 
.

Problem 1.18 Very roughly speaking, quantum mechanics is relevant when the de Broglie wavelength of the particle in question $( h / p )$ is greater than the characteristic size of the system (d). In thermal equilibrium at (Kelvin) temperature T , the average kinetic energy of a particle is

$$
\displaystyle { \frac { p ^ { 2 } } { 2 m } = \frac { 3 } { 2 } k _ { B } T }
$$

(where $k _ { B }$ is Boltzmann’s constant), so the typical de Broglie wavelength is

$$
\lambda = \frac { h } { \sqrt { 3 m k _ { B } T } } .\tag{1.45}
$$

The purpose of this problem is to determine which systems will have to be treated quantum mechanically, and which can safely be described classically.

(a) Solids. The lattice spacing in a typical solid is around d = 0.3 nm. Find the temperature below which the unbound<sup>23</sup> electrons in a solid are quantum mechanical. Below what temperature are the nuclei in a solid quantum mechanical? (Use silicon as an example.)

23 In a solid the inner electrons are attached to a particular nucleus, and for them the relevant size would be the radius of the atom. But the outer-most electrons are not attached, and for them the relevant distance is the lattice spacing. This problem pertains to the outer electrons.



---
> 📄 **Página 22**
---

Moral: The free electrons in a solid are always quantum mechanical; the nuclei are generally not quantum mechanical. The same goes for liquids (for which the interatomic spacing is roughly the same), with the exception of helium below 4 K.

(b) Gases. For what temperatures are the atoms in an ideal gas at pressure P quantum mechanical? Hint: Use the ideal gas law $( P V = N k _ { B } T )$ to deduce the interatomic spacing.

Answer: $T < ( 1 / k _ { B } ) \left( h ^ { 2 } / 3 m \right) ^ { 3 / 5 } P ^ { 2 / 5 }$ . Obviously (for the gas to show quantum behavior) we want m to be as small as possible, and P as large as possible. Put in the numbers for helium at atmospheric pressure. Is hydrogen in outer space (where the interatomic spacing is about 1 cm and the temperature is 3 K) quantum mechanical? (Assume it’s monatomic hydrogen, not $\mathrm { H } _ { 2 } . )$