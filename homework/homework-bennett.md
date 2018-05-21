---
title: "Information Security 2 Homework"
author: [Bennett Piater]
date: 2018-05-23
titlepage: false
toc: false
---

# 1) SPA of RSA Using CRT

# 2) No Covert Channel?

## a) Can you still think of a covert channel?
The number/frequency of failing computers, and thus of replacement purchases, could be used to extract information over long times.

E.g. a bit could be transmitted by breaking/buying two/three computers at once for a 0 or 1.

## b) What is the capacity of this channel?
$\frac{1b}{25}$ years to not attract attention (due to the average failing rate).

# 3) PINs, Pollen, Probability (Part II)

## a) How many trials without prior knowledge?

We know 4 keys, the missing one is 1 out of 6.
Therefore, I think the average number of trials is

$$\frac{5! \times 6}{2} = \frac{6!}{2} = 360$$ tries on average.

## b) What can be achieved using pollen?

I think I would still wipe all keys except one [TODO calculate other options].

This leaves us with some cases:

- First key is pollenated. This also reveals the unknown key! Still need all others in order, so
  $4!$ combinations $\frac{1}{5}$ of the time.
- Second or Fourth key is pollenated. We know that all pollenated keys are after, and all clean ones before the one we didn't wipe.
  + If a not worn out key is pollenated, we learned the unknown key. $3!$ combinations $\frac{2}{5 \times 2}$ of the time
  + If all worn out keys are pollenated, we still need the unkown key. $3! \times 6$ combinations $\frac{2}{5 \times 2}$ of the time.
- Middle key is pollenated.
  + If the unkown key is in the second half, and thus revealed:
    $2! \times 2!$ combinations left $\frac{1}{5\times 2}$ of the time
  + If the unkown key is not revealed: $2! \times 2! \times 6$ combinations left $\frac{1}{5 \times 2}$ of the time
- Last key is pollenated. Like first case except we didn't learn the unknown key.
  $4! \times 6$ combinations $\frac{1}{5}$ of the time.

The expected number of combinations is therefore $\frac{1}{5} \times 4! + \frac{2}{10} \times 3! + \frac{2}{10} \times 3! \times 6 + \frac{1}{10} \times 4 + \frac{1}{10} \times 24 + \frac{1}{5} \times 4! \times 6 = 2176$, which we can expect to crack in $1088$ attempts.

TODO: this number is so large - one of my calculations is wrong!

## c) What to do if only 3 keys are worn off?

In this case it would be better to polinate all warn off keys to maximize the odds of revealing the unknown keys, because trying to find those out of $6 \times 5$ combinations is much harder than just $6$.

# 4) Game Theory

Utility functions:

\begin{equation*}
\begin{aligned}
u1(ag,ag) &= 0 \\
u1(ag,mc) &= 0.2 \times 0.25 \times -7 \\
u1(mc,ag) &= 1.5 + 0.2 \times -7 \\
u1(mc,mc) &= 1.5 + 0.2 \times -7 + 0.2 \times 0.25 \times -7\\
u2(ag,ag) &= 0 \\
u2(ag,mc) &= 1.5 + 0.2 \times -7 \\
u2(mc,ag) &= 0.2 \times 0.25 \times -7 \\
u2(mc,mc) &= 1.5 + 0.2 \times -7 + 0.2 \times 0.25 \times -7\\
\end{aligned}
\end{equation*}

Matrix form:

\begin{center}
  \begin{tabular}{l | c c}
  & 2 air-gapped & 2 minecraft \\
  \hline
  1 air-gapped & $(0,0)$ & $(-0.35,0.1)$ \\
  1 minecraft & $(0.1,-0.35)$ & $(-0.25,-0.25)$
  \end{tabular}
\end{center}

Nash Equilibria:

\paragraph{Social Optima}
The social optimum is for both admins to air-gap their system.

Which game applies?
The prisoners dilemma: Social optimum if both air-gap, but (slight) advantage if one is the only one to play minecraft.

I would definitely not apply for this job.

