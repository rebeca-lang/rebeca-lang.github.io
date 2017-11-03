---
layout: default
---
#### Introduction
**Rebeca** (Reactive Objects Language) is an actor-based language with a formal foundation,
designed in an effort to bridge the gap between formal verification approaches and real applications.
It can be considered as a reference model for concurrent computation,
based on an operational interpretation of the actor model.
It is also a platform for developing object-based concurrent systems in practice.

Besides having an appropriate and efficient way for modeling concurrent and distributed systems,
one needs a formal verification approach to ensure their correctness.
Rebeca is supported by Rebeca Verifier tool, as a front-end, to translate the codes into
existing model-checker languages and thus, be able to verify their properties.
Modular verification and abstraction techniques are used to reduce the state space
and make it possible to verify complicated reactive systems.

**Rebeca** is an actor-based language for modeling and verification of reactive systems.
Modeling a system in Rebeca requires one to specify reactive-object templates
and a finite set of object instances that run in parallel.
Properties can be specified in temporal logic.
Different approaches are proposed for verifying correctness of these properties.

#### Key features of Rebeca
* using actor-based concepts for the specification of reactive systems and their communications
* introducing components as an additional structure for verification purposes
* providing a formal semantics for the model and components, comprising their states,
communications, state transitions, and the knowledge of accessible interfaces
* using different abstraction techniques which preserve a set of behavioral specification in temporal logic,
and reduce the state space of a model, making it more suitable for model checking techniques
* establishing the soundness of these abstraction techniques by proving a weak simulation relation between the constructs
* applying a compositional verification approach, using the specified abstraction techniques
* translating Rebeca models into target languages of existing model checkers, enabling model checking of open, distributed systems
* direct model checking using RMC.

**Rebeca** is inspired by the actors paradigm, but goes beyond it by adding the concept of components
and the ability to analyze a group of reactive objects as a component.
Also, we have classes that reactive objects are instantiated from.
Classes serve as templates for state, behavior, and the interface access,
adding reusability in both modeling and verification process.

---
The word "rebec" is also the name of a bowed string musical instrument,
developed from the Persian instrument, the rabab.

Like all good medieval things, the rebec's origins can be traced to the Middle East.
Around the middle to the end of the ninth century AD, there are several discussions of
an instrument called a rabab in Persia ... rebec
