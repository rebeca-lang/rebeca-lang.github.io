---
layout: page
title: Examples

---
#### Overview
Rebeca is an actor-based language for modeling concurrent and reactive systems with asynchronous message passing. The actor model was originally introduced by Hewitt as an agent-based language, and is a mathematical model of concurrent computation that treats as the universal primitives of concurrent computation. A Rebeca model is similar to the actor model as it has reactive objects with no shared variables, asynchronous message passing with no blocking send and no explicit receive, and unbounded buffers for messages. Objects in Rebeca are reactive, self-contained, and each of them is called a _rebec_ (reactive object). Communication takes place by message passing among rebecs. Each rebec has an unbounded buffer, called message _queue_, for its arriving messages. Computation is event-driven, meaning that each rebec takes a message that can be considered as an event from the top of its message queue and execute the corresponding message server (also called a method). The execution of a message server is atomic execution (non-preemptive execution) of its body that is not interleaved with any other method execution.

#### Examples

To illustrate how models can be developed in Rebeca family language, we provided the following examples using different extensions of Rebeca.
<div class="row">
<div class="col s12 m4">
  <div class="icon-block">
    <h2 class="center light-blue-text"><i class="material-icons"></i></h2>
    <h5 class="center">Rebeca<br/><br/></h5>
    <p class="light">
	    <a href="{{ "/projects/CoreRebecaExamples/DiningPhilosophers" | relative_url }}">Dining Philosophers</a> <br/>
	    <a href="{{ "/projects/CoreRebecaExamples/TrainController" | relative_url }}">Train Controller</a><br/>
	    <a href="{{ "/projects/CoreRebecaExamples/CSMACD" | relative_url }}">CSMA-CD</a>
	    <a href="{{ "/projects/CoreRebecaExamples/LeaderElection" | relative_url }}">Leader Election</a><br/>
	    <a href="{{ "/projects/CoreRebecaExamples/CommitProblem" | relative_url }}">Commit Problem</a><br/>
	    <a href="{{ "/projects/CoreRebecaExamples/SenderReceiver" | relative_url }}">Sender Receiver</a><br/>
	    <a href="{{ "/projects/CoreRebecaExamples/ProducerConsumer" | relative_url }}">Producer Consumer</a><br/>
	    <a href="{{ "/projects/CoreRebecaExamples/SpanningTreeProtocol" | relative_url }}">Spanning Tree Protocol</a><br/>
        <a href="{{ "/projects/CoreRebecaExamples/MicroServiceArchitecture" | relative_url }}">[Micro Service Architecture]</a><br/>
	</p>
  </div>
</div>
<div class="col s12 m4">
  <div class="icon-block">
    <h2 class="center light-blue-text"><i class="material-icons"></i></h2>
    <h5 class="center">Time Rebeca<br/><br/></h5>
    <p class="light">
	    A GALS design for NoC 4x4 <a href="{{ "/assets/projects/TARO/case-studies/ASPIN.rebeca" | relative_url }}">[Rebeca model]</a><br/>
	    Routing algorithms for NoCs <a href="{{ "/assets/projects/TARO/case-studies/Dyad-OE-XY.zip" | relative_url }}"></a><br/>
	    Sensor Network <a href="{{ "/assets/projects/TARO/case-studies/sensornetwork.rebeca" | relative_url }}">[Rebeca model]</a><br/>
	    CDMA protocol with timing <a href="{{ "/assets/projects/TARO/case-studies/tcsma.rebeca" | relative_url }}">[Rebeca model]</a><br/>
	    <a href="{{ "/allprojects/TAROExamples/TicketService" | relative_url }}">Ticket Service System</a><br/>
	    ASPIN Network on Chip (TCTL) <a href="{{ "/assets/projects/TARO/case-studies/noc-prop.zip" | relative_url }}">[zip]</a><br/>
	    Ticket Service System (TCTL) <a href="{{ "/assets/projects/TARO/case-studies/ticket-service-prop.zip" | relative_url }}">[zip]</a><br/>
	    WSAN Applications (TCTL) <a href="{{ "/assets/projects/TARO/case-studies/tinyos-prop.zip" | relative_url }}">[zip]</a><br/>
	    Hadoop Yarn Schedule (TCTL) <a href="{{ "/assets/projects/TARO/case-studies/yarn-prop.zip" | relative_url }}">[zip]</a><br/>
	    Autonomous Vehicles <a href="{{ "/assets/projects/TARO/case-studies/AutonomousVehicles.rebeca" | relative_url }}">[Rebeca model]</a><br/>
	    <a href="{{ "/allprojects/DistributedControllers" | relative_url }}">[Consistency of Distributed Controllers]</a><br/>
	</p>
  </div>
</div>
<div class="col s12 m4">
  <div class="icon-block">
    <h2 class="center light-blue-text"><i class="material-icons"></i></h2>
    <h5 class="center">Probabilistic Timed Rebeca</h5>
    <p class="light">
	    <a href="{{ "/allprojects/PTRebecaExamples/ProbabilisticSensorNetwork" | relative_url }}">Probabilistic Sensor Network</a><br/>
	    <a href="{{ "/allprojects/PTRebecaExamples/ProbabilisticTicketService" | relative_url }}">Probabilistic Ticket Service</a><br/>
	    <a href="{{ "/allprojects/PTRebecaExamples/FaultTolerantNoC4x4" | relative_url }}">Fault Tolerant NoC 4x4</a><br/>
	</p>
  </div>
</div>
</div> 


#### Detailed Description
##### Rebeca
A Rebeca model consists of a set of reactive classes and the main block. In the main block the rebecs which are instances of the reactive classes are declared.  The body of the reactive class includes the declaration for its known rebecs, state variables, and message servers. The rebecs instantiated from a reactive class can only send messages to the known rebecs of that reactive class. Message servers consist of the declaration of local variables and the body of the message server. The statements in the body can be assignments, conditional statements, enumerated loops, non-deterministic assignment, and method calls. Method calls are sending asynchronous messages to other rebecs (or to self). A reactive class has an argument of type integer denoting the maximum size of its message queue. Although message queues are unbounded in the semantics of Rebeca, to avoid state space explosion in model checking we need a user-specified upper bound for the queue size. In comparison with the standard actor model, dynamic creation and dynamic topology are not supported by Rebeca. Also, actors in Rebeca are single-threaded.

We illustrate Rebeca language with the following example, shows the Rebeca model of a ticket service system. The model consists of three reactive classes: _TicketService_, _Agent_, and _Customer_. _Customer_ sends the _requestTicket_ message to _Agent_ and _Agent_ forwards the message to _TicketService_. _TicketService_ replies to _Agent_ by sending a _ticketIssued_ message and _Agent_ responds to _Customer_ by sending the issued ticket.

```
reactiveclass TicketService {
    knownrebecs {Agent a;}
    statevars {
        int nextId;
    }
    TicketService() {
        nextId = 0;
    }
    msgsrv requestTicket() {
        a.ticketIssued(nextId);
        nextId = nextId + 1;
    }
}

reactiveclass Agent {
    knownrebecs {
        TicketService ts;
        Customer c;
    }
    msgsrv requestTicket() {
        ts.requestTicket();
    }
    msgsrv ticketIssued(byte id) {
        c.ticketIssued(id);
    }
}

reactiveclass Customer {
    knownrebecs {Agent a;}
    Customer() {
        self.try();
    }
    msgsrv try() {
        a.requestTicket();
    }
    msgsrv ticketIssued(byte id) {
        self.try();
    }
}
main {
    Agent a(ts, c):();
    TicketService ts(a):(3);
    Customer c(a):();
}
```

##### Timed Rebeca
**Timed Rebeca** is an extension on Rebeca with time features for modeling and verification of time-critical systems. These primitives are added to Rebeca to address _computation time_, _message delivery time_, _message expiration_, and _period of occurrence of events_. In a Timed Rebeca model, each rebec has its own local clock. The local clocks evolves uniformly. Methods are still executed atomically, however passing of time while executing a method can be modeled. In addition, instead of queue for messages, there is a bag of messages for each rebec.

The timing primitives that are added to the syntax of Rebeca are _delay_, _deadline_ and _after_. The _delay_ statement models the passing of time for a rebec during execution of a message server. The keywords _after_ and _deadline_ can only be used in conjunction with a method call. The value of the argument of _after_ shows how long it takes for the message to be delivered to its receiver. The _deadline_ shows the timeout for the message, i.e., how long it will stay valid. We illustrate the application of these keywords with an example. The following source code shows the Timed Rebeca model of a ticket service system with timing constraints. As shown in 11 of the model, issuing the ticket takes two or three time units (the non-deterministic expression). At line 22 the rebec instantiated from _Agent_ sends a message _requestTicket_ to rebec _ts_ instantiated from  _TicketService_, and gives a deadline of five to the receiver to take this message and start serving it. The periodic task of retrying for a new ticket is modeled in line 39 by the customer sending a _try_ message to itself and letting the receiver to take it from its bag only after 30 units of time (by stating _after(30)_).

```
reactiveclass TicketService {
    knownrebecs {Agent a;}
    statevars {
        int issueDelay, nextId;
    }
    TicketService(int myDelay) {
        issueDelay = myDelay;
        nextId = 0;
    }
    msgsrv requestTicket() {
        delay(?(2, 3));
        a.ticketIssued(nextId); 
        nextId = nextId + 1;
    }
}

reactiveclass Agent {
    knownrebecs {
        TicketService ts;
        Customer c;
    }
    msgsrv requestTicket() {
        ts.requestTicket() deadline(5);
    }
    msgsrv ticketIssued(byte id) {
        c.ticketIssued(id);
    }
}

reactiveclass Customer {
    knownrebecs {Agent a;}
    Customer() {
        self.try();
    }
    msgsrv try() {
        a.requestTicket();
    }
    msgsrv ticketIssued(byte id) {
        self.try() after(30);
    }
}


main {
    Agent a(ts, c):();
    TicketService ts(a):(3);
    Customer c(a):();
}
```
