---
layout: page
title: Dining Philosophers
permalink: /allprojects/SysfierExamples/DiningPhilosophers

---

#### Problem Description
There are some philosophers sitting at a round table. Between each adjacent pair of philosophers is a chopstick. In other words, the chopsticks are equal to philosophers number. Each philosopher does two things: think and eat. The philosopher thinks for a while, and then stops thinking and becomes hungry. When the philosopher becomes hungry, he/she cannot eat until he/she owns the chopsticks to his/her left and right. When the philosopher is done eating he/she puts down the chopsticks and begins thinking again.

#### Properties

**Safety (mutual exclusion):** We want to check the model if there is any possibility that the two philosophers access to a same fork at a same time.

**Starvation:** We want to be sure that each philosophers will eat some time.

**Deadlock:** Deadlock does not occur.

#### Related Files
* The specification of the model [ [zip] ](/assets/projects/Sysfier/case-studies/Dining-Philosophers.zip)
