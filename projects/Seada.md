---
layout: page
title: SEADA&#58; Self-Adaptive Actors
permalink: /allprojects/Seada

---

#### Description
In SEADA, we will propose a framework for self-adaptive systems with a component-based architecture built in Ptolemy II that forms the feedback loop. Our models@runtime will be coded in an extension of Probabilistic Timed Rebeca (with dynamic features). Supporting tools for customized run- time formal verification of these models will be developed. Our focus will be on safety assurance while addressing uncertainty and responsiveness of the applications. SEADA will benefit from using Ptolemy in various ways. Ptolemy gives us the support for modeling cyber-physical systems; hence interaction with the physical world can be done smoothly. Furthermore, connecting Ptolemy actors and Rebeca actors can be done in a natural way, so, keeping the model@runtime up-to-date using Ptolemy event queues takes the least effort. The distinctive feature of SEADA is its actor-based flavor which will reflect in the design of the components of the architecture, the models in the knowledge-base, and in the V&V and formal verification techniques. In developing SEADA models we focus on the air traffic control and flight network applications. These applications are safety critical, and highly sensitive to changes that can occur in the system and the environment.

<!--
In SEADA we will use Ptolemy to represent the architecture, and extensions of Rebeca for modeling and verification. Ptolemy is a modeling and simulation tool for cyber-physical systems where the components are actors and the communication and coordination of actors are captured in a director which represents the Model of Computation. Rebeca is an actor-based modeling language with formal verification support. In SEADA, we will propose a framework for self-adaptive systems with a component-based architecture built in Ptolemy II. Our models@runtime will be coded in an extension of Probabilistic Timed Rebeca (with dynamic features), and supporting tools for customized run-time formal verification of these models will be developed. SEADA architecture in Ptolemy II forms the feedback loop and consists of four components of Monitor, Analyze, Plan, and Execute, together with a Knowledge-base, similar to the MAPE-K architecture. A Model of Computation for self-adaptive systems will be designed in Ptolemy. The distinctive feature of SEADA is its actor-based flavor which will reflect in the design of the components of the architecture, the models in the knowledge-base, and in the V&V and formal verification techniques. Ptolemy gives us the much-needed support to model and evaluate the system in a more abstract level, and the means to connect to the physical world, while Rebeca gives us the formal verification support for the model@runtime to assure safety concerns.\\
Ptolemy components in SEADA call the external tools to verify models@runtime and check the safety in order to react accordingly. Before sending any command to the system for reconfiguration or change, they will check the safety of new configurations.\\
Models in Dynamic Probabilistic Timed Rebeca, an actor-based language supporting dynamic and probabilistic behavior with timing constraints, will be the core models for runtime safety analysis. Probabilistic and statistical model checking and compositional verification will be the main analysis techniques in SEADA. We will create models on which we can zoom-in and zoom-out and reach to the necessary level of abstraction for the required analysis; we call these models magnifiable models. Instead of a predefined hierarchical or nested model, we will propose a flat model which can be modularized (partitioned) and be refined or abstracted (zoomed-in or zoomed-out) during runtime.\\
The actor model serves as the model@runtime in the core of the knowledge-base of SEADA, and any dangerous situation will be reported to the Plan component to be dealt with. Our experience in specific state-space reduction techniques for actors, and bounded model checking empowered by heuristics, will be the foundation to build more agile runtime verification methods which are necessary for reliable and quick adaptation. In the following, we presented our model@runtime for two different application domains.
-->

#### Case Studies
* The demo of our model@runtime for air traffic control: [ [video] ](http://rebeca.cs.ru.is/files/Movies/SEADA/ATC5.mov) (by Maryam Bagheri). 
* The demo of our model@runtime for railway systems: [ [video] ](http://rebeca.cs.ru.is/files/Movies/SEADA/TCS1.mov) (by Maryam Bagheri).
* An example of ATC model: [ [zip] ](http://rebeca.cs.ru.is/files/ATC.zip)

#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Ehsan Khamespanah
* Ali Jafari
* Edward A. Lee
* Narges Khakpour

#### Related Publications
- Maryam Bagheri, Marjan Sirjani, Ehsan Khamespanah and Ali Movaghar: Runtime Compositional Verification of Self-adaptive Track-based Traffic Control Systems, Submitted to IEEE Transactions on Software Engineering, Nov 2018 [ [pdf] ](/assets/papers/2018/Runtime-Compositional-Verification-of-Self-adaptive-Systems.pdf)

- Maryam Bagheri, Marjan Sirjani, Ehsan Khamespanah, Narges Khakpour, Ilge Akkaya, Ali Movaghar and Edward A. Lee: Coordinated Actor Model of Self-adaptive Track-based Traffic Control Systems, Journal of Systems and Software, 2018 [ [pdf] ](/assets/papers/2018/Self-Adaptive-Coordinated-Actors.pdf)

- Maryam Bagheri, Ehsan Khamespanah, Marjan Sirjani, Ali Movaghar, Edward A. Lee: Runtime Compositional Analysis of Track-based Traffic Control Systems, CRTS, 2016 [ [pdf] ](/assets/papers/2016/RuntimeCompositionalAnalysisofTTCS.pdf)

- Maryam Bagheri, Ilge Akkaya, Ehsan Khamespanah, Narges Khakpour, Marjan Sirjani, Ali Movaghar, Edward A. Lee: Coordinated Actors for Reliable Self-Adaptive Systems, FACS, 2016  [ [pdf] ](/assets/papers/2016/CoordinatedActorsforReliableSelfAdaptiveSystems.pdf) [ [bib] ](http://dblp.uni-trier.de/rec/bibtex/conf/facs2/BagheriAKKSML16)

- Maryam Bagheri, Ilge Akkaya, Ehsan Khamespanah, Narges Khakpour, Marjan Sirjani, Ali Movaghar, Edward A. Lee: Modeling and Analyzing Air Traffic Control Systems using Ptolemy, Ptolemy Mini-Conference, 2015 [ [pdf] ](/assets/papers/2015/ATC-PtolemyPoster-Final.pdf)

